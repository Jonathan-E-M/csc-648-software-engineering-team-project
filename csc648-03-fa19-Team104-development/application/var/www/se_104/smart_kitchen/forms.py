from django import forms
from .models import *
from .models import Fridges
from .models import FoodDetails
from .models import Lists
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Form for milestone 2 vertical prototype to enter values into food_details table
class FoodDetailsForm(forms.ModelForm):
	class Meta:
		model = FoodDetails
		fields = ("__all__")

# Form for milestone 2 vertical prototype to search values from food_details table
class FoodDetailsSearchForm(forms.ModelForm):
	class Meta:
		model = FoodDetails
		fields = ("__all__")

# Form for milestone 3  search values from food_details table
class InventorySearchForm(forms.ModelForm):
	class Meta:
		model = FoodDetails
		fields = ("__all__")

# Form for creating fridge
class FridgeCreateForm(forms.ModelForm):
	class Meta:
		model = Fridges
		fields = ['name']

# Form for user signup
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for adding receipt image to db
class ImagesForm(forms.ModelForm): 
	class Meta: 
		model = Images
		fields = ['path'] 

# Form for adding receipt items to db
class SubmitReceiptFoodForm(forms.ModelForm):
	class Meta:
		model = Inventories
		fields = ("__all__")
		
# Form for creating invitation
class InvitationCreateForm(forms.ModelForm): 
	email = forms.EmailField()

	class Meta: 
		model = FridgeInvitations
		fields = ['email'] 

# Form for creating list item
class ListItemCreateForm(forms.ModelForm):
	class Meta: 
		model = Lists
		fields = ['food_name']
