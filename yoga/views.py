from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, F
from django.urls import reverse
from .forms import YogaEventForm, YogaeventRequestForm, HealthForm
from .models import Asana, YogaEvent, Health


class PageNotFoundView(TemplateView):
    template_name = 'yoga/404.html'


class AboutView(TemplateView):
    """
    Класс (статический) для отображения страницы "Стили йоги"
    """
    template_name = 'yoga/about.html'
    extra_context = {'title': 'Стили йоги'}  # Обновляется только при загрузке Сервера


class AboutHathaYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Хатха йога"
    """
    template_name = 'yoga/hathayoga.html'
    extra_context = {'title': 'Хатха йога'}


class AboutKundaliniYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Кундалини йога"
    """
    template_name = 'yoga/kundaliniyoga.html'
    extra_context = {'title': 'Кундалини йога'}


class AboutAshtangaYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Аштанга Виньяса йога"
    """
    template_name = 'yoga/ashtangayoga.html'
    extra_context = {'title': 'Аштанга Виньяса йога'}


class AboutAyengarYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Айенгар йога"
    """
    template_name = 'yoga/ayengaryoga.html'
    extra_context = {'title': 'Айенгар йога'}


class AboutShivanandaYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Шивананда йога"
    """
    template_name = 'yoga/shivanandayoga.html'
    extra_context = {'title': 'Шивананда йога'}


class AboutNidraYoga(TemplateView):
    """
    Класс (статический) для отображения страницы "Йога Нидра"
    """
    template_name = 'yoga/nidrayoga.html'
    extra_context = {'title': 'Йога Нидра'}


class AdviceView(TemplateView):
    """
    Класс (статический) для отображения страницы "Советы начинающим"
    """
    template_name = 'yoga/advice.html'
    extra_context = {'title': 'Советы начинающим'}  # Обновляется только при загрузке Сервера


class IndexView(TemplateView):
    """
    Класс (статический) для отображения страницы "Главная"
    """
    template_name = 'yoga/main.html'


class HealthBreathView(ListView):
    """
    Класс для отображения страницы Блог про дыхание со статьями
    """
    model = Health  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/health_breath.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'healthes'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 7  # Количество объектов на странице
    extra_context = {'title': 'Блог про дыхание'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        """
        Метод для модификации начального запроса к БД.
        Получает параметры сортировки из GET-запроса
        :return: сет контекста
        """
        # Параметры для сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')  # по дате публикации
        order = self.request.GET.get('order', 'desc')  # по убывающему порядку

        # условие для определения направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        queryset = Health.objects.order_by(order_by)
        return queryset


class HealthNutritionView(ListView):
    """
    Класс для отображения страницы Блог про питание со статьями
    """
    model = Health  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/health_nutrition.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'healthes'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 7  # Количество объектов на странице
    extra_context = {'title': 'Блог про питание'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        """
        Метод для модификации начального запроса к БД.
        Получает параметры сортировки из GET-запроса
        :return: сет контекста
        """
        # Параметры для сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')  # по дате публикации
        order = self.request.GET.get('order', 'desc')  # по убывающему порядку

        # условие для определения направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        queryset = Health.objects.order_by(order_by)
        return queryset


class HealthAyurvedaView(ListView):
    """
    Класс для отображения страницы Блог про аюрведу со статьями
    """
    model = Health  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/health_ayurveda.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'healthes'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 7  # Количество объектов на странице
    extra_context = {'title': 'Блог про аюрведу'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        """
        Метод для модификации начального запроса к БД.
        Получает параметры сортировки из GET-запроса
        :return: сет контекста
        """
        # Параметры для сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')  # по дате публикации
        order = self.request.GET.get('order', 'desc')  # по убывающему порядку

        # условие для определения направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        queryset = Health.objects.order_by(order_by)
        return queryset


class HealthYogatherapyView(ListView):
    """
    Класс для отображения страницы Блог про йогатерапию со статьями
    """
    model = Health  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/health_yogatherapy.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'healthes'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 7  # Количество объектов на странице
    extra_context = {'title': 'Блог про йогатерапию'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        """
        Метод для модификации начального запроса к БД.
        Получает параметры сортировки из GET-запроса
        :return: сет контекста
        """
        # Параметры для сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')  # по дате публикации
        order = self.request.GET.get('order', 'desc')  # по убывающему порядку

        # условие для определения направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        queryset = Health.objects.order_by(order_by)
        return queryset


class HealthPurificationView(ListView):
    """
    Класс для отображения страницы Блог про очищение со статьями
    """
    model = Health  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/health_purification.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'healthes'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 7  # Количество объектов на странице
    extra_context = {'title': 'Блог про очищение'}  # Дополнительный контекст для передачи в шаблон


    def get_queryset(self):
        """
        Метод для модификации начального запроса к БД.
        Получает параметры сортировки из GET-запроса
        :return: сет контекста
        """
        # Параметры для сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')  # по дате публикации
        order = self.request.GET.get('order', 'desc')  # по убывающему порядку

        # условие для определения направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        queryset = Health.objects.order_by(order_by)
        return queryset


class AddHealthCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Класс для добавления статьи о здоровье
    """
    model = Health  # Указываем модель, с которой работает представление
    form_class = HealthForm # Указываем класс формы для создания статьи
    template_name = 'yoga/add_health.html'  # Указываем шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('yoga:health_breath')  # URL для перенаправления после успешного создания статьи
    redirect_field_name = 'next'  # имя параметра запроса, в котором хранится URL-адрес, на который пользователь должен быть перенаправлен после успешного входа в систему.
    permission_required = 'yoga.add_health'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def form_valid(self, form):
        """
        Метод для добавления автора к мероприятию перед сохранением
        """
        # Добавляем автора к мероприятию перед сохранением
        form.instance.author = self.request.user
        # Логика обработки данных формы перед сохранением объекта
        return super().form_valid(form)


class EditHealthUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Класс для редактирования формы статьи о здоровье.
    Используется класс-миксин LoginRequiredMixin для контроля действий незарегистрированного пользователя.
    Используется класс-миксин UserPassesTestMixin для контроля прав для действий пользователя
    """
    model = Health  # Указываем модель, с которой работает представление
    form_class = HealthForm # Указываем класс формы для редактирования статьи
    template_name = 'yoga/add_health.html'  # Указываем шаблон, который будет использоваться для отображения формы
    context_object_name = 'health'  # Имя переменной контекста для статьи
    success_url = reverse_lazy('yoga:health_breath')  # URL для перенаправления после успешного редактирования статьи
    permission_required = 'yoga.change_health'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def test_func(self):
        health = self.get_object()
        user = self.request.user
        is_administrator = user.is_superuser
        return user == health.author or is_administrator


class DeleteHealthView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Класс для удаления статей в каталоге.
    Используется класс-миксин LoginRequiredMixin для контроля действий незарегистрированного пользователя.
    Используется класс-миксин UserPassesTestMixin для контроля прав для действий пользователя
    """
    # Указываем модель, с которой работает представление
    model = Health
    # Указываем шаблон, который будет использоваться для отображения формы подтверждения удаления
    template_name = 'yoga/delete_health.html'
    # URL для перенаправления на страницу статей о дыхании после успешного удаления статьи
    success_url = reverse_lazy('index')
    permission_required = 'yoga.delete_health'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def test_func(self):
        health = self.get_object()
        user = self.request.user
        is_administrator = user.is_superuser
        return user == health.author or is_administrator


class AsanaCatalogView(ListView):
    model = Asana  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/asanas.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'asanas'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 10  # Количество объектов на странице
    extra_context = {'title': 'Каталог асан'}  # Дополнительный контекст для передачи в шаблон

    # Метод для модификации начального запроса к БД
    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'title')
        order = self.request.GET.get('order', 'desc')
        search_query = self.request.GET.get('search_query', '')

        # Определение направления сортировки
        if order == 'asc':
            order_by = f'-{sort}'
        else:
            order_by = sort

        # Фильтрация карточек по поисковому запросу и сортировка
        if search_query:
            queryset = Asana.objects.filter(
                Q(title__iregex=search_query) |
                Q(translate__iregex=search_query) |
                Q(effect__iregex=search_query) |
                Q(technique__iregex=search_query)
            ).order_by(order_by).distinct()
        else:
            queryset = Asana.objects.order_by(order_by)
        return queryset


