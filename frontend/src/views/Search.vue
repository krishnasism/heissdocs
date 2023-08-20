<template>
  <div>
    <SearchInput class="mb-8" submit-search="handleSearch"></SearchInput>
    <LoadingCircle v-if="loading && (documents || !errorMessage)"></LoadingCircle>
    <div v-else>
      <DocumentsTable :documents="documents" v-if="documents && documents.length > 0" class="w-full"></DocumentsTable>
      <DangerAlert v-if="errorMessage" alert="Error" :message="errorMessage"></DangerAlert>
      <div class="flex flex-col">
        <div class="inline-flex mt-2 xs:mt-0">
          <button v-if="hasPreviousPage && !disablePagination" @click="handlePreviousPage"
            class="flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            <svg class="w-3.5 h-3.5 mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
              viewBox="0 0 14 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13 5H1m0 0 4 4M1 5l4-4" />
            </svg>
            {{ $t('labels.previousPageButton') }}
          </button>
          <button v-if="hasNextPage && !disablePagination" @click="handleNextPage"
            class="flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-l border-gray-700 rounded-r hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            {{ $t('labels.nextPageButton') }}
            <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
              viewBox="0 0 14 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M1 5h12m0 0L9 1m4 4L9 9" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import DocumentsTable from "@/components/DocumentsTable.vue";
import SearchInput from "@/components/SearchInput.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';
import AuthService from "@/services/auth";
import DangerAlert from "@/components/DangerAlert.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import SettingsService from "@/services/settings";

export default {
  components: {
    DocumentsTable,
    SearchInput,
    LoadingCircle,
    DangerAlert,
  },
  data() {
    return {
      loading: true,
      documents: [],
      apiToken: null,
      authService: null,
      loading: false,
      errorMessage: null,
      currentPage: 0,
      hasNextPage: false,
      hasPreviousPage: false,
      disablePagination: true,
    }
  },
  async mounted() {
    this.loading = true;
    const search = this.$route.query.search;
    if (this.isAuthenticated && this.apiToken == null) {
      this.authService = new AuthService(this.user.email, this.user.sub);
      this.apiToken = await this.authService.getApiToken();
      this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
      this.settings = await this.settingsService.getSettings();
      if (!this.settings.searchDocumentDb) {
        this.disablePagination = false;
      }
      else {
        this.disablePagination = true;
      }
    }
    if (search !== undefined || search != null) {
      this.handleSearch(search);
    }
    this.loading = false;
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated,
      AuthService,
      SettingsService,
    };
  },
  computed: {
    baseApiUrl() {
      return import.meta.env.VITE_BASE_API_URL
    },
    pdfSearchApiUrl() {
      return this.baseApiUrl + "/pdf/search"
    }
  },
  methods: {
    async handleSearch(evt, nextPage = false, previousPage = false) {
      this.loading = true;
      if (evt == null || evt == undefined || evt == "") {
        this.documents = [];
        this.loading = false;
        return;
      }
      if (this.isAuthenticated) {
        if (nextPage) {
          this.currentPage++;
        }
        if (previousPage) {
          if (this.currentPage > 0) {
            this.currentPage--;
          }
        }
        if (!nextPage && !previousPage) {
          this.currentPage = 0;
        }
        const nextPageChunk = 10 * this.currentPage;
        fetch(this.pdfSearchApiUrl + "?query=" + evt + '&user_email=' + this.user.email + '&page_start=' + nextPageChunk,
          {
            method: 'GET',
            headers: {
              'Authorization': 'Bearer ' + this.apiToken,
              'Content-Type': 'application/json; charset=utf-8'
            },
          })
          .then(response => response.json())
          .then(data => {
            this.documents = data.documents;
            this.errorMessage = data.error;
            this.loading = false;
            if (data.documents){
              this.hasNextPage = data.documents.length >= 10;
            }
            else{
              this.hasNextPage = false;
            }
            if (this.currentPage > 0) {
              this.hasPreviousPage = true;
            } else {
              this.hasPreviousPage = false;
            }
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    async handleNextPage() {
      this.handleSearch(this.$route.query.search, true, false);
    },
    async handlePreviousPage() {
      this.handleSearch(this.$route.query.search, false, true);
    },
  }
}
</script>