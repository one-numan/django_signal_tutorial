from django.dispatch import receiver,Signal
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.core.exceptions  import PermissionDenied

# Local Modules
from .models import Car
from loguru import logger


logger.add("signal.log")


####  In Built Signals  #
# Pre_save Dispatch
@receiver(pre_save,sender=Car)
def signal_new_car_add(sender,instance,**kwargs):
    # This Is Execute Before adding a New Car
    print("Signals : New Car Added")
    print(F"Signals : Sender : {sender} \n Instance : {instance}")


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    # This is Execute After adding a New Car and Also showing the all cars
    if created:
        logger.info(f"New car added: {instance.car_name}")
        # logger.warning("Here is an Error")
        # logger.debug("Error Handle")
        # You can add more complex logic here, like logging, sending notifications, etc.
        # For example, to get all car names and print them:
        all_cars = Car.objects.all()
        print("Current Car Models:")
        for car in all_cars:
            print(f"- {car.car_name}")


@receiver(pre_delete,sender=Car)
def car_pre_delete(sender,instance,**kwargs):
    print(F"Sender : {sender}")
    print(F"Car : {instance.car_name} is try to delete")


@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance,**kwargs):
    print(kwargs)
    print(F"Car Deleted : {instance.car_name}")
    # Using PermissionDenied After Deletion Of Car, Its execute and RoleBack Applied 
    # In_Short : Car is Deleted but after Error Occurs its roleback and Deleted cars is back into the DB
    raise PermissionDenied("Cars cannot be deleted via signal.")



####  Custom Built Signals  #

notification = Signal() # Creating a Signals


@receiver(notification) # Defining a Signals
# Signal execute when Index_page() is run
def show_notification(sender,**kwargs):
    print("-------------")
    print("Notification")
    print(sender)
    print(F"{kwargs}")