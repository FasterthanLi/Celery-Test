from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from .models import User

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class VerifyView(View):
    def get(self, request, uuid):
        try:
            user = User.objects.get(verification_uuid=uuid, is_verified=False)
        except User.DoesNotExist:
            raise Http404("User does not exist or is already verified")

        user.is_verified = True
        user.save()

        return redirect('home')
