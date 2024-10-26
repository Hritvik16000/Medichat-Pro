import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model Configuration
MODEL_CONFIG = {
    "model": "gemini-1.5-flash",
    "temperature": 0.7
}

# Streamlit Page Configuration
def initialize_page_config():
    import streamlit as st
    
    st.set_page_config(
        page_title="MediChat Pro - Interactive Health Assistant",
        page_icon="🏥",
        layout="centered"
    )

# Symptom Assessment Configuration
SYMPTOM_QUESTIONS = [
    "What symptoms are you experiencing?",
    "How long have you been experiencing these symptoms?",
    "Rate your discomfort level from 1-10:",
    "Have you taken any medication for this?",
    "Do you have any pre-existing medical conditions?",
    "Are you experiencing fever or elevated temperature?",
    "Have these symptoms affected your daily activities?",
    "Have you experienced similar symptoms before?"
]

# Memory Configuration
MEMORY_CONFIG = {
    "window_size": 5
}