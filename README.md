# 🤖 AI Career Copilot

> An AI-powered resume analysis and career guidance platform that helps users understand their current skills, identify skill gaps, build a personalized learning roadmap, and prepare for interviews based on their target career.

---

## 📌 Overview

**AI Career Copilot** is a full-stack AI-powered web application designed to help students, freshers, and job seekers make better career decisions.

Instead of giving every user the same resume feedback, the application analyzes a resume **according to the user's specific career goal**.

For example:

A user can upload the same resume and select:

- Backend Developer
- Full Stack Developer
- Data Scientist
- Machine Learning Engineer
- Frontend Developer

The AI will provide a different analysis for each goal.

### Example

If the user's goal is:

```text
Backend Developer
````

 The system focuses on backend-related technologies such as:

```
Python
Flask
Django
SQL
REST APIs
Databases
Authentication
Git
Docker
```

 It avoids treating unrelated tools as important backend skills.

 The system then identifies:

 1. Relevant skills already present
2. Missing skills
3. A roadmap for learning the missing skills
4. Interview questions relevant to the target role

---

 # ✨ Key Features

 ## 🔐 User Authentication

 Users can:

 - Create an account
- Login
- Logout
- Access their personal dashboard
- View their previous resume analyses

---

 ## 📄 Resume Upload

 Users can upload resumes in:

 - PDF
- DOCX

 The application extracts text from the uploaded resume and sends the extracted information to the AI analysis system.

---

 ## 🎯 Goal-Based Resume Analysis

 The user specifies their target career.

 Examples:

```
Backend Developer
Full Stack Developer
Frontend Developer
Software Engineer
Data Scientist
Machine Learning Engineer
DevOps Engineer
```

 The AI evaluates the resume specifically for that goal.

---

 ## 🧠 AI Skill Analysis

 The system identifies skills relevant to the user's target role.

 The AI does not simply list every technology found in the resume.

 Instead, it evaluates whether the skill is relevant to the selected career goal.

---

 ## 🔍 Skill Gap Detection

 The system identifies skills that are important for the selected career but are missing from the user's resume.

 Example:

```
Target Role:
Backend Developer
```

 Possible missing skills:

```
REST APIs
Docker
Redis
Authentication
Testing
```

---

 ## 🗺️ Personalized Learning Roadmap

 The application generates a roadmap based only on the user's missing skills.

 Example:

```
1. Learn REST API fundamentals
2. Build APIs using Flask
3. Learn authentication
4. Learn database optimization
5. Learn Docker
6. Build a production-ready backend project
```

 The roadmap changes depending on the user's existing skills.

---

 ## 💬 Interview Preparation

 The system generates interview questions related to:

 - Target role
- Existing skills
- Missing skills
- Resume projects
- Technologies mentioned in the resume

 Example:

```
How does REST API authentication work?

What is the difference between SQL and NoSQL?

How would you optimize a slow database query?

How does Flask handle routing?
```

---

 ## 📚 Analysis History

 Previous resume analyses are stored in the database.

 Users can access their previous reports through the History section.

---

 # 🏗️ System Architecture

```
                         ┌────────────────────┐
                         │       User         │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Flask Web App    │
                         └─────────┬──────────┘
                                   │
                 ┌─────────────────┼─────────────────┐
                 │                 │                 │
                 ▼                 ▼                 ▼
          ┌─────────────┐  ┌──────────────┐  ┌──────────────┐
          │ PDF Parser  │  │ DOCX Parser  │  │ User Goal    │
          │   PyPDF2    │  │ python-docx  │  │              │
          └──────┬──────┘  └──────┬───────┘  └──────┬───────┘
                 │                │                 │
                 └────────────────┼─────────────────┘
                                  ▼
                         ┌────────────────────┐
                         │   AI Analyzer      │
                         │     OpenAI         │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Analysis Result    │
                         │                    │
                         │ • Skills           │
                         │ • Missing Skills   │
                         │ • Roadmap          │
                         │ • Interview Qs     │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │     TiDB Cloud     │
                         │      Database      │
                         └────────────────────┘
