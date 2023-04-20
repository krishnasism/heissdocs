import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Settings from '../views/Settings.vue'
import News from '../views/News.vue'
import Contact from '../views/Contact.vue'
import Setup from '../views/Setup.vue'
import Search from '../views/Search.vue'
import Login from '../views/Login.vue'
import { createAuth0, authGuard } from '@auth0/auth0-vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root',
      component: Dashboard,
      beforeEnter: authGuard,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      beforeEnter: authGuard,
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings,
      beforeEnter: authGuard,
    },
    {
      path: '/news',
      name: 'news',
      component: News,
      beforeEnter: authGuard,
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact,
      beforeEnter: authGuard,
    },
    {
      path: '/setup',
      name: 'setup',
      component: Setup,
      beforeEnter: authGuard,
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      beforeEnter: authGuard,
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
  ]
})

export default router
