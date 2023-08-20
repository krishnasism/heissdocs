<template>
    <div>
        <div class="relative w-full bg-gray-200 rounded-full dark:bg-gray-700 h-4">
    <div class="absolute top-0 left-0 bg-blue-600 text-xs font-medium text-blue-100 leading-none rounded-full transition-all duration-500 ease-in-out pl-4 h-4"
        :style="'width:' + (progressPercent > 100 ? 100 : progressPercent) + '%'">{{ progressPercent > 100 ? 100 : progressPercent }}%</div>
</div>
    </div>
</template>

<script>
export default {
    name: 'ProgressBar',
    props: {
        progressPercent: Number,
    }
}
</script>