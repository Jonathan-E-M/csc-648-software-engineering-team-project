from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from .models import FoodDetails, Inventories, Fridges, FridgeInvitations, Lists, Recipes
from .forms import FoodDetailsForm
from .forms import FoodDetailsSearchForm
from .forms import InventorySearchForm, FridgeCreateForm
from .forms import InvitationCreateForm
from .forms import ListItemCreateForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

def homepage(request):
    return render(request, 'site/homepage.html')

# Other pages of the website

def landing(request):
    return render(request, 'landing/landing.html')

@login_required
def receipt(request):
    if request.method == 'POST': 
        form = ImagesForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            
    else: 
        form = ImagesForm() 
    return render(request, 'receipt/receipt.html', {'form' : form})  

# Recipe pages of the website    

@login_required
def recipe(request):
    user_id = request.user.id
    fridge = Fridges.objects.filter(user_id=user_id)[:1].get()
    fridges = Fridges.objects.filter(user_id=user_id)
    recipes = Recipes.objects.all()
    custom_recipes = []
    final_recipes = []
    inventory_items = []
    lists = []
    inventory = Inventories.objects.filter(fridge_id=fridge.id)
    list_objects = Lists.objects.filter(fridge_id=fridge.id)

    for l in list_objects:
        lists.append(l.food_name)

    for i in inventory:
        inventory_items.append(i.food.name.split(",")[0])

    for ii in inventory_items:
        recipe = Recipes.objects.filter(ingredients__icontains=ii)
        custom_recipes.append(recipe)

    for c in custom_recipes:
        for cc in c:
            ingredients = cc.ingredients.split(",")
            ingredients_has = [x for x in ingredients if x in inventory_items]
            ingredients_not_has = [x for x in ingredients if x not in inventory_items]
            final_recipes.append([cc, ingredients_has, ingredients_not_has])

    return render(request, 'recipes/recipe.html', {'fridges': fridges, 'fridge': fridge, 'recipes': final_recipes, 'lists': lists})

@login_required
def recipeGroup(request):
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    recipes = Recipes.objects.all()
    custom_recipes = []
    final_recipes = []
    inventory_items = []
    lists = []
    inventory = Inventories.objects.filter(fridge_id=fridge.id)
    list_objects = Lists.objects.filter(fridge_id=fridge.id)

    for l in list_objects:
        lists.append(l.food_name)

    for i in inventory:
        inventory_items.append(i.food.name.split(",")[0])

    for ii in inventory_items:
        recipe = Recipes.objects.filter(ingredients__icontains=ii)
        custom_recipes.append(recipe)

    for c in custom_recipes:
        for cc in c:
            ingredients = cc.ingredients.split(",")
            ingredients_has = [x for x in ingredients if x in inventory_items]
            ingredients_not_has = [x for x in ingredients if x not in inventory_items]
            final_recipes.append([cc, ingredients_has, ingredients_not_has])

    return render(request, 'recipes/recipe.html', {'fridges': fridges, 'fridge': fridge, 'recipes': final_recipes, 'lists': lists})

@login_required
def addListItemFromRecipe(request):      
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    recipes = Recipes.objects.all()
    custom_recipes = []
    final_recipes = []
    inventory_items = []
    lists = []
    inventory = Inventories.objects.filter(fridge_id=fridge.id)
    list_objects = Lists.objects.filter(fridge_id=fridge.id)

    for l in list_objects:
        lists.append(l.food_name)

    for i in inventory:
        inventory_items.append(i.food.name.split(",")[0])

    for ii in inventory_items:
        recipe = Recipes.objects.filter(ingredients__icontains=ii)
        custom_recipes.append(recipe)

    for c in custom_recipes:
        for cc in c:
            ingredients = cc.ingredients.split(",")
            ingredients_has = [x for x in ingredients if x in inventory_items]
            ingredients_not_has = [x for x in ingredients if x not in inventory_items]
            final_recipes.append([cc, ingredients_has, ingredients_not_has])
    if request.method == 'POST':
        form = ListItemCreateForm(request.POST)
        if form.is_valid():

            try:
                food_name = form.cleaned_data.get('food_name')
                quantity = 1
                status = 0
                fridge_id = fridge.id
                Lists.objects.create(food_name=food_name, quantity=quantity, status=status, fridge_id=fridge_id)
                list_objects = Lists.objects.filter(fridge_id=fridge.id)
                lists = []
                for l in list_objects:
                    lists.append(l.food_name)
                return render(request, 'recipes/recipe.html', {'fridges': fridges, 'fridge': fridge, 'recipes': final_recipes, 'lists': lists})
            except:
                pass
    else:
        form = ListItemCreateForm()
    return render(request, 'recipes/recipe.html', {'fridges': fridges, 'fridge': fridge, 'recipes': final_recipes, 'lists': lists})

