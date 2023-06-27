<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <DocumentsProgressTable :documents="documents" v-if="documents"></DocumentsProgressTable>
        <p v-else>No files in progress...</p>
    </div>
</template>
<script>
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import DocumentsProgressTable from "@/components/DocumentsProgressTable.vue";
import LoadingCircle from '@/components/LoadingCircle.vue';

export default {
    components: {
        DocumentsProgressTable,
        LoadingCircle,
    },
    data() {
        return {
            apiToken: String,
            documents: Array,
            timer: '',
            authService: null,
            loading: false,
        }
    },
    async mounted() {
        this.loading = true;
        this.authService = new AuthService(this.user.email, this.user.sub);
        this.apiToken = await this.authService.getApiToken();
        this.documents = await this.getDocumentsProgress();
        this.timer = setInterval(this.getDocumentsProgress, 10000);
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
        documentsProgressUrl() {
            return this.baseApiUrl + "/documents-progress"
        }
    },
    methods: {
        cancelAutoUpdate() {
            clearInterval(this.timer);
        },
        async getDocumentsProgress() {
            if (this.isAuthenticated) {
                fetch(this.documentsProgressUrl + "?userEmail=" + this.user.email,
                    {
                        method: 'GET',
                        headers: {
                            'Authorization': 'Bearer ' + this.apiToken,
                            'Content-Type': 'application/json; charset=utf-8'
                        },
                    })
                    .then(response => response.json())
                    .then(data => {
                        this.documents = data.documents;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            }
        }
    }
}
</script>