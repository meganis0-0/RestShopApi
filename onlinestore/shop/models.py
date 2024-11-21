from django.db import models
from uuid import uuid4

#модель для продуктов
class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()


#модель для токена
def generate_token():
    return str(uuid4())

class Token(models.Model):
    token = models.CharField(max_length=36, unique=True, default=generate_token)