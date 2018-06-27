from django.contrib.auth.models import User

from factory import DjangoModelFactory, SubFactory, Faker, fuzzy

from . import models


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = models.Company

    name = Faker("company")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")


class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = models.Review

    company = SubFactory(CompanyFactory)
    created = Faker("date_time_this_month")
    rating = fuzzy.FuzzyInteger(1, 5)
    title = Faker("sentence")
    summary = Faker("paragraphs")
    ip_address = Faker("ipv4_public")
    reviewer = SubFactory(UserFactory)
