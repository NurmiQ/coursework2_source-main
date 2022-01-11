from flask import Flask, abort, request, render_template, send_from_directory
from functions import read_posts, read_comments, get_id, search_post

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', posts=read_posts(), comments=read_comments())


@app.route("/post/<int:post_id>")
def page_post(post_id):
    posts = get_id(post_id)
    return render_template('post.html', posts=posts)


@app.route("/search/")
def page_search(word):
    word = request.args.get('s')
    posts = search_post(word)
    return render_template('search.html', posts=posts, count_posts=len(posts))


if __name__ == "__main__":
    app.run()
