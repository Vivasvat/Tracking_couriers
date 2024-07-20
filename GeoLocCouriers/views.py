from django.shortcuts import render

def GeoLocCouriers(request):
    context = {
            'title' : 'Навигатор',
            'Message': 'Да здравствует стажировка!'
        }
    return render(request, 'GeoLocCouriers/GeoLocCouriers.html', context)