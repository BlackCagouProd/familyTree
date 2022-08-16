from django.db import models


class Personne(models.Model):

    Nom_de_famille = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    genre = models.CharField(max_length=1,
                              choices=(('H', 'Homme'), ('F', 'Femme')),
                              blank=False,
                              default=None)
    dateDeNaissance = models.ForeignKey('Event',
                                        models.SET_NULL,
                                        null=True,
                                        blank=True,
                                        related_name='+')
    dateDeDeces = models.ForeignKey('Event',
                                    models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name='+')
    deceder = models.BooleanField(default=True)
    mere = models.ForeignKey('self',
                               models.SET_NULL,
                               blank=True,
                               null=True,
                               limit_choices_to={'genre': 'F'},
                               related_name='enfants_de_la_mere')
    pere = models.ForeignKey('self',
                               models.SET_NULL,
                               blank=True,
                               null=True,
                               limit_choices_to={'genre': 'H'},
                               related_name='enfants_du_pere')

    pub_date = models.DateTimeField('date de publication')
