# Журнал тренировок 

# Запускае команду для установки виртуального окружения
pip install -r requirements.txt
# Входим в директорию urban_project
cd urban_project
# Производим миграции
python manage.py makemigrations
python manage.py migrate
# Запускаем DjangoProject
python manage.py runserver
python manage.py createsuperuser

# Так выглядит начальная страница проекта

![Uploading 1.png…](https://github.com/SergeyTsVL/TZ_vacancy/blob/main/images/1.png)

# Заходим во вкладку "регистрация", регистрируемся.

![Uploading 1.png…](https://github.com/SergeyTsVL/TZ_vacancy/blob/main/images/2.png)

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/8.png)

# Если ввести не корректные записи для добавления.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/9.png)

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/10.png)

# Окно доски с объявлениями.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/1.png)

# Заходим в одно из объявлений, кликая по нему.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/2.png)

# Кликаем по ссылке на которой написано "Редактировать"

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/9.png)

# Вносим необходимые изменения в названии или тексте объявления. Нажимаем кнопку "Сохранить изменения".

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/4.png)

# После сохранения изменений видим их в общем списке объявлений.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/5.png)


# Создаем объявления для удаления.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/11.png)

# Входим в это объявление и кликаем надпись с надписью "Удалить".

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/12.png)

# Подтверждаем удаление кликом по кнопке "Удалить".

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/13.png)

# После удаления возвращаемся (автоматически) на страницу со списком объявлений, убеждаемся что объявление удалено.

![Uploading 1.png…](https://github.com/SergeyTsVL/DjangoProject/blob/1.2/images/14.png)


