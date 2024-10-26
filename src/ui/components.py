import streamlit as st
from core.symptom_analyzer import get_symptom_progress, get_current_question, process_symptom_response

def render_introduction():
    """Render the introduction section"""
    st.markdown("""
        <div class='chat-container introduction'>
        <h4>Welcome to MediChat Pro!</h4>
        <p>I'm here to help you understand your health concerns better. I can:</p>
        <ul>
            <li>Ask relevant questions about your symptoms</li>
            <li>Provide general health information</li>
            <li>Guide you towards appropriate medical care</li>
            <li>Remember our conversation context</li>
        </ul>
        <p><em>Note: This is an AI assistant and not a substitute for professional medical advice.</em></p>
        </div>
    """, unsafe_allow_html=True)

def render_chat_history(chat_history):
    """Render the chat history"""
    for message in chat_history:
        if message["role"] == "user":
            st.markdown(
                f"<div class='user-message'>👤 You: {message['content']}</div>", 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='bot-message'>🏥 MediChat: {message['content']}</div>", 
                unsafe_allow_html=True
            )

def render_symptom_assessment():
    """Render the symptom assessment interface"""
    st.markdown(
        "<div class='symptom-checker'>📋 Symptom Assessment in Progress...</div>", 
        unsafe_allow_html=True
    )
    
    # Display progress bar
    progress = get_symptom_progress()
    st.markdown(f"""
        <div class='progress-bar-container'>
            <div class='progress-bar' style='width: {progress}%'></div>
        </div>
        <p style='text-align: center;'>Progress: {int(progress)}%</p>
    """, unsafe_allow_html=True)
    
    current_question = get_current_question()
    if current_question:
        user_response = st.text_input(
            f"Question {st.session_state.current_question_index + 1}/{len(SYMPTOM_QUESTIONS)}: {current_question}",
            key=f"q_{st.session_state.current_question_index}"
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Next", key="next_symptom"):
                if process_symptom_response(user_response):
                    complete_assessment()

def complete_assessment():
    """Complete the symptom assessment process"""
    st.session_state.assessment_complete = True
    response = get_medical_response(
        st.session_state.conversation,
        "Analysis complete",
        st.session_state.collected_symptoms
    )
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.session_state.symptom_collection_mode = False
    st.rerun()

def render_disclaimer():
    """Render the disclaimer section"""
    st.markdown("""
        <div class='disclaimer'>
        ⚠️ Disclaimer: This chatbot provides general health information only. 
        Always consult healthcare professionals for medical advice, diagnosis, or treatment.
        </div>
    """, unsafe_allow_html=True)

def render_error(error_message):
    """Render an error message"""
    st.markdown(
        f"<div class='error-message'>❌ {error_message}</div>",
        unsafe_allow_html=True
    )