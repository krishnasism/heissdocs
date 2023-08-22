<template>
  <LoadingCircle v-if="loading"></LoadingCircle>
  <div v-else>
    <DangerAlert v-if="pageError" :alert="pageErrorAlert" :message="pageError"></DangerAlert>
    <div class="flex mb-4" :class="{ 'shake': deleteDocumentDbNotConfirmed }">
      <div class="flex items-center h-5 mr-1">
        <input id="chkDeleteDocumentDbConfirmed" aria-describedby="chkDeleteDocumentDbConfirmed-text" type="checkbox"
          @click="toggleDeleteDocumentDbConfirmed"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
      </div>
      <div class="ml-1 text-sm">
        <label for="chkDeleteDocumentDbConfirmed" class="font-medium text-gray-900 dark:text-gray-300">{{
          $t('labels.deleteDocumentDb') }}</label>
        <p id="chkDeleteDocumentDbConfirmed-text" class="text-xs font-normal text-gray-500 dark:text-gray-300">{{
          $t('labels.deleteDocumentDbHelper') }}</p>
      </div>
    </div>
    <DocumentDbDocumentsTable :documents="documents" v-if="!loading && !pageError && documents" class="w-full"
      @delete-document="deleteDocument"></DocumentDbDocumentsTable>
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
import DocumentDbDocumentsTable from "@/components/DocumentDbDocumentsTable.vue";
import WarningToast from "@/components/WarningToast.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';
import CheckBoxWithTipVue from "@/components/CheckBoxWithTip.vue";

export default {
  components: {
    DangerAlert,
    DocumentDbDocumentsTable,
    WarningToast,
    LoadingCircle,
    CheckBoxWithTipVue,
  },
  data() {
    return {
      loading: false,
      elasticSearchFiles: null,
      apiToken: null,
      settings: null,
      pageError: null,
      pageErrorAlert: this.$t('errors.loadDocumentDbAllFiles'),
      settingsService: null,
      toasts: [],
      authService: null,
      documents: [],
      scrollId: null,
      deleteDocumentDb: false,
      deleteDocumentDbNotConfirmed: false,
    }
  },
  async mounted() {
    this.loading = true;
    if (this.isAuthenticated && this.apiToken == null) {
      this.authService = new AuthService(this.user.email, this.user.sub);
      this.apiToken = await this.authService.getApiToken();
      this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
      this.settings = await this.settingsService.getSettings();
      await this.loadDocumentDbFiles();
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
    documentDbAllFilesUrl() {
      return this.cloudApiUrl + "/all-documentdb-files"
    },
    documentDbDeleteUrl() {
      return this.cloudApiUrl + "/documentdb-file"
    }
  },
  methods: {
    async deleteDocument(evt) {
      if (!this.deleteDocumentDb) {
        this.deleteDocumentDbNotConfirmed = false;
        setTimeout(() => {
          this.deleteDocumentDbNotConfirmed = true;
        }, 0);
        return;
      }
      await this.settingsService.refreshSettings();
      const formData = new FormData();
      if (evt.id) {
        formData.append('cosmos_id', evt.id)
      }
      else {
        formData.append('cosmos_id', 'xxx')
      }
      formData.append('file_id', evt.unique_id)
      formData.append('user_email', this.user.email)
      const response = await fetch(this.documentDbDeleteUrl, {
        method: 'DELETE',
        body: formData,
        headers: {
          'Authorization': 'Bearer ' + this.apiToken,
        }
      });
      if (response.status == 200) {
        this.createSuccessToast(evt);
        const indexToRemove = this.documents.findIndex(doc => doc.unique_id === evt.unique_id);
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
    toggleDeleteDocumentDbConfirmed(evt) {
      this.deleteDocumentDb = evt.target.checked;
    },
    async loadDocumentDbFiles() {
      if (this.isAuthenticated) {
        try {
          let url = `${this.documentDbAllFilesUrl}?user_email=${this.user.email}`;
          let headers = {
            'Authorization': `Bearer ${this.apiToken}`,
            'Content-Type': 'application/json; charset=utf-8'
          };

          const response = await fetch(url, {
            method: 'GET',
            headers: headers,
          });
          const data = await response.json();
          if (data.error === null) {
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