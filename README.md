#postgresutil
簡単にお試しデータベース構築、操作

#ClassTree
Psql
|-Creator
|    |-Schema
|    |-Table
|    |-Role
|    |-Authority
|    |-Editor
|    |    |-Writer
|    |    |-Updater
|    |    |-Remover
|    |    |-Inserter
|-Reader
|    |-DataReader
|    |-Exists
ConnectingInformation
Controller

#Using
##Creator
info = ConnectingInformation(ip, port, user, password)
Controller(info).create_schema().run()

##Reader
info = ConnectingInformation(ip, port, user, password)
Controller(info).get_data("query").run()# psqlutil
