<template>
  <div>
    <div class="relative overflow-x-auto">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3 w-5" @click="sortBy('document_name')">
              <div class="flex items-center">
                {{ $t('labels.fileName') }}
                <a href="#">
                  <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                    viewBox="0 0 24 24">
                    <path
                      d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                  </svg>
                </a>
              </div>
            </th>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.pageNumber') }}
            </th>
            <th scope="col" class="px-6 py-3 w-5" @click="sortBy('made_on')">
              <div class="flex items-center">
                {{ $t('labels.uploadedOn') }}
                <a href="#">
                  <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                    viewBox="0 0 24 24">
                    <path
                      d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                  </svg>
                </a>
              </div>
            </th>
            <th scope="col" class="px-6 py-3 w-5" @click="sortBy('blob_file_name')">
              <div class="flex items-center">
                {{ $t('labels.fileId') }}
                <a href="#">
                  <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                    viewBox="0 0 24 24">
                    <path
                      d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                  </svg>
                </a>
              </div>
            </th>
            <th scope="col" class="px-6 py-3 w-5" @click="sortBy('bucket_name')">
              <div class="flex items-center">
                {{ $t('labels.bucket') }}
                <a href="#">
                  <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                    viewBox="0 0 24 24">
                    <path
                      d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                  </svg>
                </a>
              </div>
            </th>
            <th scope="col" class="px-2 py-3 text-right">
            </th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(document, index) in sortedDocuments" :key="index">
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ document.file_name }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ document.page_num }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ document.made_on }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ document.blob_file_name }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ document.bucket_name }}
              </td>
              <td class="px-2 py-4 text-right">
                <button @click="deleteDocument(document)"
                  class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 focus:outline-none dark:focus:ring-red-800">{{
                    $t('labels.deleteFile') }}</button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ElasticDocumentsTable',
  props: {
    documents: {
      type: Array,
      required: true
    },
  },
  data() {
    return {
      sortColumn: '',
      sortDirection: 'asc',
    }
  },
  mounted() {
  },
  computed: {
    sortedDocuments() {
      const sortedDocs = [...this.documents];
      if (this.sortColumn === 'document_name') {
        sortedDocs.sort((a, b) => {
          const stageA = String(a.file_name).toLowerCase();
          const stageB = String(b.file_name).toLowerCase();
          return this.sortDirection === 'asc'
            ? stageA.localeCompare(stageB)
            : stageB.localeCompare(stageA);
        });
      } else if (this.sortColumn === 'made_on') {
        sortedDocs.sort((a, b) => {
          const stageA = new Date(a.made_on);
          const stageB = new Date(b.made_on);
          return this.sortDirection === 'asc' ? stageA - stageB : stageB - stageA;
        });
      } else if (this.sortColumn === 'blob_file_name') {
        sortedDocs.sort((a, b) => {
          const stageA = String(a.blob_file_name).toLowerCase();
          const stageB = String(b.blob_file_name).toLowerCase();
          return this.sortDirection === 'asc'
            ? stageA.localeCompare(stageB)
            : stageB.localeCompare(stageA);
        });
      } else if (this.sortColumn === 'bucket_name') {
        sortedDocs.sort((a, b) => {
          const stageA = String(a.bucket_name).toLowerCase();
          const stageB = String(b.bucket_name).toLowerCase();
          return this.sortDirection === 'asc'
            ? stageA.localeCompare(stageB)
            : stageB.localeCompare(stageA);
        });
      }
      return sortedDocs;
    },
  },
  methods: {
    async deleteDocument(document) {
      this.$emit("delete-document", document);
    },
    sortBy(column) {
      if (this.sortColumn === column) {
        this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
      } else {
        this.sortColumn = column;
        this.sortDirection = 'asc';
      }
    },
  }
}
</script>