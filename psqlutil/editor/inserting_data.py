# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
from pandas import read_csv, DataFrame

from psqlutil.connection_information import ConnectioinInfromation
from psqlutil.psql import Psql
from psqlutil.committing import Committing
from querycreator import InsertIntoQureryCreator

class InsertingData(Psql):
    DIRPATH = "psqlutil/data"
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: InsertingData) -> InsertingData:
        if not isinstance(obj, InsertingData): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return InsertingData(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> InsertingData:
        querys = querys + self.__querys
        return InsertingData(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys
    
    # @override
    def set_query(self,query :str) -> InsertingData:
        querys = self.__querys + [query]
        return InsertingData(self.__info , querys)

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()

    def __get_query(self, table_name: str, row: dict):
        return InsertIntoQureryCreator(table_name, row).get_query()

    def __get_querys_from_csv(self, filepath: Path) -> str:
        try:
            df:DataFrame = read_csv(filepath, engine="python", encoding="cp932", dtype=str).fillna("")
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem
        return [self.__get_query(table_name, row.to_dict()) for _, row in df.iterrows()]

    def __get_filepahs_csv(self) -> list[Path]:
        return [f for f in Path(self.DIRPATH).glob("*.csv") if f.is_file()]
    
    def set_insert_data_from_csv(self) -> InsertingData:
        filepaths = self.__get_filepahs_csv()
        for f in filepaths:
            print(f"data inserting from {f.name}")
            querys = self.__get_querys_from_csv(f)
        return InsertingData(self.__info, self.__querys + querys)
            