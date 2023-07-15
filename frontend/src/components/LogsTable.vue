<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3" @click="sortByLogLevel">
                            <div class="flex items-center">
                                Log Level
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" @click="sortByMessage">
                            <div class="flex items-center">
                                Message
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" @click="sortByCreatedOn">
                            <div class="flex items-center">
                                Date
                                <a href="#">
                                    <svg class="w-3 h-3 ml-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 24 24">
                                        <path
                                            d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z" />
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" @click="sortByCaller">
                            <div class="flex items-center">
                                Caller Info
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
                    <tr v-for="log in sortedLogs" :key="log.log_id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {{ log.log_level }}
                        </td>
                        <td class="px-6 py-4">{{ log.message }}</td>
                        <td class="px-6 py-4">{{ formatDate(log.created_on) }}</td>
                        <td class="px-6 py-4">
                            {{ log.caller_filename }} - {{ log.caller_function_name }}() - Line
                            {{ log.caller_line_number }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
  
<script>
export default {
    name: "LogsTable",
    props: {
        logs: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            sortColumn: "",
            sortDirection: "asc",
        };
    },
    computed: {
        sortedLogs() {
            if (!this.logs) return [];
            const sortedLogs = [...this.logs];
            if (this.sortColumn === "log_level") {
                sortedLogs.sort((a, b) => {
                    const levelA = a.log_level.toLowerCase();
                    const levelB = b.log_level.toLowerCase();
                    return this.sortDirection === "asc"
                        ? levelA.localeCompare(levelB)
                        : levelB.localeCompare(levelA);
                });
            } else if (this.sortColumn === "message") {
                sortedLogs.sort((a, b) => {
                    const messageA = a.message.toLowerCase();
                    const messageB = b.message.toLowerCase();
                    return this.sortDirection === "asc"
                        ? messageA.localeCompare(messageB)
                        : messageB.localeCompare(messageA);
                });
            } else if (this.sortColumn === "created_on") {
                sortedLogs.sort((a, b) => {
                    const dateA = new Date(a.created_on);
                    const dateB = new Date(b.created_on);
                    return this.sortDirection === "asc" ? dateA - dateB : dateB - dateA;
                });
            } else if (this.sortColumn === "caller") {
                sortedLogs.sort((a, b) => {
                    const callerA =
                        a.caller_filename +
                        a.caller_function_name +
                        a.caller_line_number;
                    const callerB =
                        b.caller_filename +
                        b.caller_function_name +
                        b.caller_line_number;
                    return this.sortDirection === "asc"
                        ? callerA.localeCompare(callerB)
                        : callerB.localeCompare(callerA);
                });
            }
            return sortedLogs;
        },
    },
    methods: {
        sortByLogLevel() {
            this.setSortColumn("log_level");
        },
        sortByMessage() {
            this.setSortColumn("message");
        },
        sortByCreatedOn() {
            this.setSortColumn("created_on");
        },
        sortByCaller() {
            this.setSortColumn("caller");
        },
        setSortColumn(column) {
            if (this.sortColumn === column) {
                this.sortDirection = this.sortDirection === "asc" ? "desc" : "asc";
            } else {
                this.sortColumn = column;
                this.sortDirection = "asc";
            }
        },
        formatDate(dateStr) {
            const options = {
                year: "numeric",
                month: "short",
                day: "numeric",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: false,
            };
            return new Date(dateStr).toLocaleDateString("en-US", options);
        },
    },
};
</script>
  

