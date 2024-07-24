from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

from GeoLocCouriers.models import Couriers, ListOrderId


def save_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        count = data.get('count')

        cour = Couriers(latitude = latitude, longitude = longitude, count = count)
        cour.save()
        # Здесь вы можете сохранить местоположение в базу данных или обработать его иным образом

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'fail'}, status=400)


def GetDataCouriers(request):
    # Местположение курьера
    url = 'https://robotapitest.dostavista.ru/api/business/1.5/courier'

    headers = {
        'X-DV-Auth-Token': '6DF1D823AA1439E7AEF2BB98E9A116D4CAC629F0',
        'Content-Type': 'application/json'
        }
    
    listorder = ListOrderId.objects.values()
    listres = [entry for entry in listorder] 

    for id in listres:
        order_id = id['order_id']
        urlcour = f'{url}?order_id={order_id}'
        # data = {
        #         'order_id' : id,
        #     }
        response_data = requests.post(urlcour, headers=headers)
        response_loc_data = response_data.json()
        # Обработка ответа

        # courier_extra_data = response_loc_data['courier']

        # courier_data = Couriers(
        #     courier_id = courier_extra_data['courier_id'],
        #     surname = courier_extra_data['surname'],
        #     name = courier_extra_data['name'],
        #     middlename = courier_extra_data['middlename'],
        #     phone = courier_extra_data['phone'],
        #     photo_url = courier_extra_data['photo_url'],
        #     latitude = courier_extra_data['latitude'],
        #     longitude = courier_extra_data['longitude'],
        # )
        # courier_data.save()

    context = {
            # 'response_loc_data' : response_loc_data,
        'listres' : listres,
        'urlcour' : urlcour,
        'listorder' : response_loc_data,
        }
    
    return render(request, 'GeoLocCouriers/geomain.html', context)


def CreateTestOrder(request):
    url = 'https://robotapitest.dostavista.ru/api/business/1.5/create-order'

    # Заголовки запроса
    headers = {
        'X-DV-Auth-Token': '6DF1D823AA1439E7AEF2BB98E9A116D4CAC629F0',
        'Content-Type': 'application/json'
    }

    # Данные для отправки (в формате JSON)
    data = {    
    "matter" : "Документы",
    "points":[{
        "address" : "Москва, ул. Покровка, 11",
        "contact_person":{"phone":"79030000001"}},
              {
                  "address" : "Москва, ул. Солянка, 4",
                  "contact_person":{"phone":"79163779894"}}]
                  }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        
        response_data = response.json()

        tmp = response_data['order']
        order_id = tmp['order_id']

        context = {
            'response_data' : response_data,
        }

        listorder = ListOrderId(order_id = order_id)
        listorder.save()

        return render(request, 'GeoLocCouriers/geomain.html', context)
    else:
        print(f'Error: {response.status_code}')
    

def geolocation(request):
    return render(request, 'GeoLocCouriers/geolocation.html')
