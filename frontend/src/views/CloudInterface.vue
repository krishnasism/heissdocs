<template>
    <div>
      <DangerAlert v-if="pageError" :alert="pageErrorAlert" :message="pageError"></DangerAlert>
      <S3DocumentsTable :s3Documents="s3Documents" v-if="!loading" class="w-full" @parse-document="sendToParse"></S3DocumentsTable>
    </div>
  </template>
  <script>
  import getApiToken from "@/services/auth";
  import { useAuth0 } from '@auth0/auth0-vue';
  import getSettings from "@/services/settings";
  import DangerAlert from "@/components/DangerAlert.vue";
  import S3DocumentsTable from "../components/S3DocumentsTable.vue";

  export default {
    components: {
      DangerAlert,
      S3DocumentsTable,
    },
    data() {
      return {
        loading: true,
        s3Documents: null,
        apiToken: null,
        bucketName: null,
        settings: null,
        pageError: null,
        pageErrorAlert: "Unable to Load S3 Bucket Objects: "
      }
    },
    async mounted() {
      const bucket_name = "krishdocuments";
      if (this.isAuthenticated && this.apiToken == null) {
        this.apiToken = await this.getApiToken(this.user.email, this.user.sub)
        this.settings = await this.getSettings();
        if (bucket_name !== undefined || bucket_name != null) {
          await this.loadS3Files(bucket_name);
      }
      }
    },
    setup() {
      const { user, isAuthenticated } = useAuth0();
      return {
        user,
        isAuthenticated,
        getApiToken,
        getSettings
      };
    },
    computed: {
      baseApiUrl() {
        return import.meta.env.VITE_BASE_API_URL
      },
      settingsApiUrl() {
        return this.baseApiUrl + "/settings"
      },
      s3BucketAllFilesUrl() {
        return this.baseApiUrl + "/cloud/all-bucket-files"
      }
    },
    methods: {
      async sendToParse(evt) {
        console.log(evt);
      },
      async loadS3Files(bucket_name) {
        this.loading = true;
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
              if(data.s3_response.error == null) {
                this.s3Documents = data.s3_response.files;
              }
              else{
                this.pageError = data.s3_response.error;
              }
              this.loading = false;
            })
            .catch(error => {
              console.error(error);
            });
        }
      }
    }
  }
  </script>