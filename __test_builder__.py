# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from pathlib import Path
from glob import glob
from shutil import rmtree

from psqlutil.conn_info import ConnectingInfromation
from psqlutil.db_builder import DataBaseBuilder


def init():
    cd = str(Path.cwd() / "**/__pycache__")
    dirpaths = [Path(d) for d in glob(cd, recursive=True)]
    for d in dirpaths:
        if d.is_dir(): rmtree(d)
        print("Delete !!",d)

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
    
    builder.create_schema()
    builder.create_parent_table()
    builder.create_child_table()
    builder.create_role()
    builder.insert_ini_data()
    
    
    init()
    


    
    
    
    
    
    