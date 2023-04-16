<template>
  <div>
    <span>Dashboard</span>
    <p>
      User does all operations like Upload, Search, etc. to happen from here
    </p>
    <SearchInput class="m-8"></SearchInput>
    <FileUpload class="m-8 w-80"></FileUpload>
  </div>
</template>

<script setup>
import FileUpload from "@/components/FileUpload.vue";
import SearchInput from "@/components/SearchInput.vue";

</script>