from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# QuestionInline to be used in LessonAdmin
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# ChoiceInline to be used in QuestionAdmin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# LessonInline to be used in CourseAdmin
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# CourseAdmin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# LessonAdmin with QuestionInline
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# QuestionAdmin with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']
    search_fields = ['question_text']

# Register models with admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
