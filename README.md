# postgresutil  
PostgreSQLの低級操作練習

# ClassTree
```Psql  
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
```
# Using
## Creator
```creator.py
info = ConnectingInformation(ip, port, user, password)  
Controller(info).create_schema().run()
```
## Reader
```reader.py
info = ConnectingInformation(ip, port, user, password)  
Controller(info).get_data("query").run()
```

