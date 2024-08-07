from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Asana, YogaEvent, YogaeventRequest, Health


@admin.register(Asana)
class AsanaAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = (
        'id', 'title', 'translate', 'effect', 'contraindication', 'technique', 'asana_image', 'upload_date', 'views')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('title', 'translate', 'effect', 'contraindication')
    # Поля по которым будет фильтрация
    # list_filter = ('category', 'upload_date')
    # Ordering - сортировка
    ordering = ('title',)
    # List_per_page - количество элементов на странице
    list_per_page = 5
    # Поля, которые можно редактировать
    list_editable = ('views', 'title', 'translate', 'effect', 'contraindication', 'technique')
    fields = ['views', 'title', 'translate', 'effect', 'contraindication', 'technique', 'image']

    @admin.display(description="Изображение асаны")
    def asana_image(self, asana: Asana):
        if asana.image:
            return mark_safe(f'<img src="{asana.image.url}" width="96">')
        else:
            return 'Без изображения'


@admin.register(YogaEvent)
class YogaEventAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = (
        'id', 'category', 'place', 'link_2', 'time_event', 'description', 'yogaevent_image', 'upload_date', 'status', 'link')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('place', 'description')
    # Поля по которым будет фильтрация
    list_filter = ('category', 'upload_date')
    # Ordering - сортировка
    ordering = ('time_event',)
    # List_per_page - количество элементов на странице
    list_per_page = 10
    # Поля, которые можно редактировать
    list_editable = ('place', 'link_2', 'time_event', 'description', 'status', 'link')
    fields = ['category', 'place', 'link_2', 'time_event', 'description', 'image_event', 'status', 'link']

    @admin.display(description="Изображение мероприятия")
    def yogaevent_image(self, yogaevent: YogaEvent):
        if yogaevent.image_event:
            return mark_safe(f'<img src="{yogaevent.image_event.url}" width="96">')
        else:
            return 'Без изображения'


@admin.register(YogaeventRequest)
class YogaEventRequestAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ('id', 'first_name', 'email', 'phone', 'comment', 'created_at')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('email', 'phone', 'created_at')
    # Поля по которым будет фильтрация
    list_filter = ('created_at',)
    # Ordering - сортировка
    ordering = ('created_at',)
    # List_per_page - количество элементов на странице
    list_per_page = 10
    # Поля, которые можно редактировать
    list_editable = ('first_name', 'email', 'phone', 'comment')
    fields = ['first_name', 'email', 'phone', 'comment', 'created_at']


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = (
        'id', 'subject', 'name', 'description', 'text_image', 'upload_date', 'link')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('name', 'description')
    # Поля по которым будет фильтрация
    list_filter = ('subject', 'upload_date')
    # Ordering - сортировка
    ordering = ('upload_date',)
    # List_per_page - количество элементов на странице
    list_per_page = 10
    # Поля, которые можно редактировать
    list_editable = ('name', 'description', 'link')
    fields = ['subject', 'name', 'description', 'image_text', 'link']

    @admin.display(description="Изображение мероприятия")
    def text_image(self, health: Health):
        if health.image_text:
            return mark_safe(f'<img src="{health.image_text.url}" width="96">')
        else:
            return 'Без изображения'