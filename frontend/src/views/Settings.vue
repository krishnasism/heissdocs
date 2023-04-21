<template>
  <div>
    <SettingsForm v-if="settings" @submit="postSettings" :settings="settings"></SettingsForm>
  </div>
</template>

<script>
import SettingsForm from "@/components/SettingsForm.vue";
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    SettingsForm
  },
  data() {
    return {
      settings: null,
    }
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated
    };
  },
  async mounted() {
    this.settings = await this.getSettings();
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
              'Authorization': 'abcde', //TODO: Add auth here,
              'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify(evt)
          })
        const data = await response.json()
        if (data['message'] == 'updated') {
          alert("Settings Updated!")
        }
      }
    },
    async getSettings() {
      if (this.isAuthenticated) {
        const response = await fetch(this.settingsApiUrl + "?userEmail=" + this.user.email,
          {
            method: 'GET',
            headers: {
              'Authorization': 'abcde', //TODO: Add auth here,
              'Content-Type': 'application/json; charset=utf-8'
            },
          })
        const data = await response.json();
        return data.settings;
      }
    }
  }
}
</script>