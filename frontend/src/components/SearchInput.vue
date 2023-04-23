<template>
    <div>

        <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor"
                    viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
            </div>
            <input type="search" id="default-search" v-model="searchText" @keydown.enter="submitSearch"
                class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                :placeholder="$t('component.search')" required>
        </div>

    </div>
</template>
<script>
export default {
    name: 'SearchInput',
    props: {
    },
    data() {
        return {
            searchText: '',
        }
    },
    mounted() {
    },
    computed: {
    },
    methods: {
        submitSearch() {
            this.$router.push({ path: "/search", query: { search: this.searchText } });
            this.$emit("submit-search", this.searchText);
        },
    }
}
</script>