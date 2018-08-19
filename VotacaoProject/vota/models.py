from django.db import models

# User
# -----------------------
class User(models.Model):

  id = models.IntegerField(primary_key=True, verbose_name='usuario')
  name = models.CharField(max_length=150, verbose_name='nome')
  email = models.CharField(max_length=60,verbose_name='email')
  password = models.CharField(max_length=30, verbose_name='senha')  

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'usuario'
    verbose_name_plural = 'usuarios'

# Suggestion
# -----------------------------
class Suggestion(models.Model):

  id = models.IntegerField(primary_key=True, verbose_name='proposta')
  name = models.CharField(max_length=150, verbose_name='nome')
  description = models.TextField(verbose_name='descrição')
  result = models.CharField(max_length=150, verbose_name='resultado')


  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'proposta'
    verbose_name_plural = 'propostas'

# Comment
# --------------------------
class Comment(models.Model):
  
  user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, verbose_name='usuário')
  suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE, related_name='sugges', verbose_name='comentário')
  description = models.TextField(verbose_name='descrição')

  def __str__(self):
    return self.description
  
  class Meta:
    verbose_name = 'comentário'
    verbose_name_plural = 'comentários'


class Vote(models.Model):


  id = models.IntegerField(primary_key=True, verbose_name='identificacao')
  kind = models.CharField(max_length=150,verbose_name='tipo')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name_user', verbose_name='usuário')
  suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE, related_name='id_suggestion', verbose_name='comentário')
  
  def __str__(self):
    return 'lou'
    #return "%s - %s" % (self.id_user.name, self.id_suggestion.name)
  
  class Meta:
    verbose_name = 'votos'
    verbose_name_plural = 'votos'
