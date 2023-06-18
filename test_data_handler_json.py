import pytest
import data_handler_json
import os


post1 = {'id': -5, 'author': 'John Doe', 'title': 'First Post',
        'content': 'This is my first post.'}
post2 = {'id': 55, 'author': 'John Doe', 'title': 'Second Post',
        'content': 'This is my second post.'}


def test_blog_created():
    data_handler = data_handler_json.JsonStorage("master_blog")
    assert data_handler
    assert len(data_handler.load_blog_data()) == 0
    os.remove('master_blog.json')


def test_add_post():
    data_handler = data_handler_json.JsonStorage("master_blog")
    # first post
    data_handler.add_post(post1)
    blog_data = data_handler.load_blog_data()
    assert blog_data[0]['author'] == 'John Doe'
    assert blog_data[0]['title'] == 'First Post'
    assert blog_data[0]['content'] == 'This is my first post.'
    assert blog_data[0]['id'] == 1

    # second post
    data_handler.add_post(post2)
    blog_data = data_handler.load_blog_data()
    assert blog_data[1]['author'] == 'John Doe'
    assert blog_data[1]['title'] == 'Second Post'
    assert blog_data[1]['content'] == 'This is my second post.'
    assert blog_data[1]['id'] == 2

    os.remove('master_blog.json')


def test_update_post():
    #  update data and save
    data_handler = data_handler_json.JsonStorage("master_blog")
    data_handler.add_post(post1)
    user_post = data_handler.load_blog_data()[0]
    user_post['content'] = 'new content'
    data_handler.update_post(user_post)

    # load updated data and check
    updated_user_post = data_handler.load_blog_data()[0]
    assert updated_user_post['content'] == 'new content'

    os.remove('master_blog.json')

def test_delete_post():
    data_handler = data_handler_json.JsonStorage("master_blog")
    data_handler.add_post(post1)
    data_handler.add_post(post2)
    data_handler.delete_post(post1['id'])

    blog_data: list = data_handler.load_blog_data()
    assert len(blog_data) == 1
    assert data_handler.load_blog_data()[0]['id'] == 2

    os.remove('master_blog.json')


def test_get_post_by_id():
    data_handler = data_handler_json.JsonStorage("master_blog")
    data_handler.add_post(post1)
    data_handler.add_post(post2)
    returned_post1_by_id = data_handler.get_post_by_id(1)
    returned_post2_by_id = data_handler.get_post_by_id(2)

    assert all(returned_post1_by_id[key] == post1[key] for key in post1)
    assert all(returned_post2_by_id[key] == post2[key] for key in post2)

    os.remove('master_blog.json')



if __name__ == '__main__':
    pytest.main()