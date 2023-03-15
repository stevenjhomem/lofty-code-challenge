from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from keys.models import Key
from keys.api.serializers import KeySerializer
from utilities import handle_request_key_errors, create_error_list


class KeysListView(APIView):

    @extend_schema(
        summary='Retrieve a list of Keys',
        description="",
        responses={
            200: KeySerializer(many=True),
        }
    )
    def get(self, request):
        keys_queryset = Key.objects.all()

        serializer = KeySerializer(keys_queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary='Create a Key Instance',
        description="",
        request=inline_serializer(
            name='CreateKeyRequestSerializer',
            fields={
                'key': serializers.CharField(),
            }
        ),
        responses={
            201: KeySerializer,
        },
    )
    def post(self, request):

        errors = handle_request_key_errors(
            expected_request_keys=[
                'key'
            ],
            request=request,
            can_be_empty=False
        )
        if errors:
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(create_error_list(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class KeyDetailView(APIView):

    @extend_schema(
        summary='Retrieve a key',
        description="",
        parameters=[
            OpenApiParameter('key_id', OpenApiTypes.INT, OpenApiParameter.PATH, True),
        ],
        responses={
            200: KeySerializer,
        }
    )
    def get(self, request, key_id):
        key = get_object_or_404(Key, id=key_id)
        serializer = KeySerializer(key)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class KeyIncrementView(APIView):

    @extend_schema(
        summary='Increment a value for a key',
        description="",
        parameters=[
            OpenApiParameter('key_id', OpenApiTypes.INT, OpenApiParameter.PATH, True),
        ],
        responses={
            200: KeySerializer,
        }
    )
    def post(self, request, key_id):
        key_exists = Key.objects.filter(id=key_id).exists()
        if not key_exists:
            return Response(data={'errors': [f'Resource with id: {key_id} could not be found.']},
                            status=status.HTTP_404_NOT_FOUND)
        with transaction.atomic():
            Key.objects.select_for_update().filter(pk=key_id).update(value=F("value") + 1)

        return Response(status=status.HTTP_200_OK)
