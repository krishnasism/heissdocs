<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3 w-5">
                            File Name
                        </th>
                        <th scope="col" class="px-6 py-3 w-5">
                            Status
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Progress
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="document in documents"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white w-5 overflow-x-clip">
                            {{ document.document_name }}
                        </th>
                        <td class="px-6 py-4 w-5">
                            {{ document.stage }}
                        </td>
                        <td class="px-6 py-4">
                            <ProgressBar :progressPercent="document.total_pages > 0 ? Math.trunc((document.pages_parsed / document.total_pages) * 100) : 0"></ProgressBar>
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
        ProgressBar
    },
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