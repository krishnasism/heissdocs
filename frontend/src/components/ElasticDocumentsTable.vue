<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.fileName')}}
            </th>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.pageNumber')}}
            </th>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.uploadedOn')}}
            </th>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.fileId')}}
            </th>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.bucket')}}
            </th>
            <th scope="col" class="px-2 py-3 text-right">
            </th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(document, index) in documents" :key="index">
            <tr
              class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
            >
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
                class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 focus:outline-none dark:focus:ring-red-800"
                >{{ $t('labels.deleteFile') }}</button>
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
        }
    },
    mounted() {
    },
    computed: {

    },
    methods: {
        async deleteDocument(document) {
            this.$emit("delete-document", document);
        },
    }
}
</script>