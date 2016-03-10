# -*- coding: utf-8 -*-

from openerp.tools.config import config
from openerp.sql_db import Cursor

def db_autocommit(self, on):
    isolation_level = int(config.get("db_isolation_level"))
    self._cnx.set_isolation_level(isolation_level)
    
Cursor.autocommit = db_autocommit