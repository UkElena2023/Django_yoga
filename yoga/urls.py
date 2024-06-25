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