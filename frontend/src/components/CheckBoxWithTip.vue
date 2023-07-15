<template>
    <div class="flex mt-4 w-30">
      <div class="flex items-center h-5">
        <input
          id="helper-checkbox"
          aria-describedby="helper-checkbox-text"
          type="checkbox"
          v-bind="$attrs"
          :checked="value"
          @change="$emit('toggled', $event.target.checked)"
          :disabled="disabled"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
        >
      </div>
      <div class="ml-2 text-sm">
        <label for="helper-checkbox" class="font-medium text-gray-900 dark:text-gray-300">{{ label }}</label>
        <p id="helper-checkbox-text" class="text-xs font-normal text-gray-500 dark:text-gray-300">{{ helper }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CheckBoxWithTip',
    props: {
      disabled: Boolean,
      label: String,
      helper: String,
      value: Boolean,
    },
  };
  </script>
  