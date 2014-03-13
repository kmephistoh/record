#coding: utf8
from flask import Flask, request, url_for, render_template
app = Flask("__main__")


@app.route("/")
def hello():
    return "呵呵呵"


@app.route("/about")
def about():
    return "About page"


@app.route("/user/")
@app.route("/user/<username>")
def user_info(username=None):
    return render_template('hello.html', name=username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Your post id is %s" % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


# url_for('static', filename='1.go')
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


if __name__ == '__main__':
    app.debug = True
    app.run()
