from flask import Blueprint, render_template, request
from loader import utils

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/', methods=["GET"])
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post/', methods=["POST"])
def upload_page():
    picture = request.files.get('picture')
    content = request.form.get('content')
    post = utils.upload_post(picture, content, "posts.json")
    if post:
        return render_template("post_uploaded.html", post=post)
    else:
        return "Файл не загружен<br/><a href = \"/post/\">Назад</a>"
