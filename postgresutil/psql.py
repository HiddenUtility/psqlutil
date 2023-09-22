# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:49:58 2023

@author: nanik
"""

from postgresutil.conn_info import ConnectingInfromation
from copy import copy

class Psql():
    #//Field
    querys: list[str] 
    def __init__(self, info: ConnectingInfromation):
        if not isinstance(info, ConnectingInfromation): raise TypeError("NOT ConnectingInfromation Object")
        if not info.can_connect():raise ConnectionError("SQLに接続できません。")
        self.host = info.host
        self.port = info.port
        self.database = info.database
        self.username = info.username
        self.password = info.password
        self.querys = []
        
    def __str__(self):
        return "\n".join(self.querys)
    
    def __repr__(self):
        return self.__str__()

    def _return(self,*querys:str):
        if len(querys)==0:return self
        new = copy(self)
        for query in querys:
            if not isinstance(query, str): raise TypeError
            new.querys.append(query)
        return new