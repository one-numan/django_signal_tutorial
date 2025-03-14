from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.core.exceptions  import PermissionDenied

# Local Modules
from .models import Car
from loguru import logger


logger.add("signal.log")

# Pre_save Dispatch
@receiver(pre_save,sender=Car)
def signal_new_car_add(sender,instance,**kwargs):
    print("Signals : New Car Added")
    print(F"Signals : Sender : {sender} \n Instance : {instance}")


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
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


@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance,**kwargs):
    print(F"Car Deleted : {instance.car_name}")
    raise PermissionDenied("Cars cannot be deleted via signal.")