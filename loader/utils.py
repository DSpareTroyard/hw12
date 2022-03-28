import json


def upload_post(picture, content, path):
    if picture:
        with open(path, "r", encoding='utf-8') as f:
            posts = json.load(f)

        filename = picture.filename
        picture_path = f"./uploads/{filename}"
        picture.save(picture_path)

        post = {'pic': picture_path,
                'content': content}

        print(post)
        posts.append(post)
        print(posts)
    else:
        return False
