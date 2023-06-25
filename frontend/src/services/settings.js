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
}

export default SettingsService;