```

---

 # 🛠️ Technology Stack

 ## Frontend

 - HTML5
- CSS3
- Jinja2 Templates

 ## Backend

 - Python
- Flask

 ## AI

 - OpenAI API

 ## Database

 - TiDB Cloud
- SQLAlchemy
- PyMySQL

 ## Resume Processing

 - PyPDF2
- python-docx

 ## Environment Management

 - Python Virtual Environment
- python-dotenv

---

 # 📁 Project Structure

```
AI CareerCopilot/
│
├── app.py
│
├── ai.py
│
├── db.py
│
├── models.py
│
├── README.md
│
├── .env
│
├── .gitignore
│
├── ca.pem
│
├── templates/
│   │
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│   │
│   ├── style.css
│   └── ...
│
└── venv/
```

---

 # 📄 File Responsibilities

 ## `app.py`

 Main Flask application.

 Responsible for:

 - Routing
- Signup
- Login
- Dashboard
- Resume upload
- PDF/DOCX processing
- AI analysis
- Saving reports
- History
- Logout

---

 ## `ai.py`

 Contains the AI resume analysis logic.

 Responsible for:

 - Sending resume information to OpenAI
- Evaluating resume according to user's goal
- Finding relevant skills
- Finding missing skills
- Generating roadmap
- Generating interview questions
- Returning structured JSON

---

 ## `db.py`

 Responsible for:

 - Connecting Flask to TiDB
- Creating SQLAlchemy engine
- Creating database sessions
- Creating the SQLAlchemy Base

---

 ## `models.py`

 Contains database models such as:

```
User
Reports
```

 The `User` model stores user information.

 The `Reports` model stores previous resume analyses.

---

 # 🚀 Getting Started

 ## Prerequisites

 Before running the project, make sure you have:

 - Python 3.10+
- VS Code
- Git
- TiDB Cloud account
- OpenAI API key

---

 # 🐍 1. Create Virtual Environment

 Open the VS Code terminal.

 Navigate to the project:

```
cd "D:\Vanshika\AI CareerCopilot"
```

 Create a virtual environment:

```
python -m venv venv
```

 Activate it:

```
.\venv\Scripts\activate
```

 You should see:

```
(venv)
```

 in the terminal.

---

 # 📦 2. Install Dependencies

 Run:

```
pip install flask sqlalchemy pymysql openai python-dotenv PyPDF2 python-docx
```

 Verify installed packages:

```
pip freeze
```

 Important packages include:

```
Flask
SQLAlchemy
PyMySQL
OpenAI
python-dotenv
PyPDF2
python-docx
```

---

 # 🔑 3. Configure OpenAI

 Create a file called:

```
.env
```

 in the project root.

 Example:

```
OPENAI_API_KEY=your_openai_api_key
FLASK_SECRET_KEY=your_secret_key
```

 Do not commit the `.env` file to GitHub.

---

 # 🗄️ 4. Configure TiDB Cloud

 Create a TiDB Cloud database.

 From TiDB Cloud:

```
Instance
   ↓
Connect
   ↓
PyMySQL
```

 Use the provided credentials.

 You will need:

 - Host
- Port
- Username
- Password
- Database
- CA certificate

---

 # 🔐 5. Download TiDB CA Certificate

 For secure SSL connection, download the CA certificate from the TiDB Cloud connection page.

 Place the certificate inside your project.

 Example:

```
AI CareerCopilot/
└── ca.pem
```

 Do not upload the certificate or database credentials to GitHub.

---

 # ⚙️ 6. Database Configuration

 Example `db.py`:

```
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CA_PATH = os.getenv("TIDB_CA_PATH")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": CA_PATH
        }
    }
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

 Example `.env`:

```
DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@HOST:4000/sys
TIDB_CA_PATH=D:\Vanshika\AI CareerCopilot\ca.pem
```

 Use your actual TiDB credentials locally.

---

 # 🤖 7. Configure AI

 Example `ai.py`:

```
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

def analyze_resume(resume_text, user_goal):

    prompt = f"""
    You are a senior software engineer and hiring manager.

    Evaluate the resume based on the user's goal.

    User goal:
    {user_goal}

    STRICT RULES:

    - Extract only relevant skills for this goal.
    - Remove irrelevant tools.
    - Identify real skill gaps.
    - Generate a roadmap only for missing skills.
    - Make the output different based on the user's goal.

    Return only JSON:

    {{
        "skills": [],
        "missing_skills": [],
        "roadmap": [],
        "interview_questions": []
    }}

    Resume:
    {resume_text}
    """

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict hiring manager."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        return json.loads(content[start:end])

    except Exception as e:

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }
```

---

 # 🧑‍💻 8. Run the Application

 Make sure your virtual environment is active:

```
.\venv\Scripts\activate
```

 Run:

```
python app.py
```

 You should see:

