from flask import Blueprint, render_template, request
from main import utils

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@search_blueprint.route('/search/')
def search_page():
    s = request.args.get('s')
    posts = utils.get_posts_from_json("main/posts.json")
    filtered_posts = utils.filter_posts(posts, s)
    return render_template("post_list.html", s=s, posts=filtered_posts)
