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
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Buckets</label>
                        <input type="text" name="bucketsList" id="bucketsList"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of buckets that you want to be able to upload to (comma separated)" v-model="bucketsList">
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
                            <option value="other">Other  [Unsupported]</option>
                        </select>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="documentTableName"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Document Table
                            Name</label>
                        <input type="text" name="documentTableName" id="documentTableName"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of database where parsed PDF data will be stored in" v-model="documentTableName">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">S3 Bucket (To Scan)</label>
                        <input type="text" name="scanBucket" id="scanBucket"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Name of bucket that has PDFs to be parsed" v-model="scanBucket">
                    </div>
                    <p class="mt-5 font-black sm:col-span-2">Parsing Engine [Unsupported]</p>
                    <p class="sm:col-span-2">In case you are not hosting the Parsing Engine yourself, please provide the
                        API key that you got from our <a class="text-blue-700" href="#">portal.</a></p>
                    <div class="sm:col-span-2">
                        <label for="parsingAPIKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Parsing API Key</label>
                        <input type="password" name="parsingAPIKey" id="parsingAPIKey"
                            disabled
                            class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter your Parsing API Key" v-model="parsingApiKey">
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
            }
        }
    }
}

</script>