# -*- coding: utf-8 -*-
from __future__ import annotations
from psqlutil.psql import Psql
from psqlutil.committing import Committing
from psqlutil.connection_information import ConnectioinInfromation

class AuthorityGiver(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: AuthorityGiver) -> AuthorityGiver:
        if not isinstance(obj, AuthorityGiver): raise TypeError()
        querys = obj.to_querys() + self.__querys()
        return AuthorityGiver(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> AuthorityGiver:
        querys = querys + self.__querys()
        return AuthorityGiver(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()

    def set_query_to_edite(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT ALL ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return AuthorityGiver(self.__info , self.__querys + querys)
    
    def set_query_to_read(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return AuthorityGiver(self.__info , self.__querys + querys)
    
    def set_query_to_write(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT, UPDATE, DELETE, INSERT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return AuthorityGiver(self.__info , self.__querys + querys)