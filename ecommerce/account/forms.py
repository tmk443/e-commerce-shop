
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms


from django.forms.widgets import PasswordInput, TextInput


# form rejestracyjny

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # oznacz ze email jest wymagany

        self.fields['email'].required = True
        self.fields['email'].label = 'Ades Email'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Powtórz hasło'
        self.fields['username'].label = 'Nazwa użytkownika'

        self.fields['username'].help_text='150 znaków lub mniej. Tylko litery, cyfry i @/./+/-/_.'
        self.fields['username'].error_messages={
            'unique': 'Ta nazwa użytkownika jest już zajęta.',
            'invalid': 'Nieprawidłowy format.'
        }
        self.fields['password1'].help_text="Twoje hasło powinno spełniać następujące kryteria:" "<ul>" "<li> Nie może być zbyt podobne do innych informacji osobistych.</li>" "<li> Musi zawierać co najmniej 8 znaków.</li>""<li> Nie może być powszechnie używanym hasłem.</li>""<li> Nie może być całkowicie numeryczne.</li>""</ul>"
        self.fields['password1'].error_messages={
            'password_mismatch': ('Podane hasła nie są identyczne.'),
            'password_too_short': ('Twoje hasło musi zawierać co najmniej 8 znaków.'),
            'password_common': ('Twoje hasło nie może być powszechnie używanym hasłem.'),
            'password_entirely_numeric': ('Twoje hasło nie może być całkowicie numeryczne.'),
        }
        self.fields['password2'].help_text="Dla potwierdzenia, podaj hasło jeszcze raz."

    # walidacje emaila
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('Email jest nieprawidłowy')


        if len(email) >= 100:

            raise forms.ValidationError("Twój Email jest zbyt długi")


        return email
    

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget = PasswordInput())
    username.label="Nazwa Użytkownika"
    password.label="Hasło"

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # oznacz ze email jest wymagany

        self.fields['email'].required = True
        self.fields['username'].label="Nazwa Użytkownika"
        self.fields['email'].label="Adres Email"

        self.fields['username'].help_text='150 znaków lub mniej. Tylko litery, cyfry i @/./+/-/_.'
        self.fields['username'].error_messages={
            'unique': 'Ta nazwa użytkownika jest już zajęta.',
            'invalid': 'Nieprawidłowy format.'
        }
        #self.exclude['password1'].label="Hasło"
        #self.exclude['password2'].label="Powtórz hasło"




        def clean_email(self):

            email = self.cleaned_data.get("email")

            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

                raise forms.ValidationError('Email jest nieprawidłowy')


            if len(email) >= 100:

                raise forms.ValidationError("Twój Email jest zbyt długi")


            return email