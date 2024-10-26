import unittest
from src.core.symptom_analyzer import (
    should_collect_symptoms,
    get_current_question,
    process_symptom_response,
    get_symptom_progress
)
import streamlit as st
from unittest.mock import patch

class TestSymptomAnalyzer(unittest.TestCase):
    def setUp(self):
        # Mock session state
        if not hasattr(st, 'session_state'):
            st.session_state = {}
        st.session_state.current_question_index = 0
        st.session_state.collected_symptoms = {}

    def test_should_collect_symptoms(self):
        # Test symptom detection in user input
        self.assertTrue(should_collect_symptoms("I'm feeling sick"))
        self.assertTrue(should_collect_symptoms("I have pain"))
        self.assertFalse(should_collect_symptoms("How are you?"))

    @patch('streamlit.session_state')
    def test_get_current_question(self, mock_session_state):
        # Test getting current question
        mock_session_state.current_question_index = 0
        question = get_current_question()
        self.assertIsNotNone(question)
        self.assertIsInstance(question, str)

    def test_process_symptom_response(self):
        # Test processing valid symptom response
        response = "Severe headache"
        result = process_symptom_response(response)
        self.assertIn(get_current_question(), st.session_state.collected_symptoms)
        
        # Test processing empty response
        empty_response = ""
        result = process_symptom_response(empty_response)
        self.assertFalse(result)

    def test_get_symptom_progress(self):
        # Test progress calculation
        progress = get_symptom_progress()
        self.assertIsInstance(progress, float)
        self.assertTrue(0 <= progress <= 100)

        # Test progress at different stages
        st.session_state.current_question_index = 4  # Middle of questions
        progress = get_symptom_progress()
        self.assertTrue(0 < progress < 100)

if __name__ == '__main__':
    unittest.main()