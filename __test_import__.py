# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 04:55:27 2023

@author: nanik

from psqlutil.authority_giver import AuthorityGiver
from psqlutil.conn_info import ConnectingInfromation
from psqlutil.creator import Creator
from psqlutil.data_exists import DataExists
from psqlutil.db_builder import DataBaseBuilder
from psqlutil.db_reader import DataBaseReader
from psqlutil.dummiy_dictionary import DummiyDictionary
from psqlutil.inserting_data import InsertingData
from psqlutil.psql import Psql
from psqlutil.remover import Remover
from psqlutil.role_creator import RoleCreator
from psqlutil.schema_creator import SchemaCreator
from psqlutil.table_creator import TableCreator
from psqlutil.updater import Updater
from psqlutil.writer import Writer
from psqlutil.reader import Reader
"""
from psqlutil import ConnectingInfromation


if __name__ == "__main__":
    import init
    init.init()