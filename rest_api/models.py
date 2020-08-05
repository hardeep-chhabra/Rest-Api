from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Project(models.Model):
	project_name = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	created_by = models.ManyToManyField(User)

	def __str__(self):
		return self.project_name


class Client(models.Model):
	client_name = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE)
	projects = models.ManyToManyField(Project)

	def __str__(self):
		return self.client_name