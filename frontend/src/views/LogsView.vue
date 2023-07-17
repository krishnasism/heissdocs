<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-2 pointer-events-none">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" class="w-full h-4 mr-2 text-gray-400"
                    viewbox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd"
                        d="M3 3a1 1 0 011-1h12a1 1 0 011 1v3a1 1 0 01-.293.707L12 11.414V15a1 1 0 01-.293.707l-2 2A1 1 0 018 17v-5.586L3.293 6.707A1 1 0 013 6V3z"
                        clip-rule="evenodd" />
                </svg>
            </div>
            <select v-model="selectInterval" @change="handleIntervalChange"
                class="block w-48 pl-8 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option value="30">{{ $t('labels.last30mins') }}</option>
                <option value="60">{{ $t('labels.last1hour') }}</option>
                <option value="180">{{ $t('labels.last3hours') }}</option>
                <option value="720">{{ $t('labels.last12hours') }}</option>
                <option value="1440">{{ $t('labels.last24hours') }}</option>
                <option value="-1">{{ $t('labels.allTime') }}</option>
            </select>
        </div>
        <div v-if="logs.length == 0">{{ $t('labels.noLogsMessage') }}</div>
        <LogsTable v-else :logs="logs"></LogsTable>
    </div>
</template>
<script>
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import LogsTable from "@/components/LogsTable.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';

export default {
    components: {
        LogsTable,
        LoadingCircle,
    },
    data() {
        return {
            apiToken: '',
            logs: [],
            timer: '',
            authService: null,
            loading: false,
            selectInterval: "30",
        }
    },
    async mounted() {
        this.loading = true;
        this.authService = new AuthService(this.user.email, this.user.sub);
        this.apiToken = await this.authService.getApiToken();
        this.logs = await this.getLogs();
        this.timer = setInterval(this.getLogs, 10000);
        this.loading = false;
    },
    setup() {
        const { user, isAuthenticated } = useAuth0();
        return {
            user,
            isAuthenticated,
        };
    },
    beforeUnmount() {
        this.cancelAutoUpdate();
    },
    computed: {
        baseApiUrl() {
            return import.meta.env.VITE_BASE_API_URL
        },
        logsUrl() {
            return this.baseApiUrl + "/logs"
        }
    },
    methods: {
        cancelAutoUpdate() {
            clearInterval(this.timer);
        },
        handleIntervalChange() {
            this.getLogs();
        },
        async getLogs() {
            if (this.isAuthenticated) {
                let url = ""
                if (this.selectInterval === "-1") {
                    url = `${this.logsUrl}?user_email=system`;
                } else {
                    const intervalInMinutes = parseInt(this.selectInterval);
                    const endTime = new Date();
                    const startTime = new Date(endTime.getTime() - intervalInMinutes * 60 * 1000);
                    url = `${this.logsUrl}?user_email=system&start_time=${encodeURIComponent(
                        startTime.toISOString()
                    )}&end_time=${encodeURIComponent(endTime.toISOString())}`;
                }
                fetch(
                    url,
                    {
                        method: "GET",
                        headers: {
                            Authorization: "Bearer " + this.apiToken,
                            "Content-Type": "application/json; charset=utf-8",
                        },
                    }
                )
                    .then((response) => response.json())
                    .then((data) => {
                        this.logs = data.logs;
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            }
        },
    }
}
</script>