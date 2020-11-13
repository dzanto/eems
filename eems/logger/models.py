from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=10, blank=True, verbose_name='Дом')
    entrance = models.CharField(max_length=2, blank=True, verbose_name='Подъезд')
    floor = models.CharField(max_length=10, blank=True, verbose_name='Этаж')
    apartment = models.CharField(max_length=20, blank=True, verbose_name='Квартира')

    def __str__(self):
        address = []
        if self.city != '':
            address.append(f'г. {self.city}')
        if self.street != '':
            address.append(f'ул. {self.street}')
        if self.house != '':
            address.append(f'д. {self.house}')
        if self.entrance != '':
            address.append(f'п. {self.entrance}')
        if self.floor != '':
            address.append(f'эт. {self.floor}')
        if self.apartment != '':
            address.append(f'кв. {self.apartment}')
        return ', '.join(address)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'city',
                    'street',
                    'house',
                    'entrance',
                    'floor',
                    'apartment',
                ],
                name='unique_address')
        ]


class Claim(models.Model):
    claim_text = models.CharField(max_length=300, verbose_name='Заявка')
    pub_date = models.DateTimeField(verbose_name='Дата заявки')
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адрес'
    )

    def __str__(self):
        return self.claim_text
