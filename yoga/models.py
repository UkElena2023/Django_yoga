from django.contrib.auth import get_user_model
from django.db import models


class Asana(models.Model):
    title = models.CharField(max_length=80, db_column='Title', verbose_name='Название асаны')
    translate = models.CharField(max_length=80, blank=True, db_column='Translate', verbose_name='Перевод с санскрита')
    effect = models.TextField(max_length=10000, db_column='Effect', verbose_name='Показания')
    contraindication = models.TextField(max_length=10000, db_column='Сontraindication', verbose_name='Противопоказания')
    technique = models.TextField(max_length=10000, db_column='Technique', verbose_name='Техника выполнения')
    image = models.ImageField(upload_to='yoga/images/%Y/%m/%d/', default=None, blank=True, null=True, db_column='Image',
                              verbose_name='Изображение асаны')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата создания')
    views = models.IntegerField(default=0, db_column='Views', verbose_name='Просмотры')
    favorites = models.ManyToManyField(get_user_model(), related_name='favorite_asanas', blank=True,
                                       verbose_name='Избранное')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='asanas', null=True,
                               default=None, verbose_name='Автор')

    class Meta:
        db_table = 'Asanas'  # имя таблицы в базе данных
        verbose_name = 'Асана'  # имя модели в единственном числе
        verbose_name_plural = 'Асаны'  # имя модели во множественном числе

    def __str__(self):
        return f'Асана {self.title}'

    def get_absolute_url(self):
        return f'/yoga/{self.pk}/detail/'


class Category(models.Model):
    name = models.CharField(max_length=100, db_column='Name')

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория {self.name}'


class YogaEvent(models.Model):
    place = models.TextField(max_length=500, db_column='Place', verbose_name='Место проведения')
    link = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link',
                            verbose_name='Ссылка')
    link_2 = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link_2',
                              verbose_name='Ссылка на место')
    time_event = models.TextField(max_length=500, db_column='Time_event', verbose_name='Время проведения')
    description = models.TextField(max_length=10000, db_column='Description', verbose_name='Описание')
    image_event = models.ImageField(upload_to='yoga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                    db_column='Image_event',
                                    verbose_name='Изображение мероприятия')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата загрузки')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='yogaevents', null=True,
                               default=None, verbose_name='Автор')
    status = models.BooleanField(default=True, db_column='Status', verbose_name='Статус')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'YogaEvent'  # имя таблицы в базе данных
        verbose_name = 'Мероприятие'  # имя модели в единственном числе
        verbose_name_plural = 'Мероприятия'  # имя модели во множественном числе

    def __str__(self):
        return f'Мероприятие {self.category} + {self.time_event} + {self.place}'


class YogaeventRequest(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'YogaeventRequest'  # имя таблицы в базе данных
        verbose_name = 'Запись на мероприятие'  # имя модели в единственном числе
        verbose_name_plural = 'Запись на мероприятия'  # имя модели во множественном числе

    def save(self, *args, **kwargs):
        # Вызываем метод clean, чтобы убедиться, что данные валидны
        # После, мы можем отправить уведомление на почту, например
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return f"Запись от: {self.first_name} {self.created_at}"


class Health(models.Model):
    name = models.CharField(max_length=80, db_column='Name', verbose_name='Название статьи')
    description = models.TextField(max_length=10000, db_column='Description', verbose_name='Описание')
    link = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link',
                            verbose_name='Ссылка')
    image_text = models.ImageField(upload_to='yoga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                   db_column='Image', verbose_name='Изображение асаны')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата создания')
    status = models.BooleanField(default=True, db_column='Status', verbose_name='Статус')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name='Тема статьи')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='health', null=True,
                               default=None, verbose_name='Автор')


class Subject(models.Model):
    name = models.CharField(max_length=100, db_column='Name')

    class Meta:
        db_table = 'Subjects'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return f'Тема {self.name}'
