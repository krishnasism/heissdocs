<template>
  <div>
    <SearchInput class="mb-8" @submit-search="handleSearch"></SearchInput>
    <DocumentsTable :documents="documents" v-if="!loading" class="w-full"></DocumentsTable>
  </div>
</template>
<script>
import DocumentsTable from "@/components/DocumentsTable.vue";
import SearchInput from "@/components/SearchInput.vue";
import AuthService from "@/services/auth";
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    DocumentsTable,
    SearchInput
  },
  data() {
    return {
      loading: true,
      documents: [],
      apiToken: null,
      authService: null,
    }
  },
  async mounted() {
    const search = this.$route.query.search;
    if (this.isAuthenticated && this.apiToken == null) {
      this.authService = new AuthService(this.user.email, this.user.sub);
      this.apiToken = await this.authService.getApiToken();
    }
    if (search !== undefined || search != null) {
      this.handleSearch(search);
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
  computed: {
    baseApiUrl() {
      return import.meta.env.VITE_BASE_API_URL
    },
    pdfSearchApiUrl() {
      return this.baseApiUrl + "/pdf/search"
    }
  },
  methods: {
    async handleSearch(evt) {
      this.loading = true;
      if (this.isAuthenticated) {
        fetch(this.pdfSearchApiUrl + "?query=" + evt + '&user_email=' + this.user.email,
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
            this.loading = false;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  }
}
</script>