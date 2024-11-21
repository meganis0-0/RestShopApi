from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Good, Token
from .serializers import GoodSerializer, TokenSerializer

class GetTokenView(APIView):
    """
    Представление для получения нового токена.
    При GET-запросе создается новый токен и возвращается в формате JSON.
    """
    def get(self, request):
        token_instance = Token.objects.create()  # Создаем новый экземпляр токена
        serializer = TokenSerializer(token_instance)  # Сериализуем токен
        return Response(serializer.data)  # Возвращаем токен в ответе

class GoodsListView(APIView):
    """
    Представление для получения списка всех товаров.
    Проверяет наличие токена в запросе и возвращает список товаров или ошибку.
    """
    def get(self, request):
        token = request.query_params.get('token')  # Получаем токен из параметров запроса
        if not token:
            return Response("Token must be present", status=status.HTTP_401_UNAUTHORIZED)  # Ошибка 401, если токен отсутствует

        try:
            Token.objects.get(token=token)  # Проверяем, существует ли токен в базе данных
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)  # Ошибка 401, если токен недействителен

        goods = Good.objects.all()  # Получаем все товары из базы данных
        serializer = GoodSerializer(goods, many=True)  # Сериализуем список товаров
        return Response(serializer.data)  # Возвращаем список товаров в ответе


class NewGoodView(APIView):
    """
    Представление для добавления нового товара.
    Проверяет наличие токена и валидирует данные о товаре.
    """
    def post(self, request):
        token = request.query_params.get('token')  # Получаем токен из параметров запроса
        if not token:
            return Response("Token must be present", status=status.HTTP_401_UNAUTHORIZED)  # Ошибка 401, если токен отсутствует

        try:
            Token.objects.get(token=token)  # Проверяем, существует ли токен в базе данных
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)  # Ошибка 401, если токен недействителен

        serializer = GoodSerializer(data=request.data)  # Сериализуем данные о новом товаре
        if serializer.is_valid():  # Проверяем валидность данных
            price = serializer.validated_data.get('price')
            amount = serializer.validated_data.get('amount')
            if price <= 0:
                return Response("Price must be more than 0", status=status.HTTP_400_BAD_REQUEST)  # Ошибка, если цена некорректна
            if amount <= 0:
                return Response("Amount must be more than 0", status=status.HTTP_400_BAD_REQUEST)  # Ошибка, если количество некорректно
            serializer.save()  # Сохраняем новый товар в базе данных
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращаем созданный товар в ответе
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Ошибка валидатора при некорректных данных