from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from reviews.views import ReviewViewSet, UserViewSet
from reviews.factories import UserFactory, ReviewFactory, CompanyFactory


class ReviewTestCase(APITestCase):
    def test_get_all_reviews_from_an_autenthicated_user(self):
        factory = APIRequestFactory()
        view = ReviewViewSet.as_view({"get": "list"})
        user = UserFactory()
        user2 = UserFactory()
        ReviewFactory.create_batch(3, reviewer=user)
        ReviewFactory(reviewer=user2)

        request = factory.get("/reviews")
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        for review in response.data:
            self.assertEqual(review["reviewer"], user.id, "The review creator must match the user")

        self.assertEqual(response.status_code, status.HTTP_200_OK, "Must return 200 OK on a successful request")

    def test_get_reviews_with_am_unautenthicated_user(self):
        factory = APIRequestFactory()
        view = ReviewViewSet.as_view({"get": "list"})
        ReviewFactory.create_batch(3)

        request = factory.get("/reviews")
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, "Must return 401 unauthorized on an unauthenticate request")

    def test_post_reviews_with_an_unautenthicated_user(self):
        factory = APIRequestFactory()
        view = ReviewViewSet.as_view({"post": "create"})

        request = factory.post("/reviews", {"rating": 1, "title": "bla", "summary": "ble", "company": 1, "reviewer": 1, "created": "2018-06-27T16:57:10.307457-03:00", "ip_address": "192.165.77.63"})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, "Must return 401 unauthorized on an unauthenticate request")

    def test_post_reviews_with_an_autenthicated_user_correct_arguments(self):
        factory = APIRequestFactory()
        view = ReviewViewSet.as_view({"post": "create"})
        company = CompanyFactory()
        user = UserFactory()

        request = factory.post("/reviews", {"rating": 1, "title": "bla", "summary": "ble", "company": company.id, "reviewer": user.id, "created": "2018-06-27T16:57:10.307457-03:00", "ip_address": "192.165.77.63"})
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Must return 201 on a successful request")
        self.assertEqual(response.data[0]["reviewer"], user.id, "Must match the created user")
        self.assertEqual(response.data[0]["company"], company.id, "Must match the created company")

    def test_post_reviews_with_an_autenthicated_user_incorrect_arguments(self):
        factory = APIRequestFactory()
        view = ReviewViewSet.as_view({"post": "create"})
        company = CompanyFactory()
        user = UserFactory()

        request = factory.post("/reviews", {"rating": 1, "summary": "ble", "company": company.id, "reviewer": user.id, "created": "2018-06-27T16:57:10.307457-03:00", "ip_address": "192.165.77.63"})
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Must return 400 Bad request on a unsuccessful request")

    def test_create_user(self):
        factory = APIRequestFactory()
        view = UserViewSet.as_view({"post": "create"})

        request = factory.post("/reviews", {"email": "a@a.com", "first_name": "name", "last_name": "last", "username": "totallyvalid", "password": "trendypassword123"})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Must return 201 on a successful request")

    def test_create_user_existing_username(self):
        factory = APIRequestFactory()
        view = UserViewSet.as_view({"post": "create"})
        user = UserFactory()

        request = factory.post("/reviews", {"username": user.username, "email": "a@a.com", "first_name": "name", "last_name": "last", "password": "trendypassword123"})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Must return 400 Bad Request on a unsuccessful request")
