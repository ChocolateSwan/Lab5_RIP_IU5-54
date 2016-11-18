from django.shortcuts import render
from django.views import View

class First_page_view(View):
    def get (self,request):
        data = {
            'flats': [
                {'title': 'Первая квартира', 'id': 1},
                {'title': 'Вторая квартира', 'id': 2},
                {'title': 'Третья квартира', 'id': 3},
                {'title': 'Четвертая квартира', 'id': 4},
                {'title': 'Пятая квартира', 'id': 5},
                {'title': 'Шестая квартира', 'id': 6}
            ]
        }
        return render(request, 'first_page.html', data)

class Flat (View):
    def get (self,request,id):
        data = {
            'flat': {
                'id': id,
                "rooms" : int(id)
            }
        }
        return render(request, 'flat.html', data)
