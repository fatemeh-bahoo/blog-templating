from flask import Flask, render_template
import requests

url = "https://api.npoint.io/27f4fa24e392f5db7968"
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    response = requests.get(url)
    blog_data = response.json()
    return render_template("index.html", data=blog_data)

@app.route('/post/<int:num>')
def get_allpost(num):
    response = requests.get(url)
    all_posts = response.json()
    requested_post = None
    for post in all_posts:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
