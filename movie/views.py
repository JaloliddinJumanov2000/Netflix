from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie.models import Genre, Content
from movie.serializers import GenreSerializer, ContentSerializer


# CRUD
@api_view(['GET', 'POST'])
def genre_list_or_create(request, format=None):
    if request.method == 'GET':
        genres = Genre.objects.all()
        search = request.query_params.get('search', None)
        if search:
            genres = genres.filter(name__icontains=search)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_retrive_update_delete(request, pk, format=None):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response({"delete": "Object is delete!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def content_retrive_update_or_delete(request, pk,format=None):
    try:
        content = Content.objects.get(id=pk)
    except Content.DoesNotExist:
        return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        genre = request.query_params.get('genre')
        director = request.query_params.get('director')
        title = request.query_params.get('title')
        desc = request.query_params.get('desc')
        contents = Content.objects.all()
        if genre:
            contents = contents.filter(genres__name__icontains=genre)
        serializer = ContentSerializer(contents)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ContentSerializer(content, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        content.delete()
        return Response({"message": "Object is deleted!"}, status=status.HTTP_204_NO_CONTENT)
