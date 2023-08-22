import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Settings from '../views/Settings.vue'
import News from '../views/News.vue'
import Contact from '../views/Contact.vue'
import Search from '../views/Search.vue'
import Login from '../views/Login.vue'
import FileView from '../views/FileView.vue'
import DocumentsProgress from '../views/DocumentsProgress.vue'
import CloudIngest from '../views/CloudIngest.vue'
import LogsView from '../views/LogsView.vue'
import AskView from '../views/AskView.vue'
import ElasticSearchInterface from '../views/ElasticSearchInterface.vue'
import DocumentDbInterface from '../views/DocumentDbInterface.vue'
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
      path: '/search',
      name: 'search',
      component: Search,
      beforeEnter: authGuard,
    },
    {
      path: '/view-file',
      name: 'view-file',
      component: FileView,
      beforeEnter: authGuard,
    },
    {
      path: '/progress',
      name: 'progress',
      component: DocumentsProgress,
      beforeEnter: authGuard,
    },
    {
      path: '/cloud-ingest',
      name: 'cloud-ingest',
      component: CloudIngest,
      beforeEnter: authGuard,
    },
    {
      path: '/logs',
      name: 'logs',
      component: LogsView,
      beforeEnter: authGuard,
    },
    {
      path: '/ask',
      name: 'ask',
      component: AskView,
      beforeEnter: authGuard,
    },
    {
      path: '/elastic-interface',
      name: 'elastic-interface',
      component: ElasticSearchInterface,
      beforeEnter: authGuard,
    },
    {
      path: '/document-db-interface',
      name: 'document-db-interface',
      component: DocumentDbInterface,
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
