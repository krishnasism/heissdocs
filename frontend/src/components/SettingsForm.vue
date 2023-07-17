<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="px-4 ml-4 max-w-4xl">
                <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">{{ $t('labels.settings') }}</h2>
                <p class="mb-4 font-black">{{ $t('labels.cloudProvider') }}</p>
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                    <div class="sm:col-span-2">
                        <label for="awsAccessKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            {{ $t('labels.awsAccessKey') }}</label>
                        <input type="password" name="awsAccessKey" id="awsAccessKey" @focus="showTip('awsAccessKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsAccessKeyPlaceholder')" v-model="awsAccessKey">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsSecret" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            {{ $t('labels.awsSecret') }}</label>
                        <input type="password" name="awsSecret" id="awsSecret" @focus="showTip('awsSecret')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsSecretPlaceholder')" v-model="awsSecret">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsRegion" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.awsRegion') }}</label>
                        <input type="text" name="awsRegion" id="awsRegion" @focus="showTip('awsRegion')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsRegionPlaceholder')" v-model="awsRegion">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.destinationBuckets') }}</label>
                        <input type="text" name="bucketsList" id="bucketsList" @focus="showTip('bucketsList')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsBucketListPlaceholder')"
                            v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.s3BucketSource') }}</label>
                        <input type="text" name="scanBucket" id="scanBucket" @focus="showTip('scanBucket')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsScanBucketPlaceholder')"
                            v-model="scanBucket">
                    </div>
                    <p class="mt-5 font-black">{{ $t('labels.nosqlEngineHost') }}</p>
                    <div class="sm:col-span-2">
                        <label for="noSqlProvider"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.noSqlEngineHostHelper') }}</label>
                        <select v-model="noSqlProvider" id="noSqlProvider" @focus="showTip('noSqlProvider')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected value="default">{{ $t('labels.noSqlEngineHostDropdown') }}</option>
                            <option value="aws">Amazon Web Services</option>
                            <option value="mongodb">MongoDB [Unsupported]</option>
                            <option value="azure">MS Azure [Unsupported]</option>
                            <option value="other">Other [Unsupported]</option>
                        </select>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="documentTableName"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.documentTableName') }}</label>
                        <input type="text" name="documentTableName" id="documentTableName"
                            @focus="showTip('documentTableName')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.documentTableNamePlaceholder')"
                            v-model="documentTableName">
                    </div>
                    <p class="mt-5 font-black">{{ $t('labels.elasticsearchSettings') }}</p>
                    <div class="sm:col-span-2">
                        <button type="button" @click="overrideElasticLocalSettings"
                            @mouseover="showTip('overrideElasticLocalSettings')" id="overrideElasticLocalSettings"
                            name="overrideElasticLocalSettings"
                            class="text-yellow-400 hover:text-white border border-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1 text-center mr-2 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-white dark:hover:bg-yellow-400 dark:focus:ring-yellow-900">
                            {{ $t('labels.setlocalmode') }}
                        </button>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="elasticSearchIndex"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.elasticSearchIndex') }}</label>
                        <input type="text" name="elasticSearchIndex" id="elasticSearchIndex"
                            @focus="showTip('elasticSearchIndex')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchIndexPlaceholder')" v-model="elasticSearchIndex">
                        <br />
                        <label for="elasticSearchHost"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.elasticSearchHostUrl') }}</label>
                        <input type="text" name="elasticSearchHost" id="elasticSearchHost"
                            @focus="showTip('elasticSearchHost')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchHostPlaceholder')" v-model="elasticSearchHost">
                        <br />
                        <label for="elasticSearchPort"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.elasticSearchPort') }}</label>
                        <input type="text" name="elasticSearchPort" id="elasticSearchPort"
                            @focus="showTip('elasticSearchPort')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchPortPlaceholder')" v-model="elasticSearchPort">
                        <br />
                        <label for="elasticSearchApiKey"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ $t('labels.elasticSearchApiKey') }}</label>
                        <input type="password" name="elasticSearchApiKey" id="elasticSearchApiKey"
                            @focus="showTip('elasticSearchApiKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchApiKeyPlaceholder')"
                            v-model="elasticSearchApiKey">
                    </div>
                </div>
                <p class="mt-5 font-black">{{ $t('labels.advancedSettings') }}</p>
                <div>
                    <CheckBoxWithTipVue :value="storeLogsInDb" @toggled="toggleStoreLogsInDb" :label="$t('labels.storeLogsInDb')"
                        :helper="$t('labels.storeLogsInDbHelper')">
                    </CheckBoxWithTipVue>
                </div>
                <button type="submit" @click="submitSettings"
                    class="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-black rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                    {{ $t('labels.save') }}
                </button>
            </div>
        </section>
    </div>
</template>
<script>
import { driver } from "driver.js";
import "driver.js/dist/driver.css";
import CheckBoxWithTipVue from "@/components/CheckBoxWithTip.vue";

