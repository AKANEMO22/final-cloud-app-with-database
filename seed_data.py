import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# 1. Superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
    print("Created superuser 'admin'")

# 2. Student user
student, _ = User.objects.get_or_create(username='student', defaults={'first_name': 'Alex', 'last_name': 'Johnson'})
student.set_password('student123')
student.save()

# 3. Instructor
instructor, _ = Instructor.objects.get_or_create(user=student, defaults={'total_learners': 250})

# 4. Course
course, _ = Course.objects.get_or_create(
    name="Cloud Application Development with Django",
    defaults={
        'description': "Learn how to build, test, and deploy cloud-native web applications using Django and relational databases.",
        'total_enrollment': 1200
    }
)
course.instructors.add(instructor)

# 5. Lessons
lesson1, _ = Lesson.objects.get_or_create(
    title="Introduction to Django Models and ORM",
    course=course,
    defaults={
        'order': 1,
        'content': "In this lesson, you explore Django's Object-Relational Mapper (ORM), define models, relationships, and perform database migrations."
    }
)
lesson2, _ = Lesson.objects.get_or_create(
    title="Building Views and Handling Exam Submissions",
    course=course,
    defaults={
        'order': 2,
        'content': "Learn how to create class-based and functional views in Django, handle POST form submissions, evaluate scores, and redirect to result pages."
    }
)

# 6. Questions & Choices
q1, _ = Question.objects.get_or_create(
    question_text="Which Django model method or field is used to link a Choice to a specific Question?",
    course=course,
    defaults={'lesson': lesson1, 'grade': 50}
)
c1_1, _ = Choice.objects.get_or_create(question=q1, choice_text="models.ForeignKey(Question, on_delete=models.CASCADE)", defaults={'is_correct': True})
c1_2, _ = Choice.objects.get_or_create(question=q1, choice_text="models.ManyToManyField(Question)", defaults={'is_correct': False})
c1_3, _ = Choice.objects.get_or_create(question=q1, choice_text="models.OneToOneField(Question)", defaults={'is_correct': False})

q2, _ = Question.objects.get_or_create(
    question_text="How do you register an inline admin model to edit Choices directly inside QuestionAdmin?",
    course=course,
    defaults={'lesson': lesson2, 'grade': 50}
)
c2_1, _ = Choice.objects.get_or_create(question=q2, choice_text="inlines = [ChoiceInline] inside QuestionAdmin class", defaults={'is_correct': True})
c2_2, _ = Choice.objects.get_or_create(question=q2, choice_text="admin.site.register(ChoiceInline)", defaults={'is_correct': False})
c2_3, _ = Choice.objects.get_or_create(question=q2, choice_text="TabularInline(ChoiceAdmin)", defaults={'is_correct': False})

# 7. Enrollment & Submission
enrollment, _ = Enrollment.objects.get_or_create(user=student, course=course, defaults={'mode': 'honor'})
submission = Submission.objects.create(enrollment=enrollment)
submission.choices.add(c1_1, c2_1)
submission.save()

print(f"Data seeded! Course ID: {course.id}, Submission ID: {submission.id}")
