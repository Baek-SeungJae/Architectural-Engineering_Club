from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	student_no = models.CharField(max_length=10, blank =False)
	permission = models.CharField(max_length=10, default='일반')
	""" 
	image = ProcessedImageField (
			blank = True,
    		upload_to = profile_image_path,
		 	processors = [ResizeToFill(300, 300)],
			format = 'JPEG',
			options = {'quality':90},
			)
	"""
	def __unicode__(self):
		return self.student_no+ " " + self.user.username

	def __str__(self):
		return self.student_no+ " " + self.user.username