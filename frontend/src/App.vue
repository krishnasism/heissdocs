<template>
  <div>
    <NavigationBar v-if="!['login', 'register', 'help'].includes($route.name)" />
    <div>
      <button data-drawer-target="sidebar-multi-level-sidebar" data-drawer-toggle="sidebar-multi-level-sidebar"
        aria-controls="sidebar-multi-level-sidebar" type="button"
        v-if="!['login', 'register', 'help'].includes($route.name)"
        class="inline-flex mt-20 items-center p-2 ml-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
        <span class="sr-only">Open sidebar</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" fill-rule="evenodd"
            d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z">
          </path>
        </svg>
      </button>
      <aside id="sidebar-multi-level-sidebar" v-if="!['login', 'register', 'help'].includes($route.name)"
        class="fixed mt-16 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
        aria-label="Sidebar">
        <div class="h-full px-3 py-4 overflow-y-auto border-2 dark:bg-gray-800">
          <ul class="space-y-2 font-medium">
            <li>
              <RouterLink :to="{ name: 'dashboard' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'dashboard',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700': true
              }">
                <svg fill="currentColor"
                  class="w-6 h-6 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <path
                    d="M11.47 3.84a.75.75 0 011.06 0l8.69 8.69a.75.75 0 101.06-1.06l-8.689-8.69a2.25 2.25 0 00-3.182 0l-8.69 8.69a.75.75 0 001.061 1.06l8.69-8.69z">
                  </path>
                  <path
                    d="M12 5.432l8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 01-.75-.75v-4.5a.75.75 0 00-.75-.75h-3a.75.75 0 00-.75.75V21a.75.75 0 01-.75.75H5.625a1.875 1.875 0 01-1.875-1.875v-6.198a2.29 2.29 0 00.091-.086L12 5.43z">
                  </path>
                </svg>
                <span class="ml-3">{{ $t('component.dashboard') }}</span>
              </RouterLink>
            </li>
            <li>
              <RouterLink :to="{ name: 'search' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'search',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700': true
              }">
                <svg class="w-6 h-6 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                  fill="none" viewBox="0 0 20 20">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                </svg>
                <span class="ml-3">{{ $t('component.search') }}</span>
              </RouterLink>
            </li>
            <li>
              <RouterLink :to="{ name: 'ask' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'ask',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700': true
              }">
                <svg
                  class="flex-shrink-0 w-6 h-6 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M16 5h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1h-2v3l-4-3H8m4-13H2a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h2v3l4-3h4a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z" />
                </svg>
                <span class="ml-3">{{ $t('component.ask') }}</span>
              </RouterLink>
            </li>
            <li>
              <button type="button"
                class="flex items-center w-full p-2 text-base text-gray-900 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                aria-controls="cloud-operations" data-collapse-toggle="cloud-operations">
                <svg
                  class="flex-shrink-0 w-6 h-6 text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <path clip-rule="evenodd" fill-rule="evenodd"
                    d="M.99 5.24A2.25 2.25 0 013.25 3h13.5A2.25 2.25 0 0119 5.25l.01 9.5A2.25 2.25 0 0116.76 17H3.26A2.267 2.267 0 011 14.74l-.01-9.5zm8.26 9.52v-.625a.75.75 0 00-.75-.75H3.25a.75.75 0 00-.75.75v.615c0 .414.336.75.75.75h5.373a.75.75 0 00.627-.74zm1.5 0a.75.75 0 00.627.74h5.373a.75.75 0 00.75-.75v-.615a.75.75 0 00-.75-.75H11.5a.75.75 0 00-.75.75v.625zm6.75-3.63v-.625a.75.75 0 00-.75-.75H11.5a.75.75 0 00-.75.75v.625c0 .414.336.75.75.75h5.25a.75.75 0 00.75-.75zm-8.25 0v-.625a.75.75 0 00-.75-.75H3.25a.75.75 0 00-.75.75v.625c0 .414.336.75.75.75H8.5a.75.75 0 00.75-.75zM17.5 7.5v-.625a.75.75 0 00-.75-.75H11.5a.75.75 0 00-.75.75V7.5c0 .414.336.75.75.75h5.25a.75.75 0 00.75-.75zm-8.25 0v-.625a.75.75 0 00-.75-.75H3.25a.75.75 0 00-.75.75V7.5c0 .414.336.75.75.75H8.5a.75.75 0 00.75-.75z">
                  </path>
                </svg>
                <span class="flex-1 ml-3 text-left whitespace-nowrap">{{ $t('component.cloudInterface') }}</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="m1 1 4 4 4-4" />
                </svg>
              </button>
              <ul id="cloud-operations" class="hidden py-2 space-y-2">
                <li>
                  <RouterLink :to="{ name: 'cloud-ingest' }" :class="{
                    'bg-blue-50 text-blue-500': $route.name === 'cloud-ingest',
                    'flex items-center w-full p-2 text-gray-600 rounded-lg pl-11 group hover:bg-blue-100 dark:text-white dark:hover:bg-gray-700': true
                  }">
                    <svg class="w-5 h-5  dark:text-white" aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                    </svg>
                    <span class="ml-3">{{ $t('component.cloudIngest') }}</span>
                  </RouterLink>
                </li>
                <li>
                  <RouterLink :to="{ name: 'elastic-interface' }" :class="{
                    'bg-blue-50 text-blue-500': $route.name === 'elastic-interface',
                    'flex items-center w-full p-2 text-gray-600 rounded-lg pl-11 group hover:bg-blue-100 dark:text-white dark:hover:bg-gray-700': true
                  }">
                    <svg class="w-5 h-5  dark:text-white" aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M8 3h4M8 17h4m-9-5V8m14 4V8M1 1h4v4H1V1Zm14 0h4v4h-4V1ZM1 15h4v4H1v-4Zm14 0h4v4h-4v-4Z" />
                    </svg>
                    <span class="ml-3">{{ $t('component.elasticInterface') }}</span>
                  </RouterLink>
                </li>
                <li>
                  <RouterLink :to="{ name: 'document-db-interface' }" :class="{
                    'bg-blue-50 text-blue-500': $route.name === 'document-db-interface',
                    'flex items-center w-full p-2 text-gray-600 rounded-lg pl-11 group hover:bg-blue-100 dark:text-white dark:hover:bg-gray-700': true
                  }">
                    <svg class="w-5 h-5  dark:text-white" aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M17 4c0 1.657-3.582 3-8 3S1 5.657 1 4m16 0c0-1.657-3.582-3-8-3S1 2.343 1 4m16 0v6M1 4v6m0 0c0 1.657 3.582 3 8 3s8-1.343 8-3M1 10v6c0 1.657 3.582 3 8 3s8-1.343 8-3v-6" />
                    </svg>
                    <span class="ml-3">{{ $t('component.exploreNosql') }}</span>
                  </RouterLink>
                </li>
              </ul>
            </li>
          </ul>
          <ul class="pt-4 mt-4 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700">
            <li>
              <RouterLink :to="{ name: 'settings' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'settings',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700': true
              }">
                <svg
                  class="w-6 h-6  group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <path clip-rule="evenodd" fill-rule="evenodd"
                    d="M8.34 1.804A1 1 0 019.32 1h1.36a1 1 0 01.98.804l.295 1.473c.497.144.971.342 1.416.587l1.25-.834a1 1 0 011.262.125l.962.962a1 1 0 01.125 1.262l-.834 1.25c.245.445.443.919.587 1.416l1.473.294a1 1 0 01.804.98v1.361a1 1 0 01-.804.98l-1.473.295a6.95 6.95 0 01-.587 1.416l.834 1.25a1 1 0 01-.125 1.262l-.962.962a1 1 0 01-1.262.125l-1.25-.834a6.953 6.953 0 01-1.416.587l-.294 1.473a1 1 0 01-.98.804H9.32a1 1 0 01-.98-.804l-.295-1.473a6.957 6.957 0 01-1.416-.587l-1.25.834a1 1 0 01-1.262-.125l-.962-.962a1 1 0 01-.125-1.262l.834-1.25a6.957 6.957 0 01-.587-1.416l-1.473-.294A1 1 0 011 10.68V9.32a1 1 0 01.804-.98l1.473-.295c.144-.497.342-.971.587-1.416l-.834-1.25a1 1 0 01.125-1.262l.962-.962A1 1 0 015.38 3.03l1.25.834a6.957 6.957 0 011.416-.587l.294-1.473zM13 10a3 3 0 11-6 0 3 3 0 016 0z">
                  </path>
                </svg>
                <span class="ml-3">{{ $t('component.settings') }}</span>
              </RouterLink>
            </li>
            <li>
              <RouterLink :to="{ name: 'progress' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'progress',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700': true
              }">
                <svg
                  class="flex-shrink-0 w-6 h-6  group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm2 10a1 1 0 10-2 0v3a1 1 0 102 0v-3zm2-3a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1zm4-1a1 1 0 10-2 0v7a1 1 0 102 0V8z"
                    clip-rule="evenodd"></path>
                </svg>
                <span class="ml-3">{{ $t('component.progress') }}</span>
              </RouterLink>
            </li>
            <li>
              <RouterLink :to="{ name: 'logs' }" :class="{
                'bg-blue-50 text-blue-500': $route.name === 'logs',
                'flex items-center p-2 text-gray-600 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700': true
              }">
                <svg
                  class="flex-shrink-0 w-6 h-6  group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path>
                  <path fill-rule="evenodd"
                    d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                    clip-rule="evenodd"></path>
                </svg>
                <span class="ml-3">{{ $t('component.logs') }}</span>
              </RouterLink>
            </li>
            <li>
              <button type="button" @click="logout"
                class="w-full flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-blue-100 dark:hover:bg-gray-700">
                <svg class="w-6 h-6 text-red-500 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                  fill="none" viewBox="0 0 16 16">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4 8h11m0 0-4-4m4 4-4 4m-5 3H3a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h3" />
                </svg>
                <span class="ml-3 text-red-500">{{ $t('component.logout') }}</span>
              </button>
            </li>
          </ul>
        </div>
      </aside>
      <div class="p-4 sm:ml-64">
        <RouterView class="p-4 bg-white self-start mt-20" />
      </div>
    </div>
  </div>
</template>

<script>
import { RouterView } from "vue-router";
import NavigationBar from "@/components/NavigationBar.vue";
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    RouterView,
    NavigationBar
  },
  setup() {
    const { user, isAuthenticated, logout } = useAuth0();
    return {
      user,
      isAuthenticated,
      logout: () => {
        logout({ logoutParams: { returnTo: window.location.origin } });
      }
    };
  },
}
</script> 
