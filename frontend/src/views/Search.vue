<template>
  <div>
    <p>
      Search
    </p>
    <SearchInput class="m-8" @submit-search="handleSearch"></SearchInput>
    <DocumentsTable :documents="documents" v-if="!loading" class="w-full"></DocumentsTable>
  </div>
</template>
<script>
import DocumentsTable from "@/components/DocumentsTable.vue";
import SearchInput from "@/components/SearchInput.vue";

export default {
  components: {
    DocumentsTable,
    SearchInput
  },
  mounted() {
    const search = this.$route.query.search;
    this.handleSearch(search);
  },
  data() {
    return {
      loading: true,
      documents: [],
    }
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
    handleSearch(evt) {
      this.loading = true;
      fetch(this.pdfSearchApiUrl + "?query=" + evt)
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
</script>