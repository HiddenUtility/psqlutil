# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from psqlutil.dummiy_dictionary import DummiyDictionary

from psqlutil.conn_info import ConnectingInfromation
from psqlutil.db_builder import DataBaseBuilder
from psqlutil.schema_creator import SchemaCreator
from psqlutil.table_creator import TableCreator
from psqlutil.reader import Reader
from psqlutil.writer import Writer
from psqlutil.role_creator import RoleCreator
from psqlutil.authority_giver import AuthorityGiver
from psqlutil.remover import Remover





if __name__ == "__main__":
    """
    \c postgres
    pqsl -U postgres
    DROP DATABASE test;
    CREATE DATABASE test;
    DROP OWNED BY Taro CASCADE;
    DROP ROLE Taro;
    
    """
    info = ConnectingInfromation(database="test",password="password")
    builder = DataBaseBuilder(info)
    
    #builder.create_schema()
    #builder.create_parent_table()
    builder.create_child_table()
    #builder.create_role()
    


    
    
    
    
    
    