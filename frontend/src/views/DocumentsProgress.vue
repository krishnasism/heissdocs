<template>
    <LoadingCircle v-if="loading"></LoadingCircle>
    <div v-else>
        <DocumentsProgressTable :documents="documents" v-if="documents"></DocumentsProgressTable>
        <p v-else>{{ $t('labels.noFilesInProgress') }}</p>
        <div class="inline-flex mt-2 xs:mt-0">
            <button v-if="hasPreviousPage" @click="handlePreviousPage"
                class="flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                <svg class="w-3.5 h-3.5 mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                    viewBox="0 0 14 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 5H1m0 0 4 4M1 5l4-4" />
                </svg>
                {{ $t('labels.previousPageButton') }}
            </button>
            <button v-if="hasNextPage" @click="handleNextPage"
                class="flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-l border-gray-700 rounded-r hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                {{ $t('labels.nextPageButton') }}
                <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                    viewBox="0 0 14 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M1 5h12m0 0L9 1m4 4L9 9" />
                </svg>
            </button>
        </div>
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
            apiToken: '',
            documents: [],
            timer: '',
            authService: null,
            loading: false,
            currentPage: 1,
            perPage: 10,
            hasNextPage: false,
            hasPreviousPage: false,
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
        handleNextPage() {
            this.currentPage++;
            this.getDocumentsProgress();
        },
        handlePreviousPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.getDocumentsProgress();
            }
        },
        async getDocumentsProgress() {
            if (this.isAuthenticated) {
                fetch(this.documentsProgressUrl + "?userEmail=" + this.user.email + `&page=${this.currentPage}&per_page=${this.perPage}`,
                    {
                        method: 'GET',
                        headers: {
                            'Authorization': 'Bearer ' + this.apiToken,
                            'Content-Type': 'application/json; charset=utf-8'
                        },
                    })
                    .then(response => response.json())
                    .then(data => {
                        this.hasNextPage = data.has_next_page;
                        this.hasPreviousPage = data.has_previous_page;
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