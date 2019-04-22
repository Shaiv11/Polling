from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "polling.db"))


app = Flask(__name__)
db = SQLAlchemy(app)


poll_data = {
   'question': 'Which web framework do you use?',
   'fields': ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}


@app.route('/')
def base():
    return render_template('index.html')


@app.route('/vote')
def vote():
    return render_template('poll.html', data=poll_data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
