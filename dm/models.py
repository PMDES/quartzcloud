from django.db import models
from message.models import Message
from django.contrib.auth.models import User


class DM(models.Model):
    name = models.CharField(default="", max_length=50)
    messages = models.ManyToManyField(Message, related_name='dm_messages')
    id = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_1',
                               default=None)
    user_2 = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_2',
                               default=None)

    # admin_perm_write = models.BooleanField(default = True)

    def __str__(self):
        return self.name
