from django.db import models
# from bdrclib.auditlib import audittest
from auditlib.audittest import AuditTestType

# Create your models here.

class Item(models.Model):
    """
    Typically, a work
    """
    name = models.CharField('Work', max_length=80)

    # We're going to add this in a super class
    create_date = models.DateTimeField('Creation date')
    mod_date = models.DateTimeField('Last modification date')

    def __str__(self):
        return self.name


class Volume(models.Model):
    """
    A section of a work
    """
    name = models.CharField('Volume', max_length=80)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name}-{self.name}"

    @property
    def work(self):
        return self.item


class Contributor(models.Model):
    """
    Contributor to a submission
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Submittal(models.Model):
    """
    Assembles metadata for a work.
    """
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    work = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contributor.name} -> {self.work_id} "

class Test(models.Model):
    """
    Defines a test
    """

    # See https://docs.python.org/3/library/enum.html for casting enum into int
    user_name = models.CharField('Name', max_length=80)
    test_geometry = models.IntegerField('Test Geometry','geometry', default= AuditTestType.COMPLETE_TREE.value)

    def __str__(self):
        return self.user_name


