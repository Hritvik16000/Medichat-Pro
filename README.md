# MediChat Pro - Interactive Health Assistant

MediChat Pro is an AI-powered health assistant built with Streamlit and LangChain, designed to help users understand their health concerns through interactive conversations and systematic symptom assessment.

## Features

- Interactive chat interface with medical context awareness
- Systematic symptom collection and analysis
- Professional medical conversation handling
- Progress tracking for symptom assessment
- Clean and intuitive user interface
- Conversation memory for context-aware responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medichat-pro.git
cd medichat-pro
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

## Usage

Run the application:
```bash
streamlit run src/main.py
```

## Project Structure

- `src/`: Main application code
  - `config/`: Configuration settings
  - `core/`: Core business logic
  - `utils/`: Utility functions and prompts
  - `ui/`: UI components and styles
- `tests/`: Unit tests
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not in repo)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This application provides general health information only and is not a substitute for professional medical advice, diagnosis, or treatment.