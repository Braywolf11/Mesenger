from django.db import models

# Create your models here.
class main(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status',default=True)
    create_date = models.DateField('Creation_date', auto_now=False , auto_now_add=True)
    modify_date = models.DateField('Modify_date', auto_now=True , auto_now_add=False )
    delete_date = models.DateField('Delete_date', auto_now=True , auto_now_add=False )