import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status

fake = Faker()

# TODO: Find out how to test if password was incorrectly entered


@pytest.mark.django_db
def test_register_success(api_client, register_url):

    password = fake.password()
    response = api_client.post(
        path=register_url,
        data={
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": password,
            "re_password": password,
        },
        format="json",
    )
    print(response.json())
    print(password)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json.get("email") is not None


@pytest.mark.django_db
def test_register_password_mismatch(api_client, register_url):
    response = api_client.post(
        path=register_url,
        data={
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": fake.password(),
            "re_password": fake.password(),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_success(api_client, login_url, user_test_factory):
    password = "testuser123#"
    user = user_test_factory.create(password=password)
    response = api_client.post(
        path=login_url,
        data={
            "email": user.email,
            "password": password,
        },
        format="json",
    )
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("refresh") is not None
    assert response.json().get("access") is not None


def test_login_wrong_password(api_client, login_url, user_test_factory):
    user = user_test_factory.build(password="testuser123#")
    response = api_client.post(
        path=login_url,
        data={
            "email": user.email,
            "password": fake.password,
        },
        content_type="application/json",
    )
    print(response)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
