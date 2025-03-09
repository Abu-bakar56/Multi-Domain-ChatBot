from langchain_google_genai import GoogleGenerativeAI
import gradio as gr
import os

# Load API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it and try again.")

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

generation_config = {
    "temperature": 0.3,  # Lower temperature for more structured responses
    "max_output_tokens": 300,
}

# Initialize the LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash", generation_config=generation_config, google_api_key=API_KEY)

# Task-specific system prompts
SYSTEM_PROMPTS = {
    "General": "You are a helpful AI chatbot that answers general queries in a concise and informative manner.",
    "Medical": "You are an AI medical assistant. Provide detailed, factual, and informative responses to medical inquiries based on existing medical knowledge. Avoid direct diagnosis and always recommend consulting a healthcare professional for personalized advice.",
    "Financial": "You are a financial assistant. Offer insights on budgeting, investments, and financial planning based on best practices and market trends.",
    "Legal": "You are a legal assistant. Provide general legal information based on laws and regulations but avoid giving actual legal advice or representation.",
}

def generate_response(task, prompt_txt):
    system_prompt = SYSTEM_PROMPTS.get(task, SYSTEM_PROMPTS["General"])
    full_prompt = f"System: {system_prompt}\nUser: {prompt_txt}\nAI:"  # Structuring input for better responses
    generated_response = llm.invoke(full_prompt)
    return generated_response

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Radio(list(SYSTEM_PROMPTS.keys()), label="Select Chatbot Type"),
        gr.Textbox(label="Input", lines=2, placeholder="Type your question here...")
    ],
    outputs=gr.Textbox(label="Output"),
    title="Multi-Domain ChatBot",
    description="Select a chatbot type and ask your question. The chatbot will respond based on the selected domain.",
    article="© 2025 by AbuBakar Shahzad | All Rights Reserved"
)

chat_application.launch(server_port=7862)
