from django.db import models

# Create your models here.
class Division:
    def __init__(self, name, age, roster, hcoach, acoach):
        self.name = name
        self.age = age
        self.roster = roster
        self.hcoach = hcoach
        self.acoach = acoach

Divisions = [
  Division('23', '2012-2013', '14', 'Wiz Kalifa', 'Kid Cudi'),
]