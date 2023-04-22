<template>
    <div>
        <h2 class="mb-2 text-lg font-semibold text-gray-900 dark:text-white">Uploaded</h2>
        <ul class="max-w-md space-y-1 text-gray-500 list-disc list-inside dark:text-gray-400">
            <div v-for="fileName in fileNameList">
            <li>
                {{ fileName }}
            </li>
            </div>
        </ul>
    </div>
</template>
<script>
export default {
    name: 'FileList',
    props: {
        fileNameList: Array
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