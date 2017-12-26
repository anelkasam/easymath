from django.db import models


class Grade(models.Model):
    """
    School grade for the topic
    """
    title = models.IntegerField(verbose_name='Класс')

    def __str__(self):
        return str(self.title) + ' клас'


class Subject(models.Model):
    """
    Allowable subjects. This table contains only two subjects: Algebra and Geometry
    """
    title = models.CharField(max_length=30, verbose_name='Предмет')

    def __str__(self):
        return self.title


class Package(models.Model):
    """
    Study packages allowable on this service
    """
    title = models.CharField(max_length=50, verbose_name='Направление подготовки')

    def __str__(self):
        return self.title


class Definition(models.Model):
    """
    Strict definitions
    """
    name = models.CharField(primary_key=True, max_length=50, verbose_name='Название')
    text = models.TextField(verbose_name='Определение')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    Topic of subject
    """
    title = models.CharField(max_length=50, verbose_name='Тема')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


def article_file_path(instance, filename):
    """
    Returns the path where we should save our files
    """
    return f'library/articles/{instance.topic.subject}/{instance.topic.grade}/{filename}'


class Article(models.Model):
    """
    Some article
    """
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    file = models.FileField(upload_to=article_file_path)

    def __str__(self):
        return self.title


def assignment_file_path(instance, filename):
    """
    Returns the path to folder with assignments and solutions
    """
    return f'library/assignments/{instance.topic.subject}/{instance.topic.grade}/{filename}'


class Assignment(models.Model):
    """ Assignments """
    COMPLEXITY = (
        (0, 'Elementary'),
        (1, 'Easy'),
        (2, 'Average'),
        (3, 'Challenge')
    )

    text = models.TextField(verbose_name='Текст задачи')
    answer_choices = models.TextField(verbose_name='Варианты ответов')
    short_answer = models.IntegerField(verbose_name='Краткий ответ')
    detail_answer = models.FileField(upload_to=assignment_file_path, verbose_name='Детальное решение')
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    complexity = models.IntegerField(choices=COMPLEXITY, default=2, verbose_name='Уровень сложности')

    def __str__(self):
        return f'{self.topic}: {self.text[:15]}'
