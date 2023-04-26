async function getSettings() {
    if (this.isAuthenticated) {
      const response = await fetch(this.settingsApiUrl + "?userEmail=" + this.user.email,
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

export default getSettings