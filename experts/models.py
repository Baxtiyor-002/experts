from django.db import models


# Create your models here.
class Structure(models.Model):
    name = models.CharField("Отдел", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class Sex(models.Model):
    name = models.CharField("Пол", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Sphere(models.Model):
    name = models.CharField("Сфера", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сфера"
        verbose_name_plural = "Сферы"


class Type(models.Model):
    name = models.CharField("Тип", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Experts(models.Model):
    fname = models.CharField("Фамилия", max_length=200)
    name = models.CharField("Имя", max_length=200)
    oname = models.CharField("Отчество", max_length=200)
    sex = models.ForeignKey(
        Sex,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        Country,
        verbose_name="Страна",
        on_delete=models.CASCADE
    )
    sphere = models.ForeignKey(
        Sphere,
        verbose_name="Сфера",
        on_delete=models.CASCADE
    )
    position = models.TextField("Должность")
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.CASCADE
    )
    structure = models.ForeignKey(
        Structure,
        verbose_name="Отдел",
        on_delete=models.CASCADE
    )
    description = models.TextField("Описание", blank=True)
    contact = models.CharField("Контакт", max_length=200, blank=True)
    contact_tel = models.CharField("Контакт телефон", max_length=200, blank=True)
    twitter = models.CharField("Твиттер", max_length=200, blank=True)
    email = models.CharField("Почта", max_length=200, blank=True)
    photo = models.ImageField("Изображения", upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"
