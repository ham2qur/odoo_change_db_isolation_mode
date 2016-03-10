# odoo_change_db_isolation_mode
Custom odoo module to enable isolation level of postgresql db. 

This will enable you to set the custom isolation level in odoo configurations. 
        
        Just set this parameter to your odoo configuration file. 
        db_isolation_level = n

        where n is the isolation level. 

Here are the isolation levels from the psycopg2:

"Isolation level values."

ISOLATION_LEVEL_AUTOCOMMIT          = 0

ISOLATION_LEVEL_READ_UNCOMMITTED    = 4

ISOLATION_LEVEL_READ_COMMITTED      = 1

ISOLATION_LEVEL_REPEATABLE_READ     = 2

ISOLATION_LEVEL_SERIALIZABLE        = 3



Context: 

I was getting an error "Operational error: could not use closed cursor" while performing an transaction. By diagonising it in deep found that this was causing 
due to the problem "could not serialize access due to concurrent update". Changing the default isolation level fixed my problem. 

Other resource: 
http://initd.org/psycopg/docs/extensions.html

https://github.com/odoo/odoo/issues/4257

http://stackoverflow.com/questions/29807033/postgresql-concurrent-transaction-issues
