import { createI18n } from "vue-i18n";
import en from "./en.json";
import de from "./de.json";

const defaultLocale = "en";

const storedLocale = localStorage.getItem("preferredLanguage");

const i18n = createI18n({
    locale: storedLocale || defaultLocale,
    messages: {
        en,
        de
    },
    fallbackLocale: defaultLocale
});

export default i18n;