class SettingsService {
  constructor(userEmail, isAuthenticated, apiToken) {
    this.baseApiUrl = import.meta.env.VITE_BASE_API_URL;
    this.settingsApiUrl = `${this.baseApiUrl}/settings`;
    this.refreshSettingsUrl = `${this.baseApiUrl}/refresh-queue-settings`;
    this.userEmail = userEmail;
    this.isAuthenticated = isAuthenticated;
    this.apiToken = apiToken;
  }
  async getSettings() {
    if (this.isAuthenticated) {
      const response = await fetch(this.settingsApiUrl + "?userEmail=" + this.userEmail,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + this.apiToken
          },
        })
      const data = await response.json();
      return data.settings;
    }
  }

  async refreshSettings() {
    if (this.isAuthenticated) {
      const response = await fetch(this.refreshSettingsUrl + "?userEmail=" + this.userEmail,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + this.apiToken
          },
        })
      const data = await response.json();
      return data.message;
    }
  }

  async updateSettings(settingsObject) {
    if (this.isAuthenticated) {
      settingsObject['userEmail'] = this.userEmail;
      const response = await fetch(this.settingsApiUrl,
        {
          method: 'POST',
          headers: {
            'Authorization': 'Bearer ' + this.apiToken,
            'Content-Type': 'application/json; charset=utf-8'
          },
          body: JSON.stringify(settingsObject)
        })
      const data = await response.json()
      if (data['message'] == 'updated') {
        return true;
      }
      return false;
    }
  }
}

export default SettingsService;