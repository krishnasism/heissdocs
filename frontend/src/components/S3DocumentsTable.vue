<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3">
              {{ $t('labels.fileName')}}
            </th>
            <th scope="col" class="px-2 py-3 text-right">
              
            </th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(s3DocumentName, index) in s3Documents" :key="index">
            <tr
              class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
            >
              <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ s3DocumentName }}
              </td>
              <td class="px-2 py-4 text-right">
                <button @click="sendToParse(s3DocumentName)"
                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                >{{ $t('labels.sendToParser') }}</button>
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
    name: 'S3DocumentsTable',
    props: {
        s3Documents: {
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
        async sendToParse(s3DocumentName) {
            this.$emit("parse-document", s3DocumentName);
        },
    }
}
</script>