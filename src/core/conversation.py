from langchain.memory import ConversationBufferWindowMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from config.settings import GEMINI_API_KEY, MODEL_CONFIG, MEMORY_CONFIG
from utils.prompts import MEDICAL_PROMPT
import streamlit as st

def initialize_conversation():
    """Initialize the LangChain conversation with memory"""
    try:
        llm = ChatGoogleGenerativeAI(
            model=MODEL_CONFIG["model"],
            google_api_key=GEMINI_API_KEY,
            temperature=MODEL_CONFIG["temperature"]
        )
        
        memory = ConversationBufferWindowMemory(
            k=MEMORY_CONFIG["window_size"],
            return_messages=True
        )
        
        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=MEDICAL_PROMPT
        )
        
        conversation = ConversationChain(
            llm=llm,
            memory=memory,
            prompt=prompt,
            verbose=True
        )
        
        return conversation
    
    except Exception as e:
        st.error(f"Error initializing conversation: {str(e)}")
        return None

def get_medical_response(conversation, user_input, collected_symptoms=None):
    """Get response from the medical assistant"""
    try:
        if collected_symptoms:
            analysis_prompt = analyze_symptoms(collected_symptoms)
            response = conversation.predict(input=analysis_prompt)
        else:
            response = conversation.predict(input=user_input)
        
        return response
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try rephrasing your question."

def analyze_symptoms(symptoms):
    """Generate a comprehensive analysis of collected symptoms"""
    symptoms_text = "\n".join([f"{q}: {a}" for q, a in symptoms.items()])
    analysis_prompt = f"""Based on the following symptoms and information:

{symptoms_text}

Please provide:
1. A careful analysis of the symptoms
2. Possible common causes (without making definitive diagnoses)
3. Recommended next steps
4. Self-care suggestions if appropriate
5. Clear guidance on when to seek professional medical attention

Remember to be thorough but emphasize that this is not a diagnosis."""

    return analysis_prompt