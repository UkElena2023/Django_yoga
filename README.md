# Django_yoga
Это проект о йоге. Он создан для инструктора по хатха-йоге.
Инструктору необходимо предоставить права на добавление и редактирование мероприятий в личном кабинете.
Для обычных зарегистрированных пользователей не будет отображаться часть профиля пользователя.
В проекте присутствует функционал телеграм-бота, который осуществляет оповещение инструктора о записи на его мероприятие.
Для это в файле .env добавить необходимые для данного функционала переменные.

Для установки проекта Вам необходимо:
1. Склонируйте проект к себе на компьютер.
2. Установите виртуальное окружение и зависимости из файла requirements.txt
3. В данной проекте используются переменные окружения (все пароли и секретные ключи спрятаны в файл .env,
его Вам необходимо создать в корне проекта по примеру из файла .env.example)
4. Выполните миграции командой: python manage.py migrate
5. Загрузите в базу данных фикстуру с асанами йоги из файла db_asanas.json командой:
 python manage.py loaddata db_asanas.json
6. Запустите проект командой: python manage.py runserver

После этого проект будет доступен на локальном сервере по адресу:
 https://127.0.0.1:8000/