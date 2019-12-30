from django.db import models
import datetime
from django.utils.translation import gettext as _

# Create your models here.
class NodeMQTT(models.Model):
    device = models.CharField(max_length=120)

    topicName = models.CharField(max_length=120, unique = True)

    last_msg = models.CharField(max_length=120)
    lastUpdated = models.DateField(_("Date"), default=datetime.date.today)

    createdDate = models.DateField(_("Date"), default=datetime.date.today)
    
