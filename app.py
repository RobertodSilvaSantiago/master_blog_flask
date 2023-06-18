"""This web app module uses Flask to create a blogging application with CRUD
functionality. It includes routes for rendering the main page, adding a new
blog post, updating an existing blog post, deleting a blog post, and
incrementing the like count of a blog post. The data is stored using a
JsonStorage class from the "data_handler_json" module."""

from flask import Flask, render_template, request, redirect, url_for
from data_handler_json import JsonStorage

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page HTML template with all blog posts displayed."""
    return render_template('index.html', posts=app_blog.load_blog_data())


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handle GET and POST requests
    GET - render the add.html template with form for creating the post. it will
        send a POST request to this route with arguments to create new post.
    Post -  will create new post in json file and redirect to the main page
    """
    if request.method == 'POST':
        post_to_add = {'author': request.form.get('author'),
                    'title': request.form.get('title'),
                    'content': request.form.get('content')}

        app_blog.add_post(post_to_add)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    GET - render the update.html template with form to update the post. it will
        send a POST request to this route with updated information in arguments.
    Post -  will update the post in json file and redirect to the main page
    """
    # getting the blog posts from the JSON file
    post = app_blog.get_post_by_id(post_id)

    if post is None:
        # Post not found
        return "Post not found", 404

    # POST method case
    if request.method == 'POST':
        # create post: dict to update with sent arguments and updated it in json file
        post_likes = app_blog.get_post_by_id(post_id)['likes']
        post_to_update = {'id': post_id,
                        'author': request.form.get('author'),
                        'title': request.form.get('title'),
                        'content': request.form.get('content'),
                        'likes': post_likes}

        app_blog.update_post(post_to_update)
        return redirect(url_for('index'))

    # case of method GET
    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """deleting post and redirect to main page"""
    app_blog.delete_post(post_id)
    return redirect(url_for('index'))


@app.route('/like/<int:post_id>')
def like(post_id):
    """Increment the like count for a specific blog post identified by the
    post_id, update the post in the storage, and redirect to the main page.
    """
    post = app_blog.get_post_by_id(post_id)
    post['likes'] += 1
    app_blog.update_post(post)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app_blog = JsonStorage("master_blog")
    app.run(debug=True)