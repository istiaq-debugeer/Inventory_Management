from django.db import models

class stockStatus(models.IntegerChoices):
    IN_STOCK=0,"In stock"
    OUT_OF_STOCK= 1,"Out of stock"
    COMING_SOON=2,"Coming Soon"