from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class OwnedModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Document(TimestampModel, OwnedModel):
    class Type(models.TextChoices):
        # KOODI_NIMI = ("TIETOKANTAAN TALLENNETTAVA", _("Kayttajalle nakyva"))
        BILL = ("BILL", _("Lasku"))
        RECEIPT = ("RECEIPT", _("Kuitti"))
        CALCULATION = ("CALCULATION", _("Laskelma"))
        OTHER = ("OTHER", _("Muu"))

    type = models.CharField(max_length=20, choices=Type.choices)
    name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to="docs/%Y-%M/")

    class Meta:
        verbose_name = _("dokumentti")
        verbose_name_plural = _("dokumentit")

    def __str__(self):
        return self.name if self.name else f"Document{self.id}"


class Category(TimestampModel, OwnedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="subcategorie",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("kategoria")
        verbose_name_plural = _("kategoriat")

    def __str__(self):
        prefix = f"{self.parent} / " if self.parent else ""
        return f"{prefix}{self.name}"


class Account(TimestampModel, OwnedModel):
    name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("tili")
        verbose_name_plural = _("tilit")

    def __str__(self):
        return f"{self.id:04d} {self.name}"


class Transaction(TimestampModel):
    class Type(models.TextChoices):
        INCOME = ("INCOME", _("Tulo"))
        EXPENSE = ("EXPENSE", _("Meno"))

    class State(models.TextChoices):
        UPCOMING = ("UPCOMING", _("Tuleva"))
        DONE = ("DONE", _("Tapahtunut"))

    account = models.ForeignKey(
        Account, on_delete=models.RESTRICT, verbose_name=_("tili")
    )
    type = models.CharField(max_length=20, choices=Type.choices)
    state = models.CharField(max_length=20, choices=State.choices)
    date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    documents = models.ManyToManyField(
        Document,
        related_name="transactions",
        blank=True,
    )

    class Meta:
        verbose_name = _("tilitapahtuma")
        verbose_name_plural = _("tilitapahtumat")

    def __str__(self):
        return f"{self.date} {self.account} {self.amount} ({self.state})"