@login_required
def mygrouplist(request):
    user_id = request.user.id
    fridge = Fridges.objects.filter(user_id=user_id)[:1].get()
    fridges = Fridges.objects.filter(user_id=user_id)
    lists = Lists.objects.filter(fridge_id=fridge.id)
    return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})

@login_required
def grouplist(request):
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    lists = Lists.objects.filter(fridge_id=code)
    return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})

@login_required
def addListItem(request):      
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    lists = Lists.objects.filter(fridge_id=code)
    if request.method == 'POST':
        form = ListItemCreateForm(request.POST)
        if form.is_valid():

            try:
                food_name = form.cleaned_data.get('food_name')
                quantity = 1
                status = 0
                fridge_id = fridge.id
                Lists.objects.create(food_name=food_name, quantity=quantity, status=status, fridge_id=fridge_id)
                return redirect()
            except:
                pass
    else:
        form = ListItemCreateForm()
    return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})

@login_required
def removeListItem(request):
    list_item_id = request.POST.get('list_item_id')
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    lists = Lists.objects.filter(fridge_id=code)
    try:
        Lists.objects.get(id=list_item_id).delete()
        return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})
    except:
        print("Item delete failed")
    return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})

@login_required
def editListItem(request):
    user_id = request.user.id
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(user_id=user_id)
    fridge = Fridges.objects.filter(id=code)[:1].get()
    lists = Lists.objects.filter(fridge_id=code)
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken', None)
    data.pop('code', None)
    for i in data.items():
        item = Lists.objects.get(id=int(i[0].split("_")[1]))
        try:
            item.quantity = int(i[1])
            item.save()
            print("Item edit successful")
        except:
            print("Item edit failed")
    return render(request, 'lists/mygrouplist.html', {'fridge': fridge, 'fridges': fridges, 'lists': lists})

# group pages of the website 
@login_required
def group(request):
    user_id = request.user.id
    fridges = Fridges.objects.filter(user_id=user_id)
    if request.method == 'POST':
        form = FridgeCreateForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get('name')
                fridge_code = "{}_{}".format(name, user_id)
                fridge = Fridges(name=name, code=fridge_code, user_id=user_id)
                try:
                    fridge.save()
                except:
                    print("Fridge name already exists")
                return redirect()
            except:
                pass
    else:
        form = FridgeCreateForm()
    return render(request, 'groups/group.html', {'form': form, 'fridges': fridges})


@login_required
def membershome(request):
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(code=code)
    fridge = Fridges.objects.filter(code=code)[:1].get()
    return render(request, 'groups/membershome.html', {'fridges': fridges, 'fridge': fridge})

@login_required
def removemember(request):
    user_id = request.user.id
    fridge_id = request.POST.get('fridge')
    fridge = Fridges.objects.get(id=fridge_id)
    code = fridge.code
    fridges = Fridges.objects.filter(code=code)
    try:
        Fridges.objects.get(id=fridge_id).delete()    
        if fridge.user_id == user_id:
            return redirect('group')
    except:
        print("Fridge delete failed")
    return render(request, 'groups/membershome.html', {'fridges': fridges, 'fridge': fridge})

@login_required
def leaveFridge(request):
    fridge_id = request.POST.get('fridge')
    try:
        Fridges.objects.get(id=fridge_id).delete()
    except:
        print("Fridge delete failed")
    return redirect('group')

@login_required
def inviteMember(request):
    code = request.POST.get('code')
    fridges = Fridges.objects.filter(code=code)
    fridge = Fridges.objects.filter(code=code)[:1].get()

    from_user_id = request.user.id
    if request.method == 'POST':
        form = InvitationCreateForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get('email')
                to_user_id = User.objects.filter(email=email)[:1].get().id
                fridge_id = fridge.id
                FridgeInvitations.objects.create(fridge_id=fridge_id, from_user_id=from_user_id, to_user_id=to_user_id)
                return redirect()
            except:
                pass
    else:
        form = InvitationCreateForm()
    return render(request, 'groups/membershome.html', {'fridges': fridges, 'fridge': fridge})

@login_required
def invitations(request):
    user_id = request.user.id
    invitations = FridgeInvitations.objects.filter(to_user_id=user_id, status=3)
    if request.method == 'POST':
        if request.POST.get('accept') != None:
            invitation_id = request.POST.get('accept')
            invitation = FridgeInvitations.objects.get(pk = invitation_id)
            invitation.status = 1
            invitation.save()

            fridge_id = invitation.fridge_id
            fridge = Fridges.objects.get(pk=fridge_id)
            Fridges.objects.create(name=fridge.name, code=fridge.code, user_id=user_id)
        else:
            invitation_id = request.POST.get('decline')
            invitation = FridgeInvitations.objects.get(pk = invitation_id)
            invitation.status = 2
            invitation.save()
    return render(request, 'invitation/invitations.html', {'invitations': invitations})

