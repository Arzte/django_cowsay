from django.db import models

"""

CowsayText:
    - text (uncowsayified text)

"""


class CowsayText(models.Model):
    text = models.TextField()
