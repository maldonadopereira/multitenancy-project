from core.models import Tenant, Domain

new_tenant = Tenant(name='dave', schema_name='dave')
new_tenant.save()

new_domain = Domain(tenant=new_tenant, domain=f'{new_tenant.name}.davemaldonado.online', is_primary=True)
new_domain.save()
