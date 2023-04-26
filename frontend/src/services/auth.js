async function getApiToken(userEmail, userKey) {
    const payload = {
        'userEmail': userEmail,
        'userKey': userKey
    }
    const authEndpoint = import.meta.env.VITE_BASE_API_URL + "/auth/get-token"
    const response = await fetch(authEndpoint,
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

export default getApiToken;
