from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', 'GET'])  # 创建一个login接口
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)


if __name__ == '__main__':
    app.run(host=" 10.28.242.8", port=80, debug=True)
