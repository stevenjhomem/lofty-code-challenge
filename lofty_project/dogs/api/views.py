from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from dogs.models import DogImageSet
from dogs.api.serializers import DogImageSetSerializer


class DogImageSetListView(APIView):

    @extend_schema(
        summary='Retrieve the list of Dog Image Sets',
        responses={
            200: DogImageSetSerializer(many=True),
        }
    )
    def get(self, request):
        dis_qs = DogImageSet.objects.all()

        serializer = DogImageSetSerializer(dis_qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DogImageSetDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    @extend_schema(
        summary='Retrieve a Dog Image Set and meta data',
        description="",
        parameters=[
            OpenApiParameter('dis_id', OpenApiTypes.INT, OpenApiParameter.PATH, True),
        ],
        responses={
            200: DogImageSetSerializer,
        }
    )
    def get(self, request, dis_id):
        dog_image_set = get_object_or_404(DogImageSet, id=dis_id)
        serializer = DogImageSetSerializer(dog_image_set)
        return Response(data=serializer.data, template_name='doggie_detail.html', status=status.HTTP_200_OK)
