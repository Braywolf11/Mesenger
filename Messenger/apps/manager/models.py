from django.db import models
from ckeditor.fields import     RichTextField

# Create your models here.
class main(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status',default=True)
    create_date = models.DateField('Creation_date', auto_now=False , auto_now_add=True)
    modify_date = models.DateField('Modify_date', auto_now=True , auto_now_add=False )
    delete_date = models.DateField('Delete_date', auto_now=True , auto_now_add=False )

    class Meta:
        abstract = True

class category(main):
    name = models.CharField('Category name', max_length=100, unique=True)
    image = models.ImageField('Category image', upload_to='category/')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    def __str__(self):
        return self.name

class author(main):
    first_name = models.CharField('First name ', max_length=100)
    last_name = models.CharField('Last name ', max_length=100)
    email = models.EmailField('E-mail', max_length=50)
    description = models.TextField('Descripcion')
    image = models.ImageField('Author image', null= True, blank=True, upload_to='authors/')
    facebook = models.URLField('Facebook',null= True, blank=True)
    twitter = models.URLField('Twitter',null= True, blank=True)
    instagram = models.URLField('Instagram',null= True, blank=True)
    web = models.URLField('Webpage',null= True, blank=True)
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return '{0}{1}'.format(self.first_name,self.last_name)

class post(main):
    title = models.CharField('Title', max_length=100, unique=True)
    tslug = models.CharField('Slug', max_length=100, unique=True)
    description = models.TextField('Descripcion')
    id_author = models.ForeignKey(author, on_delete=models.CASCADE)
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField('Image post', upload_to='images/', max_length=150)
    published = models.BooleanField('Published / No Published', default=False)
    published_date = models.DateField('Published date')
    content = RichTextField()
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.title   

