import json


def get_posts_from_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def filter_posts(posts, filter_):
    filtered_posts = []
    for post in posts:
        print(post['content'].lower())
        print(filter_)
        if filter_.lower() in post['content'].lower():
            filtered_posts.append(post)

    print(filtered_posts)
    return filtered_posts