```
* Running on http://127.0.0.1:5000
```

 Open your browser and visit:

```
http://127.0.0.1:5000
```

---

 # 🌐 Application Routes

 | Route | Purpose |
| --- | --- |
| `/` | Home |
| `/signup` | Create account |
| `/login` | Login |
| `/dashboard` | Resume analysis |
| `/history` | Previous reports |
| `/logout` | Logout |

---

 # 🔄 Application Workflow

 ## Step 1 — Create Account

 Go to:

```
/signup
```

 Enter:

```
Email
Password
```

 Create the account.

---

 ## Step 2 — Login

 Go to:

```
/login
```

 Enter your credentials.

---

 ## Step 3 — Dashboard

 After login, the user reaches:

```
/dashboard
```

 Enter a career goal.

 Example:

```
Backend Developer
```

---

 ## Step 4 — Upload Resume

 Upload:

```
resume.pdf
```

 or:

```
resume.docx
```

---

 ## Step 5 — Resume Extraction

 The backend extracts text.

 ### PDF

 Using:

```
PyPDF2
```

 ### DOCX

 Using:

```
python-docx
```

---

 ## Step 6 — AI Analysis

 Extracted resume text and career goal are sent to the AI.

 The AI evaluates the resume based on the selected career.

---

 ## Step 7 — Result

 The application returns:

```
{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}
```

---

 # 📊 Example Output

 For a Backend Developer:

```
{
    "skills": [
        "Python",
        "Flask",
        "SQL",
        "REST APIs"
    ],
    "missing_skills": [
        "Docker",
        "Redis",
        "Automated Testing"
    ],
    "roadmap": [
        "Learn Docker fundamentals",
        "Learn Redis caching",
        "Practice backend testing",
        "Build a production-ready backend project"
    ],
    "interview_questions": [
        "What is REST?",
        "How does Flask routing work?",
        "What is database indexing?",
        "How would you improve API performance?"
    ]
}
```

---

 # 🗃️ Database

 The application uses TiDB Cloud as the database.

 SQLAlchemy provides the database abstraction layer.

 Conceptually:

```
Flask
  ↓
SQLAlchemy
  ↓
PyMySQL
  ↓
TiDB Cloud
```

---

 # 👤 User Data

 The application stores user information such as:

```
User ID
Email
Password
```

---

 # 📑 Reports

 Each analysis can contain:

```
User ID
Resume Text
AI Analysis Result
```

 The AI result is stored as JSON.

---

 # 🔐 Security

 ## Never expose API keys

 Do not put this directly in public code:

```
client = OpenAI(
    api_key="your-key"
)
```

 Use environment variables instead.

---

 ## Never commit `.env`

 Add:

```
.env
```

 to `.gitignore`.

---

 ## Never expose database passwords

 Do not commit:

```
DATABASE_URL
```

 with real credentials.

---

 ## Never expose CA certificates

 Keep your TiDB CA certificate private and out of public repositories.

---

 # 📄 Recommended `.gitignore`

 Create `.gitignore`:

```
.env
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.vscode/
*.pem
```

---

 # 🧪 Testing

 Before deployment, test the following:

 ### Authentication

 - [ ] Signup works
- [ ] Duplicate email is handled
- [ ] Login works
- [ ] Invalid credentials are rejected
- [ ] Logout works

 ### Resume Upload

 - [ ] PDF upload works
- [ ] DOCX upload works
- [ ] Invalid files are handled
- [ ] Empty resume is handled

 ### AI

 - [ ] OpenAI API key works
- [ ] Resume analysis works
- [ ] Different career goals produce different results
- [ ] Invalid AI responses are handled

 ### Database

 - [ ] TiDB connection works
- [ ] Users are saved
- [ ] Reports are saved
- [ ] History loads correctly

---

 # 🐛 Troubleshooting

 ## `ModuleNotFoundError: No module named 'PyPDF2'`

 Run:

```
pip install PyPDF2
```

---

 ## `ModuleNotFoundError: No module named 'docx'`

 Run:

```
pip install python-docx
```

---

 ## `ModuleNotFoundError: No module named 'pymysql'`

 Run:

```
pip install pymysql
```

---

 ## `Missing credentials`

 If OpenAI shows:

```
Missing credentials
```

 check:

```
OPENAI_API_KEY
```

 in `.env`.

 Also ensure `ai.py` contains:

```
from dotenv import load_dotenv

load_dotenv()
```

---

 ## `MySQLdb` error

 If SQLAlchemy tries to import:

