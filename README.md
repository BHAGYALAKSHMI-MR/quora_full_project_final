===========================

Quora-style Django Project.
===========================

----------------------------------
🌐 Live Demo (Deployed Version)
----------------------------------

✅ Visit the deployed project here:
Quora-style Django Project(just named thinkflow)
🔗 https://thinkflow.pythonanywhere.com/

(just copy paste link in browser)

This is a Django-based Q&A web app inspired by Quora. Users can sign up, log in, post questions, answer them, like answers/questions, and delete their own questions.
 You can now:
    - Sign up or log in 
    - Post and answer questions(by clicking on question question details will come. There you can answer questions)
    - Like/unlike answers and questions by clicking on like/unlike
    - Delete your own questions

---------------------------
🔧 Setup Instructions (Local)
---------------------------

1. 🔽 Clone or download the project

    If using Git:
    > git clone https://github.com/BHAGYALAKSHMI-MR/quora_full_project_final

    Or just download and extract the zip.

2. 📁 Navigate into the project folder

    > cd quora_full_project_final

3. 🐍 Create and activate a virtual environment (optional but recommended)

    > python -m venv env
    > env\Scripts\activate       # On Windows
    > source env/bin/activate   # On Mac/Linux

4. 📦 Install required packages

    > pip install django

    (Or if you have a `requirements.txt`, use: `pip install -r requirements.txt`)

5. ⚙️ Run migrations

    > python manage.py makemigrations quoraapp
    
    > python manage.py migrate

6. 👤 Create a superuser

    > python manage.py createsuperuser

7. 🌐 Start the development server

    > python manage.py runserver

8. 🚀 Visit in your browser

    > http://127.0.0.1:8000/

    You can now:
    - Sign up or log in 
    - Post and answer questions(by clicking on question question details will come. There you can answer questions)
    - Like/unlike answers and questions by clicking on like/unlike
    - Delete your own questions

---------------------------
📁 Project Structure
---------------------------

quora_full_project_final/
├── manage.py
├── quoraproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quoraapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── home.html
│       ├── login.html
│       ├── signup.html
│       ├── question_detail.html
│       └── confirm_delete.html



