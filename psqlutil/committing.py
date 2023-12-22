from __future__ import annotations
import psycopg2

from psqlutil.psql import Psql
from psqlutil.connection_information import ConnectioinInfromation

class Committing(Psql):
    __info: ConnectioinInfromation
    __querys: str
    def __init__(self, info: ConnectioinInfromation, querys) -> None:
        self.__info = info
        self.__querys = querys
        
    # @override
    def __add__(self,obj: Committing) -> Committing:
        if not isinstance(obj, Committing): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return Committing(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Committing:
        querys = querys + self.__querys
        return Committing(self.__info , querys)

    # @override
    def to_querys(self):
        return self.__querys
    
    # @override
    def set_query(self,query :str) -> Committing:
        querys = self.__querys + [query]
        return Committing(self.__info , querys)

    
    # @override
    def commit(self) -> None:
        if len(self.__querys) == 0: raise Exception("queryがセットされていません。")
        try:
            conn = psycopg2.connect(
                host=self.__info.host, 
                port=self.__info.port, 
                user=self.__info.username, 
                password=self.__info.password, 
                database=self.__info.database
            )
        except Exception as ex:
            raise ex
        
        cur = conn.cursor()
        for query in self.__querys:
            try:
                cur.execute(query)
            except Exception as ex:
                print(f"{query}問題があります。")
                raise ex
            
        try:
            conn.commit()
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            conn.close()
