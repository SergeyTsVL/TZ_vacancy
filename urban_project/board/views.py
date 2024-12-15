from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    """
    Этот метод выполняет выход пользователя из системы и перенаправляет его на домашнюю страницу.
    """
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

def signup(request):
    """
    ызывает страницу для подписи объявлений.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    """
    Вызывает страницу home.html .
    """
    return render(request, 'home.html')

def advertisement_list(request):
    """
    Вызывает страницу advertisement_list.html.
    """
    advertisements = Advertisement.objects.all()
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})

def advertisement_detail(request, pk):
    """
    Вызывает страницу advertisement_detail.html .
    """
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})

@login_required  # Проверяет регистрацию пользователя
def add_advertisement(request):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    обавлении данных, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    """
    if request.method == "POST":
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            # advertisement.name = request.user
            advertisement.status = 'заявка создана'
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})

@login_required    # Проверяет регистрацию пользователя
def edit_advertisement(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    редактировании, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    :param request:
    :param pk:
    :return:
    """
    advertisement = Advertisement.objects.get(pk=pk)
    if advertisement.status != 'товар передан в доставку' and advertisement.status != 'товар доставлен':
        if request.method == "POST":
            form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)

            if form.is_valid():
                advertisement.name = request.user

                advertisement.status = 'заявка создана'
                form.save()
                img_obj = form.instance
                # Перенаправляет на страницу с сохраненными исправлениями.
                return redirect('board:advertisement_detail', pk=img_obj.pk)
        else:
            # вызов функции которая отобразит в браузере указанный шаблон с данными формы и объявления.
            form = AdvertisementForm(instance=advertisement)
        return render(request, 'board/edit_advertisement.html',
                      {'form': form, 'advertisement': advertisement})
    return redirect('board:advertisement_detail', pk=pk)

@login_required
def delete_advertisement(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", после чего удаляет
    объявление и возвращается в окно объявления.
    :param request:
    :param pk:
    :return:
    """
    advertisement = Advertisement.objects.get(pk=pk)
    if advertisement.status != 'товар передан в доставку' and advertisement.status != 'товар доставлен':
        if request.method == "POST":
            advertisement.delete()
            return redirect('board:advertisement_list')
        else:
            None
        return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})
    else:
        return redirect('board:advertisement_list')
