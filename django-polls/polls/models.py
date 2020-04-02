import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Создаем модель вопроса"""
    question_text = models.CharField('Текст вопроса', max_length=100)
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Вопрос' """
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        """Вывод строкового представления поля"""
        return self.question_text

    def was_published_recently(self):
        """Функция отображения вопросов опбликованных недавно"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Вопрос опубликован сегодня?'


class Choice(models.Model):
    """Модель варианта ответа"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Текст ответа', max_length=200)
    votes = models.IntegerField('Начальное количество голосов', default=0)

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Варианты ответа' """
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        """Вывод строкового представления поля"""
        return self.choice_text
