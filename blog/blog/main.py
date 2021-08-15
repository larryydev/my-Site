from flask import Flask, render_template, url_for, redirect, request
import requests, json


app = Flask(__name__)

XAPIKey = 'h8mWXY88.bBEC8CWmjJmhnRmSdkMuZB-t4W48phcxu'

@app.route("/")
def index():
    posts = reversed(json.loads(requests.get('https://38vaq8.deta.dev/blogs', 
    headers= {
        'Content-Type': 'application/json',
        'X-API-Key': XAPIKey
        }
    ).text)['_items'])
    return render_template('blogs.html', posts = posts)


@app.route('/addblog', methods=['POST'])
def addblog():
    key = request.form['key']
    title = request.form['title']
    content = request.form['content']

    requests.post('https://38vaq8.deta.dev/blog', 
    headers= {
        'Content-Type': 'application/json',
        'X-API-Key': key
    }, 
    json= {
        'title': title,
        'content': content
    }
    )

    return redirect(url_for('index'))


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    selected = request.args.get('type')
    url = f'https://38vaq8.deta.dev/blog/{selected}'
    post = json.loads(requests.get(url, 
    headers= {
        'Content-Type': 'application/json',
        'X-API-Key': XAPIKey
        }
    ).text)
    return render_template('singleblog.html', post = post)


if __name__ == '__main__':
    app.run(debug=True)