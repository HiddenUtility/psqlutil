# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:24:07 2023

@author: nanik
"""

from psqlutil.where_query_creator import WhereQureryCreator
from psqlutil.insert_valus_query_creator import InsertValuesQureryCreator
from psqlutil.set_valus_query_creator import SetValuesQureryCreator

from psqlutil.select_query_creator import SelectQureryCreator
from psqlutil.delete_query_creator import DeleteQureryCreator
from psqlutil.update_query_creator import UpdateQureryCreator
from psqlutil.insert_into_query_creator import InsertIntoQureryCreator

def test_sub_class():
    where: dict = dict(id=1234, name="takeshi")
    creator = WhereQureryCreator(where)
    
    print(creator)
    
    data: dict = dict(id=1234, name="takeshi")
    creator = InsertValuesQureryCreator(data)
    
    print(creator)
    
    data: dict = dict(id=1234, name="takeshi")
    creator = SetValuesQureryCreator(data)
    
    print(creator)


if __name__ == "__main__":
    
    table_name = "table_name"
    
    columns = []
    where = dict(id="1234")
    value = dict(id="1234", name="花子")
    data = dict(id="1234", pai="3.14")
    
    creator = SelectQureryCreator(table_name).set_columns(columns).set_where(where)
    print(creator)
    
    creator = DeleteQureryCreator(table_name).set_where(where)
    print(creator)
    
    creator = UpdateQureryCreator(table_name).set_values(value).set_where(where)
    print(creator)
    
    creator = InsertIntoQureryCreator(table_name).set_data(data)
    print(creator)
