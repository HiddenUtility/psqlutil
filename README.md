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
QueryCreator
|-TableQueryCreator
|    |-SelectQureryCreator
|    |-DeleteQureryCreator
|    |-UpdateQureryCreator
|    |-InsertIntoQureryCreator
ConnectingInformation  
DataBaseBuilder  
```
# Using
## Creator
```test_creator.py
from psqlutil import ConnectingInformation, Creator
info = ConnectingInformation(ip, port, user, password)
query = "CREATE SCHEMA test"
Creator(info).set_free_query(query).commit()
```
## Editor
```test_Editor.py
from psqlutil import ConnectingInformation, Editor, InsertIntoQureryCreator
info = ConnectingInformation(ip, port, user, password)  
data = dict(id="1234")
query:str = InsertIntoQureryCreator("table_name").set_data(data).query
Editor(info).set_free_query(query).commit()
```

## Reader
```test_reader.py
from psqlutil import ConnectingInformation, Reader, SelectQureryCreator
info = ConnectingInformation(ip, port, user, password) 
where = dict(id="1234")
query:str = SelectQureryCreator("table_name").set_where(where).query
df: DataFrame = Reader(info).set_free_query(query).get_df()
```

