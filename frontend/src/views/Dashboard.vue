<template>
  <LoadingCircle v-if="loading"></LoadingCircle>
  <div v-else>
    <DangerAlert v-if="settingsNotSet" :alert="settingsNotSetAlert" :message="settingsNotSetMessage"></DangerAlert>
    <SearchInput class="mb-8"></SearchInput>
    <FileUpload :disabled="parsing" class="w-60" @fileUpload="filesUploaded"></FileUpload>

    <!--TODO: Enable this-->
    <!-- <CheckBoxWithTipVue :disabled="parsing" @toggled="toggleSummarization" label="Summarize Document [Coming Soon]"
      helper="Generate and store an extractive summary of the uploaded documents."></CheckBoxWithTipVue> -->

    <CheckBoxWithTipVue :disabled="parsing" @toggled="toggleStoreInCloud" :label="$t('labels.storeCloudStorage')" :helper="$t('labels.storeCloudStorageHelper')"></CheckBoxWithTipVue>
    <BucketList class="mt-1 ml-6" v-if="storeFilesInCloud" :bucketList="bucketsList" @bucketSelected="bucketSelected">
    </BucketList>
    <CheckBoxWithTipVue :disabled="parsing" @toggled="toggleStoreInElastic" :label="$t('labels.storeElasticSearch')" :helper="$t('labels.storeElasticSearchHelper')"></CheckBoxWithTipVue>
    <CheckBoxWithTipVue :disabled="parsing" @toggled="toggleStoreInDocumentDb" :label="$t('labels.storeDocumentDb')" :helper="$t('labels.storeDocumentDbHelper')"></CheckBoxWithTipVue>
    <FileList class="mt-4" v-if="uploadedFileNameList.length > 0" :fileNameList="uploadedFileNameList"
      @deleteFile="deleteFile"></FileList>
    <button type="button" @click="sendFilesForParsing" v-if="uploadedFileNameList.length > 0" :disabled="parsing"
      class="ml-4 mt-4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      {{ sendButtonMessage }}
    </button>

    <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <SuccessToast style="position: fixed; bottom: 0; right: 20;" v-if="showSuccessToast" :message="toastMessage"
        @close-toast="closeSuccessToast"></SuccessToast>
    </Transition>
    <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <FailureToast style="position: fixed; bottom: 0; right: 20;" v-if="showFailureToast" :message="failureToastMessage"
        @close-toast="closeFailureToast"></FailureToast>
    </Transition>

    <!-- <SuccessToast message="test"></SuccessToast>
    <FailureToast message="test"></FailureToast>
    <WarningToast message="test"></WarningToast> -->
  </div>
</template>

<script>
import FileUpload from "@/components/FileUpload.vue";
import SearchInput from "@/components/SearchInput.vue";
import FileList from "@/components/FileList.vue";
import SuccessToast from "@/components/SuccessToast.vue";
import FailureToast from "@/components/FailureToast.vue";
import WarningToast from "@/components/WarningToast.vue";
import DangerAlert from "@/components/DangerAlert.vue";
import BucketList from "@/components/BucketList.vue";
import CheckBoxWithTipVue from "@/components/CheckBoxWithTip.vue";
import SettingsService from "@/services/settings";
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import LoadingCircle from "@/components/LoadingCircle.vue";

export default {
  components: {
    FileUpload,
    SearchInput,
    FileList,
    SuccessToast,
    FailureToast,
    WarningToast,
    DangerAlert,
    BucketList,
    CheckBoxWithTipVue,
    LoadingCircle,
  },
  data() {
    return {
      uploadedFileNameList: [],
      fileList: [],
      parsing: false,
      showSuccessToast: false,
      toastMessage: '',
      apiToken: '',
      settingsNotSet: false,
      settingsNotSetAlert: this.$t('errors.settingsNotSet'),
      settingsNotSetMessage: this.$t('errors.settingsNotSetMessage'),
      settings: null,
      failureToastMessage: '',
      showFailureToast: false,
      storeFilesInCloud: false,
      bucketsList: [],
      bucketName: '',
      summaryEnabled: false,
      settingsService: null,
      authService: null,
      loading: false,
      storeInElastic: false,
      storeInDocumentDb: false,
    }
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
  async mounted() {
    this.loading = true;
    this.authService = new AuthService(this.user.email, this.user.sub);
    this.apiToken = await this.authService.getApiToken(this.user.email, this.user.sub)
    this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
    this.settings = await this.settingsService.getSettings();
    this.settingsNotSet = (this.settings == null) || (Object.keys(this.settings).length == 0);

    if (!(this.settings.bucketsList == null || this.settings.bucketsList == undefined)) {
      this.bucketsList = this.settings.bucketsList.split(",");
    }
    if (this.bucketsList.length > 0) {
      this.bucketName = this.bucketsList[0];
    }
    this.settingsService.refreshSettings();
    this.loading = false;
  },
  computed: {
    baseApiUrl() {
      return import.meta.env.VITE_BASE_API_URL
    },
    uploadApiUrl() {
      return this.baseApiUrl + "/pdf/upload"
    },
    sendButtonMessage() {
      if (this.parsing) {
        return this.$t('labels.parsing')
      }
      return this.$t('labels.sendforparsing')
    }
  },
  methods: {
    filesUploaded(files) {
      if (this.fileList.length == 0 || this.uploadedFileNameList == 0) {
        this.fileList = [];
        this.uploadedFileNameList = [];
      }
      for (let i = 0; i < files.length; i++) {
        this.uploadedFileNameList.push(files[i].name);
        this.fileList.push(files[i])
      }
    },
    async sendFilesForParsing() {
      await this.settingsService.refreshSettings();
      this.parsing = true;
      for (let i = 0; i < this.fileList.length; i++) {
        const formData = new FormData()
        formData.append('file', this.fileList[i])
        formData.append('summarize', this.summaryEnabled);
        formData.append('user_email', this.user.email);
        formData.append('store_files_in_cloud', this.storeFilesInCloud);
        formData.append('store_in_elastic', this.storeInElastic);
        formData.append('store_in_document_db', this.storeInDocumentDb);
        formData.append('bucket_name', this.bucketName);
        const response = await fetch(this.uploadApiUrl, {
          method: 'POST',
          body: formData,
          headers: {
            'Authorization': 'Bearer ' + this.apiToken,
          }
        })
        if (!response.ok) {
          this.showFailureToast = true;
          this.failureToastMessage = this.$t('errors.failedToParse');
          this.parsing = false;
          break;
        }
      }
      if (!this.showFailureToast) {
        this.uploadedFileNameList = [];
        this.fileList = [];
        this.showSuccessToast = true;
        this.toastMessage = this.$t('labels.sentToQueue')
        this.parsing = false;
      }
    },
    closeSuccessToast() {
      this.showSuccessToast = false;
    },
    closeFailureToast() {
      this.showFailureToast = false;
    },
    deleteFile(idx) {
      if (this.uploadedFileNameList.length == 1 || this.fileList.length == 1) {
        this.uploadedFileNameList = [];
        this.fileList = [];
      }
      this.uploadedFileNameList.splice(idx, 1);
      this.fileList.splice(idx, 1);
    },
    bucketSelected(bucketName) {
      this.bucketName = bucketName;
    },
    toggleStoreInCloud(value) {
      this.storeFilesInCloud = value;
    },
    toggleStoreInElastic(value) {
      this.storeInElastic = value;
    },
    toggleStoreInDocumentDb(value) {
      this.storeInDocumentDb = value;
    },
    toggleSummarization(value) {
      this.summaryEnabled = value;
    },
  }
};

</script>