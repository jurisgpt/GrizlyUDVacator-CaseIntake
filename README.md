# 🏠 GrizlyUDVacator – Symbolic AI based Tenant Case Triage and Attorney Decision Support System

A symbolic AI-powered case triage assistant designed to help community based legal aid professionals analyze default judgments in unlawful detainer (eviction) cases under California Code of Civil Procedure § 473.5.

## 🚀 Features

### 1. Dynamic Intake Form
- YAML-driven form with configurable questions
- Date and boolean input types
- Clear prompts for legal relevance

### 2. Legal Evaluation Engine
- Formal legal logic implementation
- CCP § 473.5 eligibility evaluation
- Rule-based decision making
- Clear status and reasoning

### 3. AI-Powered Explanation
- GPT-3.5 generated narrative
- Natural language summaries
- Legal reasoning breakdown
- Case-specific guidance

### 4. Case Summary Generation
- Professional case summary reports
- Downloadable text format
- Automatic file saving
- Timestamped documentation

## 📁 File Structure

```
GrizlyUDVacator-CaseIntake/
├── streamlit_app.py          # Main application with UI and integration
├── legal_logic.py           # Formal legal evaluation logic
├── response_logic.py        # GPT explanation generation
├── summary_generator.py     # Case summary generation
├── intake_questions.yaml    # YAML configuration for intake form
├── requirements.txt         # Python dependencies
└── .streamlit/              # Streamlit configuration
    └── secrets.toml         # OpenAI API key
```

## 📌 Version Tags

- `v1.0.0-logic-locked`: First logic-stable milestone release
- `awareness-freeze-20250516`: Snapshot of complexity, coverage, and structure

## 🛠️ Technical Details

### Core Components

1. **Intake Form**
   - YAML-driven dynamic form
   - Date and boolean inputs
   - Legal relevance validation

2. **Legal Logic**
   - CCP § 473.5 implementation
   - Rule-based evaluation
   - Status determination
   - Reason generation

3. **AI Integration**
   - OpenAI GPT-3.5
   - Natural language explanations
   - Case-specific guidance

4. **Summary Generation**
   - Professional formatting
   - Timestamped reports
   - Download functionality
   - File saving

## 📚 Legal Considerations

- This tool is for research and educational use only
- Not a substitute for legal advice
- No attorney-client relationship established
- Results are for informational purposes

## 🚀 Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure OpenAI API key:
   - Create `.streamlit/secrets.toml`
   - Add your API key:
   ```toml
   [openai]
   api_key = "your-api-key-here"
   ```

3. Run the application:

   ```bash
   streamlit run streamlit_app.py
   ```
