import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createAuth0 } from '@auth0/auth0-vue';
import i18n from './locales/i18n'

import './assets/tailwind.css'
import './assets/global.css'
const app = createApp(App);
app.use(i18n);
app.use(router);

app.use(
  createAuth0({
    domain: import.meta.env.VITE_AUTH0_DOMAIN,
    clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
    authorizationParams: {
      redirect_uri: window.location.origin
    },
    useRefreshTokens: true,
    cacheLocation: 'localstorage'
  })
);

app.mount('#app')
