from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_name(self):
    if self.first_name:
        user_name = '{} {}.'.format(self.last_name, self.first_name[:1])
    else:
        user_name = self.username
    return user_name


User.add_to_class("__str__", get_user_name)


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
            address.append(f'г.{self.city}')
        if self.street != '':
            address.append(f'{self.street}')
        if self.house != '':
            address.append(f'д.{self.house}')
        if self.entrance != '':
            address.append(f'п.{self.entrance}')
        if self.floor != '':
            address.append(f'эт.{self.floor}')
        if self.apartment != '':
            address.append(f'кв.{self.apartment}')
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


class Owner(models.Model):
    owner_name = models.CharField(max_length=20, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Владелец'

    def __str__(self):
        return self.owner_name


class Elevator(models.Model):
    serial_number = models.CharField(max_length=10, verbose_name='Заводской номер', blank=True)
    reg_number = models.CharField(max_length=10,
                                     verbose_name='Регистрационный номер', blank=True)
    capacity = models.IntegerField(verbose_name='Грузоподъемность', blank=True, null=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адрес'
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        null=True,
        blank=True,
    )
    note = models.CharField(max_length=50, verbose_name='Примечание', blank=True)

    def __str__(self):
        return f'{self.address} {self.note}'

    # def unique_error_message(self, model_class, unique_check):
    #     if model_class == type(self) and unique_check == ('address', 'note'):
    #         return 'Лифт с таким адресом уже существует'
    #     else:
    #         return super().unique_error_message(model_class, unique_check)

    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифты'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'address',
                    'note',
                ],
                name='unique_elevator')
        ]


class Claim(models.Model):
    claim_text = models.CharField(max_length=300, verbose_name='Заявка')
    pub_date = models.DateTimeField(verbose_name='Дата заявки', default=timezone.now)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адрес',
        null=True,
        blank=True,
    )
    elevator = models.ForeignKey(
        Elevator,
        on_delete=models.CASCADE,
        verbose_name='Лифт',
        related_name='claims_elevator',
        null=True,
        blank=True,
    )
    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
        related_name='claims_worker',
        null=True,
        blank=True,
        default=None,
    )
    fix_date_time = models.DateTimeField(verbose_name='Дата выполнения', blank=True, null=True)
    report_text = models.CharField(max_length=300, verbose_name='Отчёт', blank=True, )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Диспетчер',
        related_name="claims_author",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.claim_text


REGIONS = (
    ('region1', '1 участок'),
    ('region2', '2 участок'),
)


class Task(models.Model):

    task_text = models.CharField(
        max_length=300,
        verbose_name='Замечание',
        blank=True,
    )
    pub_date = models.DateField(
        verbose_name='Дата замечания',
        default=timezone.now,
        blank=True,
    )
    region = models.CharField(
        max_length=7,
        choices=REGIONS,
        verbose_name='Участок',
        blank=True,
        null=True
    )
    elevator = models.ForeignKey(
        Elevator,
        on_delete=models.CASCADE,
        verbose_name='Лифт',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='tasks_author',
        null=True,
        blank=True,
    )
    order_date = models.DateField(
        verbose_name='Дата выдачи задания',
        blank=True,
        null=True
    )
    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
        related_name='tasks_worker',
        null=True,
        blank=True,
        default=None,
    )
    fix_date = models.DateField(
        verbose_name='Дата выполнения',
        blank=True,
        null=True
    )
    report_text = models.CharField(
        max_length=300,
        verbose_name='Отчёт',
        blank=True
    )
    fixed = models.BooleanField(
        default=False,
        verbose_name='Отметка о выполнении',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.task_text

    def get_absolute_url(self):
        return reverse('logger:task-update', kwargs={'id': self.id})
