<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="py-8 max-w-screen-xl lg:py-16 lg:px-6">
                <div class="mx-auto max-w-screen-sm text-center">
                    <h1
                        class="mb-4 text-md tracking-tight font-extrabold lg:text-9xl text-primary-200 dark:text-primary-200">
                        heißdocs</h1>
                    <p class="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">Start
                        getting your PDFs in Order!</p>
                    <a @click="login"
                        class="inline-flex text-white bg-blue-600 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900 my-4">Login</a>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import { useAuth0 } from '@auth0/auth0-vue';
export default {
    setup() {
        const { loginWithRedirect } = useAuth0();
        return {
            login: () => {
                loginWithRedirect();
            }
        };
    }
};
</script>