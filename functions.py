import json
import pprint


def read_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def read_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
        return comments


def get_post_by_id(post_id):
    posts = read_posts()
    for post in posts:
        if post_id == post['pk']:
            return post
    return None


def get_post_comments_by_pk(post_id):
    comments = read_comments()
    match_comments = []
    for comment in comments:
        if comment['post_id'] == post_id:
            match_comments.append(comment)
    return match_comments


def search_post(word):
    match_posts = []
    posts = read_posts()
    if word is None:
        return posts
    for post in posts:
        if word.lower() in post['content'].lower():
            match_posts.append(post)
    return match_posts


def count_comments():
    comments = read_comments()
    count = {}
    for comment in comments:
        post_id = comment['post_id']
        if post_id in count:
            count[post_id] += 1
        else:
            count[post_id] = 1
    return count


# print(count_comments())


def get_posts_with_comments():
    posts = read_posts()
    comment_count = count_comments()
    for index, post in enumerate(posts):
        post_id = post['pk']
        posts[index]['comments_count'] = comment_count.get(post_id, 0)
    return posts


# pprint.pprint(get_posts_with_comments())


# print(search_post('красиво'))


def get_posts_by_user(username):
    match_posts = []
    posts = get_posts_with_comments()
    for post in posts:
        if username == post['poster_name']:
            match_posts.append(post)
    return match_posts

