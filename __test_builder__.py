# -*- coding: utf-8 -*-
from psqlutil import ConnectioinInfromation
from psqlutil import DataBaseBuilder

if __name__ == "__main__":
    """
    \c postgres
    pqsl -U postgres
    DROP DATABASE test;
    CREATE DATABASE test;
    DROP OWNED BY Taro CASCADE;
    DROP ROLE Taro;
    """
    info = ConnectioinInfromation(database="test", password="password")
    builder = DataBaseBuilder(info)
    
    builder.create_schema()
    builder.create_parent_table()
    builder.create_child_table()
    builder.create_role()
    builder.insert_ini_data()
    