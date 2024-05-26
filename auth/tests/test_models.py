import pytest


def test_create_single_user_success(user_test_factory):
    user = user_test_factory.build()
    assert user.email is not None
    assert user.id is not None


def test_create_batch_user_success(user_test_factory):
    user_list = user_test_factory.build_batch(30)
    assert len(user_list) == 30


def test_password_properly_hashed(user_test_factory):
    user = user_test_factory.build(password="testuser123#")
    assert user.password.startswith("pbkdf2")
    assert user.check_password("testuser123#")
