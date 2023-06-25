<template>
    <div>
        <FileEmbed :link="fileLink" height="1000" width="800">
        </FileEmbed>
    </div>
</template>

<script>
import FileEmbed from "@/components/FileEmbed.vue";

import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';

export default {
    components: {
        FileEmbed
    },
    data() {
        return {
            uploadedFileNameList: [],
            bucketName: '',
            fileLink: '',
            authService: null,
        }
    },
    setup() {
        const { user, isAuthenticated } = useAuth0();
        return {
            user,
            isAuthenticated,
            AuthService,
        };
    },
    async mounted() {
        this.authService = new AuthService(this.user.email, this.user.sub);
        this.apiToken = await this.authService.getApiToken();
        const file_name = this.$route.query.file_name;
        const s3_bucket_name = this.$route.query.s3_bucket;
        const page = this.$route.query.page;
        this.fileLink = await this.getFileLink(file_name, s3_bucket_name, page);
    },
    computed: {
        baseApiUrl() {
            return import.meta.env.VITE_BASE_API_URL
        },
        getFileUrl() {
            return this.baseApiUrl + "/pdf/get-file-url"
        },
    },
    methods: {
        async getFileLink(fileName, bucketName, page) {
            if (this.isAuthenticated) {
                const response = await fetch(this.getFileUrl + "?file_name=" + fileName + '&bucket_name=' + bucketName + '&user_email=' + this.user.email,
                    {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json; charset=utf-8',
                            'Authorization': 'Bearer ' + this.apiToken
                        },
                    })
                const data = await response.json();
                return data.file_url + '#page=' + String(page);
            }
        }

    }
};

</script>