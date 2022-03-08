from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Horror_genre, Action
from .serializers import Horrormodelserializer, Actionmodelserializer


class HorrorAllData(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            query = Horror_genre.objects.all()
            serializers = Horrormodelserializer(query, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class HorrorFavData(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            query = Horror_genre.objects.filter(actor_fav=True)
            serializers = Horrormodelserializer(query, many=True)
            return Response(serializers.data, status= status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class SearchHorror(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            search = request.GET['Name']
            query = Horror_genre.objects.filter(movie_name__contains=search)
            serializer = Horrormodelserializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class ViewSetHorror(APIView):

    def put(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Horror_genre.objects.get(pk=pk)
            serializer = Horrormodelserializer(query, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return  Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse('You must first arrive at join...')
    def get(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Horror_genre.objects.get(pk=pk)
            serializer = Horrormodelserializer(query)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
    def delete(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Horror_genre.objects.get(pk= pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('You must first arrive at join...')
    def post(self, request):
        if request.user.is_active and request.user.is_authenticated:
            serializer = Horrormodelserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse('You must first arrive at join...')


class ActionAllData(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            query = Action.objects.all()
            serializer = Actionmodelserializer(query, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class ActionFavData(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            query = Action.objects.filter(actor_fav=True)
            serializers = Actionmodelserializer(query, many= True)
            return Response(serializers.data, status= status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class SearchAction(APIView):
    def get(self, request):
        if request.user.is_active and request.user.is_authenticated:
            search = request.GET['Name']
            query = Action.objects.filter(movie_name__contains=search)
            serializer = Actionmodelserializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
class ViewSetAction(APIView):

    def put(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Action.objects.get(pk=pk)
            serializer = Actionmodelserializer(query, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return  Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse('You must first arrive at join...')
    def get(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Action.objects.get(pk=pk)
            serializer = Actionmodelserializer(query)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return HttpResponse('You must first arrive at join...')
    def delete(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = Action.objects.get(pk= pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('You must first arrive at join...')
    def post(self, request):
        if request.user.is_active and request.user.is_authenticated:
            serializer = Actionmodelserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse('You must first arrive at join...')
