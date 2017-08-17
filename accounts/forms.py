from django import forms
from .models import UserProfile


class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'profile_picture', 'phone_number', )

    def __init__(self, *args, **kwargs):
        super(CreateUserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field_obj in self.fields.items():
            if field_name is 'profile_picture':
                pass
            else:
                field_obj.widget.attrs.update({'class': 'form-control'})