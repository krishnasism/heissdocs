class AuthService {
  constructor(userEmail, userKey) {
    this.userEmail = userEmail;
    this.userKey = userKey;
    this.authEndpoint = import.meta.env.VITE_BASE_API_URL + "/auth/get-token"
    this.apiToken = null
  }
  async getApiToken() {
    this.apiToken = sessionStorage.getItem('apiToken');
    if (!this.isTokenExpired()){
      return this.apiToken
    }
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
    this.apiToken  = data['access_token']
    sessionStorage.setItem('apiToken', this.apiToken);
    return this.apiToken;
  }
  isTokenExpired() {
    if(!this.apiToken){
      return true
    }
    try {
      const tokenParts = this.apiToken.split('.');
      if (tokenParts.length !== 3){
        return true
      }
      const payload = JSON.parse(atob(tokenParts[1]));
      const expiration = payload.exp;
      if (expiration === undefined || expiration === null){
        return true
      }
      if (expiration < Date.now() / 1000){
        return true
      }
    } catch(error){
      return true
    }
    return false
  }
}

export default AuthService;
