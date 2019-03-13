from django.db import models

class Newsletter(models.Model):
        nome = models.CharField(max_length=256)
        email = models.EmailField(unique=True)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)

        class Meta:
                ordering = ['criado_em']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome

        def __str__(self):
            return self.nome + ' - ' + self.email