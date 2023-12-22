from __future__ import annotations
import pandas as pd
from pathlib import Path

from psqlutil.psql import Psql
from psqlutil.committing import Committing
from psqlutil.connection_information import ConnectioinInfromation

class RoleCreator(Psql):
    DIRNAME_TABLE = "psqlutil/roles"
    USER_NAME = "user_name"
    PASSWORD = "password"
    CONNECTION = "connection_limit"

    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: RoleCreator) -> RoleCreator:
        if not isinstance(obj, RoleCreator): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return RoleCreator(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> RoleCreator:
        querys = querys + self.__querys
        return RoleCreator(self.__info , querys)
    
    # @override
    def set_query(self,query :str) -> RoleCreator:
        querys = self.__querys + [query]
        return RoleCreator(self.__info , querys)

    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()

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
    
    def __get_querys_from_csv(self) -> list[str]:
        filepath:Path = Path(self.DIRNAME_TABLE) / "roles.csv"
        try:
            df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem
        return self.__get_role_create_query(table_name, df)
    
    def set_querys_from_csv(self) -> RoleCreator:
        querys = self.__get_querys_from_csv()
        return RoleCreator(self.__info, self.__querys + querys)
        