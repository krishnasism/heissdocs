<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor"
                    viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
            </div>
            <input type="search" id="default-search" v-model="question" @keydown.enter="submitAsk"
                class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                :placeholder="$t('component.ask')" required>
            <button @click="submitAsk"
                class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{{ $t('labels.ask') }}</button>
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