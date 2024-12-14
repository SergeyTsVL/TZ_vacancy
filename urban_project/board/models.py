from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    """
    Этот класс определяет модель для хранения информации об объявлениях в базе данных.
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_name')
    telephone = models.IntegerField()
    order = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.CharField(max_length=255)


    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return str(self.name)

class Comment(models.Model):
    """
    Этот класс определяет модель для хранения комментариев к статьям или другим объектам в базе данных.
    """
    advertisement = models.ForeignKey(Advertisement, related_name='comments', on_delete=models.CASCADE)
    telephone = models.IntegerField()
    order = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return self.advertisement

# author = models.ForeignKey(User, on_delete=models.CASCADE)