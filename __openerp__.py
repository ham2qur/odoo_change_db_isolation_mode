# -*- coding: utf-8 -*-
##############################################################################
#    Dated 10/March/2016
##############################################################################
{
    "name": "Odoo custom postgresql isolation level",
    'category': 'system',
    "version": "1.0",
    'author' : "ham2qur@yahoo.com",
    "description": """
        Enable you to set custom isolation level in odoo configurations. 
        
        Just set this parameter to your odoo configuration file. 
        db_isolation_level = n

        where n is the isolation level. 
        
        "Isolation level values."
        ISOLATION_LEVEL_AUTOCOMMIT          = 0
        ISOLATION_LEVEL_READ_UNCOMMITTED    = 4
        ISOLATION_LEVEL_READ_COMMITTED      = 1
        ISOLATION_LEVEL_REPEATABLE_READ     = 2
        ISOLATION_LEVEL_SERIALIZABLE        = 3
        
        """,
    'author': 'Hammadhq',
    'website': 'http://www.github.com/',
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
