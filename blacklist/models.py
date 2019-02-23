from django.db import models

# Create your models here.
class blacklist(models.Model):
	user = models.CharField(max_length=20, blank=True, null=True, default='0')
	edit = models.IntegerField(blank=True, null=True, default=0)
	blacklist_size = models.IntegerField(blank=True, null=True, default=0)
	pub_date = models.DateTimeField(blank=True, null=True, default=0)

	def __str__(self):
		return str(self.pub_date)