from django.db import models

class Bd(models.Model):
    fact=models.CharField(max_length=50, verbose_name='Fact')
    content=models.TextField(null=True, blank=True, verbose_name='Description')
    level=models.FloatField(null=True, blank=True, verbose_name='Level')
    published=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publicate')
    rubric=models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')
    class Meta:
        verbose_name_plural='Facts'
        verbose_name='Fact'
        ordering=['-level']

class Rubric(models.Model):
    name=models.CharField(max_length=20, db_index=True, verbose_name='Rubric')
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural='Rubrics'
        verbose_name='Rubric'
        ordering=['name']