export default {
    name: 'SettingsForm',
    props: {
        settings: {
            type: Object
        }
    },
    components: {
        driver,
        CheckBoxWithTipVue,
    },
    setup() {
        return {
            driver: new driver(),
        }
    },
    data() {
        return {
            awsAccessKey: "",
            awsSecret: "",
            awsRegion: "",
            noSqlProvider: "default",
            documentTableName: "",
            parsingApiKey: "",
            bucketsList: "",
            scanBucket: "",
            elasticSearchIndex: "documents",
            elasticSearchHost: "localhost",
            elasticSearchPort: "9200",
            elasticSearchApiKey: "",
            storeLogsInDb: false,
            tipMap: {
                "awsAccessKey": {
                    "title": this.$t('labels.awsAccessKey'),
                    "description": this.$t('labels.awsAccessKeyTip'),
                },
                "awsSecret": {
                    "title": this.$t('labels.awsSecret'),
                    "description": this.$t('labels.awsSecretTip'),
                },
                "awsRegion": {
                    "title": this.$t('labels.awsRegion'),
                    "description": this.$t('labels.awsRegionTip'),
                },
                "bucketsList": {
                    "title": this.$t('labels.destinationBuckets'),
                    "description": this.$t('labels.bucketsListTip'),
                },
                "scanBucket": {
                    "title": this.$t('labels.s3BucketSource'),
                    "description": this.$t('labels.scanBucketTip'),
                },
                "noSqlProvider": {
                    "title": this.$t('labels.nosqlEngineHost'),
                    "description": this.$t('labels.noSqlProviderTip'),
                },
                "documentTableName": {
                    "title": this.$t('labels.documentTableName'),
                    "description": this.$t('labels.documentTableNameTip'),
                },
                "overrideElasticLocalSettings": {
                    "title": this.$t('labels.setlocalmode'),
                    "description": this.$t('labels.overrideElasticLocalSettingsTip'),
                },
                "elasticSearchIndex": {
                    "title": this.$t('labels.elasticSearchIndex'),
                    "description": this.$t('labels.elasticSearchIndexTip'),
                },
                "elasticSearchHost": {
                    "title": this.$t('labels.elasticSearchHostUrl'),
                    "description": this.$t('labels.elasticSearchHostTip'),
                },
                "elasticSearchPort": {
                    "title": this.$t('labels.elasticSearchPort'),
                    "description": this.$t('labels.elasticSearchPortTip'),
                },
                "elasticSearchApiKey": {
                    "title": this.$t('labels.elasticSearchApiKey'),
                    "description": this.$t('labels.elasticSearchApiKeyTip'),
                },
            }
        }
    },
    mounted() {
        this.setSettings();
    },
    computed: {
    },
    methods: {
        submitSettings() {
            let settings = {
                'awsAccessKey': this.awsAccessKey,
                'awsSecret': this.awsSecret,
                'awsRegion': this.awsRegion,
                'noSqlProvider': this.noSqlProvider,
                'documentTableName': this.documentTableName,
                'parsingApiKey': this.parsingApiKey,
                'bucketsList': this.bucketsList,
                'scanBucket': this.scanBucket,
                'elasticSearchIndex': this.elasticSearchIndex,
                'elasticSearchHost': this.elasticSearchHost,
                'elasticSearchPort': this.elasticSearchPort,
                'elasticSearchApiKey': this.elasticSearchApiKey,
                'storeLogsInDb': this.storeLogsInDb,
            }
            this.$emit('submit', settings);
        },
        setSettings() {
            if (this.settings) {
                this.awsAccessKey = this.settings.awsAccessKey
                this.awsSecret = this.settings.awsSecret
                this.awsRegion = this.settings.awsRegion
                this.noSqlProvider = this.settings.noSqlProvider
                this.documentTableName = this.settings.documentTableName
                this.parsingApiKey = this.settings.parsingApiKey
                this.bucketsList = this.settings.bucketsList
                this.scanBucket = this.settings.scanBucket
                this.elasticSearchIndex = this.settings.elasticSearchIndex
                this.elasticSearchHost = this.settings.elasticSearchHost
                this.elasticSearchPort = this.settings.elasticSearchPort
                this.elasticSearchApiKey = this.settings.elasticSearchApiKey
                this.storeLogsInDb = this.settings.storeLogsInDb
            }
        },
        overrideElasticLocalSettings() {
            this.elasticSearchIndex = "documents";
            this.elasticSearchHost = "host.docker.internal";
            this.elasticSearchPort = "9200";
            this.elasticSearchApiKey = "";
        },
        toggleStoreLogsInDb(value) {
            this.storeLogsInDb = value;
        },
        showTip(element) {
            const driverObj = driver({
                popoverClass: "driverjs-theme",
                stagePadding: 4,
            });

            driverObj.highlight({
                element: `#${element}`,
                popover: {
                    side: "top",
                    title: this.tipMap[element].title,
                    description: this.tipMap[element].description,
                }
            })
        },
    }
}

</script>