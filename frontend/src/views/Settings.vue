<template>
  <div>
    <SettingsForm @submit="postSettings"></SettingsForm>
  </div>
</template>

<script>
import SettingsForm from "@/components/SettingsForm.vue";
export default {
  components: {
    SettingsForm
  },
  mounted() {
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
      const response = await fetch(this.settingsApiUrl,
        {
          method: 'POST',
          headers: {
            'Authorization': 'abcde', //TODO: Add auth here,
            'userId': 'user1',
            'Content-Type': 'application/json; charset=utf-8'
          },
          body: JSON.stringify(evt)
        })
      const data = await response.json()
      console.log(data)

    }
  }
  ,
}
</script>