<template>
  <div>
    <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <SuccessToast style="position: fixed; bottom: 0; right: 20;" v-if="showSuccessToast" :message="toastMessage"
        @close-toast="closeSuccessToast"></SuccessToast>
    </Transition>
    <SettingsForm v-if="settings" @submit="postSettings" :settings="settings"></SettingsForm>
  </div>
</template>

<script>
import SettingsForm from "@/components/SettingsForm.vue";
import SuccessToast from "@/components/SuccessToast.vue";
import getApiToken from "@/services/auth";
import SettingsService from "@/services/settings";


import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    SettingsForm,
    SuccessToast
  },
  data() {
    return {
      settings: null,
      showSuccessToast: false,
      toastMessage: '',
      apiToken: ''
    }
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated,
      getApiToken,
      SettingsService,
    };
  },
  async mounted() {
    this.apiToken = await this.getApiToken(this.user.email, this.user.sub);
    this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
    this.settings = await this.settingsService.getSettings();
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
      if (this.isAuthenticated) {
        evt['userEmail'] = this.user.email
        const response = await fetch(this.settingsApiUrl,
          {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + this.apiToken,
              'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify(evt)
          })
        const data = await response.json()
        if (data['message'] == 'updated') {
          this.toastMessage = 'Settings updated!'
          this.showSuccessToast = true;
        }
      }
    },
    closeSuccessToast() {
      this.showSuccessToast = false;
    }
  }
}
</script>