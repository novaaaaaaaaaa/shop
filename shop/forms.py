from django import forms
from django.forms import ModelForm
from .models import Profile, Stock, CartItems

class ProfileForm(ModelForm):
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'phone', 'class':'form-control'}), required=False)
    address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'address1', 'class':'form-control'}), required=False)
    address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'address2', 'class':'form-control'}), required=False)
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'city', 'class':'form-control'}), required=False)
    postcode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'postcode', 'class':'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = '__all__'

class AddStockForm(ModelForm):
    name = forms.CharField(label='Item Name', widget=forms.TextInput(attrs={'placeholder':'name', 'class':'form-control'}), required=True)
    description = forms.CharField(label='Item Description', widget=forms.Textarea(attrs={'placeholder':'description', 'class':'form-control'}), required=False)
    price = forms.CharField(label='Price (£)', widget=forms.TextInput(attrs={'placeholder':'0.00', 'class':'form-control', 'style':'border: 0 5px 0 5px'}), required=True)

    class Meta:
        model = Stock
        fields = '__all__'
    
class AddToCart(ModelForm):
    item = forms.ModelChoiceField(queryset=Stock.objects.values_list('name', flat=True), widget=forms.Select(attrs={'class':'form-control bootstrap-select'}), label='Item')
    quantity = forms.IntegerField(label='Quantity', min_value=1, max_value=999, widget=forms.TextInput(attrs={'min':1, 'max':999, 'type':'number', 'class':'form-control'}))

    class Meta:
        model = CartItems
        fields = [ "item", "quantity" ]