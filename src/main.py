import streamlit as st
from config.settings import initialize_page_config, SYMPTOM_QUESTIONS
from core.conversation import initialize_conversation, get_medical_response
from ui.styles import load_custom_styles

def main():
    initialize_page_config()
    load_custom_styles()
    
    st.title("🏥 MediChat Pro - Interactive Health Assistant")
    
    # Initialize session states
    if 'conversation' not in st.session_state:
        st.session_state.conversation = initialize_conversation()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'symptom_collection_mode' not in st.session_state:
        st.session_state.symptom_collection_mode = False
    if 'collected_symptoms' not in st.session_state:
        st.session_state.collected_symptoms = {}
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    if 'assessment_complete' not in st.session_state:
        st.session_state.assessment_complete = False
    if 'showed_welcome' not in st.session_state:
        st.session_state.showed_welcome = False
    if 'first_interaction' not in st.session_state:
        st.session_state.first_interaction = True

    # Show welcome message only once
    if not st.session_state.showed_welcome:
        st.markdown("""
            <div class='chat-container'>
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
        st.session_state.showed_welcome = True

    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div class='user-message'>👤 You: {message['content']}</div>", 
                       unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>🏥 MediChat: {message['content']}</div>", 
                       unsafe_allow_html=True)

    # Symptom collection mode
    if st.session_state.symptom_collection_mode and not st.session_state.assessment_complete:
        st.markdown("<div class='symptom-checker'>📋 Symptom Assessment in Progress...</div>", 
                   unsafe_allow_html=True)
        
        # Display progress
        progress = (st.session_state.current_question_index / len(SYMPTOM_QUESTIONS)) * 100
        st.markdown(f"""
            <div class='progress-bar-container'>
                <div class='progress-bar' style='width: {progress}%'></div>
            </div>
            <p style='text-align: center;'>Progress: {int(progress)}%</p>
        """, unsafe_allow_html=True)
        
        if st.session_state.current_question_index < len(SYMPTOM_QUESTIONS):
            current_question = SYMPTOM_QUESTIONS[st.session_state.current_question_index]
            user_response = st.text_input(
                f"Question {st.session_state.current_question_index + 1}/{len(SYMPTOM_QUESTIONS)}: {current_question}",
                key=f"q_{st.session_state.current_question_index}"
            )
            
            if st.button("Next"):
                if user_response:
                    st.session_state.collected_symptoms[current_question] = user_response
                    st.session_state.current_question_index += 1
                    
                    if st.session_state.current_question_index >= len(SYMPTOM_QUESTIONS):
                        # Complete symptom collection
                        st.session_state.assessment_complete = True
                        response = get_medical_response(
                            st.session_state.conversation,
                            "Analysis complete",
                            st.session_state.collected_symptoms
                        )
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": response
                        })
                        st.session_state.symptom_collection_mode = False
                        st.session_state.current_question_index = 0
                        st.session_state.first_interaction = False
                    st.rerun()
    else:
        # Regular chat mode
        user_input = st.text_input("How can I help you today?", key="user_input")
        
        if st.button("Send"):
            if user_input.strip():
                # Add user message to chat history
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Always start symptom collection on first interaction
                if st.session_state.first_interaction:
                    st.session_state.symptom_collection_mode = True
                    response = "I'll help you assess your condition. Let me ask you a series of questions to better understand your symptoms."
                else:
                    response = get_medical_response(st.session_state.conversation, user_input)
                
                # Add assistant response to chat history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
                st.rerun()

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.symptom_collection_mode = False
        st.session_state.collected_symptoms = {}
        st.session_state.current_question_index = 0
        st.session_state.assessment_complete = False
        st.session_state.conversation = initialize_conversation()
        st.session_state.showed_welcome = False
        st.session_state.first_interaction = True  # Reset first interaction state
        st.rerun()

    # Add disclaimer
    st.markdown("""
        <div style='font-size: 0.8em; color: #666; padding: 20px;'>
        ⚠️ Disclaimer: This chatbot provides general health information only. 
        Always consult healthcare professionals for medical advice, diagnosis, or treatment.
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()