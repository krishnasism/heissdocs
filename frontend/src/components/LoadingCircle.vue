<template>
    <div class="loading-circle">
        <div class="circle"></div>
    </div>
</template>

<script>
export default {
  name: 'LoadingCircle',
}
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
  