from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Введите вопрос', {'fields': ['question_text']}),
        ('Информация о дате вопроса', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')#список полей в таблице
    list_filter = ['pub_date']# боковая панель с фильтром по дате
    search_fields = ['question_text']#добавляем поиск по свойству question_text


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
