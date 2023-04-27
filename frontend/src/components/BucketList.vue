<template>
    <div>
        <select
            class="bg-white-50 border border-gray-200 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-15 dark:bg-gray-200 dark:border-gray-200 dark:placeholder-gray-200 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 p-0 pl-4 h-8">
            <option @select="bucketSelected(bucketName)" v-for="bucketName in bucketList" :key="bucketName" :value="bucketName">
                {{ bucketName }}
            </option>
        </select>
    </div>
</template>
  
<script>
export default {
    name: 'BucketList',
    components: {
    },
    props: {
        bucketList: Array
    },
    methods: {
        bucketSelected(bucketName) {
            this.$emit('bucketSelected', bucketName);
        }
    }
}
</script>
