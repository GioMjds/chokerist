from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    fullname = f"{firstname} {lastname}"
    studentID = request.form['studentID']
    course = request.form['course']
    block = request.form['block']
    subject = request.form['subject']
    return render_template('user.html', fullname=fullname, studentID=studentID, course=course, block=block, subject=subject)

@app.route('/redirect')
def redirect_page():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)