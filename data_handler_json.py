import os
import json


class JsonStorage():
    """json data CRUD handler for master blog app"""

    def __init__(self, storage_name):
        self.file_path = storage_name

    def _get_last_post_id(self) -> int:
        """return last post id. if no posts - return 0"""
        blog_data = self.load_blog_data()
        if blog_data:
            return blog_data[-1]['id']

        return 0

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, storage_name):
        """Check if storage with that name exist. if not creates one.
        setting file_path"""
        storage_path = storage_name + ".json"
        if not os.path.exists(storage_path):
            with open(storage_path, "w") as file:
                json.dump([], file)
        self._file_path = storage_path

    def _save_data(self, blog_data: list) -> None:
        """Serialize the blog data(list of dictionaries) in json file"""
        with open(self._file_path, "w") as file:
            json.dump(blog_data, file)

    def load_blog_data(self) -> list:
        """return a list of dictionaries that contain blog posts
        :return example
        [
            {
            'id': 1,
            'author':
            'John Doe',
            'title': 'First Post',
            'content': 'This is my first post.'
            },
            .....
        ]
        """
        with open(self._file_path, "r") as file:
            blog_data = json.load(file)

        return blog_data

    def add_post(self, blog_post: dict):
        """Adding blog post to json file. the function will add/rewrite
        unique id"""
        # loading and and adding blog post to data
        blog_data = self.load_blog_data()
        new_id_for_post = self._get_last_post_id() + 1
        blog_post['id'] = new_id_for_post
        blog_post['likes'] = 0
        blog_data.append(blog_post)

        self._save_data(blog_data)

    def update_post(self, post_to_update: dict):
        """updating the post in json file"""

        blog_data = self.load_blog_data()

        # finding the index of post we want to update
        index_to_update = next((i for i, post in enumerate(blog_data)
                                if post['id'] == post_to_update['id']), None)

        # updating
        if index_to_update is not None:
            blog_data[index_to_update] = post_to_update

        self._save_data(blog_data)

    def delete_post(self, id_to_delete: int):
        """Delete post by its id: int passed to the function"""
        blog_data = self.load_blog_data()

        # finding index of post to delete
        index_to_delete = next((i for i, post in enumerate(blog_data)
                                if post['id'] == id_to_delete), None)

        # deleting post and saving data
        if index_to_delete is not None:
            del blog_data[index_to_delete]
            self._save_data(blog_data)

    def get_post_by_id(self, post_id: int) -> dict:
        """Return a post based on its ID - if id exist. otherwise None"""
        blog_data = self.load_blog_data()

        # finding index of post
        index_of_post = next((i for i, post in enumerate(blog_data)
                            if post['id'] == post_id), None)

        if index_of_post is not None:
            return blog_data[index_of_post]

