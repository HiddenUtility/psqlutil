# -*- coding: utf-8 -*-
from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.creator.schema_creator import SchemaCreator
from psqlutil.creator.table_creator import TableCreator
from psqlutil.creator.role_creator import RoleCreator
from psqlutil.editor.inserting_data import InsertingData

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
        self.table_creator.set_parent_from_csv().commit()
        
    def create_child_table(self):
        self.table_creator.set_child_table_from_csv().commit()

    def create_role(self):
        self.role_creator.set_querys_from_csv().commit()
        
    def insert_ini_data(self):
        self.inserting.set_insert_data_from_csv().commit()
        