class AuthService {
  constructor(userEmail, userKey) {
    this.userEmail = userEmail;
    this.userKey = userKey;
    this.authEndpoint = import.meta.env.VITE_BASE_API_URL + "/auth/get-token"
  }
  async getApiToken() {
    const payload = {
      'userEmail': this.userEmail,
      'userKey': this.userKey
    }
    const response = await fetch(this.authEndpoint,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify(payload)
      })
    const data = await response.json()
    return data['access_token']
  }
}

export default AuthService;
