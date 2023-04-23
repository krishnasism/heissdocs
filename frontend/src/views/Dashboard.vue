<template>
  <div>
    <span>Dashboard</span>
    <div v-if="isAuthenticated">
      <p> {{ $t('message.greeting') + " " + user.name}}</p>
    </div>
    <SearchInput class="m-8"></SearchInput>
    <FileUpload class="m-8 w-60" @fileUpload="filesUploaded"></FileUpload>
    <FileList class="ml-8 mt-2" v-if="uploadedFileNameList.length > 0" :fileNameList="uploadedFileNameList"></FileList>
    <button type="button" @click="sendFilesForParsing" v-if="uploadedFileNameList.length > 0" :disabled="parsing"
      class="ml-8 mt-4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      {{ sendButtonMessage }}
    </button>

    <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <SuccessToast style="position: fixed; bottom: 0; right: 20;" v-if="showSuccessToast" :message="toastMessage"
        @close-toast="closeSuccessToast"></SuccessToast>
    </Transition>
  </div>
</template>

<script>
import FileUpload from "@/components/FileUpload.vue";
import SearchInput from "@/components/SearchInput.vue";
import FileList from "@/components/FileList.vue";
import SuccessToast from "@/components/SuccessToast.vue";

import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    FileUpload, SearchInput, FileList, SuccessToast
  },
  data() {
    return {
      uploadedFileNameList: [],
      fileList: [],
      parsing: false,
      showSuccessToast: false,
      toastMessage: '',
    }
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated
    };
  },
  mounted() {
    console.log(this.user)
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
        return "Parsing..."
      }
      return "Send for parsing"
    }
  },
  methods: {
    filesUploaded(files) {
      for (let i = 0; i < files.length; i++) {
        this.uploadedFileNameList.push(files[i].name);
        this.fileList.push(files[i])
      }
    },
    async sendFilesForParsing() {
      this.parsing = true;
      for (let i = 0; i < this.fileList.length; i++) {
        const formData = new FormData()
        formData.append('file', this.fileList[i])
        formData.append('summarize', false);
        const response = await fetch(this.uploadApiUrl, {
          method: 'POST',
          body: formData,
        })

        if (!response.ok) {
          throw new Error('Upload failed')
        }
        const data = await response.json()
        console.log(data)
      }
      this.parsing = false;
      this.uploadedFileNameList = [];
      this.fileList = [];
      this.showSuccessToast = true;
      this.toastMessage = 'Parsed!'
    },
    closeSuccessToast() {
      this.showSuccessToast = false;
    }
  }
};

</script>