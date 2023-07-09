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
                        <input type="password" name="awsAccessKey" id="awsAccessKey"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter your AWS Access Key" v-model="awsAccessKey">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsSecret" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            AWS Secret</label>
                        <input type="password" name="awsSecret" id="awsSecret"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter your AWS Secret" v-model="awsSecret">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="awsRegion" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">AWS
                            Region</label>
                        <input type="text" name="awsRegion" id="awsRegion"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="us-east-1" v-model="awsRegion">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Destination Buckets</label>
                        <input type="text" name="bucketsList" id="bucketsList"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of buckets that you want to be able to upload to (comma separated)"
                            v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">S3
                            Bucket [Source - Parsing]</label>
                        <input type="text" name="scanBucket" id="scanBucket"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of bucket that has PDFs to be parsed in the Cloud Interface"
                            v-model="scanBucket">
                    </div>
                    <p class="mt-5 font-black">NoSQL Engine Host</p>
                    <div class="sm:col-span-2">
                        <label for="noSqlProvider"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Where is your NoSQL DB
                            hosted?</label>
                        <select v-model="noSqlProvider" id="noSqlProvider"
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
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of database where parsed PDF data will be stored in"
                            v-model="documentTableName">
                    </div>
                    <p class="mt-5 font-black">Elasticsearch Settings</p>
                    <div class="sm:col-span-2">
                        <button type="button" @click="overrideElasticLocalSettings"
                            class="text-yellow-400 hover:text-white border border-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1 text-center mr-2 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-white dark:hover:bg-yellow-400 dark:focus:ring-yellow-900">
                            Set Local/Debugging Mode
                        </button>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="elasticSearchIndex"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Index
                            Name</label>
                        <input type="text" name="elasticSearchIndex" id="elasticSearchIndex"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of your Elasticsearch index" v-model="elasticSearchIndex">
                        <br />
                        <label for="elasticSearchHost"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Host
                            URL</label>
                        <input type="text" name="elasticSearchHost" id="elasticSearchHost"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Host URL of your Elasticsearch instance" v-model="elasticSearchHost">
                        <br />
                        <label for="elasticSearchPort"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch Port</label>
                        <input type="text" name="elasticSearchPort" id="elasticSearchPort"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Port of your Elasticsearch instance" v-model="elasticSearchPort">
                        <br />
                        <label for="elasticSearchApiKey"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticsearch API
                            Key</label>
                        <input type="password" name="elasticSearchApiKey" id="elasticSearchApiKey"
                            class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="API Key of your Elasticsearch instance (leave blank for localhost)"
                            v-model="elasticSearchApiKey">
                    </div>
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
export default {
    name: 'SettingsForm',
    props: {
        settings: {
            type: Object
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
            }
        },
        overrideElasticLocalSettings() {
            this.elasticSearchIndex = "documents";
            this.elasticSearchHost = "host.docker.internal";
            this.elasticSearchPort = "9200";
            this.elasticSearchApiKey = "";
        }
    }
}

</script>