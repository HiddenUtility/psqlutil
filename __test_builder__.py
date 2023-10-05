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
    
    builder.create_schema()
    builder.create_table()
    builder.create_role()
    
    
    import sys
    sys.exit()

    
    #// Create table
    tableCreator = TableCreator(ConnectingInfromation)
    tableCreator = tableCreator.set_querys_from_csv()\
        .set_query("ConnectingInfromation_info.administrator", ["id"], ["text"], ["f"*32])
    print(tableCreator)
    tableCreator.commit()
    
    #// ロール作成
    roleCreator = RoleCreator(ConnectingInfromation)
    roleCreator = roleCreator.set_query("taro", "password")
    #// 権限付与
    authorityGiver = AuthorityGiver(ConnectingInfromation)
    authorityGiver = authorityGiver.set_query_to_edit("Taro", "ConnectingInfromation_info")
    #//足せる
    creator = roleCreator + authorityGiver
    print(creator)
    creator.commit()
    
    #太郎で操作する
    ConnectingInfromationTaro = ConnectingInfromation(database="test",ConnectingInfromationname="taro",password="password")
    print(ConnectingInfromationTaro)
    
    #//wirter
    writer = Writer(ConnectingInfromationTaro)
    for i in range(10):
        datas = DummiyDictionary.random_dict()
        writer = writer.set_query("ConnectingInfromation_info.ConnectingInfromation_info", datas)
    print(writer)
    writer.commit()
    
    #//reader
    reader = Reader(ConnectingInfromationTaro)
    reader = reader.set_query("ConnectingInfromation_info.ConnectingInfromation_info",datas)
    rows,columns = reader.read()
    #Table全データ
    df = reader.getDataFrame("ConnectingInfromation_info.ConnectingInfromation_info")
    
    #最後消す
    #//remover
    remover = Remover(ConnectingInfromationTaro).set_query_table_all_data("ConnectingInfromation_info.ConnectingInfromation_info")
    print(remover)
    remover.commit()
    
    
    
    """
    \c test
    \dn
    \dt ConnectingInfromation_info.*
    \du
    
    Dummiyを消す。
    select * from ConnectingInfromation_info.ConnectingInfromation_info;
    DELETE FROM ConnectingInfromation_info.ConnectingInfromation_info;
    """

    
    
    
    
    
    