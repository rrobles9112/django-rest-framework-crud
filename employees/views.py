from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Employee
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import EmployeeSerializer
from .pagination import CustomPagination

class get_delete_update_movie(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return employee

    # Get a movie
    def get(self, request, pk):

        movie = self.get_queryset(pk)
        serializer = EmployeeSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a movie
    def put(self, request, pk):
        
        employee = self.get_queryset(pk)

        if(request.user == employee.creator): # If creator is who makes request
            serializer = EmployeeSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a movie
    def delete(self, request, pk):

        employee = self.get_queryset(pk)

        if(request.user == employee.creator): # If creator is who makes request
            employee.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_movies(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       employee = Employee.objects.all()
       return employee

    # Get all movies
    def get(self, request):
        employee = self.get_queryset()
        paginate_queryset = self.paginate_queryset(employee)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new movie
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

