# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class meme(models.Model):
    meme_image= models.ImageField("https://scontent-ams3-1.xx.fbcdn.net/v/t1.0-9/29101767_1717204321680003_2332367017836806144_n.jpg?oh=0b715285a700bdade3a3041190015a4d&oe=5B434890")
    meme_no = models.IntegerField()
    field_1 = models.IntegerField()
    field_2 = models.IntegerField()
    field_3 = models.IntegerField()
    field_4 = models.IntegerField()
#    def __str__(self):
 #       return self.meme_no + 'with fields as  ' + self.field_1 + ' '+ self.field_2 + ' '+ self.field_3 + ' '+ self.field_4