# Receipt and Inventory pages

@login_required
def receipt(request):
    
    if request.method == 'POST' and "submitImage" in request.POST:
        form = ImagesForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 

        import os
        import io
        import re
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "~/csc648-03-fa19-Team104/application/var/www/se_104/KeyFile.json"
        # Google Vision
        # Detects text in the file.
        a = []
        b = []
        c = []
        flag1 = False
        flag2 = False

        client = vision.ImageAnnotatorClient()
        path = 'media/images/'+str(form.cleaned_data.get('path'))
        with io.open(path,'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        out = next(iter(texts))
        output = out.description.splitlines()
        dblist = FoodDetails.objects.all().values_list('name')
        for x in output:
            splitted = x.splitlines()
            for i in splitted:
                a.append(i)
                    
        for j in dblist:
            j = str(j)
            j = j[2:]
            j = j.split(',', 1)[0]
            b.append(j)

        for j in b:
            for i in a:
                if(j.lower() in i.lower()):
                    if j not in c:
                        c.append(j)
                    break
            continue

        return render(request, 'receipt/receipt.html', {"c":c})
            
    else: 
        form = ImagesForm() 
    return render(request, 'receipt/receipt.html', {'form' : form})

@login_required
def imageSave(request):
    user_id = request.user.id
    fridge = Fridges.objects.filter(user_id=user_id)[:1].get()
    foods = Inventories.objects.filter(fridge_id=fridge.id)
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken', None)
    data.pop('example_length', None)

    for i in data.items():
        name = i[0].split("_")[0]
        quantity = i[1]
        item = 'food_item'

        if name == 'quantity':
            item = i[0].split("_")[1]
            food_item = FoodDetails.objects.filter(name__icontains=item)[:1].get()
            if food_item:
                if int(quantity) > 0:
                    try:
                        Inventories.objects.create(quantity=quantity, addition_date=timezone.now(),
                                                expiration_date=timezone.now() + datetime.timedelta(days=10), status=0, food_id=food_item.id, fridge_id=fridge.id, image_id=36)
                    except:
                        print("Item not saved")

    return render(request, 'inventory/inventorySearch.html', {'foods': foods})

@login_required
def inventory(request):
    user_id = request.user.id
    fridge = Fridges.objects.filter(user_id=user_id)[:1].get()
    foods = Inventories.objects.filter(fridge_id=fridge.id)
    if request.method == 'POST':
        form = InventorySearchForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
    else:
        form = InventorySearchForm()
    return render(request, 'inventory/inventorySearch.html', {'form': form, 'foods': foods})

# Register new users and assign them to a default group
# The code for group is groupname_userid
# where groupname is the name of the group (MyHome by default)
# and userid is the user_id of the user creating the group
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_id = request.user.id
            fridge_code = "MyHome_{}".format(user_id)
            fridge = Fridges(name='MyHome', code=fridge_code, user_id=user_id)
            fridge.save()
            return redirect('inventory')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

# About pages for all team members
def about(request):
    template = loader.get_template('about/about.html')
    return HttpResponse(template.render())



def index(request):
    return render(request, 'about/index.html')

# Vertical prototype for milestone 2
# Displays all the food entries in food_details table
# Also takes input from the FoodDetailsForm and saves to database
def food(request):
    foods = FoodDetails.objects.all()
    if request.method == 'POST':
        form = FoodDetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
    else:
        form = FoodDetailsForm()
    return render(request, 'food/food-details.html', {'form': form, 'foods': foods})

# Vertical prototype for milestone 2
# Search for a food item from food_details table
def search(request):
    if request.method == 'GET':
        query = request.GET.get('name')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(name__icontains=query)

            results = FoodDetails.objects.filter(lookups).distinct()

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'food/food-search.html', context)
        else:
            return render(request, 'food/food-search.html')

    else:
        return render(request, 'food/food-search.html')

def khyo(request):
    template = loader.get_template('about/khyo.html')
    return HttpResponse(template.render())

def darnell(request):
    template = loader.get_template('about/darnell.html')
    return HttpResponse(template.render())

def brian(request):
    template = loader.get_template('about/brian.html')
    return HttpResponse(template.render())

def srushti(request):
    template = loader.get_template('about/srushti.html')
    return HttpResponse(template.render())

def jonathan(request):
    template = loader.get_template('about/jonathan.html')
    return HttpResponse(template.render())

def david(request):
    return render(request, 'about/david.html')
   
# Meeting logs

def logSite(request):
    return render(request, 'log/logSite.html')
    
def sept10(request):
    return render(request, 'log/sept10.html')
    
def sept12(request):
    return render(request, 'log/sept12.html')
    
def sept16(request):
    return render(request, 'log/sept16.html')

def sept19(request):
    return render(request, 'log/sept19.html')

def sept23(request):
    return render(request, 'log/sept23.html')
