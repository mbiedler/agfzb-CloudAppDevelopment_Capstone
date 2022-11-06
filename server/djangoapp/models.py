from django.db import models
import datetime

from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=30, default="title",unique=True)
    description = models.CharField(max_length=200, default="title")

    content = models.TextField()
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
    
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    PICKUP_TRUCK = 'pickup_truck'
    COUPE = 'coupe'
    CONVERTIBLE = 'convertible'
    
    CARTYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (PICKUP_TRUCK, 'Pickup Truck'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE,'Convertible')
    ]
    # Occupation Char field with defined enumeration choices
    cartype = models.CharField(
        null=False,
        max_length=20,
        choices=CARTYPE_CHOICES,
        default=SEDAN
    )

    
    name = models.CharField(max_length=20, default="title")
    description = models.CharField(max_length=200, default="title")
    carmake = models.ForeignKey(CarMake, to_field='name', null=True, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    # Create a toString method for object string representation
    def __str__(self):
        return "Car model name: " + self.name




# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, car_year, car_model, car_make, id, sentiment, purchase_date, review, purchase, name, dealership):
        # Review Car Year
        self.car_year = car_year
        # Review Car Model
        self.car_model= car_model
        # Review Car Mak
        self.car_make= car_make
        # Dealer id
        self.id = id
        # Sentiment
        self.sentiment = sentiment
        # purchase_date
        self.purchase_date = purchase_date
        # Review text
        self.review = review
        # Purchase yes/no
        self.purchase = purchase
        # Reviewer Name
        self.name= name
        #Dealership id
        self.dealership=dealership

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name