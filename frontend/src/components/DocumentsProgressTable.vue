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
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3 w-5" @click="sortBy('stage')">
                            <div class="flex items-center">
                                {{ $t('labels.status') }}
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" @click="sortBy('pages_parsed')">
                            <div class="flex items-center">
                                {{ $t('labels.progress') }}
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="document in sortedDocuments" :key="document.id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row"
                            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white w-5 overflow-x-clip">
                            {{ document.document_name }}
                        </th>
                        <td class="px-6 py-4 w-5">
                            {{ document.stage }}
                        </td>
                        <td>
                            <ProgressBar
                                :progressPercent="document.total_pages > 0 ? Math.trunc((document.pages_parsed / document.total_pages) * 100) : 0">
                            </ProgressBar>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
  
<script>
import ProgressBar from '@/components/ProgressBar.vue';

export default {
    name: 'DocumentsProgressTable',
    components: {
        ProgressBar,
    },
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
        };
    },
    computed: {
        sortedDocuments() {
            const sortedDocs = [...this.documents];
            if (this.sortColumn === 'document_name') {
                sortedDocs.sort((a, b) => {
                    const nameA = a.document_name.toLowerCase();
                    const nameB = b.document_name.toLowerCase();
                    return this.sortDirection === 'asc'
                        ? nameA.localeCompare(nameB)
                        : nameB.localeCompare(nameA);
                });
            } else if (this.sortColumn === 'stage') {
                sortedDocs.sort((a, b) => {
                    const stageA = a.stage.toLowerCase();
                    const stageB = b.stage.toLowerCase();
                    return this.sortDirection === 'asc'
                        ? stageA.localeCompare(stageB)
                        : stageB.localeCompare(stageA);
                });
            } else if (this.sortColumn === 'pages_parsed') {
                sortedDocs.sort((a, b) => {
                    return this.sortDirection === 'asc'
                        ? a.pages_parsed - b.pages_parsed
                        : b.pages_parsed - a.pages_parsed;
                });
            }
            return sortedDocs;
        },
    },
    methods: {
        sortBy(column) {
            if (this.sortColumn === column) {
                this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
            } else {
                this.sortColumn = column;
                this.sortDirection = 'asc';
            }
        },
    },
};
</script>
  