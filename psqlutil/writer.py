# -*- coding: utf-8 -*-
from __future__ import annotations

from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.psql import Psql
from psqlutil.committing import Committing

class Writer(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: Writer) -> Writer:
        if not isinstance(obj, Writer): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return Writer(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Writer:
        querys = querys + self.__querys
        return Writer(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()
        
    def set_query(self,table_name: str, datas: dict) -> Writer:
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        where_clause = "WHERE " + " AND ".join(conditions)
        delete_query = f"delete from {table_name} {where_clause}"
        columns_query = ", ".join(["%s" % key for key in datas])
        values_query = ", ".join([f"'{datas[key]}'" for key in datas])
        insert_query = f"insert into {table_name} ({columns_query}) values ({values_query});"

        return Writer(self.__info, self.__querys + [delete_query, insert_query])
