from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, F
from django.urls import reverse
from .forms import YogaEventForm, YogaeventRequestForm
from .models import Asana, YogaEvent


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


class IndexView(TemplateView):
    """
    Класс (статический) для отображения страницы "Главная"
    """
    template_name = 'yoga/main.html'


class AsanaCatalogView(ListView):
    model = Asana  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/asanas.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'asanas'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 5  # Количество объектов на странице

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
    Используется класс-миксин для добавления меню в контекст шаблона страницы для детального отображения карточки
    """
    # указываем модель для представления
    model = Asana
    # Указываем путь к шаблону для детального отображения карточки
    template_name = 'yoga/asana_detail.html'
    # Переопределяем имя переменной в контексте шаблона на 'asana' (до этого было 'asanas')
    context_object_name = 'asana'

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


class YogaEventCatalogView(ListView):
    model = YogaEvent  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'yoga/events.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'yogaevents'  # Имя переменной контекста, которую будем использовать в шаблоне


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