from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
from .restapis import get_query_from_cf,post_request
import logging
import json
from requests.auth import HTTPBasicAuth
# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def indexhtml(request):
    return render(request,'index.html')


# Create an `about` view to render a static about page
def about(request):
    return render(request,'djangoapp/about.html')


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request,'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request

def login_request(request):
    context = {}
    logger.debug(request.POST)
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        logger.debug(request)
        return render(request, 'djangoapp/registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':         
         # Get username and password from request.POST dictionary
          username = request.POST['username']
          password = request.POST['psw']
          # Try to check if provide credential can be authenticated
          user = authenticate(username=username, password=password)
          if user is not None:
               # If user is valid, call login method to login current user
               login(request, user)
               logger.debug("LOGGED IN!")
               return redirect('djangoapp:index')
          else:
            # If not, return to login page again
                logger.debug("Wrong something!")
                return redirect('djangoapp:index')
    else:
        return render(request, 'djangoapp/registration.html', context)


       
# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)   
    return redirect('./')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
        context = {}
        logger.debug(request.method)
        # Handles POST request
        if request.method == "POST":
         # Get username and password from request.POST dictionary
          username = request.POST['username']
          psw = request.POST['psw']
          # Try to check if provide credential can be authenticated
          user = authenticate(username=username, password=psw)
          if user is not None:
               # If user is valid, call login method to login current user
               login(request, user)
               logger.debug("LOGGED IN!")
               return redirect('djangoapp:index')
          else:
            logger.debug(request)
            user_exist = False
            try:
                # Check if user already exists
                User.objects.get(username=username)
                user_exist = True
            except:
                # If not, simply log this is a new user
                logger.debug("{} is new user".format(username))
            # If it is a new user
            if not user_exist:
                # Create user in auth_user table
                lastname=request.POST['lastname']
                firstname=request.POST['firstname']
                user = User.objects.create_user(username=username,password=psw)
                # if you want to change other fields.
                user.last_name = lastname
                user.first_name = firstname
                user.save()
                return render(request, 'djangoapp/index.html', context)
            else:
                return render(request, 'djangoapp/index.html', context)
        else:
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
        #if request.method == "GET":
        #url = "https://us-south.functions.appdomain.cloud/api/v1/web/TemporaryTest_TemporaryTest/capstone/get_dealerships"
        # Get dealers from the URL
        #dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        # Return a list of dealer short name
        #context={'dealerships':dealerships}
        return render(request, 'djangoapp/index.html')

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    return render(request,'djangoapp/dealer_details.html')

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    return render(request,'djangoapp/add_review.html')
def ajaxDealerships(request):
        name=request.GET.get('name')
        address=request.GET.get('address')
        city=request.GET.get('city')
        state=request.GET.get('state')
        zip=request.GET.get('zip')
        skip=request.GET.get('skip')
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/TemporaryTest_TemporaryTest/capstone/get_dealerships"
        # Get dealers from the URL
        dealers = get_query_from_cf(url,name=name, address=address, city=city, state=state,zip=zip,skip=skip)
        # Concat all dealer's short name
        # Return a list of dealer short name
        
        return HttpResponse((dealers), content_type="application/json")
def ajaxReviews(request):
    dealership=request.GET.get('dealership')
    
    url = "https://us-south.functions.appdomain.cloud/api/v1/web/TemporaryTest_TemporaryTest/capstone/get_reviews"
        
    if dealership is None:
        reviews={'error':'Not a valid dealership'}
    else:
        reviews = get_query_from_cf(url,dealership=dealership)
    
    return HttpResponse(reviews, content_type="application/json")
def ajaxNLU(request):
    
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/7b3b7dce-9511-4c59-bccc-66ff1889eb9b/v1/analyze?version=2022-04-07"
    api_key="ampj5lWzMj_lRpFD4MwvcQtHJbDtrxYh1pFD_y3_A_hW"
    myobj = {
 "features": {
    "entities": {
      "emotion": True,
      "sentiment": True,
      "limit": 2
    },
    "keywords": {
      "emotion": True,
      "sentiment": True,
      "limit": 2
    }
  }
}
    text=request.GET.get('review')
    reviewid=request.GET.get('reviewid')

    myobj['text']=text
    

    if text  is None:
        reviewsSentiment={'error':'Not a valid review'}
    else:
        reviewsSentiment = post_request(url,params=myobj, api_key=api_key)
    reviewsSentiment['reviewid']=reviewid

    
    return HttpResponse(json.dumps(reviewsSentiment), content_type="application/json")

def ajaxDealerCars(request):
        name=request.GET.get('name')
        address=request.GET.get('address')
        city=request.GET.get('city')
        state=request.GET.get('state')
        zip=request.GET.get('zip')
        skip=request.GET.get('skip')

        
        return HttpResponse(json.dumps(dealers), content_type="application/json")
def addReview(request):
    if request.user.is_authenticated:
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/TemporaryTest_TemporaryTest/capstone/get_reviews"
        dealership=request.POST.get('dealership')
        name=request.POST.get('name') 
        review=request.POST.get('review')
        purchase=request.POST.get('purchase')
        purchase_date=request.POST.get('purchase_date')
        car_make=request.POST.get('car_make')
        car_model=request.POST.get('car_model')
        car_year=request.POST.get('car_year')

        if (review is None) or (review==''):
            myres={'message':'Error: Not a valid review'}
        elif (dealership is None):
            myres={'message':'Error: Not a valid dealership'}
        else:
            try:
                result = post_request(url,
                        dealership=dealership,
                        name=name,
                        review=review,
                        purchase=purchase,
                        purchase_date=purchase_date,
                        car_make=car_make,
                        car_model=car_model,
                        car_year=car_year)
                myres={'message':'Submitted Succesfully!'}
            except:
                myres={'message':'Error: submition failed.'}
    else:
        myres={'message':'User is not Authorized'}
    
    return HttpResponse(json.dumps(myres), content_type="application/json")
