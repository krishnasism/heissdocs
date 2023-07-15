<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <LogsTable :logs="logs" v-if="logs"></LogsTable>
        <p v-else>No Logs to show</p>
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
        async getLogs() {
            if (this.isAuthenticated) {
                fetch(this.logsUrl + "?user_email=system",
                    {
                        method: 'GET',
                        headers: {
                            'Authorization': 'Bearer ' + this.apiToken,
                            'Content-Type': 'application/json; charset=utf-8'
                        },
                    })
                    .then(response => response.json())
                    .then(data => {
                        this.logs = data.logs;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            }
        }
    }
}
</script>