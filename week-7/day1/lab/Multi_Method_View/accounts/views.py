from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
def home_view(request):
    return render(request, 'accounts/home.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('profile')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('profile')

class ProfileView(View):
    def get(self, request):
        username = request.session.get('username', 'Guest')
        return render(request, 'accounts/profile.html', {'username': username})

def status_endpoint(request):
    return JsonResponse({'status': 'active', 'message': 'System is running smoothly'})
