<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3" @click="sortByFileName">
                            <div class="flex items-center">
                                {{ $t('labels.fileName') }}
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <div class="flex items-center">
                                {{ $t('labels.pageNumber') }}
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" @click="sortByUploadedOn">
                            <div class="flex items-center">
                                {{ $t('labels.uploadedOn') }}
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="document in sortedDocuments" :key="document.id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {{ document.file_name.split(".pdf_")[0] + ".pdf" }}
                        </th>
                        <td class="px-6 py-4">{{ document.page_num }}</td>
                        <td class="px-6 py-4">{{ document.made_on }}</td>
                        <td class="px-6 py-4" v-if="document.s3_bucket_name">
                            <a :href="`/view-file?file_name=${document.s3_blob_file_name}&page=${document.page_num}&bucketName=${document.s3_bucket_name}`"
                                class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
                                target="_blank">{{ $t('labels.view') }}</a>
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
            required: true,
        },
    },
    data() {
        return {
            sortColumn: '',
            sortDirection: 'asc',
        }
    },
    computed: {
        sortedDocuments() {
            if(!this.documents) return [];
            const sortedDocs = [...this.documents];
            if (this.sortColumn === 'file_name') {
                sortedDocs.sort((a, b) => {
                    const nameA = a.file_name.toLowerCase();
                    const nameB = b.file_name.toLowerCase();
                    return this.sortDirection === 'asc'
                        ? nameA.localeCompare(nameB)
                        : nameB.localeCompare(nameA);
                });
            } else if (this.sortColumn === 'made_on') {
                sortedDocs.sort((a, b) => {
                    const dateA = new Date(a.made_on);
                    const dateB = new Date(b.made_on);
                    return this.sortDirection === 'asc' ? dateA - dateB : dateB - dateA;
                });
            }
            return sortedDocs;
        },
    },
    methods: {
        sortByFileName() {
            if (this.sortColumn === 'file_name') {
                this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
            } else {
                this.sortColumn = 'file_name';
                this.sortDirection = 'asc';
            }
        },
        sortByUploadedOn() {
            if (this.sortColumn === 'made_on') {
                this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
            } else {
                this.sortColumn = 'made_on';
                this.sortDirection = 'asc';
            }
        }
    },
}
</script>
  