# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Model']
__metaclass__ = PoolMeta


class Model:
    __name__ = 'ir.model'

    @classmethod
    def __register__(cls, module_name):
        super(Model, cls).__register__(module_name)
        models = cls.search([('model', 'in', ['sale.opportunity'])])
        if models:
            cls.write(models, {
                    'babi_enabled': True
                    })
