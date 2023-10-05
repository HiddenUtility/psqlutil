# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:53:14 2023

@author: iwill
"""

from __future__ import annotations


from psqlutil.editor import Editor


class Updater(Editor):
    #//Field

        
    def set_query(self,table_name: str, datas: dict[str:str], main_keys:list[str])->Updater:
        
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        main_keys = [f"{key} = {datas[key]}" for key in main_keys]
        where_clause = " AND ".join(main_keys)
        query = f"update {table_name} set {conditions} where {where_clause};"
        

        return self._return(query)