from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.response import Response
from rest_framework import status
from .custom_responses import (
    LATEST_REVIEWS_RESPONSE, REVIEW_CREATED_RESPONSE, REVIEW_CREATION_ERROR,
    REVIEW_RETRIEVED_RESPONSE, REVIEW_UPDATED_RESPONSE, REVIEW_UPDATE_ERROR,
    REVIEW_DELETED_RESPONSE, REVIEW_DELETION_ERROR, REVIEW_NOT_FOUND_RESPONSE
)

# Create your views here.
# View to list the latest reviews
class LatestReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # Override the get_queryset method to return the latest 'n' reviews
    def get_queryset(self):
        n = int(self.request.query_params.get('n', 5))
        reviews = Review.objects.order_by('-created_at')[:n]
        return reviews

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(LATEST_REVIEWS_RESPONSE(response.data), status=status.HTTP_200_OK)

# View to create a new review
# @login_required
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Override the perform_create method to update the course rating after creating a review
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.course.update_rating()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response(REVIEW_CREATED_RESPONSE(response.data), status=status.HTTP_201_CREATED)
        return Response(REVIEW_CREATION_ERROR(response.data), status=response.status_code)

# View to retrieve, update, or delete a review
# @login_required
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response(REVIEW_RETRIEVED_RESPONSE(response.data), status=status.HTTP_200_OK)
        return Response(REVIEW_NOT_FOUND_RESPONSE, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response(REVIEW_UPDATED_RESPONSE(response.data), status=status.HTTP_200_OK)
        return Response(REVIEW_UPDATE_ERROR(response.data), status=response.status_code)

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     instance.course.update_rating()

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            course = instance.course
            instance.delete()
            # course.update_rating()
            return Response(REVIEW_DELETED_RESPONSE, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(REVIEW_DELETION_ERROR(str(e)), status=status.HTTP_400_BAD_REQUEST)