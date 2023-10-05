# postgresutil  
PostgreSQLの低級操作練習

# ClassTree
```  
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
|    |-DataBaseReader  
|    |-Exists  
ConnectingInformation  
|-DataBaseBuilder  
```
# Using
## Creator
```test_creator.py
from psqlutil.creator import Creator
info = ConnectingInformation(ip, port, user, password)
query = "CREATE SCHEMA test"
Creator(info).set_free_query(query).commit()
```
## Editor
```test_Editor.py
from psqlutil.editor import Editor
info = ConnectingInformation(ip, port, user, password)  
query = "UPDATE FROM test ..."
rows, colnames = Editor(info).set_free_query(query).commit()
```

## Reader
```test_reader.py
from psqlutil.reader import Reader
info = ConnectingInformation(ip, port, user, password)  
query = "SELECT * FROM test"
rows, colnames = Reader(info).set_free_query(query).get_df()
```

