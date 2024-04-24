from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest, HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import force_str
from django.contrib.auth import login, authenticate, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import CustomUser
from .forms import CustomUserCreationForm, MyLoginForm, AccountForm
from .tokens import account_activation_token


class SignupView(View):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until email confirmation
            user.save()

            # Send email confirmation
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('accounts:account_activation_sent')
        return render(request, self.template_name, {'form': form})


class AccountActivationSentView(TemplateView):
    template_name = 'registration/account_activation_sent.html'


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.email_confirmed = True
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('accounts:account_activation_complete')
        else:
            return HttpResponseBadRequest('Activation link is invalid!')


class AccountActivationComplete(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'registration/account_activation_complete.html'
    success_url = 'تبریک، حساب شما با موفقیت فعال شد.'


class LoginView(View):
    form_class = MyLoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:

                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد.')
                if request.GET.get('next'):
                    return redirect(request.GET['next'])
                return redirect('products:products_list')

            else:
                return HttpResponse('رمز و نام کاربری صحیح نیست')

        else:

            return render(request, self.template_name, {'form': form})


class LogOutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request ,'خارج شدید.')
        return redirect('products:products_list')


class AccountInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = AccountForm
    template_name = 'accounts/user_info.html'
    success_url = reverse_lazy('accounts:account_info')
    success_message = 'اطلاعات با موفقیت تغییر یافت.'
    
    def get_object(self, queryset=None):
        return self.request.user


