<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="px-4 ml-4 max-w-4xl">
                <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">{{ $t('labels.settings') }}</h2>
                <p class="mb-4 font-black">{{ $t('labels.cloudProvider') }}</p>
                <p class="mb-4">{{
                    $t('labels.selectCloudProviderLabel') }}
                </p>
                <ul class="grid w-full gap-6 md:grid-cols-3 mb-5">
                    <li>
                        <input type="radio" id="awschoice" name="cloudprovider" value="aws" class="hidden peer"
                            v-model="cloudProvider">
                        <label for="awschoice"
                            class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                            <div class="block">
                                <div class="w-full text-lg font-semibold">Amazon Web Services</div>
                            </div>
                        </label>
                    </li>
                    <li>
                        <input type="radio" id="azurechoice" name="cloudprovider" value="azure" class="hidden peer"
                            v-model="cloudProvider">
                        <label for="azurechoice"
                            class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                            <div class="block">
                                <div class="w-full text-lg font-semibold">Microsoft Azure</div>
                            </div>
                        </label>
                    </li>
                    <li>
                        <input type="radio" id="gcpchoice" name="cloudprovider" value="gcp" v-model="cloudProvider"
                            class="hidden peer">
                        <label for="gcpchoice"
                            class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                            <div class="block">
                                <div class="w-full text-lg font-semibold">Google Cloud Platform</div>
                            </div>
                        </label>
                    </li>
                </ul>
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6 " id="aws-options" v-if="cloudProvider === 'aws'">
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
                        <label for="awsRegion" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.awsRegion') }}</label>
                        <input type="text" name="awsRegion" id="awsRegion" @focus="showTip('awsRegion')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsRegionPlaceholder')" v-model="awsRegion">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.destinationBuckets') }}</label>
                        <input type="text" name="bucketsList" id="bucketsList" @focus="showTip('bucketsList')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsBucketListPlaceholder')" v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.scanBucket') }}</label>
                        <input type="text" name="scanBucket" id="scanBucket" @focus="showTip('scanBucket')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsScanBucketPlaceholder')" v-model="scanBucket">
                    </div>
                </div>
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6" id="azure-options" v-if="cloudProvider === 'azure'">
                    <div class="sm:col-span-2">
                        <label for="azureBlobConnectionString"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            {{ $t('labels.azureBlobConnectionString') }}</label>
                        <input type="password" name="azureBlobConnectionString" id="azureBlobConnectionString"
                            @focus="showTip('azureBlobConnectionString')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.azureBlobConnectionStringPlaceholder')"
                            v-model="azureBlobConnectionString">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.azureBlobContainerName') }}</label>
                        <input type="text" name="bucketsList" id="bucketsList"
                            @focus="showTip('dest')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.azureBlobContainerNamePlaceholder')" v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.scanBucket') }}</label>
                        <input type="text" name="scanBucket" id="scanBucket" @focus="showTip('scanBucket')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsScanBucketPlaceholder')" v-model="scanBucket">
                    </div>
                </div>
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6" id="gcp-options" v-if="cloudProvider === 'gcp'">
                    <div class="sm:col-span-2">
                        <label for="gcpkeyfile" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.gcpKeyFile') }}</label>
                        <div class="flex">
                            <input
                                class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
                                id="gcpkeyfile" type="file" accept=".json" @change="gcpKeyFileChanged">
                            <svg v-if="settings.gcpKeyFileContent" class="w-6 h-6 text-green-500 dark:text-white mt-2 ml-2"
                                aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                                <title>{{ $t('labels.gcpKeyFileExists') }}</title>
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M5 5h8m-1-3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1m6 0v3H6V2m6 0h4a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h4m0 9.464 2.025 1.965L12 9.571" />
                            </svg>
                        </div>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="bucketsList" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.destinationBuckets') }}</label>
                        <input type="text" name="bucketsList" id="bucketsList" @focus="showTip('bucketsList')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsBucketListPlaceholder')" v-model="bucketsList">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="scanBucket" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.scanBucket') }}</label>
                        <input type="text" name="scanBucket" id="scanBucket" @focus="showTip('scanBucket')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.awsScanBucketPlaceholder')" v-model="scanBucket">
                    </div>
                </div>
                <br />
                <hr />
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                    <p class="mt-5 font-black">{{ $t('labels.nosqlEngineHost') }}</p>
                    <div class="sm:col-span-2">
                        <label for="noSqlProvider" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.noSqlEngineHostHelper') }}</label>
                        <select v-model="noSqlProvider" id="noSqlProvider" @focus="showTip('noSqlProvider')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected value="default">{{ $t('labels.noSqlEngineHostDropdown') }}</option>
                            <option v-if="cloudProvider == 'aws'" value="aws">DynamoDB (AWS)</option>
                            <option v-if="cloudProvider == 'gcp'" value="gcp">Firestore (GCP)</option>
                            <option value="mongodb">MongoDB</option>
                            <option v-if="cloudProvider == 'azure'" value="azure">CosmosDB (Azure)</option>
                        </select>
                    </div>
                    <div class="sm:col-span-2" v-if="noSqlProvider != 'azure'">
                        <label for="documentTableName"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.documentTableName') }}</label>
                        <input type="text" name="documentTableName" id="documentTableName"
                            @focus="showTip('documentTableName')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.documentTableNamePlaceholder')" v-model="documentTableName">
                    </div>
                    <div class="sm:col-span-2" v-if="noSqlProvider == 'mongodb'">
                        <p class="mb-4 font-black">{{ $t('labels.mongodbsettingsheader') }}</p>
                        <div class="sm:col-span-2 mb-5">
                            <label for="mongoDbHost" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.mongoDbHost') }}</label>
                            <input type="text" name="mongoDbHost" id="mongoDbHost" @focus="showTip('mongoDbHost')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.mongoDbHostPlaceholder')" v-model="mongoDbHost">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="mongoDbDatabase"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.mongoDbDatabase') }}</label>
                            <input type="text" name="mongoDbDatabase" id="mongoDbDatabase"
                                @focus="showTip('mongoDbDatabase')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.mongoDbDatabasePlaceholder')" v-model="mongoDbDatabase">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="mongoDbUsername"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.mongoDbUsername') }}</label>
                            <input type="text" name="mongoDbUsername" id="mongoDbUsername"
                                @focus="showTip('mongoDbUsername')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.mongoDbUsernamePlaceholder')" v-model="mongoDbUsername">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="mongoDbPassword"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.mongoDbPassword') }}</label>
                            <input type="password" name="mongoDbPassword" id="mongoDbPassword"
                                @focus="showTip('mongoDbPassword')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.mongoDbPasswordPlaceholder')" v-model="mongoDbPassword">
                        </div>
                    </div>
                    <div class="sm:col-span-2" v-if="noSqlProvider == 'azure'">
                        <p class="mb-4 font-black">{{ $t('labels.azureNosqlSettingsHeader') }}</p>
                        <div class="sm:col-span-2 mb-5">
                            <label for="cosmosDbHost" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.cosmosDbHost') }}</label>
                            <input type="text" name="cosmosDbHost" id="cosmosDbHost" @focus="showTip('cosmosDbHost')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.cosmosDbHostPlaceholder')" v-model="cosmosDbHost">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="cosmosDbKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.cosmosDbKey') }}</label>
                            <input type="password" name="cosmosDbKey" id="cosmosDbKey" @focus="showTip('cosmosDbKey')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.cosmosDbKeyPlaceholder')" v-model="cosmosDbKey">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="cosmosDbContainer"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.cosmosDbContainer') }}</label>
                            <input type="text" name="cosmosDbContainer" id="cosmosDbContainer"
                                @focus="showTip('cosmosDbContainer')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.cosmosDbContainerPlaceholder')" v-model="cosmosDbContainer">
                        </div>
                        <div class="sm:col-span-2 mb-5">
                            <label for="cosmosDbDatabase"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                {{ $t('labels.cosmosDbDatabase') }}</label>
                            <input type="text" name="cosmosDbDatabase" id="cosmosDbDatabase"
                                @focus="showTip('cosmosDbDatabase')"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('labels.cosmosDbDatabasePlaceholder')" v-model="cosmosDbDatabase">
                        </div>
                    </div>
                </div>
                <br />
                <hr />
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
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
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.elasticSearchIndex') }}</label>
                        <input type="text" name="elasticSearchIndex" id="elasticSearchIndex"
                            @focus="showTip('elasticSearchIndex')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchIndexPlaceholder')" v-model="elasticSearchIndex">
                        <br />
                        <label for="elasticSearchHost"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.elasticSearchHostUrl') }}</label>
                        <input type="text" name="elasticSearchHost" id="elasticSearchHost"
                            @focus="showTip('elasticSearchHost')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchHostPlaceholder')" v-model="elasticSearchHost">
                        <br />
                        <label for="elasticSearchPort"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.elasticSearchPort') }}</label>
                        <input type="text" name="elasticSearchPort" id="elasticSearchPort"
                            @focus="showTip('elasticSearchPort')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchPortPlaceholder')" v-model="elasticSearchPort">
                        <br />
                        <label for="elasticSearchApiKey"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.elasticSearchApiKey') }}</label>
                        <input type="password" name="elasticSearchApiKey" id="elasticSearchApiKey"
                            @focus="showTip('elasticSearchApiKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.elasticSearchApiKeyPlaceholder')" v-model="elasticSearchApiKey">
                    </div>
                </div>
                <br />
                <hr />
                <p class="mt-5 font-black">{{ $t('labels.llmSettings') }}</p>
                <br />
                <div class="sm:col-span-2 mb-5">
                    <label for="openaiApiKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                        $t('labels.openaiApiKey') }}</label>
                    <input type="password" name="openaiApiKey" id="openaiApiKey" @focus="showTip('openaiApiKey')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        :placeholder="$t('labels.openaiApiKeyPlaceholder')" v-model="openaiApiKey" />
                </div>
                <!-- <div class="sm:col-span-2">
                    <label for="huggingfaceApiKey"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                                $t('labels.huggingfaceApiKey') }}</label>
                        <input type="password" name="huggingfaceApiKey" id="huggingfaceApiKey"
                            @focus="showTip('huggingfaceApiKey')"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            :placeholder="$t('labels.huggingfaceApiKeyPlaceholder')" v-model="huggingfaceApiKey"/>
                </div> -->
                <div class="sm:col-span-2 mb-5">
                    <label for="qdrantHost" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                        $t('labels.qdrantHost') }}</label>
                    <input type="text" name="qdrantEndpoint" id="qdrantHost" @focus="showTip('qdrantHost')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        :placeholder="$t('labels.qdrantHostPlaceholder')" v-model="qdrantHost" />
                </div>
                <div class="sm:col-span-2 mb-5">
                    <label for="qdrantPort" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                        $t('labels.qdrantPort') }}</label>
                    <input type="text" name="qdrantPort" id="qdrantPort" @focus="showTip('qdrantPort')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        :placeholder="$t('labels.qdrantPortPlaceholder')" v-model="qdrantPort" />
                </div>
                <div class="sm:col-span-2 mb-5">
                    <label for="qdrantApiKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                        $t('labels.qdrantApiKey') }}</label>
                    <input type="password" name="qdrantApiKey" id="qdrantApiKey" @focus="showTip('qdrantApiKey')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        :placeholder="$t('labels.qdrantApiKeyPlaceholder')" v-model="qdrantApiKey" />
                </div>
                <div class="sm:col-span-2 mb-5">
                    <label for="qdrantCollectionName"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{
                            $t('labels.qdrantCollectionName') }}</label>
                    <input type="text" name="qdrantCollectionName" id="qdrantCollectionName"
                        @focus="showTip('qdrantCollectionName')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        :placeholder="$t('labels.qdrantCollectionNamePlaceholder')" v-model="qdrantCollectionName" />
                </div>
                <hr />
                <p class="mt-5 font-black">{{ $t('labels.advancedSettings') }}</p>
                <div>
                    <CheckBoxWithTipVue :value="storeLogsInDb" @toggled="toggleStoreLogsInDb"
                        :label="$t('labels.storeLogsInDb')" :helper="$t('labels.storeLogsInDbHelper')">
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
            showMongoDbSettings: false,
            showAzureSettings: false,
            mongoDbHost: "",
            mongoDbPort: "",
            mongoDbUser: "",
            mongoDbPassword: "",
            mongoDbDatabase: "",
            elasticSearchIndex: "",
            elasticSearchHost: "",
            elasticSearchPort: "",
            elasticSearchApiKey: "",
            openaiApiKey: "",
            huggingfaceApiKey: "",
            qdrantHost: "",
            qdrantPort: "",
            qdrantApiKey: "",
            qdrantCollectionName: "",
            cloudProvider: "aws",
            azureBlobConnectionString: "",
            cosmosDbHost: "",
            cosmosDbContainer: "",
            cosmosDbDatabase: "",
            cosmosDbKey: "",
            gcpKeyFileContent: null,
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
                    "title": this.$t('labels.scanBucket'),
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
                "mongoDbDatabase": {
                    "title": this.$t('labels.mongoDbDatabase'),
                    "description": this.$t('labels.mongoDbDatabaseTip'),
                },
                "mongoDbUsername": {
                    "title": this.$t('labels.mongoDbUsername'),
                    "description": this.$t('labels.mongoDbUsernameTip'),
                },
                "mongoDbPassword": {
                    "title": this.$t('labels.mongoDbPassword'),
                    "description": this.$t('labels.mongoDbPasswordTip'),
                },
                "mongoDbHost": {
                    "title": this.$t('labels.mongoDbHost'),
                    "description": this.$t('labels.mongoDbHostTip'),
                },
                "openaiApiKey": {
                    "title": this.$t('labels.openaiApiKey'),
                    "description": this.$t('labels.openaiApiKeyTip'),
                },
                "huggingfaceApiKey": {
                    "title": this.$t('labels.huggingfaceApiKey'),
                    "description": this.$t('labels.huggingfaceApiKeyTip'),
                },
                "qdrantHost": {
                    "title": this.$t('labels.qdrantHost'),
                    "description": this.$t('labels.qdrantHostTip'),
                },
                "qdrantPort": {
                    "title": this.$t('labels.qdrantPort'),
                    "description": this.$t('labels.qdrantPortTip'),
                },
                "qdrantApiKey": {
                    "title": this.$t('labels.qdrantApiKey'),
                    "description": this.$t('labels.qdrantApiKeyTip'),
                },
                "qdrantCollectionName": {
                    "title": this.$t('labels.qdrantCollectionName'),
                    "description": this.$t('labels.qdrantCollectionNameTip'),
                },
                "cloudProvider": {
                    "title": this.$t('labels.cloudProvider'),
                    "description": this.$t('labels.cloudProviderTip'),
                }
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
                'mongoDbUsername': this.mongoDbUsername,
                'mongoDbPassword': this.mongoDbPassword,
                'mongoDbHost': this.mongoDbHost,
                'mongoDbDatabase': this.mongoDbDatabase,
                'openaiApiKey': this.openaiApiKey,
                'huggingfaceApiKey': this.huggingfaceApiKey,
                'qdrantHost': this.qdrantHost,
                'qdrantPort': this.qdrantPort,
                'qdrantApiKey': this.qdrantApiKey,
                'qdrantCollectionName': this.qdrantCollectionName,
                'cloudProvider': this.cloudProvider,
                'gcpKeyFileContent': this.gcpKeyFileContent,
                'azureBlobConnectionString': this.azureBlobConnectionString,
                'cosmosDbHost': this.cosmosDbHost,
                'cosmosDbContainer': this.cosmosDbContainer,
                'cosmosDbDatabase': this.cosmosDbDatabase,
                'cosmosDbKey': this.cosmosDbKey,
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
                this.mongoDbUsername = this.settings.mongoDbUsername
                this.mongoDbPassword = this.settings.mongoDbPassword
                this.mongoDbHost = this.settings.mongoDbHost
                this.mongoDbDatabase = this.settings.mongoDbDatabase
                this.openaiApiKey = this.settings.openaiApiKey
                this.huggingfaceApiKey = this.settings.huggingfaceApiKey
                this.qdrantHost = this.settings.qdrantHost
                this.qdrantPort = this.settings.qdrantPort
                this.qdrantApiKey = this.settings.qdrantApiKey
                this.qdrantCollectionName = this.settings.qdrantCollectionName
                this.cloudProvider = this.settings.cloudProvider
                this.azureBlobConnectionString = this.settings.azureBlobConnectionString
                this.cosmosDbHost = this.settings.cosmosDbHost
                this.cosmosDbContainer = this.settings.cosmosDbContainer
                this.cosmosDbDatabase = this.settings.cosmosDbDatabase
                this.cosmosDbKey = this.settings.cosmosDbKey
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
        gcpKeyFileChanged(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = () => {
                    try {
                        this.gcpKeyFileContent = reader.result;
                        console.log(this.gcpKeyFileContent);
                    } catch (error) {
                        console.error("Error parsing JSON file:", error);
                    }
                };
                reader.readAsText(file);
            }
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