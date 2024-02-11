from core.models import Tenant
from core.models import Domain

new_tenant = Tenant(name='teste', schema_name='teste')
new_tenant.save()

new_domain = Domain(tenant=new_tenant, domain=f'{new_tenant.name}.localhost', is_primary=True)
new_domain.save()
