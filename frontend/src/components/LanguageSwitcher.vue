<template>
    <div>
        <select v-model="selectedLang"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-15 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            <option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang.c">
                {{ lang.f }}
            </option>
        </select>
    </div>
</template>
  
<script>
export default {
    name: 'LanguageSwitcher',
    data() {
        return {
            langs: [
                { 'c': 'en', 'f': '🇬🇧' }, { 'c': 'de', 'f': '🇩🇪' }
            ],
            selectedLang: localStorage.getItem("preferredLanguage") || 'en'
        };
    },
    watch: {
        selectedLang(newValue) {
            this.$i18n.locale = newValue;
            localStorage.setItem("preferredLanguage", newValue);
        }
    }
};
</script>
  