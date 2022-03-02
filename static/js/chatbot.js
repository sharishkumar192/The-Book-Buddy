///////// CHATBOT //////////////
window.watsonAssistantChatOptions = {
    integrationID: "bd8e4589-c5c8-4123-b14b-cc0e8be5b9f0", // The ID of this integration.
    region: "us-south", // The region your integration is hosted in.
    serviceInstanceID: "5f51dc2f-ce1b-4d18-a593-1d5c107b6652", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
    };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/loadWatsonAssistantChat.js";
    document.head.appendChild(t);
  });