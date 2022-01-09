from flask import Flask, abort, request, render_template, send_from_directory
from functions import read_posts, read_comments, get_id

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', posts=read_posts(), comments=read_comments())


@app.route("/post/<int:post_id>")
def page_post(post_id):
    posts = get_id(post_id)
    return render_template('post.html', posts=posts)


if __name__ == "__main__":
    app.run()
