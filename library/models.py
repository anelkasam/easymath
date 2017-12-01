from django.db import models


class Grade(models.Model):
    title = models.IntegerField()


class Subject(models.Model):
    title = models.CharField(max_length=30)


class Package(models.Model):
    title = models.CharField(max_length=50)


class Topic(models.Model):
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)


def article_file_path(instance, filename):
    return f'library/articles/{instance.topic.subject}/{instance.topic.grade}/{filename}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    file = models.FileField(upload_to=article_file_path)


def article_file_path(instance, filename):
    return f'library/assignememts/{instance.topic.subject}/{instance.topic.grade}/{filename}'


class Assignment(models.Model):
    COMPLEXITY = (
        (0, 'Elementary'),
        (1, 'Easy'),
        (2, 'Average'),
        (3, 'Challenge')
    )

    text = models.TextField()
    answer_choices = models.TextField()
    short_answer = models.IntegerField()
    detail_answer = models.FileField(upload_to='')
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    complexity = models.IntegerField(choices=COMPLEXITY, default=2)
