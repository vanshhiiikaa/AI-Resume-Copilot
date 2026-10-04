from flask import Flask, render_template, request, redirect, session
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json
from ai import analyze_resume

app = Flask(__name__)
app.secret_key = "secret123"

Base.metadata.create_all(bind=engine)

#HOME
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/login')

#SIGN UP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    db = SessionLocal()

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user already exists
        existing_user = db.query(models.User).filter_by(email=email).first()
        if existing_user:
            return "User already exists. Please log in."

        # Create a new user
        new = models.User(email=email, password=password)
        db.add(new)
        db.commit()

        return redirect('/login')
    return render_template('signup.html')

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    db = SessionLocal()

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists
        user = db.query(models.User).filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id
            session['user'] = user.email
            return redirect('/dashboard')
        else:
            return "Invalid email or password."

    return render_template('login.html')

#DASHBOARD
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    result = None

    if request.method == 'POST':
        user_goal = request.form.get('goal')
        resume_text = request.form.get('resume')

        file = request.files.get('file')

        #filehandling
        if file and file.filename != '':
            if file.filename.endswith('.pdf'):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF error: {str(e)}"}

            elif file.filename.endswith('.docx'):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"DOCX error: {str(e)}"}
        if resume_text and user_goal:
            try:
                result = analyze_resume(resume_text, user_goal)

                #save to database
                db = SessionLocal()
                user = db.query(models.User).filter_by(email=session['user']).first()

                report = models.Reports(
                    user_id=user.id,
                    resume_text=resume_text,
                    result=json.dumps(result)
                )

                db.add(report)
                db.commit()

            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}
        return render_template(
            "dashboard.html",
            user=session['user'],
            result=result,
        )

#HISTORY
@app.route('/history')
def history():
    if 'user' not in session:
        return redirect('/login')

    db = SessionLocal()
    user = db.query(models.User).filter_by(email=session['user']).first()

    reports = db.query(models.Reports).filter_by(user_id=user.id).all()

    #Convert JSON string > dictonary
    pasred_reports = []
    for r in reports:
        try:
            result_data = json.loads(r.result)
        except:
            result_data = {}

        pasred_reports.append({
            "resume":r.resume_text,
            "result": result_data
        })    
        
    return render_template("history.html", reports=pasred_reports)

#Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)