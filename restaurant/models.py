from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        ordering = ("booking_date",)


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f"{self.title} : {str(self.price)}"

    def __str__(self):
        return self.get_item()

    class Meta:
        ordering = ("title",)
