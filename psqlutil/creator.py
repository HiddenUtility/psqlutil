# -*- coding: utf-8 -*-
from __future__ import annotations
from psqlutil.psql import Psql
from psqlutil.committing import Committing
from psqlutil.connection_information import ConnectioinInfromation


class Creator(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: Creator) -> Creator:
        if not isinstance(obj, Creator): raise TypeError()
        querys = obj.to_querys() + self.__querys()
        return Creator(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Creator:
        querys = querys + self.__querys()
        return Creator(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        Committing(self.__info, self.__querys).commit()
