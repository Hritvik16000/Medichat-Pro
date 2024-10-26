import streamlit as st

def load_custom_styles():
    """Load custom CSS styles for the application"""
    st.markdown("""
        <style>
        .stApp {
            background-color: #0A0A0A;
        }
        .chat-container {
            border-radius: 10px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .user-message {
            background-color: #15292B;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        .bot-message {
            background-color: #181818;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        .symptom-checker {
            background-color: #212124;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .progress-bar-container {
            margin: 10px 0;
            padding: 5px;
            background-color: #f0f0f0;
            border-radius: 5px;
        }
        .progress-bar {
            height: 20px;
            background-color: #242526;
            border-radius: 5px;
            transition: width 0.3s ease-in-out;
        }
        .disclaimer {
            font-size: 0.8em;
            color: #192734;
            padding: 20px;
            border-top: 1px solid #eee;
            margin-top: 20px;
        }
        .introduction {
            border-left: 4px solid #192734;
            padding-left: 15px;
        }
        .error-message {
            color: #d32f2f;
            background-color: #ffebee;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .button-container {
            display: flex;
            gap: 10px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)