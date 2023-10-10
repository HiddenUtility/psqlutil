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
        self.table_creator = TableCreator(info)
        self.role_creator = RoleCreator(info)
    
    def create_schema(self):
        self.schema_creator.set_schemas_from_csv().commit()

    def create_parent_table(self):
        self.table_creator.create_parent_from_csv()
        
    def create_child_table(self):
        self.table_creator.create_child_table_from_csv()

    def create_role(self):
        self.role_creator.set_querys_from_csv().commit()