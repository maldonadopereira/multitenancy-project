from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    payment_option = models.CharField(max_length=50, choices=[('monthly', 'Monthly'), ('annual', 'Annual')],
                                      default='monthly')


class Domain(DomainMixin):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)
