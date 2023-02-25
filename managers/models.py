from django.db import models

# Create your models here.
class nameManager(models.Model):
    name=models.CharField(max_length=64,help_text='Introduce el nombre del director')

    def __str__(self):
        return self.name


class genere(models.Model):
    genereName=models.CharField(max_length=64,help_text='Introduce el genero de la pelicula')

class summary(models.Model):
    summaryResume=models.TextField(max_length=300,help_text='Introduce un resumen de la pelicula')



class movieTitle(models.Model):
    movieName=models.CharField(max_length=64,help_text='Introduce el titulo de la pelicula')
    nameManager=models.ForeignKey(nameManager, on_delete=models.SET_NULL, null=True)
    summary=models.ForeignKey(summary, on_delete=models.SET_NULL, null=True)
    genere=models.ManyToManyField(genere)

    def __str__(self):
        return self.movieName