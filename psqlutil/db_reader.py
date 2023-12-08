# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:13:50 2023

@author: nanik
"""
from __future__ import annotations
from psqlutil.reader import Reader

from psqlutil.connection_information import ConnectioinInfromation
from pandas import DataFrame

class DataBaseReader(Reader):
    #//Field
    _info: ConnectioinInfromation
    querys: list[str] 
    
    def __get_query(self, table_name: str,
                  columns: list[str] = [],
                  wheres: dict[str:str] = {}
                  ) -> DataBaseReader:

        columns_query = self._get_column_query(columns)
        where = self._get_where_query(wheres)
        return f"SELECT {columns_query} FROM {table_name} {where};"

        
    def read(self,table_name: str,
            columns: list[str] = {},
            wheres: dict[str:str] = {},
            ) -> tuple[list[list[str]], list[str]]:
        """
        

        Parameters
        ----------
        table_name : str
            Target Talbe name.
        columns : list[str], optional
            列名指定があれば指定する. The default is {}.
        wheres : dict[str:str], optional
            検索したい値を辞書で指定する.. The default is {}.
         : TYPE
            DESCRIPTION.

        Returns
        -------
        (tuple[list[list[str]], list[str]])
            DESCRIPTION.

        """
        query = self.__get_query(table_name, wheres=wheres, columns=columns)
        rows,columns = Reader(self._info).set_free_query(query).read()
        
        return rows,columns
    
    def get_df(self, table_name: str,
               columns: list[str] = {},
               wheres: dict[str:str] = {},
               ) -> DataFrame:
        """
        

        Parameters
        ----------
        table_name : str
            Target Talbe name.
        columns : list[str], optional
            列名指定があれば指定する. The default is {}.
        wheres : dict[str:str], optional
            検索したい値を辞書で指定する.. The default is {}.
         : TYPE
            DESCRIPTION.

        Returns
        -------
        DataFrame
            DESCRIPTION.

        """
        rows,columns = self.read(table_name, wheres=wheres, columns=columns)
        if len(rows) == 0:return DataFrame()
        return DataFrame(rows, columns=columns)