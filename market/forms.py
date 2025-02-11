from django.forms import ModelForm

from market.models import Client


class WalletForm(ModelForm):
    class Meta:
        model = Client
        fields = ('balance',)