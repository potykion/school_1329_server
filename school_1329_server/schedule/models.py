import json
from operator import itemgetter

from django.db import models, transaction
from djchoices import DjangoChoices, ChoiceItem

from school_1329_server.common.utils import format_time
from school_1329_server.groups.models import Group


class Weekdays(DjangoChoices):
    Monday = ChoiceItem(1, 'Понедельник')
    Tuesday = ChoiceItem(2, 'Вторник')
    Wednesday = ChoiceItem(3, 'Среда')
    Thursday = ChoiceItem(4, 'Четверг')
    Friday = ChoiceItem(5, 'Пятница')
    Saturday = ChoiceItem(6, 'Суббота')
    Sunday = ChoiceItem(7, 'Воскресенье')


class ScheduleSubject(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class ScheduleTeacher(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ф.И.О')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class ScheduleLessonManager(models.Manager):
    def create_from_json(self, json_file):
        with open(json_file, encoding='utf-8') as f:
            lesson_dicts = json.load(f)

        with transaction.atomic():
            subject_titles = tuple(set(map(itemgetter('subject'), lesson_dicts)))
            subjects = (ScheduleSubject.objects.create(title=title) for title in subject_titles)
            subjects_index = dict(zip(subject_titles, subjects))

            teacher_names = tuple(set(map(itemgetter('teacher'), lesson_dicts)))
            teachers = (ScheduleTeacher.objects.create(name=name) for name in teacher_names)
            teachers_index = dict(zip(teacher_names, teachers))

            group_titles = tuple(set(map(itemgetter(0), map(itemgetter('groups'), lesson_dicts))))
            groups = (Group.objects.create(title=title) for title in group_titles)
            groups_index = dict(zip(group_titles, groups))

        with transaction.atomic():
            for lesson_dict in lesson_dicts:
                lesson_dict['subject'] = subjects_index[lesson_dict['subject']]
                lesson_dict['teacher'] = teachers_index[lesson_dict['teacher']]
                groups = [groups_index[lesson_dict.pop('groups')[0]]]

                lesson = ScheduleLesson(**lesson_dict)
                lesson.save()
                lesson.groups.add(*groups)
                lesson.save()


class ScheduleLesson(models.Model):
    start_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(null=True, verbose_name='Окончание')
    weekday = models.IntegerField(choices=Weekdays.choices, verbose_name='День')

    place = models.CharField(max_length=200, verbose_name='Место проведения', blank=True)

    subject = models.ForeignKey(ScheduleSubject, models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(ScheduleTeacher, models.CASCADE, verbose_name='Учитель')
    groups = models.ManyToManyField(Group, blank=True, verbose_name='Группы')

    objects = ScheduleLessonManager()

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return (
            f'{Weekdays.get_choice(self.weekday).label} {format_time(self.start_time)} - '
            f'{self.subject} ({self.teacher})'
        )
