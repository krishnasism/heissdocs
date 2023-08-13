<template>
    <div class="chat-history">
      <div v-for="(message, index) in chatHistory.messages" :key="index" class="message">
        <div :class="message.sender === 'user' ? 'user-message' : 'bot-message'">{{ message.text }}</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      chatHistory: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>  
  .message {
    margin-bottom: 10px;
    display: flex;
    align-items: flex-start;
  }
  
  .user-message {
    background-color: #F0F0F0;
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
  }
  
  .bot-message {
    background-color: #b3def5;
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
    margin-left: auto;
  }
  
  .user-message::before,
  .bot-message::before {
    content: "";
    display: block;
    width: 0;
    height: 0;
    border-style: solid;
  }
  
  .user-message::before {
    border-width: 10px 10px 0 0;
    border-color: #F0F0F0 transparent transparent transparent;
    position: absolute;
    top: 0;
    left: -10px;
  }
  
  .bot-message::before {
    border-width: 0 10px 10px 0;
    border-color: transparent transparent #DCF8C6 transparent;
    position: absolute;
    bottom: 0;
    right: -10px;
  }
  
  .user-message::after,
  .bot-message::after {
    content: "";
    display: block;
    width: 0;
    height: 0;
    border-style: solid;
  }
  
  .user-message::after {
    border-width: 10px 0 0 10px;
    border-color: #F0F0F0 transparent transparent transparent;
    position: absolute;
    top: 0;
    right: -10px;
  }
  
  .bot-message::after {
    border-width: 0 0 10px 10px;
    border-color: transparent transparent #DCF8C6 transparent;
    position: absolute;
    bottom: 0;
    left: -10px;
  }
  </style>
  