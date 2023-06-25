<template>
    <div>
        <DocumentsProgressTable :documents="documents" v-if="documents"></DocumentsProgressTable>
        <p v-else>No files in progress...</p>
    </div>
</template>
<script>
import getApiToken from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';
import DocumentsProgressTable from "@/components/DocumentsProgressTable.vue";

export default {
    components: {
        DocumentsProgressTable
    },
    data() {
        return {
            apiToken: String,
            documents: Array,
            timer: '',
        }
    },
    async mounted() {
        this.apiToken = await this.getApiToken(this.user.email, this.user.sub);
        this.documents = await this.getDocumentsProgress();
        this.timer = setInterval(this.getDocumentsProgress, 10000);
    },
    setup() {
        const { user, isAuthenticated } = useAuth0();
        return {
            user,
            isAuthenticated,
            getApiToken
        };
    },
    beforeUnmount () {
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
        cancelAutoUpdate () {
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