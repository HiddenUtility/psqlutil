# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
from typing import Final
from pathlib import Path

from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.psql import Psql
from psqlutil.committing import Committing

class SchemaCreator(Psql):
    DIRNAME_TABLE: Final = "psqlutil/parent_table"
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: SchemaCreator) -> SchemaCreator:
        if not isinstance(obj, SchemaCreator): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return SchemaCreator(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> SchemaCreator:
        querys = self.__querys + querys
        return SchemaCreator(self.__info , querys)
    
    # @override
    def set_query(self,query :str) -> SchemaCreator:
        querys = self.__querys + [query]
        return SchemaCreator(self.__info , querys)

    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()

    def __get_querys_from_csv(self) -> list[str]:
        filenames = [f.stem for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        schema_names = []
        for filename in filenames:
            strs = filename.split(".")
            if len(strs) == 1: str_ = "public"
            elif len(strs) == 2: str_ = strs[0]
            else: continue
            if str_ not in schema_names: schema_names.append(str_)
        return [self.__get_query(s) for s in schema_names]

    def __get_query(self,schema_name: str) -> str:
        return f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        
    def set_schemas(self,schema_name: str) -> SchemaCreator:
        query = self.__get_query(schema_name)
        return SchemaCreator(self.__info, self.__querys + [query])
    
    def set_schemas_from_csv(self) -> SchemaCreator:
        querys = self.__get_querys_from_csv()
        return SchemaCreator(self.__info, self.__querys + querys)