import json
import os.path

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def upload_post(picture, content, path):
    if picture:
        with open(path, "r", encoding='utf-8') as f:
            posts = json.load(f)

        filename = picture.filename
        extension = filename.split(".")[-1]
        if extension not in ALLOWED_EXTENSIONS:
            return False
        picture_path = f"./uploads/images/{filename}"
        picture_path_json = f"/uploads/images/{filename}"
        picture.save(picture_path)

        post = {'pic': picture_path_json,
                'content': content}
        posts.append(post)
        if os.path.isfile(picture_path):
            with open(path, "w", encoding='utf-8') as f:
                json.dump(posts, f)
            return post

    return False
