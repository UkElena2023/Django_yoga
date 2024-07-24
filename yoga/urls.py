from django.urls import path
from . import views

app_name = 'yoga'
urlpatterns = [
    ###### группа маршрутов для стилей йоги
    path('hathayoga/', views.AboutHathaYoga.as_view(), name='hathayoga'), # о хатха йоге
    path('kundaliniyoga/', views.AboutKundaliniYoga.as_view(), name='kundaliniyoga'),  # о кундалини йоге
    path('ashtangayoga/', views.AboutAshtangaYoga.as_view(), name='ashtangayoga'),  # о аштанга йоге
    path('ayengaryoga/', views.AboutAyengarYoga.as_view(), name='ayengaryoga'),  # о айенгар йоге
    path('shivanandayoga/', views.AboutShivanandaYoga.as_view(), name='shivanandayoga'),  # о шивананда йоге
    path('nidrayoga/', views.AboutNidraYoga.as_view(), name='nidrayoga'),  # о йоге нидре

    ###### группа маршрутов для статей о здоровье
    path('health_breath/', views.HealthBreathView.as_view(), name='health_breath'),  # статьи о дыхании
    path('health_nutrition/', views.HealthNutritionView.as_view(), name='health_nutrition'),  # статьи о питании
    path('health_ayurveda/', views.HealthAyurvedaView.as_view(), name='health_ayurveda'),  # статьи об аюрведе
    path('health_yogatherapy/', views.HealthYogatherapyView.as_view(), name='health_yogatherapy'),  # статьи об йогатерапии
    path('health_purification/', views.HealthPurificationView.as_view(), name='health_purification'),  # статьи об очищении
    path('<int:pk>/edit_health/', views.EditHealthUpdateView.as_view(), name='edit_health'),
    # Страница с формой редактирования статьи
    path('<int:pk>/delete_health/', views.DeleteHealthView.as_view(), name='delete_health'),
    # Страница с уведомлением об удалении статьи
    path('add_health/', views.AddHealthCreateView.as_view(), name='add_health'),  # добавить мероприятие

    # остальные маршруты
    path('asanas/', views.AsanaCatalogView.as_view(), name='asanas'), # каталог асан
    path('asana/<int:pk>/toggle_favorite/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('events/', views.YogaEventCatalogView.as_view(), name='events'),  # каталог мероприятий
    path('<int:pk>/detail/', views.AsanaDetailView.as_view(), name='detail_asana_by_id'), # Детальная страница acaны по pk
    path('<int:pk>/edit/', views.EditYogaEventUpdateView.as_view(), name='edit_yogaevent'),   # Страница с формой редактирования мероприятия
    path('<int:pk>/delete/', views.YogaEventDeleteView.as_view(), name='delete_yogaevent'),   # Страница с уведомлением об удалении мероприятия
    path('add/', views.AddYogaEventCreateView.as_view(), name='add_yogaevent'),  # добавить мероприятие
    path('back_contact/', views.BackContactView.as_view(), name='back_contact'),  # обратная связь
    path('thank_for_request/', views.ThankForRequestView.as_view(), name='thank_for_request'),  # благодарим за запись

]