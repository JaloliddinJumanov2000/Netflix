from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie.models import Genre, Content
from movie.serializers import GenreSerializer, ContentSerializer


# CRUD
@api_view(['GET', 'POST'])
def genre_list_or_create(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def genre_retrive_update_delete(request, pk):
    return Response({"detail": f"id:{pk} uchun  {request.method} ishladi "})







@api_view(['GET'])
def get_contents(request):
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)
