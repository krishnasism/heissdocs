<template>
  <div>
    <span>Dashboard</span>
    <div v-if="isAuthenticated">
      <p>Hello {{ user.nickname }}</p>
    </div>
    <SearchInput class="m-8"></SearchInput>
    <FileUpload class="m-8 w-80"></FileUpload>
  </div>
</template>

<script>
import FileUpload from "@/components/FileUpload.vue";
import SearchInput from "@/components/SearchInput.vue";
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  components: {
    FileUpload, SearchInput
  },
  setup() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated
    };
  },
  mounted() {
    console.log(this.user)
  }
};

</script>