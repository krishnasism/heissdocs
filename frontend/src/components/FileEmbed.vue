<template>
    <embed :src="link" :width="width" :height="height" type="application/pdf">
</template>
<script>
export default {
    name: 'FileEmbed',
    components: {
    },
    props: {
        link: String,
        width: String,
        height: String
    },
}
</script>
