from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from books_api.models import Book
from books_api.serializer import BookSerializer

@api_view(['GET','POST'])
def books(request):
     if request.method=='GET':
      books=  Book.objects.all()
      serializer=BookSerializer(books,many=True) #many_true birden fazla obje oldugu için listeye cevirmesni söyler
      return Response(serializer.data)
     if request.method=='POST':
         serializer=BookSerializer(data=request.data)
         if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
                 return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def book(request,id):
     try:
            book=Book.objects.get(pk=id)
     except:
               return Response({"error":"Eslesen bir kayıt bulunamadı"},status=status.HTTP_404_NOT_FOUND)
     
     if request.method=='GET':
            book=Book.objects.get(pk=id)
            seriallizer=BookSerializer(book)
            return Response(seriallizer.data)
     if request.method=='PUT':
        book=Book.objects.get(pk=id)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)
     if request.method=='DELETE':
        book=Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     
     
              
# @api_view(['PUT'])    
# def book_update(request,id):
#      book=Book.objects.get(pk=id)
#      serializer=BookSerializer(book,data=request.data)
#      if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#      return Response(serializer.errors)
# @api_view(['DELETE'])   
# def book_delete(request,id):
#   try:
#      book=Book.objects.get(pk=id)
#      book.delete()
#      return Response(status=status.HTTP_204_NO_CONTENT)
#   except:
#        return Response({"error":"Eslesen bir kayıt bulunamadı"},status=status.HTTP_404_NOT_FOUND)
# def book_list (request):
#     books=  Book.objects.all()
#     book_list=list(books.values())
#     return JsonResponse(
#         {
#             "books":book_list
#         }
#     )
# @api_view(['GET'])
         
# @api_view(['POST'])
# def book_create(request):
#     serializer=BookSerializer(data=request.data)
#     if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data,status=status.HTTP_201_CREATED)
#     else:
#          return Response(serializer.errors)