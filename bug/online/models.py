from django.db import models


class TblBugList(models.Model):
    updatetime = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=1)
    describe = models.TextField(max_length=100)
    experience = models.TextField(max_length=30)
    belong = models.CharField(max_length=30)

    def __unicode__(self):
        return self.belong
