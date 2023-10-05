# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:12 2023

@author: iwill
"""
from __future__ import annotations
import psycopg2

class ConnectingInfromation:

    def __init__(self, 
                 host: str="localhost",
                 port: int=5432, 
                 database: str="postgres", 
                 username: str="postgres",
                 password: str="password"):
        self.__host = host
        self.__username = username
        self.__port = port
        self.__database = database
        self.__password = password
        
    def __str__(self):
        strs = [
            "******************************",
            f"host = {self.host}",
            f"port = {self.port}",
            f"database = {self.database}",
            f"username = {self.username}",
            f"password = {self.password}",
            "******************************"
            ]
        return "\n".join(strs)
    def __repr__(self):
        return self.__str__()
        
    def set_local_user(self, 
                 host: str="localhost",
                 port: int=5432, 
                 database: str="postgres", 
                 username: str="postgres",
                 password: str="passwrod") -> ConnectingInfromation:
        return ConnectingInfromation(
            host,
            port,
            database,
            username,
            password)

        
    def can_connect(self):
        try:
            conn = psycopg2.connect(
                host=self.__host, 
                port=self.__port, 
                user=self.__username, 
                password=self.__password, 
                database=self.__database,
    
            )

        except Exception as ex:
            print(ex)
            raise ex
            return False
        
        conn.close()
        return True

    @property
    def host(self):
        return self.__host
    @property
    def port(self):
        return self.__port
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    @property
    def database(self):
        return self.__database
