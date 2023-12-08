# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:52:15 2023

@author: nanik
"""

from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.schema_creator import SchemaCreator
from psqlutil.table_creator import TableCreator
from psqlutil.role_creator import RoleCreator
from psqlutil.inserting_data import InsertingData

class DataBaseBuilder:
    __info: ConnectioinInfromation
    def __init__(self, info: ConnectioinInfromation):
        self.__info = info
        if not info.can_connect():
            raise Exception(f"接続できません。\n{info}")
        self.schema_creator = SchemaCreator(info)
        self.table_creator = TableCreator(info)
        self.role_creator = RoleCreator(info)
        self.inserting = InsertingData(info)
    
    def create_schema(self):
        self.schema_creator.set_schemas_from_csv().commit()

    def create_parent_table(self):
        self.table_creator.create_parent_from_csv()
        
    def create_child_table(self):
        self.table_creator.create_child_table_from_csv()

    def create_role(self):
        self.role_creator.set_querys_from_csv().commit()
        
    def insert_ini_data(self):
        self.inserting.set_insert_data_from_csv().commit()
        