from pytest_drf import (
    APIViewTest,
    Returns200,
    UsesGetMethod,
    ViewSetTest,
    UsesPostMethod,
    Returns201,
    Returns401,
    UsesListEndpoint,
)
from pytest_drf.util import url_for
from django.urls import reverse
import pytest
from pytest_lambda import lambda_fixture, static_fixture
from faker import Faker

fake = Faker()


@pytest.mark.django_db
class TestRegistrationEndpoint(ViewSetTest):
    # Test for user registration
    list_url = lambda_fixture(lambda: url_for("user-list"))

    class TestList(UsesGetMethod, UsesListEndpoint, Returns401):
        def test_get(self, json):
            expected = {"detail": "Authentication credentials were not provided."}
            actual = json
            assert expected == actual

    class TestCreate(UsesPostMethod, UsesListEndpoint, Returns201):
        password = fake.password()
        data = static_fixture(
            value={
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "password": password,
                "re_password": password,
            }
        )

        def test_post_registration_success(self, data, json):
            expected = data
            actual = json
            assert actual.get("id") is not None
            assert actual.get("email") is not None
            assert actual.get("last_name") is not None
            assert actual.get("first_name") is not None
