from models.user import User
from daos.user_dao_mongo import UserDAOMongo

import time

dao = UserDAOMongo()

def test_user_select():
    temp_users = [
        User(None, "Test1", "test1@example.com"),
        User(None, "Test2", "test2@example.com"),
        User(None, "Test3", "test3@example.com"),
    ]
    ids = [dao.insert(u) for u in temp_users]

    user_list = dao.select_all()
    assert len(user_list) >= 3

def test_user_insert():
    user = User(None, 'Joanne Test', 'joannetest@example.com')
    assigned_id = dao.insert(user)
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

    dao.delete(assigned_id)
    

def test_user_update():
    user = User(None, 'Joe Test', 'testttt@example.com')
    assigned_id = dao.insert(user)

    corrected_email = 'joetest@example.com'
    user.id = assigned_id
    user.email = corrected_email
    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails

    dao.delete(assigned_id)

def test_user_delete():
    user = User(None, 'Joe Test', 'joetest@example.com')
    assigned_id = dao.insert(user)
    dao.delete(assigned_id)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails