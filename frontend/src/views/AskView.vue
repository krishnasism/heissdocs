<template>
  <div>
    <AskInput v-if="!loading" class="mb-8" @submit-ask="askQuestion"></AskInput>
    <LoadingCircle v-if="loading && (answer || !errorMessage)"></LoadingCircle>
    <div v-else>
      <DangerAlert v-if="errorMessage" alert="Error" :message="errorMessage"></DangerAlert>
      <p class="mb-3 text-gray-500 dark:text-gray-400">
        {{ answer }}
      </p>
    </div>
  </div>
</template>
<script>
import DocumentsTable from "@/components/DocumentsTable.vue";
import AskInput from "@/components/AskInput.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';
import AuthService from "@/services/auth";
import DangerAlert from "@/components/DangerAlert.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import SettingsService from "@/services/settings";

export default {
  components: {
    DocumentsTable,
    AskInput,
    LoadingCircle,
    DangerAlert,
  },
  data() {
    return {
      loading: true,
      answer: "",
      apiToken: null,
      authService: null,
      loading: false,
      errorMessage: null,
    }
  },
  async mounted() {
    this.loading = true;
    const question = this.$route.query.question;
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
    if (question !== undefined || question != null) {
      this.askQuestion(question);
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
    askQuestionApiUrl() {
      return this.baseApiUrl + "/chat/ask"
    }
  },
  methods: {
    async askQuestion(evt) {
      this.loading = true;
      if (this.isAuthenticated) {
        fetch(this.askQuestionApiUrl + "?query=" + evt + '&user_email=' + this.user.email,
          {
            method: 'GET',
            headers: {
              'Authorization': 'Bearer ' + this.apiToken,
              'Content-Type': 'application/json; charset=utf-8'
            },
          })
          .then(response => response.json())
          .then(data => {
            this.answer = data.answer;
            this.errorMessage = data.error;
            this.loading = false;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
  }
}
</script>