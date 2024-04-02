select foi_pago, dt_, sum(valor) valor
from pagamentos
group by foi_pago
having foi_pago = t

union all

select foi_pago, sum(valor) valor
from pagamentos
group by foi_pago
having foi_pago = f

