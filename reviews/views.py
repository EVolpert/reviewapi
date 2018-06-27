from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from reviews.serializers import ReviewSerializer
from reviews.models import Review


class ReviewViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        Function: List all existing survivors.\n
        HTTP Verb: GET
        Endpoint: /reviews

        Returns:
            List with all the reviews of the current user
        """

        queryset = Review.objects.filter(reviewer=request.user)
        serializer = ReviewSerializer(queryset, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        return response

    def create(self, request):
            """
            Function: Create a review
            HTTP Verb: POST
            Endpoint: /reviews

            """
            review_serializer = ReviewSerializer(data=request.data)

            if(review_serializer.is_valid()):
                review_serializer.save()

                response = Response([review_serializer.data], status=status.HTTP_201_CREATED)
            else:
                response = Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return response


class UserViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):

        try:
            User.objects.create_user(
                request.data["username"],
                email=request.data["email"],
                password=request.data["password"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"]
            )

            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError as error:
            return Response("{} - Username already exists".format(error), status=status.HTTP_400_BAD_REQUEST)
        except ValueError as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
