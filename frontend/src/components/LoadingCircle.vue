<template>
    <div class="loading-circle">
        <button @click="refreshPage" v-if="showRefreshMessage">
            <svg class="w-8 h-8 text-gray-600 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                fill="none" viewBox="0 0 18 20">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97" />
            </svg>
        </button>
        <div class="circle" v-else></div>
    </div>
</template>

<script>
export default {
    name: 'LoadingCircle',
    data() {
        return {
            showRefreshMessage: false,
        };
    },
    mounted() {
        setTimeout(() => {
            this.showRefreshMessage = true;
        }, 30000);  //30s
    },
    methods: {
        refreshPage() {
            location.reload();
        },
    },
};
</script>


<style>
.loading-circle {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 4px solid #ccc;
    border-top-color: #888;
    animation: spin 1s infinite linear;
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}
</style>
  