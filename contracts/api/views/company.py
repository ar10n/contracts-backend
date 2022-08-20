from django.http import Http404
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from ..models import Company
from ..serializers import CompanySerializer


class CompanyList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        obj = Company.objects.all()
        serializer = CompanySerializer(obj, many=True)
        return Response(serializer.data)


class CompanyCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CompanyReadUpdateDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = CompanySerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = CompanySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CompanySearch(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
