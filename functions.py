import json


def read_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def read_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
        return comments


def get_id(post_id):
    comments = read_comments()
    for comment in comments:
        if post_id == comment['post_id']:
            return post_id


def search_post(word):
    match_posts = []
    posts = read_posts()
    for post in posts:
        if word.lower() in post['content'].lower():
            match_posts.append(post)
    return match_posts



print(search_post('дома'))

#
# def get_hash():
#     match_hash = []
#     g_hash = read_json()
#     for tag in g_hash:
#         content = tag['content']
#         words = content.split()
#         for word in words:
#             if word.startswith('#'):
#                 match_hash.append(word[1:])
#     return match_hash
#
#
# # print(get_hash())
#
#
# def get_posts_by_tag(tag):
#     results = []
#     posts = read_json()
#     for post in posts:
#         if f'#{tag}' in post['content']:
#             results.append(post)
#     return results
#
# # print(get_posts_by_tag('пирог'))
#
#
# def add_post(filename, post):
#     posts = read_json()
#     posts.append(post)
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(posts, file, ensure_ascii=False, indent=4, sort_keys=True)
