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
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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
        
        
        # if serializer.is_valid():
        #     serializer.save() # 시리얼라이저에서 create()메서드 호출
        #     return Response({"created":"success"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.is_valid(raise_exception=True) 
        serializer.save() 
        return Response({"created":"success"}, status=status.HTTP_201_CREATED)
     
        
    
    if request.method == "GET":
        data = Person.objects.all()
        # serializer = PersonSerializer(data, many=True) # 직렬화
        serializer = PersonModelSerializer(data, many=True) 
        # print(serializer.data) # [{'name': 'Rahul', 'age': 21, 'city': 'Tokyo'}, {'name': 'Simar', 'age': 18, 'city': 'LA'}, {'name': 'Zelon', 'age': 22, 'city': 'New York'}]
       
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        return Response(serializer.data)







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






###########################################################







class MultipleObjAPIView(APIView):
    def get(self, request):
        data = Person.objects.all()
        serializer = PersonModelSerializer(data, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        parsed_data = request.data
        serializer = PersonModelSerializer(data=parsed_data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save() 
        return Response({"created":"success"}, status=status.HTTP_201_CREATED)
    
    
    

class SingleObjAPIViw(APIView):
    def get(self, request, id):
        data = get_object_or_404(Person, id=id)
        serializer = PersonModelSerializer(data)
        return Response(serializer.data)
        
    def put(self, request, id):
        data = get_object_or_404(Person, id=id)
        parsed_data = request.data
        serializer = PersonModelSerializer(data, data=parsed_data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'updated':'success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        data = get_object_or_404(Person, id=id)
        parsed_data = request.data
        serializer = PersonModelSerializer(data, data=parsed_data, partial=True) 
        if serializer.is_valid():
            serializer.save() 
            return Response({'updated':'success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    





##########################################################







class MultipleObjGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = Person.objects.all()
    serializer_class =  PersonModelSerializer
    
    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)
   
    def post(self, request):
       return self.create(request)
   
   
   
   

class SingleObjGenericAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class =  PersonModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
    
    
    
##########################################################





# class MultipleObjConcreteAPIView(ListCreateAPIView): 
#     queryset = Person.objects.all()
#     serializer_class =  PersonModelSerializer
   
   

class MultipleObjConcreteAPIView(ListCreateAPIView): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Person.objects.all()
    serializer_class =  PersonModelSerializer
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        response = super().get(request, *args, **kwargs)
        return response
    
   


class SingleObjConcreteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class =  PersonModelSerializer
    

   
   
   
