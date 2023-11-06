from rest_framework import viewsets
from .serializer import UserSerializer
from .serializer import UserXMLSerializer
from .models import User

import cloudinary.uploader
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework_xml.renderers import XMLRenderer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        profile_picture_base64 = self.request.data.get('profile_picture', None)
        if profile_picture_base64 and profile_picture_base64 != "":
            upload_result = cloudinary.uploader.upload(profile_picture_base64)
            serializer.save(profile_picture=upload_result['secure_url'])
        else:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = instance.pk
        self.perform_destroy(instance)
        return Response({"user_id": user_id}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'email' in serializer.validated_data:
            serializer.validated_data.pop('email')

        profile_picture_base64 = self.request.data.get('profile_picture', None)
        if profile_picture_base64 and profile_picture_base64 != "":
            upload_result = cloudinary.uploader.upload(profile_picture_base64)
            serializer.save(profile_picture=upload_result['secure_url'])
        else:
            serializer.save()

        return Response(serializer.data)
    
class UserXMLAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserXMLSerializer
    renderer_classes = [XMLRenderer]