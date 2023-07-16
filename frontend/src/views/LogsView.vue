<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <select v-model="selectInterval" @change="handleIntervalChange"
            class="block w-40 p-2 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            <option value="30">Last 30 mins</option>
            <option value="60">Last 1 hour</option>
            <option value="180">Last 3 hours</option>
            <option value="720">Last 12 hours</option>
            <option value="1440">Last 24 hours</option>
            <option value="-1">All time</option>
        </select>
        <div v-if="logs.length == 0">No logs to show for selected interval</div>
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