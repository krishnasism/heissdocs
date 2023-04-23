<template>
    <div>
        <nav class="bg-white dark:bg-gray-900 fixed w-full z-20 top-0 left-0 border-b border-gray-200 dark:border-gray-600">
            <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
                <a href="/" class="flex items-center">
                    <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">heißdocs</span>
                </a>
                <div class="flex md:order-2">
                    <LanguageSwitcher class="mr-4"></LanguageSwitcher>

                    <button type="button" @click="logout"
                        class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        Logout
                    </button>
                    <button data-collapse-toggle="navbar-sticky" type="button"
                        class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                        aria-controls="navbar-sticky" aria-expanded="false">
                        <span class="sr-only">Open main menu</span>
                        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                                clip-rule="evenodd"></path>
                        </svg>
                    </button>
                </div>
                <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                    <ul
                        class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                        <li>
                            <RouterLink :to="{ name: 'dashboard' }">
                                <p>Dashboard</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'settings' }">
                                <p>Settings</p>
                            </RouterLink>
                        </li>
                        <!-- <li>
                            <RouterLink :to="{ name: 'news' }">
                                <p>News</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'contact' }">
                                <p>Contact</p>
                            </RouterLink>
                        </li> -->
                        <li>
                            <RouterLink :to="{ name: 'setup' }">
                                <p>Setup</p>
                            </RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

    </div>
</template>
<script>
import { RouterLink } from 'vue-router';
import { useAuth0 } from "@auth0/auth0-vue";
import LanguageSwitcher from "@/components/LanguageSwitcher.vue";

export default {
    components: {
        RouterLink, LanguageSwitcher
    },
    setup() {
        const { logout } = useAuth0();

        return {
            logout: () => {
                logout({ logoutParams: { returnTo: window.location.origin } });
            }
        };
    }
};

</script>