class AsanaDetailView(DetailView):
    """
    Класс для детального представления асаны.
    """
    # указываем модель для представления
    model = Asana
    # Указываем путь к шаблону для детального отображения карточки
    template_name = 'yoga/asana_detail.html'
    # Переопределяем имя переменной в контексте шаблона на 'asana' (до этого было 'asanas')
    context_object_name = 'asana'
    extra_context = {'title': 'Асана'}  # Дополнительный контекст для передачи в шаблон

    def get_object(self, queryset=None):
        """
        Метод для обновления счетчика просмотров при каждом отображении детальной страницы асаны
        :param queryset: по умолчанию None
        :return:
        """
        # Получаем объект по переданному в URL параметров pk карточки
        object_view = super().get_object(queryset=queryset)
        # Увеличиваем счетчик просмотров на 1
        Asana.objects.filter(pk=object_view.pk).update(views=F('views') + 1)
        return object_view


class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        asana = get_object_or_404(Asana, pk=pk)
        if request.user in asana.favorites.all():
            asana.favorites.remove(request.user)
            is_favorite = False
        else:
            asana.favorites.add(request.user)
            is_favorite = True
        return JsonResponse({'is_favorite': is_favorite})


class YogaEventCatalogView(ListView):
    model = YogaEvent  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/events.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'yogaevents'  # Имя переменной контекста, которую будем использовать в шаблоне
    extra_context = {'title': 'Мероприятия'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')
        order = self.request.GET.get('order', 'desc')

        # Определение направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        # Фильтрация карточек по поисковому запросу и сортировка
        queryset = YogaEvent.objects.order_by(order_by)
        return queryset


class AddYogaEventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = YogaEvent  # Указываем модель, с которой работает представление
    form_class = YogaEventForm # Указываем класс формы для создания карточки
    template_name = 'yoga/add_yogaevent.html'  # Указываем шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('yoga:events')  # URL для перенаправления после успешного создания мероприятия
    redirect_field_name = 'next'  # имя параметра запроса, в котором хранится URL-адрес, на который пользователь должен быть перенаправлен после успешного входа в систему.
    permission_required = 'yoga.add_yogaevent'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def form_valid(self, form):
        """
        Метод для добавления автора к мероприятию перед сохранением
        """
        # Добавляем автора к мероприятию перед сохранением
        form.instance.author = self.request.user
        # Логика обработки данных формы перед сохранением объекта
        return super().form_valid(form)


class EditYogaEventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = YogaEvent  # Указываем модель, с которой работает представление
    form_class = YogaEventForm  # Указываем класс формы для редактирования мероприятия
    template_name = 'yoga/add_yogaevent.html'  # Указываем шаблон, который будет использоваться для отображения формы
    context_object_name = 'yogaevent'  # Имя переменной контекста для мероприятия
    success_url = reverse_lazy('yoga:events')  # URL для перенаправления после успешного редактирования мероприятия
    permission_required = 'yoga.change_yogaevent'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def test_func(self):
        yogaevent = self.get_object()
        user = self.request.user
        is_administrator = user.is_superuser
        return user == yogaevent.author or is_administrator


class YogaEventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Класс для удаления карточек в каталоге.
    Используется класс-миксин LoginRequiredMixin для контроля действий незарегистрированного пользователя
    """
    # Указываем модель, с которой работает представление
    model = YogaEvent
    # Указываем шаблон, который будет использоваться для отображения формы подтверждения удаления
    template_name = 'yoga/delete_yogaevent.html'
    # URL для перенаправления на страницу мероприятий после успешного удаления карточки
    success_url = reverse_lazy('yoga:events')
    permission_required = 'yoga.delete_yogaevent'  # Указываем право, которое должен иметь пользователь для доступа к представлению

    def test_func(self):
        yogaevent = self.get_object()
        user = self.request.user
        is_administrator = user.is_superuser
        return user == yogaevent.author or is_administrator


class BackContactView(View):
    extra_context = {'title': 'Контакты для обратной связи'}  # Дополнительный контекст для передачи в шаблон

    def get(self, request):
        form = YogaeventRequestForm()
        return render(request, 'yoga/back_contact.html', {'form': form})

    def post(self, request):
        form = YogaeventRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('yoga:thank_for_request'))
        return render(request, 'yoga/back_contact.html', {'form': form})


class ThankForRequestView(View):
    def get(self, request):
        return render(request, 'yoga/thank_for_request.html')