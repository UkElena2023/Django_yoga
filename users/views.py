from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import get_user_model


from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm, \
    UserPasswordResetConfirmForm, UserPasswordResetForm

from yoga.models import YogaEvent, Asana, Health


class LoginUser(LoginView):
    """
    Класс для авторизации пользователя.
    """
    # указываем класс формы для авторизации пользователя
    form_class = LoginUserForm
    # Указываем путь к шаблону для страницы для авторизации пользователя
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}  # экстра контекст для шаблона страницы авторизации пользователя
    # Перенаправление на страницу после успешной авторизации с которой пользователь пришел
    redirect_field_name = 'next'

    def get_success_url(self):
        """
        Метод для перенаправления на страницу, с которой пользователь был направлен на авторизацию
        """
        if self.request.POST.get('next', '').strip():
            # Перенаправление на страницу, с которой пользователь был направлен на авторизацию
            return self.request.POST.get('next')
        # Перенаправление на страницу каталога после неудачной авторизации
        return reverse_lazy('index')


class LogoutUser(LogoutView):
    """
    Класс для выхода пользователя из системы.
    """
    # Указываем путь к шаблону об успешном выхода пользователя из системы
    template_name = 'users/logout.html'
    # next_page = reverse_lazy('users:login')


class RegisterUser(CreateView):
    """
    Класс для регистрации пользователя на базе CreateView.
    """
    # Указываем класс формы, который мы создали для регистрации
    form_class = RegisterUserForm
    # Путь к шаблону, который будет использоваться для отображения формы
    template_name = 'users/register.html'
    # Дополнительный контекст для передачи в шаблон
    extra_context = {'title': 'Регистрация'}
    # URL, на который будет перенаправлен пользователь после успешной регистрации
    success_url = reverse_lazy('users:thanks')


class ThanksForRegister(TemplateView):
    """
    Класс для представления страницы успешной регистрации пользователя.
    """
    # Указываем путь к шаблону для страницы успешной регистрации пользователя
    template_name = 'users/thanks.html'
    extra_context = {'title': 'Регистрация завершена'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования профиля пользователя.
    Используется класс-миксин LoginRequiredMixin для контроля действий незарегистрированного пользователя.
    """
    model = get_user_model()  # Используем модель текущего пользователя
    form_class = ProfileUserForm  # Связываем с формой профиля пользователя
    template_name = 'users/profile.html'  # Указываем путь к шаблону
    extra_context = {'title': 'Профиль пользователя',
                     'active_tab': 'profile'}  # Дополнительный контекст для передачи в шаблон

    def get_success_url(self):
        """
        Метод для перенаправления на страницу после успешного обновления профиля пользователя
        :return:
        """
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """
        Метод для получения объекта модели user для редактирования
        """
        user = self.request.user
        return user


class UserPasswordChange(PasswordChangeView):
    """
    Класс для изменения пароля пользователя. Наследуется от PasswordChangeView - стандартного класса для изменения
    пароля. Использует пользовательскую форму UserPasswordChangeForm, которая наследуется от PasswordChangeForm
    """
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    extra_context = {'title': 'Изменение пароля'}
    success_url = reverse_lazy('users:password_change_done')


class UserPasswordChangeDone(TemplateView):
    """
    Класс для представления страницы с сообщением успешного изменения пароля пользователя.
    Наследуется от TemplateView
    """
    template_name = 'users/password_change_done.html'
    extra_context = {'title': 'Пароль изменен успешно'}


class UserYogaEventView(ListView):
    """
    Класс для отображения всех мероприятий пользователя. Наследуется от ListView.
    Переопределяет метод get_queryset для получения мероприятий пользователя
    """
    model = YogaEvent
    template_name = 'users/profile_events.html'
    context_object_name = 'yogaevents'
    extra_context = {'title': 'Мои мероприятия'}

    def get_queryset(self):
        """
        Метод для получения мероприятий пользователя с помощью фильтра по автору и сортировки по дате загрузки
        """
        return YogaEvent.objects.filter(author=self.request.user).order_by('-upload_date')


class UserHealthView(ListView):
    """
    Класс для отображения всех статей пользователя. Наследуется от ListView.
    Переопределяет метод get_queryset для получения статей пользователя
    """
    model = Health
    template_name = 'users/profile_health.html'
    context_object_name = 'healthes'
    extra_context = {'title': 'Мои статьи'}

    def get_queryset(self):
        """
        Метод для получения статей пользователя с помощью фильтра по автору и сортировки по дате загрузки
        """
        return Health.objects.filter(author=self.request.user).order_by('-upload_date')


class UserFavoritAsanasView(ListView):
    """
    Класс для отображения асан, добавленных пользователем в избранное. Наследуется от ListView.
    Переопределяет метод get_queryset для получения мероприятий пользователя
    """
    model = Asana
    template_name = 'users/profile_asanas.html'
    context_object_name = 'asanas'
    extra_context = {'title': 'Избранные асаны'}

    def get_queryset(self):
        """
        Метод для получения каталога асан, добавленных пользователем в избранное
        """
        return self.request.user.favorite_asanas.all().order_by('-upload_date')


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления профиля пользователя. Наследуется от DeleteView.
    """
    model = get_user_model()  # Используем модель текущего пользователя
    template_name = 'users/profile_delete.html'  # Указываем путь к шаблону
    success_url = reverse_lazy('users:delete_complete')  # URL для перенаправления на главную страницу

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class UserDeleteComplete(TemplateView):
    """
    Класс для представления страницы об успешном удалении профиля пользователя.
    """
    # Указываем путь к шаблону для страницы по удалению пользователя
    template_name = 'users/delete_complete.html'
    extra_context = {'title': 'Удаление профиля завершено'}


class UserPasswordReset(PasswordResetView):
    """
    Класс для восстановления пароля пользователя.
    Наследуется от PasswordResetView - стандартного класса для восстановления.
    Запрашивает email для отправки письма со ссылкой для сброса пароля
    """
    form_class = UserPasswordResetForm
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetConfirm(PasswordResetConfirmView):
    """
    Класс для ввода нового пароля пользователя.
    Наследуется от PasswordResetConfirmView - стандартного класса для восстановления.
    """
    form_class = UserPasswordResetConfirmForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')
