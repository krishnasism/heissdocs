<template>
    <div class="text-sm text-red-600 rounded-lg dark:text-red-400" role="alert">
        <span class="font-medium">{{ header }}</span> {{ message }}
    </div>
</template>
<script>
export default {
    name: 'ErrorMessage',
    props: {
        header: String,
        message: String
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
