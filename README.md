# 🤖 AI Resume Copilot

An AI-powered career guidance platform that helps users analyze their resumes, identify skill gaps, generate personalized learning roadmaps, and prepare for job interviews.

## ✨ Features

- 📄 **Resume Upload:** Upload resumes in PDF or DOCX format.
- 🎯 **Career-Based Analysis:** Analyze resumes according to your target job role.
- 🧠 **AI-Powered Insights:** Get intelligent feedback on your existing skills.
- 🔍 **Skill Gap Detection:** Identify missing skills required for your desired career.
- 🗺️ **Personalized Learning Roadmap:** Get recommendations to improve your skills.
- 💬 **Interview Preparation:** Generate role-specific interview questions.
- 🔐 **User Authentication:** Secure registration and login functionality.
- 📚 **Analysis History:** Access previously saved resume analysis reports.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja2
- **AI Integration:** OpenAI API
- **Database:** TiDB Cloud
- **ORM:** SQLAlchemy
- **Database Driver:** PyMySQL
- **Document Processing:** PyPDF2, python-docx
- **Environment Management:** python-dotenv

## 🏗️ Project Workflow

1. Register or log in to the application.
2. Select your target career or job role.
3. Upload your resume in PDF or DOCX format.
4. Extract text from the uploaded resume.
5. Analyze the resume using AI.
6. Identify existing skills and missing skills.
7. Generate a personalized learning roadmap.
8. Get interview questions based on your career goals.
9. View previously saved analysis reports.

## 📁 Project Structure

```text
AI-Resume-Copilot/
├── app.py
├── ai.py
├── db.py
├── models.py
├── templates/
├── static/
├── test_db.py
├── .env
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Git
- OpenAI API Key
- TiDB Cloud account

### 1. Clone the Repository

```bash
git clone https://github.com/vanshhiiikaa/AI-Resume-Copilot.git
cd AI-Resume-Copilot
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask sqlalchemy pymysql openai python-dotenv PyPDF2 python-docx
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key
FLASK_SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@HOST:4000/DATABASE
TIDB_CA_PATH=path/to/ca.pem
```

Replace the placeholder values with your actual credentials.

**Important:** Never share or commit your API keys, database credentials, or other sensitive information.

### 5. Configure the Database

1. Create a database using TiDB Cloud.
2. Configure your database connection credentials.
3. Set up the required SSL certificate.
4. Add the database connection details to your `.env` file.
5. Initialize the database tables as required by the application.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🧠 Example Use Case

Suppose a user wants to become a Backend Developer.

AI Resume Copilot can help the user:

- Analyze existing backend development skills.
- Identify potential skill gaps.
- Recommend topics and technologies to learn.
- Generate relevant interview questions.
- Build a structured learning roadmap.

## 🔐 Security

- Store sensitive credentials in environment variables.
- Never commit your `.env` file to GitHub.
- Validate uploaded resume files.
- Handle user data securely.
- Use secure password hashing and session management.

## 🔮 Future Enhancements

- ATS-friendly resume scoring.
- Job description and resume matching.
- AI-powered resume improvement suggestions.
- Downloadable analysis reports.
- Learning progress tracking.
- More career paths and interview simulations.
- Cloud deployment.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit and push your changes.
5. Submit a pull request.

## 👩‍💻 Author

**Vanshika**

GitHub: [@vanshhiiikaa](https://github.com/vanshhiiikaa)

## 📄 License

A license has not yet been specified for this project.

---

⭐ If you find this project useful, consider giving it a star!

**AI Resume Copilot — Your personal AI-powered career companion.**
