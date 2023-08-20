<template>
  <LoadingCircle v-if="loading"></LoadingCircle>
  <div v-else>
    <DangerAlert v-if="pageError" :alert="pageErrorAlert" :message="pageError"></DangerAlert>
    <ElasticDocumentsTable :documents="documents" v-if="!loading && !pageError && documents" class="w-full"
      @delete-document="deleteDocument"></ElasticDocumentsTable>
    <div class="mt-4" v-if="documents">
      <button type="button" @click="loadElasticSearchFiles"
        class="text-gray-900 hover:text-white border border-gray-800 hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 dark:border-gray-600 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-800">{{
          $t('labels.loadMoreButton') }}</button>
    </div>
    <TransitionGroup enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <WarningToast v-for="(toast, index) in toasts" :key="toast.id"
        :style="{ position: 'fixed', bottom: 20 + (index * 60) + 'px', right: 20 }" :message="toast.message"
        @close-toast="closeToast(index)"></WarningToast>
    </TransitionGroup>
  </div>
</template>
<script>
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import SettingsService from "@/services/settings";
import DangerAlert from "@/components/DangerAlert.vue";
import ElasticDocumentsTable from "../components/ElasticDocumentsTable.vue";
import WarningToast from "@/components/WarningToast.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';

export default {
  components: {
    DangerAlert,
    ElasticDocumentsTable,
    WarningToast,
    LoadingCircle,
  },
  data() {
    return {
      loading: false,
      elasticSearchFiles: null,
      apiToken: null,
      settings: null,
      pageError: null,
      pageErrorAlert: this.$t('errors.loadElasticSearchAllFiles'),
      settingsService: null,
      toasts: [],
      authService: null,
      documents: [],
      scrollId: null,
    }
  },
  async mounted() {
    this.loading = true;
    if (this.isAuthenticated && this.apiToken == null) {
      this.authService = new AuthService(this.user.email, this.user.sub);
      this.apiToken = await this.authService.getApiToken();
      this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
      this.settings = await this.settingsService.getSettings();
      await this.loadElasticSearchFiles();
    }
    this.loading = false;
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated,
      SettingsService,
      AuthService,
    };
  },
  computed: {
    baseApiUrl() {
      return import.meta.env.VITE_BASE_API_URL
    },
    cloudApiUrl() {
      return this.baseApiUrl + "/cloud"
    },
    elasticSearchAllFilesUrl() {
      return this.cloudApiUrl + "/all-elasticsearch-files"
    },
    elasticSearchDeleteUrl() {
      return this.cloudApiUrl + "/elasticsearch-file"
    }
  },
  methods: {
    async deleteDocument(evt) {
      await this.settingsService.refreshSettings();
      const formData = new FormData();
      formData.append('file_id', evt._id)
      formData.append('user_email', this.user.email)
      const response = await fetch(this.elasticSearchDeleteUrl, {
        method: 'DELETE',
        body: formData,
        headers: {
          'Authorization': 'Bearer ' + this.apiToken,
        }
      });
      if (response.status == 200) {
        this.createSuccessToast(evt);
        const indexToRemove = this.documents.findIndex(doc => doc._id === evt._id);
        if (indexToRemove !== -1) {
          this.documents.splice(indexToRemove, 1);
        }
      }
    },
    createSuccessToast(fileName) {
      const message = this.$t('labels.fileDeleted', { fileName: fileName });
      const toast = {
        message,
        id: Date.now(),
      };
      this.toasts.push(toast);
      setTimeout(() => {
        this.closeToast(toast.id);
      }, 5000);
    },
    closeToast(id) {
      const index = this.toasts.findIndex(toast => toast.id === id);
      if (index !== -1) {
        this.toasts.splice(index, 1);
      }
    },
    async loadElasticSearchFiles() {
      if (this.isAuthenticated) {
        try {
          let url = `${this.elasticSearchAllFilesUrl}?user_email=${this.user.email}`;
          let headers = {
            'Authorization': `Bearer ${this.apiToken}`,
            'Content-Type': 'application/json; charset=utf-8'
          };

          if (this.scrollId) {
            url += `&scroll_id=${this.scrollId}`;
          }

          const response = await fetch(url, {
            method: 'GET',
            headers: headers,
          });

          const data = await response.json();
          console.log(data)
          if (data.error === null) {
            console.log(data)
            if (!this.scrollId) {
              this.documents = [];
            }
            this.scrollId = data.scroll_id;
            this.documents.push(...data.all_files);
          } else {
            this.pageError = data.error;
          }
        } catch (error) {
          console.error(error);
        }
      }
    },
  }
}
</script>