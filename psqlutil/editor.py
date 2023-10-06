# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:08:17 2023

@author: nanik
"""


from __future__ import annotations
from psqlutil.creator import Creator


class Editor(Creator):
    #//Field
    querys: list[str]
    #@orverride
    def __add__(self,obj: Editor) -> Editor:
        if not isinstance(obj, Editor): raise TypeError()
        self.querys += obj.querys
        return Editor(self.info ,self.querys)
    #@orverride
    def set_free_query(self, *querys: str) -> Editor:
        for query in querys:
            if not isinstance(query, str): raise TypeError()
            if not self._in_query(query, "DELETE"): raise SyntaxError(f"{query}は使用できません。")
            if not self._in_query(query, "UPDATE"): raise SyntaxError(f"{query}は使用できません。")
            if not self._in_query(query, "INSERT"): raise SyntaxError(f"{query}は使用できません。")
        return self._return(*querys)
    
    def delete_duplicate(self,table_name, *columns: str) -> Editor:
        if len(columns) == 0:return self
        key = ", ".join([f"{column}" for column in columns])
        andQuery = "WHERE "  + " AND ".join(["t2.{column} = t1.{column}" for column in columns])
        query = """
        DELETE FROM {0} t1
        WHERE EXISITS(
        SELECT {1}
        FROM {0} t2
        {2}
        AND t2.ctid > t1.ctid
        );
        """.format(table_name, key, andQuery)
        return self._return(query)