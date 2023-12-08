# -*- coding: utf-8 -*-
from __future__ import annotations

from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.psql import Psql
from psqlutil.committing import Committing

class Updater(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: Updater) -> Updater:
        if not isinstance(obj, Updater): raise TypeError()
        querys = obj.to_querys() + self.__querys()
        return Updater(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Updater:
        querys = querys + self.__querys()
        return Updater(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()
        
    def set_query(self,table_name: str, datas: dict[str:str], main_keys:list[str])->Updater:
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        main_keys = [f"{key} = {datas[key]}" for key in main_keys]
        where_clause = " AND ".join(main_keys)
        query = f"update {table_name} set {conditions} where {where_clause};"
        return Updater(self.__info, self.__querys + [query])
    