<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="px-4 ml-4 max-w-4xl">
                <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Settings</h2>
                <p class="mb-4 font-black">Cloud Provider</p>
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                    <div class="sm:col-span-2">
                        <label for="awsAccessKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            AWS Access Key</label>
                        <input type="password" name="awsAccessKey" id="awsAccessKey" @click="showTip('awsAccessKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter your AWS Access Key" v-model="awsAccessKey">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsSecret" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            AWS Secret</label>
                        <input type="password" name="awsSecret" id="awsSecret" @click="showTip('awsSecret')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter your AWS Secret" v-model="awsSecret">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsRegion" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">AWS
                            Region</label>
                        <input type="text" name="awsRegion" id="awsRegion" @click="showTip('awsRegion')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="us-east-1" v-model="awsRegion">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Destination Buckets</label>
                        <input type="text" name="bucketsList" id="bucketsList" @click="showTip('bucketsList')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of buckets that you want to be able to upload to (comma separated)"
                            v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">S3
                            Bucket [Source - Parsing]</label>
                        <input type="text" name="scanBucket" id="scanBucket" @click="showTip('scanBucket')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of bucket that has PDFs to be parsed in the Cloud Interface"
                            v-model="scanBucket">
                    </div>
                    <p class="mt-5 font-black">NoSQL Engine Host</p>
                    <div class="sm:col-span-2">
                        <label for="noSqlProvider"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Where is your NoSQL DB
                            hosted?</label>
                        <select v-model="noSqlProvider" id="noSqlProvider" @click="showTip('noSqlProvider')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected value="default">Select provider</option>
                            <option value="aws">Amazon Web Services</option>
                            <option value="mongodb">MongoDB [Unsupported]</option>
                            <option value="azure">MS Azure [Unsupported]</option>
                            <option value="other">Other [Unsupported]</option>
                        </select>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="documentTableName"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Document Table
                            Name</label>
                        <input type="text" name="documentTableName" id="documentTableName"
                            @click="showTip('documentTableName')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of database where parsed PDF data will be stored in"
                            v-model="documentTableName">
                    </div>
                    <p class="mt-5 font-black">Elasticsearch Settings</p>
                    <div class="sm:col-span-2">
                        <button type="button" @click="overrideElasticLocalSettings"
                            @mouseover="showTip('overrideElasticLocalSettings')" id="overrideElasticLocalSettings"
                            name="overrideElasticLocalSettings"
                            class="text-yellow-400 hover:text-white border border-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1 text-center mr-2 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-white dark:hover:bg-yellow-400 dark:focus:ring-yellow-900">
                            Set Local/Debugging Mode
                        </button>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="elasticSearchIndex"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Index
                            Name</label>
                        <input type="text" name="elasticSearchIndex" id="elasticSearchIndex"
                            @click="showTip('elasticSearchIndex')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of your Elasticsearch index" v-model="elasticSearchIndex">
                        <br />
                        <label for="elasticSearchHost"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Host
                            URL</label>
                        <input type="text" name="elasticSearchHost" id="elasticSearchHost"
                            @click="showTip('elasticSearchHost')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Host URL of your Elasticsearch instance" v-model="elasticSearchHost">
                        <br />
                        <label for="elasticSearchPort"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Port</label>
                        <input type="text" name="elasticSearchPort" id="elasticSearchPort"
                            @click="showTip('elasticSearchPort')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Port of your Elasticsearch instance" v-model="elasticSearchPort">
                        <br />
                        <label for="elasticSearchApiKey"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch API
                            Key</label>
                        <input type="password" name="elasticSearchApiKey" id="elasticSearchApiKey"
                            @click="showTip('elasticSearchApiKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="API Key of your Elasticsearch instance (leave blank for localhost)"
                            v-model="elasticSearchApiKey">
                    </div>
                </div>
                <p class="mt-5 font-black">Advanced Settings</p>
                <div>
                    <CheckBoxWithTipVue :value="storeLogsInDb" @toggled="toggleStoreLogsInDb" label="Store Logs into DB"
                        helper="Store parsing logs in the local database. Recommended while setting up, for easier debugging. Can be accessed under the Logs section.">
                    </CheckBoxWithTipVue>
                </div>
                <button type="submit" @click="submitSettings"
                    class="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-black rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                    Save
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
                    "title": "AWS Access Key",
                    "description": "Please enter your AWS Access Key here. Make sure that it has the right permissions. It should have access to S3 and DynamoDB.<br/> You can find your Access Key in the AWS Console under 'Security credentials'.",
                },
                "awsSecret": {
                    "title": "AWS Secret",
                    "description": "Please enter your AWS Secret here. It should correspond to the AWS Access Key you entered above.",
                },
                "awsRegion": {
                    "title": "AWS Region",
                    "description": "Please enter the AWS Region you want to use here. Example: us-east-1",
                },
                "bucketsList": {
                    "title": "S3 Buckets List - Destination",
                    "description": "Please enter the names of the S3 buckets that you would like to store your files in. You can enter multiple bucket names separated by a comma. Example: bucket1,bucket2,bucket3.<br/>This option will be available when you Upload a document from the Dashboard.",
                },
                "scanBucket": {
                    "title": "S3 Bucket - Source",
                    "description": "Please enter the name of the S3 bucket that you would like to scan for documents to parse. Example: bucket1.<br/>This option will be available in the Cloud Dashboard.",
                },
                "noSqlProvider": {
                    "title": "NoSQL Provider",
                    "description": "Please select the NoSQL provider you would like to use. For now only AWS DynamoDB is supported.",
                },
                "documentTableName": {
                    "title": "Document Table Name",
                    "description": "Please enter the name of the noSQL table you would like to use to store your documents. Example: documents.<br/>For now only AWS DynamoDB is supported.",
                },
                "overrideElasticLocalSettings": {
                    "title": "Override ElasticSearch Local Settings",
                    "description": "Please select this option if you would like to use the local ElasticSearch instance. Not recommended for production.",
                },
                "elasticSearchIndex": {
                    "title": "ElasticSearch Index",
                    "description": "Please enter the name of the ElasticSearch index you would like to use to store your documents. Example: search-documents.<br/>This option will be available when you search a query from the Dashboard.",
                },
                "elasticSearchHost": {
                    "title": "ElasticSearch Host",
                    "description": "Please enter the host URL of your remote ElasticSearch instance. Example: https://xxxx.us-east-1.aws.found.io",
                },
                "elasticSearchPort": {
                    "title": "ElasticSearch Port",
                    "description": "Please enter the port of your remote ElasticSearch instance. Example: 9200",
                },
                "elasticSearchApiKey": {
                    "title": "ElasticSearch API Key",
                    "description": "Please enter the API Key to your remote ElasticSearch instance. Leave blank for localhost.",
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