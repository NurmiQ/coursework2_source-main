from flask import Flask, abort, request, render_template, send_from_directory
from functions import read_posts, get_posts_with_comments, get_posts_by_user, get_post_comments_by_pk, read_comments, get_post_by_id, search_post

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', posts=get_posts_with_comments(), comments=read_comments())


@app.route("/post/<int:post_id>")
def page_post(post_id):
    post = get_post_by_id(post_id)
    comments = get_post_comments_by_pk(post_id)
    return render_template('post.html', post=post, comments=comments)


@app.route("/search/")
def page_search():
    word = request.args.get('s')
    posts = search_post(word)
    count_posts = len(posts)
    return render_template('search.html', posts=posts, count_posts=count_posts)


@app.route("/users/<username>")
def page_user(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


if __name__ == "__main__":
    app.run()
