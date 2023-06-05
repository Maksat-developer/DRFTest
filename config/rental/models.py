from django.db import models


# Модель друга
class Friend(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f" Друг {self.name}"


# Модель пренадлежащего
class Belonging(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f"Пренадлежит {self.name}"
    
class Newclient(models.Model):
    client = models.ForeignKey(Friend, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Клиент:{self.client} Новый клиент?{self.is_new}"

# Модель Займа
class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    client = models.ManyToManyField(Newclient)
    created_at = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Что:{self.what} Кому:{self.to_who}"
