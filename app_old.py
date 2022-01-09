from flask import Flask, render_template

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html')


# @app.route("/tag")
# def page_tag():
#     tag = request.args.get("tag")
#     if not tag:
#         abort(400)
#     data = read_json()
#     posts = get_posts_by_tag(tag)
#     return render_template('post_by_tag.html', tag=tag, posts=posts)
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_create():
#     if request.method == 'GET':
#         return render_template('post_form.html')
#
#     content = request.form.get('content')
#     picture = request.files.get('picture')
#     if not content or not picture:
#         return 'ошибка загрузки'
#     path = f'{UPLOAD_FOLDER}/{picture.filename}'
#     post = {
#             'content': content,
#             'pic': f'/{path}',
#            }
#     picture.save(path)
#     add_post(POST_PATH, post)
#     return render_template('post_uploaded.html', post=post)
#
#
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()

