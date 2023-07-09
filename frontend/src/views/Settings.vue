<template>
  <div>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
      <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
        enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
        leave-to-class="transform opacity-0">
        <SuccessToast style="position: fixed; bottom: 0; right: 20;" v-if="showSuccessToast" :message="toastMessage"
          @close-toast="closeSuccessToast"></SuccessToast>
      </Transition>
      <SettingsForm v-if="settings" @submit="postSettings" :settings="settings"></SettingsForm>
    </div>
  </div>
</template>

<script>
import SettingsForm from "@/components/SettingsForm.vue";
import SuccessToast from "@/components/SuccessToast.vue";
import AuthService from "@/services/auth";
import SettingsService from "@/services/settings";
import LoadingCircle from '@/components/LoadingCircle.vue';


import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    SettingsForm,
    SuccessToast,
    LoadingCircle,
  },
  data() {
    return {
      settings: null,
      showSuccessToast: false,
      toastMessage: '',
      apiToken: '',
      authService: null,
      loading: false,
    }
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
  async mounted() {
    this.loading = true;
    this.authService = new AuthService(this.user.email, this.user.sub);
    this.apiToken = await this.authService.getApiToken();
    this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
    this.settings = await this.settingsService.getSettings();
    this.loading = false;
  },
  computed: {
    baseApiUrl() {
      return import.meta.env.VITE_BASE_API_URL
    },
    settingsApiUrl() {
      return this.baseApiUrl + "/settings"
    }
  },
  methods: {
    async postSettings(evt) {
      const status = this.settingsService.updateSettings(evt);
      if (status) {
        this.toastMessage = 'Settings updated!'
        this.showSuccessToast = true;
      }
    },
    closeSuccessToast() {
      this.showSuccessToast = false;
    }
  }
}
</script>