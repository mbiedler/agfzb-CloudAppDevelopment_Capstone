from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
   path(route='', view=views.get_dealerships, name='index'),
    # path for about view
    path(route='about', view=views.about, name='about'),

    # path for contact us view
    path(route='contact', view=views.contact, name='contact'),

    # path for registration
    path(route='registration_request', view=views.registration_request, name='registration_request'),
    # path for login
    path(route='login', view=views.login_request, name='login'),


    # path for logout

    path(route='logout', view=views.logout_request, name='logout'),

    path(route='ajaxDealerships', view=views.ajaxDealerships, name='ajaxDealerships'),
    path(route='ajaxReviews', view=views.ajaxReviews, name='ajaxReviews'),
    path(route='ajaxNLU', view=views.ajaxNLU, name='ajaxNLU'),
    path(route='ajaxDealerCars', view=views.ajaxDealerCars, name='ajaxDealerCars'),
    # path for dealer reviews view
    path(route='get_dealer_details', view=views.get_dealer_details, name='get_dealer_details'),

    # path for add a review view
    path(route='addReview', view=views.addReview, name='addReview')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
