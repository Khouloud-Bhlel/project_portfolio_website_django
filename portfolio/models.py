from django.db import models

# model contact
class Contact(models.Model):  # Renommer la classe Contact
    name = models.CharField(max_length=25)
    email = models.EmailField()
    emailv = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name
# model service
class Service(models.Model):
    TYPE_CHOICES = [
        ('design', 'Design'),
        ('developpement', 'Développement'),
        ('consulting', 'Consulting'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    title = models.CharField(max_length=60, default="")
    description = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

class Projet(models.Model):
    libellee = models.CharField(max_length=100)
    descriptionn = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=True)
    progression = models.IntegerField()

    def __str__(self):
        return self.libellee

    def save(self, *args, **kwargs):
        if self.progression == 100:
            self.acheve = True
        else:
            self.acheve = False

        super().save(*args, **kwargs)



class Equipe(models.Model):
    Nom = models.CharField(max_length=100)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Nom

# model personnel
class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    fichier_cv = models.FileField(upload_to='cv/')
    fichier_photo = models.ImageField(upload_to='photos/')
    lien_linkedin = models.URLField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='personnels', default=None)

   
    def __str__(self):
        return f"{self.nom}"

