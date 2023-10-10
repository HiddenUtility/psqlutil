# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:48:33 2023

@author: iwill
"""

from __future__ import annotations
from psqlutil.creator import Creator
import pandas as pd
from pathlib import Path

class RoleCreator(Creator):
    DIRNAME_TABLE = "psqlutil/roles"
    #//Field
    querys: list[str]
    
    USER_NAME = "user_name"
    PASSWORD = "password"
    CONNECTION = "connection_limit"

    def __get_role_create_query(self,
                               table_name:str,
                               df: pd.DataFrame) -> list[str]:
        querys =[]
        for _, row in df.iterrows():
            user_name = row[self.USER_NAME]
            password = row[self.PASSWORD]
            connection_limit = row[self.CONNECTION]
            querys.append(self.__get_query(user_name,password,connection_limit))



        return querys
    
    def __get_querys_from_csv(self) -> list[str]:
        filepath:Path = Path(self.DIRNAME_TABLE) / "roles.csv"
        try:
            df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem
        return self.__get_role_create_query(table_name, df)
    
    def __get_query(self, user_name: str, password: str, connection_limit=16) -> str:
        query = f"""
            
                DO $$
                BEGIN
                  IF NOT EXISTS (SELECT * FROM pg_user WHERE usename = '{user_name}') THEN
                    CREATE ROLE {user_name} LOGIN PASSWORD '{password}' CONNECTION LIMIT {connection_limit};
                  END IF;
                END $$;
                """
        return query
        
    def set_query(self, user_name: str, password: str, connection_limit=16) -> RoleCreator:
        query = self._get_query(user_name, password, connection_limit)
        return self._return(query)
    
    def set_querys_from_csv(self) -> RoleCreator:
        querys = self.__get_querys_from_csv()
        return self._return(*querys)
        