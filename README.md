# WhatsApp GPT - Automation with Python and AI Integration

This project is a Python-based automation tool that enables seamless integration between WhatsApp and an AI chatbot (powered by Groq's LLaMA model). It allows you to send messages via WhatsApp Web, retrieve responses from an AI model, and maintain a chat history – all automated directly from the terminal.

### Features:
- **WhatsApp Message Automation**: Automatically send messages to any WhatsApp number using `pywhatkit`, a simple and efficient WhatsApp Web automation library.
- **AI Integration**: Uses Groq's LLaMA API (or any compatible AI model) to generate intelligent responses based on user input.
- **Conversation History Tracking**: Stores both user queries and AI responses in a conversation log (`prompts.txt`), creating a persistent chat history.
- **User-Friendly Interface**: Simple terminal interface allowing users to chat with AI and send responses to WhatsApp numbers directly.
- **Scalable Setup**: Easily adaptable to other AI models or APIs, enabling powerful conversational AI automation.

### Use Cases:
- **Customer Support Automation**: This project can be extended to automate customer support on WhatsApp, providing intelligent responses to customer inquiries.
- **AI Chatbot Deployment**: Perfect for businesses or individuals looking to deploy a conversational AI directly through WhatsApp.
- **Task Automation via WhatsApp**: Integrate with business processes to send notifications, alerts, or task updates directly to your WhatsApp contacts.

### How It Works:
1. **User Input**: You type a message/question into the terminal.
2. **AI Response**: The message is sent to the AI (Groq API), which returns an intelligent response.
3. **Message Delivery**: The response is then automatically sent to a specified WhatsApp number via `pywhatkit`.
4. **Logging**: Both the input and AI response are logged in the conversation history file.

### Technical Highlights:
- **No Selenium**: Unlike most WhatsApp automations, this project doesn’t rely on Selenium, making it lightweight and easy to run.
- **Pythonic Simplicity**: Built with Python’s standard libraries and simple third-party packages (`pywhatkit`), ensuring ease of use and integration.
- **Real-time Messaging**: Sends WhatsApp messages instantly, ensuring rapid responses and smooth user interaction.
  
### Installation & Setup:
- **Requirements**: pywhatkit, groq, python-dotenv, time (Standard library).
- Clone the repository.
- Configure your Groq API key and phone number.
- Run the script and interact with the AI chatbot via WhatsApp.

![print](https://github.com/user-attachments/assets/3f149c7e-22e6-47f1-bbd2-c0559b429547)
