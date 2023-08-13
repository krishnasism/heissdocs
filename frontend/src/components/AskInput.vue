<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg class="w-6 h-6 text-gray-400 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 20 18">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M5.5 6.5h.01m4.49 0h.01m4.49 0h.01M18 1H2a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h3v5l5-5h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z" />
                </svg>
            </div>
            <input type="search" id="default-search" v-model="question" @keydown.enter="submitAsk"
                class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                :placeholder="$t('labels.ask')" required>
            <button @click="submitAsk"
                class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{{
                    $t('component.ask') }}</button>
        </div>
    </div>
</template>
<script>
import SettingsService from "@/services/settings";
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import LoadingCircle from '@/components/LoadingCircle.vue';

export default {
    name: 'AskInput',
    props: {
    },
    setup() {
        const { user, isAuthenticated } = useAuth0();
        return {
            user,
            isAuthenticated,
            SettingsService,
            AuthService,
        };
    },
    components: {
        LoadingCircle,
    },
    data() {
        return {
            question: "",
            loading: false,
        }
    },
    async mounted() {
        this.loading = true;
        this.authService = new AuthService(this.user.email, this.user.sub);
        this.apiToken = await this.authService.getApiToken(this.user.email, this.user.sub)
        this.settingsService = new SettingsService(this.user.email, this.isAuthenticated, this.apiToken);
        this.settings = await this.settingsService.getSettings();
        this.loading = false;
    },
    computed: {
    },
    methods: {
        submitAsk() {
            this.$router.push({ path: "/ask", query: { question: this.question } });
            this.$emit("submit-ask", this.question);
        },
    }
}
</script>