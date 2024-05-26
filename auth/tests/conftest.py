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
def register_url():
    return reverse("user-list")


@pytest.fixture
def login_url():
    return reverse("jwt-create")


@pytest.fixture
def verify_url():
    return reverse("jwt-verify")


@pytest.fixture
def refresh_url():
    return reverse("jwt-refresh")
