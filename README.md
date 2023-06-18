# master_blog_flask

The application is a simple Flask blog app that allows users to create, view, update, and delete blog posts. Here's an overview of its functionality:

Main Page (index): The main page of the application displays all the existing blog posts. It retrieves the blog data from the JsonStorage class and renders the index.html template, which lists the posts along with their titles, authors, content, and options to update, delete, and like a post.

Add Page: The /add route handles both GET and POST requests. When a user visits the /add URL, they are presented with a form to add a new blog post. When the form is submitted (POST request), the data is collected from the form, including the author, title, and content of the post. The JsonStorage class is used to add the new post to the blog data.

Update Page: The /update/<int:post_id> route handles both GET and POST requests for updating an existing blog post. When a user visits the /update/<post_id> URL, the corresponding post is retrieved from the JsonStorage class based on the provided post_id. The user is presented with a form pre-filled with the existing post data (author, title, content). When the form is submitted (POST request), the updated data is collected and applied to the post using the JsonStorage class.

Delete Endpoint: The /delete/<int:post_id> route handles the request to delete a specific blog post. When a user visits the /delete/<post_id> URL, the corresponding post is deleted from the blog data using the JsonStorage class.

Like Endpoint: The /like/<int:post_id> route handles the request to increment the like count of a blog post. When a user visits the /like/<post_id> URL, the corresponding post is retrieved from the JsonStorage class based on the provided post_id. The like count of the post is incremented and updated using the JsonStorage class.

The JsonStorage class is responsible for storing and managing the blog data using a JSON file. It provides methods to load the blog data, add new posts, update existing posts, and delete posts.

Overall, the application provides a basic blogging platform where users can interact with blog posts by adding, updating, and deleting them, as well as liking posts to show their appreciation.
