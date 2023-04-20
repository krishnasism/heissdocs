<template>
  <div>
    <NavigationBar v-if="!['login', 'register', 'help'].includes($route.name)"/>
    <RouterView class="p-4 bg-white self-start mt-20"/>
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
import NavigationBar from "@/components/NavigationBar.vue";
</script> 

<style scoped></style>