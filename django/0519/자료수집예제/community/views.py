from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Comment , Review
from . serializers import ReviewSerializer, CommentSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def review_list_create(request) :
    if request.method == 'GET' :
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

        elif request.method == 'DELETE' :
            review.delete()
            return Response({ 'id': review_pk}, status=status.HTTP_204_NO_CONTENT)
