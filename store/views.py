from rest_framework import viewsets
from rest_framework import permissions
from .models import Product, CustomUser
from .serializers import ProductSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    @action(detail=False, methods=['get'])
    def available(self, request):
        queryset = self.queryset.filter(is_available=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
