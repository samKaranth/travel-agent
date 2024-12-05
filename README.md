# 🌍 Travel Advisor Chatbot
***A conversational AI bot for personalized travel recommendations and tips.***

## 🚀 About the Project
The Travel Advisor Chatbot is a smart and friendly virtual assistant designed to provide tailored travel advice. Built using cutting-edge Natural Language Processing (NLP) techniques, this chatbot offers:
- Destination Recommendations: Popular places, seasonal suggestions.
- Travel Guidelines: Packing tips, visa requirements, and more.
- Activity Ideas: Adventure sports, sightseeing, and relaxation options.
- Accommodation Tips: Luxury hotels, budget stays, and local experiences.
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
1. Clone this repository:
```
git clone https://github.com/your-username/travel-advisor-chatbot.git
cd travel-advisor-chatbot
 ```
2. Download and load the Gemma-2-2B-IT model:
```
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2-2b-it", device_map="auto")
```
3. Launch the chatbot:
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
This project is licensed under the MIT License. See the LICENSE file for details.











