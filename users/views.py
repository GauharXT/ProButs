import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Маалыматтар толук эмес'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Бул колдонуучу аты колдонууда'}, status=400)

            User.objects.create_user(username=username, password=password)
            return JsonResponse({'message': 'Катталуу ийгиликтүү!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON туура эмес'}, status=400)

    return JsonResponse({'error': 'POST гана уруксат'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Кирүү ийгиликтүү!'}, status=200)
            else:
                return JsonResponse({'error': 'Колдонуучу аты же сырсөз туура эмес'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON туура эмес'}, status=400)

    return JsonResponse({'error': 'POST гана уруксат'}, status=405)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Жүйөдөн чыктыңыз'}, status=200)
    return JsonResponse({'error': 'POST гана уруксат'}, status=405)
