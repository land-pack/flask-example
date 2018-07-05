from flask import render_template, Blueprint, request

# Config

article_blueprint = Blueprint('article', __name__, template_folder='templates')


# routes

@article_blueprint.route('/article', methods=["POST", "GET", "PUT"])
def article():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        category = request.form.get("category")

        print(title, content, category)

        return "success"


    elif request.method == 'PUT':
        pass

    elif request.method == 'GET':
        pass

    return render_template('index.html')


@article_blueprint.route('/article', methods=["GET"])
def articles():
    # TODO lists all the article for views .

    return render_template('index.html')
