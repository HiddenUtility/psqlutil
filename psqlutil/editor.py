# -*- coding: utf-8 -*-
from __future__ import annotations
from psqlutil.psql import Psql
from psqlutil.committing import Committing
from psqlutil.connection_information import ConnectioinInfromation


class Editor(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: Editor) -> Editor:
        if not isinstance(obj, Editor): raise TypeError()
        querys = obj.to_querys() + self.__querys()
        return Editor(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Editor:
        querys = querys + self.__querys()
        return Editor(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()
    
    def add_delete_duplicate(self,table_name, *columns: str) -> Editor:
        if len(columns) == 0:return self
        key = ", ".join([f"{column}" for column in columns])
        and_query = "WHERE "  + " AND ".join(["t2.{column} = t1.{column}" for column in columns])
        query = """
        DELETE FROM {0} t1
        WHERE EXISITS(
        SELECT {1}
        FROM {0} t2
        {2}
        AND t2.ctid > t1.ctid
        );
        """.format(table_name, key, and_query)
        return self.set_querys([query])
        