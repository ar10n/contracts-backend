from django.http import Http404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from ..models import Manufacturer
from ..serializers import ManufacturerSerializer


class ManufacturerList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        obj = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(obj, many=True)
        return Response(serializer.data)


class ManufacturerCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ManufacturerReadUpdateDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = ManufacturerSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = ManufacturerSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=HTTP_204_NO_CONTENT)

