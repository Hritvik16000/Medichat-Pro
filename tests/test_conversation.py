import unittest
from unittest.mock import patch, MagicMock
from src.core.conversation import initialize_conversation, get_medical_response, analyze_symptoms

class TestConversation(unittest.TestCase):
    def setUp(self):
        self.mock_conversation = MagicMock()
        self.mock_symptoms = {
            "What symptoms are you experiencing?": "Headache and fever",
            "How long have you been experiencing these symptoms?": "2 days"
        }

    @patch('src.core.conversation.ChatGoogleGenerativeAI')
    @patch('src.core.conversation.ConversationBufferWindowMemory')
    def test_initialize_conversation(self, mock_memory, mock_llm):
        # Test successful conversation initialization
        conversation = initialize_conversation()
        self.assertIsNotNone(conversation)
        mock_llm.assert_called_once()
        mock_memory.assert_called_once()

    def test_get_medical_response_normal(self):
        # Test normal conversation response
        self.mock_conversation.predict.return_value = "Test response"
        response = get_medical_response(self.mock_conversation, "Test input")
        self.assertEqual(response, "Test response")
        self.mock_conversation.predict.assert_called_once()

    def test_get_medical_response_with_symptoms(self):
        # Test response with symptom analysis
        self.mock_conversation.predict.return_value = "Symptom analysis"
        response = get_medical_response(
            self.mock_conversation,
            "Test input",
            self.mock_symptoms
        )
        self.assertEqual(response, "Symptom analysis")
        self.mock_conversation.predict.assert_called_once()

    def test_analyze_symptoms(self):
        # Test symptom analysis prompt generation
        analysis_prompt = analyze_symptoms(self.mock_symptoms)
        self.assertIn("Based on the following symptoms", analysis_prompt)
        self.assertIn("Headache and fever", analysis_prompt)
        self.assertIn("2 days", analysis_prompt)

if __name__ == '__main__':
    unittest.main()