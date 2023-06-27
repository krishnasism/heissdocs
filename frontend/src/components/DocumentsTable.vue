<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="p-4">
                            <div class="flex items-center">
                                <input id="checkbox-all-search" type="checkbox"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <label for="checkbox-all-search" class="sr-only">checkbox</label>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            File Name
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Page Number
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Uploaded On
                        </th>
                        <th scope="col" class="px-6 py-3">

                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="document in documents"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                            <div class="flex items-center">
                                <input id="checkbox-table-search-1" type="checkbox"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                            </div>
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {{ document.file_name.split(".pdf_")[0] + ".pdf" }}
                        </th>
                        <td class="px-6 py-4">
                            {{ document.page_num }}
                        </td>
                        <td class="px-6 py-4">
                            {{ document.made_on }}
                        </td>
                        <td class="px-6 py-4" v-if="document.s3_bucket_name">
                            <a :href="'/view-file?file_name=' + document.s3_blob_file_name + '&page=' + document.page_num + '&s3_bucket=' + document.s3_bucket_name"
                                class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
                                target="_blank">View</a>
                        </td>
                    </tr>

                </tbody>
            </table>

        </div>
    </div>
</template>
<script>
export default {
    name: 'DocumentsTable',
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

    }
}
</script>