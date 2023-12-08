# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:50:37 2023

@author: iwill
"""

from __future__ import annotations
from pathlib import Path
from psqlutil.editor import Editor
from psqlutil.connection_information import ConnectioinInfromation
from pandas import read_csv, DataFrame

class InsertingData(Editor):
    DIRPATH = "psqlutil/data"
    #//Field
    _info: ConnectioinInfromation
    querys: list[str] 

    def __get_query(self, table_name: str, datas: dict) -> str:
        columns_query = ", ".join(["%s" % key for key in datas])
        values_query = ", ".join([f"'{datas[key]}'" for key in datas])
        return f"insert into {table_name} ({columns_query}) values ({values_query});"
        
    def set_query(self,table_name: str, datas: dict)->InsertingData:

        insert_query = self.__get_query(table_name,datas)
        return self._return(insert_query)
    
    def __get_querys_from_csv(self, filepath: Path) -> str:
        try:
            df:DataFrame = read_csv(filepath, engine="python", encoding="cp932", dtype=str).fillna("")
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem

        return [self.__get_query(table_name, row.to_dict()) for _, row in df.iterrows()]

        
    def __get_filepahs_csv(self) -> list[Path]:
        return [f for f in Path(self.DIRPATH).glob("*.csv") if f.is_file()]
    
    def insert_data_from_csv(self):
        filepaths = self.__get_filepahs_csv()
        for f in filepaths:
            print(f"data inserting from {f.name}")
            querys = self.__get_querys_from_csv(f)
            Editor(self._info, querys).commit()
            
            
        
        