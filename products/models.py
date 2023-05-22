from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	price = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True, )
	date_update = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if self.date is not None:
			self.date = self.date.replace(tzinfo=None)
		if self.date_update is not None:
			self.date_update = self.date_update.replace(tzinfo=None)
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.id} {self.name} {self.category} {self.price} {self.date}"