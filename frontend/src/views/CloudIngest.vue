<template>
  <LoadingCircle v-if="loading"></LoadingCircle>
  <div v-else>
    <p v-if="bucketsList.length === 0">{{ $t('labels.noBucketsLoaded') }}</p>
    <p v-if="scanBucket">{{$t('labels.readingFilesFromBucket', { bucketName: scanBucket })}}</p>
    <DangerAlert v-if="pageError" :alert="pageErrorAlert" :message="pageError"></DangerAlert>
    <S3DocumentsTable :s3Documents="s3Documents" v-if="!loading && !pageError && s3Documents" class="w-full"
      @parse-document="sendToParse"></S3DocumentsTable>

    <TransitionGroup enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <SuccessToast v-for="(toast, index) in toasts" :key="toast.id"
        :style="{ position: 'fixed', bottom: 20 + (index * 60) + 'px', right: 20 }" :message="toast.message"
        @close-toast="closeToast(index)"></SuccessToast>
    </TransitionGroup>
  </div>
</template>
<script>
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import SettingsService from "@/services/settings";
import DangerAlert from "@/components/DangerAlert.vue";
import S3DocumentsTable from "../components/S3DocumentsTable.vue";
import SuccessToast from "@/components/SuccessToast.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';

export default {
  components: {
    DangerAlert,
    S3DocumentsTable,
    SuccessToast,
    LoadingCircle,
  },
  data() {
    return {
      loading: false,
      s3Documents: null,
      apiToken: null,
      scanBucket: null,
      settings: null,
      pageError: null,
      pageErrorAlert: this.$t('errors.loadS3Bucket'),
      settingsService: null,
      bucketName: null,
      toasts: [],
      authService: null,
      bucketsList: [],
    }
  },
  async mounted() {
    this.loading = true;
    if (this.isAuthenticated && this.apiToken == null) {
      this.authService = new AuthService(this.user.email, this.user.sub);
      this.apiToken = await this.authService.getApiToken();
      this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
      this.settings = await this.settingsService.getSettings();
      this.scanBucket = this.settings.scanBucket;
      if (this.scanBucket !== undefined || this.scanBucket != null) {
        await this.loadS3Files(this.scanBucket);
      }
      if (!(this.settings.bucketsList == null || this.settings.bucketsList == undefined)) {
        this.bucketsList = this.settings.bucketsList.split(",");
      }
      else{
        this.bucketsList = [];
      }
      if (this.bucketsList.length > 0) {
        this.bucketName = this.bucketsList[0];
      }
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
    s3BucketAllFilesUrl() {
      return this.cloudApiUrl + "/all-bucket-files"
    },
    s3SendParsingJobUrl() {
      return this.cloudApiUrl + "/cloud-parsing-job"
    }
  },
  methods: {
    async sendToParse(evt) {
      await this.settingsService.refreshSettings();
      const formData = new FormData();
      formData.append('source_bucket_name', this.scanBucket)
      formData.append('key_name', evt);
      formData.append('user_email', this.user.email);
      formData.append('viewer_bucket_name', this.bucketName);

      const response = await fetch(this.s3SendParsingJobUrl, {
        method: 'POST',
        body: formData,
        headers: {
          'Authorization': 'Bearer ' + this.apiToken,
        }
      });
      if (response.status == 201) {
        this.createSuccessToast(evt);
      }
    },
    createSuccessToast(fileName) {
      const message = this.$t('labels.fileQueuedForParsing', { fileName: fileName });
      const toast = {
        message,
        id: Date.now(), // Generate a unique ID for each toast
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
    async loadS3Files(bucket_name) {
      if (this.isAuthenticated) {
        fetch(this.s3BucketAllFilesUrl + "?bucket_name=" + bucket_name + '&user_email=' + this.user.email,
          {
            method: 'GET',
            headers: {
              'Authorization': 'Bearer ' + this.apiToken,
              'Content-Type': 'application/json; charset=utf-8'
            },
          })
          .then(response => response.json())
          .then(data => {
            if (data.all_files.error == null) {
              this.s3Documents = data.all_files.files;
            }
            else {
              this.pageError = data.all_files.error;
            }
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
  }
}
</script>