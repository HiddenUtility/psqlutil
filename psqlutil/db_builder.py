# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:52:15 2023

@author: nanik
"""

from psqlutil.conn_info import ConnectingInfromation
from psqlutil.schema_creator import SchemaCreator
from psqlutil.table_creator import TableCreator
from psqlutil.role_creator import RoleCreator

class DataBaseBuilder:
    def __init__(self, info: ConnectingInfromation):
        self.info = info
        if not info.can_connect():
            raise Exception(f"接続できません。\n{info}")
        self.schema_creator = SchemaCreator(info)
        self.table_ceator = TableCreator(info)
        self.role_ceator = RoleCreator(info)
    
    def create_schema(self):
        self.schema_creator.set_schemas_from_csv().commit()

    def create_table(self):
        self.table_ceator.set_querys_from_csv().commit()

    def create_role(self):
        self.table_ceator.set_querys_from_csv().commit()