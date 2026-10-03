# 🛠️ Intelligent IT Ticket Resolver

An AI-powered IT support system that automatically classifies user-reported IT issues and retrieves relevant solutions from a knowledge base.

The project uses AutoGen agents, semantic similarity search, and a Streamlit web interface to provide an interactive IT support experience.

## ✨ Features

- 🤖 AI-powered IT ticket classification
- 🔎 Semantic search over an IT knowledge base
- 🧠 AutoGen-based agent workflow
- 💡 Automatic solution recommendations
- 🌐 Streamlit web interface
- 📋 Displays ticket classification and recommended solution
- 👍 User feedback after receiving a solution
- 🎫 Support ticket creation and email notifications *(planned)*

## 🏗️ Architecture

```text
User
  ↓
Streamlit Interface
  ↓
Classifier Agent
  ↓
Ticket Classification
  ↓
Knowledge Base Agent
  ↓
Semantic Similarity Search
  ↓
Relevant Solution
  ↓
Streamlit Interface

🧰 Tech Stack

* Python
* AutoGen
* Streamlit
* Sentence Transformers
* OpenRouter API
* JSON
* Git & GitHub

Intelligent-IT-Ticket-Resolver/
│
├── agents/
│   ├── classifier_agent.py
│   └── knowledge_base_agent.py
│
├── data/
│   └── knowledge_base.json
│
├── tools/
│   └── ...
│
├── utility/
│   └── ...
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

🚀 How to Run
1. Clone the repository
git clone <repository-url>
cd Intelligent-IT-Ticket-Resolver

2. Create a virtual environment
python3 -m venv venv

3. Activate the virtual environment
macOS/Linux:
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure environment variables

Create a .env file and add the required API credentials.

6. Run the application
streamlit run app.py

The application will open in your browser.

🔄 How It Works

1. The user describes an IT problem.
2. The Classifier Agent determines the category of the issue.
3. The Knowledge Base Agent searches for a similar known problem.
4. The most relevant solution is retrieved.
5. The solution is displayed through the Streamlit interface.
6. The user can indicate whether the solution resolved the issue.

🔮 Future Improvements

* 🎫 Automatic support ticket generation
* 📧 Email notifications
* 🆔 Unique ticket IDs
* 📊 Ticket tracking
* 👨‍💻 Support-team dashboard
* ☁️ Cloud deployment

👨‍💻 Author

Saksham Thakur


