from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Question, Choice

class choiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class questionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Questions', {
            "fields": ['question_text'],
        }),
        ( 'Date and Time', {
            "fields" : ['pub_date'],
        }
        ),
    ]
    inlines = [choiceInline]

    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently'
    )

    list_filter = ['pub_date']

    search_fields = ['question_text']


admin.site.register(Question, questionAdmin)
admin.site.register(Choice)