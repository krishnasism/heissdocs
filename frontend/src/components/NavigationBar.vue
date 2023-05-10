<template>
    <div>
        <nav class="bg-white dark:bg-gray-900 fixed w-full z-50 top-0 left-0 border-b border-gray-200 dark:border-gray-600">
            <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
                <a href="/" class="flex items-center">
                    <img src="/public/logo/logo.png" height="20" width="100" alt="heißdocs">
                    <!-- <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">heißdocs</span> -->
                </a>
                <div class="flex md:order-2">
                    <LanguageSwitcher class="mr-4"></LanguageSwitcher>

                    <button type="button" @click="logout"
                        class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        {{ $t('component.logout') }}
                    </button>
                </div>
                <!-- <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                    <ul
                        class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                        <li>
                            <RouterLink :to="{ name: 'dashboard' }">
                                <p>{{ $t('component.dashboard') }}</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'settings' }">
                                <p>{{ $t('component.settings') }}</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'news' }">
                                <p>News</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'contact' }">
                                <p>Contact</p>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink :to="{ name: 'setup' }">
                                <p>{{ $t('component.setup') }}</p>
                            </RouterLink>
                        </li>
                    </ul>
                </div> -->
            </div>
        </nav>



</div></template>
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