# -*- coding: utf-8 -*-
"""travel-buddy.py

author: SamanvithaKaranth

"""

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import gradio as gr

## Alternate method to use huggingface_hub -  uncomment the below for your use
# from huggingface_hub import login

# # Replace 'your_access_token' with your Hugging Face token
# login(token='your_access_token')

# Load the Gemma-2-2B-IT model
model_name = "google/gemma-2-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Set up the chat pipeline
chat_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define the prompt template
base_prompt = """
You are a travel advisor with deep expertise in destinations, activities, and travel tips.
Provide concise, friendly, and clear recommendations for user queries.
Avoid lengthy lists or overly formal language. Focus on the best suggestions and a brief explanation.
"""

# Function to handle travel advisory with context management
class ConversationContext:
    def __init__(self):
        self.history = []  # To keep track of conversation history

    def add_to_history(self, user_input, response):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Advisor: {response}")

    def get_context(self):
        return "\n".join(self.history[-6:])  # Include only the last 3 exchanges for brevity

    def reset_history(self):
        self.history = []  # Clear history for new conversations

context = ConversationContext()

def travel_advisor_with_context(user_input):
    # Fetch the recent conversation history
    history_context = context.get_context()
    prompt = f"{base_prompt}\n{history_context}\nUser: {user_input}\nAdvisor:"

    # Generate the response
    response = chat_pipeline(prompt, max_new_tokens=300, do_sample=True, temperature=0.7, truncation=True)
    generated_text = response[0]["generated_text"]

    # Extract and clean the response
    advisor_response = generated_text.split("Advisor:")[-1].strip()  # Extract new response
    advisor_response = advisor_response.split("User:")[0].strip()  # Remove any future input accidentally added

    # Update conversation history
    context.add_to_history(user_input, advisor_response)

    return advisor_response

# Create the Gradio interface with chat-style layout
with gr.Blocks() as chat_interface:
    gr.Markdown("<h1 style='text-align: center;'>Travel Advisor Chatbot</h1>")
    gr.Markdown("Ask me about travel destinations, activities, or travel tips! Your conversation history is maintained for a natural chat experience.")

    # Chatbot and input components
    chatbot = gr.Chatbot(label="Chat with your Travel Advisor")
    user_input = gr.Textbox(placeholder="Type your question here...", show_label=False, container=False)
    send_button = gr.Button("Send")
    reset_button = gr.Button("Reset Conversation")  # Add a button to reset conversation

    # Maintain the conversation history
    history_state = gr.State([])  # State to keep track of the chat history

    # Function to handle user input and generate bot response
    def respond(history, user_query):
        if not user_query.strip():
            return history, ""  # Ignore empty inputs

        # Generate bot response
        bot_response = travel_advisor_with_context(user_query)

        # Update the history with the latest exchange
        history.append((user_query, bot_response))

        # Return updated history and clear input
        return history, ""

    # Function to reset the conversation
    def reset_conversation():
        context.reset_history()  # Clear the context history
        return [], ""  # Reset the chat interface

    # Set up the button and input functionality
    send_button.click(respond, [history_state, user_input], [chatbot, user_input])
    user_input.submit(respond, [history_state, user_input], [chatbot, user_input])
    reset_button.click(reset_conversation, inputs=None, outputs=[chatbot, user_input])

# Launch the Gradio interface
chat_interface.launch(debug=True)

