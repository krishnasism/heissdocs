<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
                <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Settings</h2>
                <form action="#">
                    <p class="mb-4 font-black">Cloud Provider</p>
                    <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                        <div class="sm:col-span-2">
                            <label for="awsAccessKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                AWS Access Key</label>
                            <input type="password" name="awsAccessKey" id="awsAccessKey"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Enter your AWS Access Key" required>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="awsSecret" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                AWS Secret</label>
                            <input type="password" name="awsSecret" id="awsSecret"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Enter your AWS Secret" required>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="awsRegion" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">AWS
                                Region</label>
                            <input type="text" name="awsRegion" id="awsRegion"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="us-east-1" required>
                        </div>
                        <p class="mt-5 font-black">NoSQL Engine Host</p>
                        <div class="sm:col-span-2">
                            <label for="noSqlProvider"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Where is your NoSQL DB
                                hosted?</label>
                            <select id="noSqlProvider"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                                <option selected>Select provider</option>
                                <option value="aws">Amazon Web Services</option>
                                <option value="mongodb">MongoDB</option>
                                <option value="azure">MS Azure</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="documentDbName"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Document Table
                                Name</label>
                            <input type="text" name="documentDbName" id="documentDbName"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Name of database where parsed PDF data will be stored in" required>
                        </div>
                        <p class="mt-5 font-black sm:col-span-2">Parsing Engine</p>
                        <p class="sm:col-span-2">In case you are not hosting the Parsing Engine yourself, please provide the
                            API key that you got from our <a class="text-blue-700" href="#">portal.</a></p>
                        <div class="sm:col-span-2">
                            <label for="parsingAPIKey" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                Parsing API Key</label>
                            <input type="password" name="parsingAPIKey" id="parsingAPIKey"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Enter your Parsing API Key" required>
                        </div>
                    </div>
                    <button type="submit"
                        class="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-black rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                        Save
                    </button>
                </form>
            </div>
    </section>
</div></template>