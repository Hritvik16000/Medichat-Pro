from config.settings import SYMPTOM_QUESTIONS
import streamlit as st

def should_collect_symptoms(user_input):
    """Determine if symptom collection should be initiated based on user input"""
    symptom_keywords = ["sick", "symptoms", "feeling", "pain", "ache"]
    return any(keyword in user_input.lower() for keyword in symptom_keywords)

def get_current_question():
    """Get the current question in the symptom assessment"""
    if st.session_state.current_question_index < len(SYMPTOM_QUESTIONS):
        return SYMPTOM_QUESTIONS[st.session_state.current_question_index]
    return None

def process_symptom_response(response):
    """Process and validate a symptom response"""
    if not response.strip():
        return False
    
    current_question = get_current_question()
    st.session_state.collected_symptoms[current_question] = response
    st.session_state.current_question_index += 1
    
    return st.session_state.current_question_index >= len(SYMPTOM_QUESTIONS)

def get_symptom_progress():
    """Calculate the progress of symptom collection"""
    return (st.session_state.current_question_index / len(SYMPTOM_QUESTIONS)) * 100