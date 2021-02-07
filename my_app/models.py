from django.db import models

# Create your models here.
class Search(models.Model):
    search  = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # return string rather than 'Search object'
    def __str__(self):
        return '{}'.format(self.search)

    # change 'Searchs' to 'Searches' (proper plural form)
    class Meta:
        verbose_name_plural = 'Searches'