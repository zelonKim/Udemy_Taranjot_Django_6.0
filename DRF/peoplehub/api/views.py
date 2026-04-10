from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','PUT','PATCH'])
def singleobj(request, id):
    data = get_object_or_404(Person, id=id)
    
    if request.method == "PUT": # 전체 수정
        # stream = io.BytesIO(request.body)
        # parsed_data = JSONParser().parse(stream)
        parsed_data = request.data
        
        # serializer = PersonSerializer(data, data=parsed_data) # 역직렬화
        serializer = PersonModelSerializer(data, data=parsed_data) 
        
        if serializer.is_valid():
            serializer.save() # 시리얼라이저에서 update()메서드 호출
            return Response({'updated':'success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    if request.method == "PATCH": # 부분 수정
        # stream = io.BytesIO(request.body)
        # parsed_data = JSONParser().parse(stream)
        parsed_data = request.data
        
        # serializer = PersonSerializer(data, data=parsed_data, partial=True) # 역직렬화
        serializer = PersonModelSerializer(data, data=parsed_data, partial=True) 
        
        if serializer.is_valid():
            serializer.save() # 시리얼라이저에서 update()메서드 호출
            return Response({'updated':'success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == "GET":
        # serializer = PersonSerializer(data)
        serializer = PersonModelSerializer(data)
        # print(serializer.data) # {'name': 'Rahul', 'age': 21, 'city': 'Tokyo'}
        
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        return Response(serializer.data)







@api_view(['GET','POST'])
def multipleobj(request):
    if request.method == "POST":
        # stream = io.BytesIO(request.body)
        # parsed_data = JSONParser().parse(stream)
        parsed_data = request.data
        # print(parsed_data) # {'name': 'john', 'age': 25, 'city': 'Osaka'}
        # print(type(parsed_data)) # <class 'dict'>
        
        # serializer = PersonSerializer(data=parsed_data) # 역직렬화
        serializer = PersonModelSerializer(data=parsed_data) 
        
        if serializer.is_valid():
            serializer.save() # 시리얼라이저에서 create()메서드 호출
            return Response({"created":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == "GET":
        data = Person.objects.all()
        # serializer = PersonSerializer(data, many=True) # 직렬화
        serializer = PersonModelSerializer(data, many=True) 
        # print(serializer.data) # [{'name': 'Rahul', 'age': 21, 'city': 'Tokyo'}, {'name': 'Simar', 'age': 18, 'city': 'LA'}, {'name': 'Zelon', 'age': 22, 'city': 'New York'}]
       
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        return Response(serializer.data)