```
MySQLdb
```

 make sure your connection URL uses:

```
mysql+pymysql://
```

 instead of:

```
mysql+mysqldb://
```

---

 ## `ssl_mode` error

 If PyMySQL reports:

```
unexpected keyword argument 'ssl_mode'
```

 configure the CA certificate through the PyMySQL SSL configuration rather than passing unsupported parameters directly.

---

 ## Flask does not start

 Make sure your virtual environment is active:

```
.\venv\Scripts\activate
```

 Then:

```
python app.py
```

---

 # 🚀 Future Roadmap

 ## Phase 1 — Core Application

 - [x] Flask backend
- [x] User authentication
- [x] Resume upload
- [x] PDF parsing
- [x] DOCX parsing
- [x] AI resume analysis
- [x] Database integration
- [x] Analysis history

 ## Phase 2 — Better Career Intelligence

 - [ ] Resume score
- [ ] Job description matching
- [ ] ATS compatibility score
- [ ] Skill priority ranking
- [ ] Career recommendations
- [ ] Personalized project recommendations

 ## Phase 3 — AI Resume Copilot

 - [ ] AI resume rewriting
- [ ] Bullet point improvement
- [ ] Achievement generation
- [ ] ATS-friendly formatting
- [ ] Resume section suggestions
- [ ] Cover letter generation

 ## Phase 4 — Interview Copilot

 - [ ] AI mock interviews
- [ ] Technical interview mode
- [ ] Behavioral interview mode
- [ ] Interview scoring
- [ ] Answer feedback
- [ ] Personalized interview preparation

 ## Phase 5 — Production

 - [ ] Password hashing
- [ ] Proper authentication
- [ ] Rate limiting
- [ ] Input validation
- [ ] Error monitoring
- [ ] Production database configuration
- [ ] Cloud deployment
- [ ] HTTPS
- [ ] Secure secret management

---

 # 💡 Why AI Career Copilot?

 Traditional resume tools often give generic advice.

 AI Career Copilot focuses on:

```
Resume
   +
Career Goal
   ↓
Personalized Analysis
   ↓
Skill Gap
   ↓
Learning Roadmap
   ↓
Interview Preparation
```

 The goal is to transform a resume from a static document into a **personalized career development plan**.

---

 # 🎯 Target Users

 AI Career Copilot is designed for:

 - 🎓 College students
- 👩‍💻 Freshers
- 💼 Job seekers
- 🔄 Career switchers
- 🧑‍💻 Software developers
- 📊 Data professionals
- 🤖 AI/ML aspirants

---

 # 📈 Example Use Case

 A student uploads a resume containing:

```
Python
Excel
HTML
CSS
SQL
Flask
```

 and selects:

```
Backend Developer
```

 Instead of simply listing all technologies, the AI focuses on backend requirements.

 It may identify:

 ### Relevant Skills

```
Python
Flask
SQL
```

 ### Less Relevant

```
Excel
Basic HTML/CSS
```

 ### Missing Skills

```
REST APIs
Testing
Docker
Authentication
```

 ### Roadmap

```
1. REST API development
2. Authentication
3. Backend testing
4. Docker
5. Build a production-ready API
```

 This makes the guidance specific to the user's career goal.

---

 # 🌟 Project Vision

 The long-term vision of AI Career Copilot is to become an AI-powered personal career assistant that helps users go from:

```
"I don't know what I am missing"
```

 to:

```
"I know exactly what skills I need,
what to learn next,
what projects to build,
and how to prepare for interviews."
```

---

 # 👩‍💻 Author

 **Vanshika**

 Built as an AI-powered career guidance and resume analysis project.

---

 # 📜 License

 This project is currently intended for educational, portfolio, and development purposes.

 A production license can be added when the project is officially released.

---

 # ⭐ Support

 If you find this project useful, consider giving it a ⭐ on GitHub.

---

 ## 🚀 AI Career Copilot

 **Resume → Skills → Skill Gaps → Roadmap → Interview Preparation**

 Built with Python, Flask, OpenAI, SQLAlchemy, PyMySQL and TiDB Cloud.

```

### ⚠️ Ek correction

README mein maine `ca.pem` ko project structure mein dikhaya hai **sirf example ke liye**. Actual project mein CA certificate ko GitHub par upload **mat karna**. `.gitignore` mein `*.pem` rakhna.

Aur jo **TiDB password tumne chat mein expose kiya tha, usko definitely regenerate/reset kar lena** before continuing with the database connection.
```
