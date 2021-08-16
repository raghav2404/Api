from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# import api_view , Response and status converts Api into django browsable api
# Create your views here. -----fn based api views 
#@csrf_exempt
"""
class ArticleApiView(APIView):
    #authentication_classes = [TokenAuthentication]
  #  permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles , many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class ArticleDetail(APIView):
     # authentication_classes = [SessionAuthentication, BasicAuthentication]
     # permission_classes = [IsAuthenticated]
   # authentication_classes = [TokenAuthentication]
   # permission_classes = [IsAuthenticated,IsAdminUser]
    def get_object(self,id):
          try:
           return Article.objects.get(id=id)
          except Article.DoesNotExist:
               return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def get(self,request,id):
          article = self.get_object(id)
          serializers = ArticleSerializer(article)
          return Response(serializers.data)
      
    def put(self,request,id):
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self,request,id):
         article=self.get_object(id)
         article.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     
     
     
     
  """   
     
     
     
     
@api_view(['GET','POST'])
def article_list(request):
    if(request.method == 'GET'):
        
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles , many=True)
        return Response(serializer.data)
    
    elif(request.method == 'POST'):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

#get article on basis of id or update 
@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        #fetch article with key as pk
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif   request.method == 'DELETE':
           article.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)

#get post put delete -- http methods
    
    

        

