from django.contrib import admin
from polls.models import Poll, Question, Choice, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True

class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_editable = ['is_active']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'poll']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Vote)