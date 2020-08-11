from django.db import models
from django.urls import reverse
from django.urls import reverse_lazy


class Album(models.Model):
	artist=models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	year=models.CharField(max_length=100)
	album_logo=models.FileField()
	is_fav = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.album_title + ' -'+ self.artist

class Song(models.Model):
	album = models.ForeignKey(Album , on_delete=models.CASCADE)
	song_title=models.CharField(max_length=250)
	audio_file=models.FileField(default='')
	file_type = models.CharField(max_length = 10)
	is_fav = models.BooleanField(default=False)


	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.album.id})
	
	def __str__(self):
		return self.song_title

	