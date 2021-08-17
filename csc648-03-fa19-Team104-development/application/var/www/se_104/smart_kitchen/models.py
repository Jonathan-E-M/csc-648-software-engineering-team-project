from django.db import models
from django.conf import settings
from datetime import timedelta
import datetime
from django.contrib.auth.models import AbstractUser

# Static table with information about food. This table will be used to show details of a food item in invetory.
class FoodDetails(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)
    expiration_age = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'food_details'

# Custom User model
class User(AbstractUser):
    pass

# Fridges model, many to many relationship with users
class Fridges(models.Model):
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	name = models.CharField(max_length = 40)
	code = models.CharField(max_length = 40)

	class Meta:
		db_table = 'fridges'
		unique_together = ('name', 'user',)

# Imaged model stores all images of receipts
# One image refers to many inventory images
class Images(models.Model):
	path = models.FileField(max_length=100, upload_to='images/')
	addition_date = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'images'

# All food items that goes into fridge
# One to one relationship with fridge, inventory, food details
class Inventories(models.Model):

	FOOD_STATUS = [
	(0, 'IN FRIDGE'),
	(1, 'NOT IN'),
	]

	image = models.ForeignKey(Images, on_delete=models.CASCADE)
	food = models.ForeignKey(FoodDetails, on_delete=models.CASCADE)
	quantity = models.IntegerField(default = 0)
	fridge = models.ForeignKey(Fridges, on_delete=models.CASCADE)
	addition_date = models.DateTimeField(auto_now_add=True)
	expiration_date= models.DateTimeField(addition_date)
	status = models.IntegerField(choices=FOOD_STATUS,default = 1)

	class Meta:
		db_table ='inventories'

# Table with information about shopping list
# One Fridge can have one list, on list can only belong to one fridge  
class Lists(models.Model):

	LIST_STATUS= [
		(0, 'PENDING'),
		(1, 'DONE'),
	]

	fridge = models.ForeignKey(Fridges, on_delete=models.CASCADE) ##references fridge
	food_name = models.CharField(max_length = 100)
	quantity = models.IntegerField(default=0)
	status = models.IntegerField(choices=LIST_STATUS,default=1)

	class Meta:
		db_table = 'list_items'

# Static table for Recipe
class Recipes(models.Model):
	name = models.CharField(max_length= 50)
	ingredients = models.TextField(max_length = 254)
	link = models.URLField(default="recipes.com")

	class Meta:
		db_table ='recipes'

# Table to keep track of invitations
class FridgeInvitations(models.Model):	
	STATUS_CHOICES = [
		(0, 'Pending'),
		(1, 'Accepted'),
		(2, 'Declined'),
		(3, 'Send'),
	]

	from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "from_user_id",
        on_delete=models.CASCADE,
    )

	to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "to_user_id",
        on_delete=models.CASCADE,
    )

	fridge =models.ForeignKey(Fridges,on_delete=models.CASCADE)
	status = models.IntegerField(choices=STATUS_CHOICES, default=3)

	class Meta:
		db_table = 'fridge_invitations'
