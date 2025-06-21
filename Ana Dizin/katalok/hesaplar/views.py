from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def kullanici_giris(request):
    if request.method == 'POST':
        kullanici_adi = request.POST['kullanici_adi']
        sifre = request.POST['sifre']
        user = authenticate(request, username=kullanici_adi, password=sifre)
        if user is not None:
            login(request, user)
            return redirect('urun_liste')  
        else:
            messages.error(request, 'Hatalı kullanıcı adı veya şifre')
    return render(request, 'hesaplar/giris.html')

def kullanici_kayit(request):
    if request.method == 'POST':
        kullanici_adi = request.POST['kullanici_adi']
        eposta = request.POST['eposta']
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(username=kullanici_adi).exists():
                messages.error(request, 'Kullanıcı adı zaten var.')
            else:
                user = User.objects.create_user(username=kullanici_adi, email=eposta, password=sifre)
                login(request, user)
                return redirect('urun_liste')
        else:
            messages.error(request, 'Şifreler uyuşmuyor.')

    return render(request, 'hesaplar/kayit.html')

def kullanici_cikis(request):
    logout(request)
    return redirect('giris')
