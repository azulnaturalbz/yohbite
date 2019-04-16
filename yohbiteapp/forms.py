from django import forms
from django.contrib.auth.models import User
from yohbiteapp.models import Restaurant,Meal,Location,District


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')



class UserFormEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name','phone','address','district','location','logo')



    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['location'].queryset = Location.objects.none()
        #Conditional Below ensures that state and location have the right mapping from state to location belize to belize city eg.
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['location'].queryset = Location.objects.filter(local__district__id=district_id).order_by('local')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['location'].queryset = self.instance.district.local_set.order_by('local')



class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude= ('restaurant',)
