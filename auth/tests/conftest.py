import pytest
from pytest_factoryboy import register
from .factories import UserFactory
from rest_framework.test import APIClient
from django.urls import reverse

register(factory_class=UserFactory)


@pytest.fixture
def user_test_factory(user_factory):
    return user_factory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def registration_endpoint():
    url = reverse("user-list")
    return url


@pytest.fixture
def login_endpoint():
    url = reverse("jwt_create")
    return url


@pytest.fixture
def refresh_endpoint():
    url = reverse("jwt_refresh")
    return url


@pytest.fixture
def verify_endpoint():
    url = "jwt_verify"
    return
