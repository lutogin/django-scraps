from django.db import models


class Technology(models.Model):
    """Model of technology"""
    name = models.CharField(verbose_name='Name of technology', max_length=255)
    link_name = models.CharField(verbose_name='Link name of technology(JavaScript=js)', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Technologis'
        verbose_name = 'Technology'


class Content(models.Model):
    """Model content for post"""
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology')
    title = models.CharField(verbose_name='Title', max_length=255)
    content = models.TextField(verbose_name='Content', default='<pre><code class="language-php"></code></pre>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Contents'
        verbose_name = 'Content'
