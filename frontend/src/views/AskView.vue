<template>
  <div>
    <AskInput class="mb-8" @submit-ask="askQuestion"></AskInput>
    <div>
      <DangerAlert v-if="errorMessage" alert="Error" :message="errorMessage"></DangerAlert>
      <p v-if="question" class="tracking-tighter text-gray-500 md:text-lg dark:text-gray-400">
        {{ $t('labels.question') }}: {{ question }}
      </p>
      <br />
      <LoadingCircle v-if="loading && (answer || !errorMessage)"></LoadingCircle>
      <p v-else class="mb-3 text-gray-900 dark:text-gray-400">
        {{ answer }}
      </p>
      <ChatHistory v-if="chatHistory.messages.length > 0" class="mt-8 bg-slate-50 p-10 rounded-md	"
        :chatHistory="chatHistory"></ChatHistory>
      <button v-if="chatHistory.messages.length > 0" type="button" @click="downloadJSON"
        class="mt-8 focus:outline-none text-white bg-green-400 hover:bg-green-600 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"><svg
          class="w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
          viewBox="0 0 20 19">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M15 15h.01M4 12H2a1 1 0 0 0-1 1v4a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-4a1 1 0 0 0-1-1h-3M9.5 1v10.93m4-3.93-4 4-4-4" />
        </svg></button>
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
import ChatHistory from "@/components/ChatHistory.vue";

export default {
  components: {
    DocumentsTable,
    AskInput,
    LoadingCircle,
    DangerAlert,
    ChatHistory,
  },
  data() {
    return {
      chatHistory: {
        messages: [],
        add_message(sender, text) {
          this.messages.push({ sender, text });
        },
        get_context(num_messages) {
          const start_idx = Math.max(0, this.messages.length - num_messages);
          return this.messages.slice(start_idx);
        },
      },
      loading: false,
      answer: "",
      apiToken: null,
      authService: null,
      errorMessage: null,
      question: "",
    };
  },
  async mounted() {
    this.loading = true;
    this.question = this.$route.query.question;
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
    if (this.question !== undefined || this.question != null) {
      this.askQuestion(this.question);
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
      this.question = evt;
      if (this.isAuthenticated) {
        try {
          const response = await fetch(this.askQuestionApiUrl + "?query=" + evt + '&user_email=' + this.user.email, {
            method: 'GET',
            headers: {
              'Authorization': 'Bearer ' + this.apiToken,
              'Content-Type': 'application/json; charset=utf-8'
            },
          });
          const data = await response.json();

          this.answer = data.answer;
          this.errorMessage = data.error;
          this.loading = false;

          this.chatHistory.add_message('user', this.question);
          this.chatHistory.add_message('bot', this.answer);
        } catch (error) {
          console.error(error);
        }
      }
    },
    downloadJSON() {
      const jsonContent = JSON.stringify(this.chatHistory.messages, null, 2);
      const blob = new Blob([jsonContent], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const currentDateTime = new Date().toISOString().replace(/[:.]/g, '-');
      const fileName = `chathistory_${currentDateTime}.json`;
      a.href = url;
      a.download = fileName;
      a.click();

      URL.revokeObjectURL(url);
    },
  }
}
</script>