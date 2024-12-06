# 🌍 Travel Advisor Chatbot
***A conversational AI bot for personalized travel recommendations and tips.***

## 🚀 About the Project
The Travel Advisor Chatbot is a smart and friendly virtual assistant designed to provide tailored travel advice. Built using cutting-edge Large Language Model (LLM), this chatbot offers:
- Destination Recommendations: Popular places, seasonal suggestions.
- Travel Guidelines: Packing tips, visa requirements, and more.
- Activity Ideas: Adventure sports, sightseeing, and relaxation options.
With a conversational design, it ensures a seamless and enjoyable user experience.

## ✨ Features
- Context-Aware Conversations: Maintains up to three previous exchanges for continuity.
- Dynamic Suggestions: Answers personalized queries about destinations, activities, and travel tips.
- Gradio Interface: A user-friendly interface for real-time interaction.
- Reset Functionality: Clear chat history for a fresh conversation start.


## 🛠️ Tech Stack
- Python
- Transformers Library: For model handling and tokenization.
- Gradio: To build an interactive web-based interface.
- Gemma-2-2B-IT Model: A powerful text-generation model for accurate and natural responses.

## 🏗️ Installation & Setup
### Prerequisites
1. Python 3.8+ installed.
2. Install required libraries:
    ``` pip install transformers gradio ```
### Steps
#### 1. Clone this repository:
```
git clone https://github.com/samKaranth/travel-advisor-chatbot.git
cd travel-advisor-chatbot
 ```
#### 2. Obtain Hugging Face Access Token:

- You need an access token to use Hugging Face's pre-trained models.
    - Go to [Hugging Face]https://huggingface.co/meta-llama/Llama-2-7b-chat-hf and create an account (if you don’t have one already).
    - After logging in, visit the Access Tokens page.
    - Click New Token and follow the instructions to generate a token.
- Copy the token once generated and save it safely as you can't see it again.

#### 3. Set up the Hugging Face Token:
- Set the token in your environment variables to authenticate API calls:
    - On Windows:
      ```
      set HF_HOME=<your_token_here>
      ```
    - On macOS/Linux:
      ```
      export HF_HOME=<your_token_here>
      ```
- Alternatively, you can authenticate by adding this snippet in your .py file:
  ```
    from huggingface_hub import login

    # Replace 'your_access_token' with your Hugging Face token
    login(token='your_access_token')
  ```
#### 4. Launch the chatbot:
```
python travel_buddy.py
```


## 💡 Usage
* Ask travel-related questions like:
    - ***"What are the best places to visit in Europe?"***
    - ***"What should I pack for a trip to Thailand in January?"***

* Receive contextually relevant and concise answers.
* Reset the chat history anytime for a fresh start!

## 📂 Project Structure
```
travel-advisor-chatbot/
├── travel_buddy.py           # Main Python script to run the chatbot
├── requirements.txt          # Python dependencies
├── LICENSE.txt               # MIT LICENSE
└── README.md                 # Project documentation (you're reading this!)
```
## 💬 Acknowledgments
- Built with ❤️ using the Transformers library by Hugging Face.
- Special thanks to the open-source community for amazing tools like Gradio and Gemma-2-2B-IT.

## 🛡️ License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/samKaranth/travel-agent/blob/main/LICENSE) file for details.












