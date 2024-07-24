from django import forms
from .models import Asana, YogaEvent, Category, YogaeventRequest, Health, Subject


class AsanaForm(forms.ModelForm):
    image = forms.ImageField(
        label='Изображение',
        required=False
    )

    class Meta:
        model = Asana  # Указываем модель, с которой работает форма
        # Указываем, какие поля должны присутствовать в форме и в каком порядке
        fields = ['title', 'translate', 'effect', 'contraindication', 'technique', 'image']
        # Указываем виджеты для полей
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'translate': forms.TextInput(attrs={'class': 'form-control'}),
            'effect': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'contraindication': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'technique': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),

        }
        # Указываем метки для полей
        labels = {
            'title': 'Название асаны',
            'translate': 'Перевод с санскрита',
            'effect': 'Показания',
            'contraindication': 'Противопоказания',
            'technique': 'Техника',
            'image': 'Изображение',
        }


class YogaEventForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                      label='Категория', widget=forms.Select(attrs={'class': 'form-control'}))
    image_event = forms.ImageField(
        label='Изображение мероприятия',
        required=False
    )

    class Meta:
        model = YogaEvent  # Указываем модель, с которой работает форма
        # Указываем, какие поля должны присутствовать в форме и в каком порядке
        fields = ['category', 'place', 'link_2', 'time_event', 'description', 'image_event', 'status', 'link']
        # Указываем виджеты для полей
        widgets = {
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'link_2': forms.TextInput(attrs={'class': 'form-control'}),
            'time_event': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # Указываем метки для полей
        labels = {
            'place': 'Место проведения',
            'link_2': 'Ссылка на место',
            'time_event': 'Время проведения',
            'description': 'Описание',
            'image_event': 'Изображение',
            'link': 'Ссылка на доп.информацию о мероприятии',
        }


class YogaeventRequestForm(forms.ModelForm):
    """
    Форма для связи и записи на мероприятия.
    """

    class Meta:
        model = YogaeventRequest
        fields = ['first_name', 'email', 'phone', 'comment']

        # Указываем виджеты для полей
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),

        }
        # Указываем метки для полей
        labels = {
            'first_name': 'Имя',
            'email': 'Адрес электронной почты',
            'phone': 'Телефон',
            'comment': 'Комментарий, на какое мероприятие вы хотите записаться?',

        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email and not phone:
            raise forms.ValidationError(
                'Необходимо ввести хотя бы один контакт: email или телефон.')
        return cleaned_data


class HealthForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="Тема не выбрана",
                                      label='Тема статьи', widget=forms.Select(attrs={'class': 'form-control'}))

    image_text = forms.ImageField(
        label='Изображение для статьи',
        required=False
    )

    class Meta:
        model = Health  # Указываем модель, с которой работает форма
        # Указываем, какие поля должны присутствовать в форме и в каком порядке
        fields = ['subject', 'name', 'description', 'link', 'image_text']
        # Указываем виджеты для полей
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'time_event': forms.TextInput(attrs={'class': 'form-control'}),

        }
        # Указываем метки для полей
        labels = {
            'name': 'Название статьи',
            'link': 'Ссылка доп.информацию для статьи',
            'description': 'Описание',
            'image_text': 'Изображение для статьи',

        }

