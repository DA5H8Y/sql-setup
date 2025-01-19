# Create_sql_schema

Converts all Excel files (xlsx, xls) in the directory into two SQL files one defining the database structure the other inserting any data found in the Excel files.

## Sample Excel file
| col_1_name: col_1_type | ... | col_n_name: col_n_type | 
|------------------------|-----|------------------------|
| value_1_1 | ... | value_1_n |
| ... | ... | ... |
| value_m_1 | ... | value_m_n |

## Sample SQL files

```sql
CREATE DATABASE fName;
CREATE TABLE tsheetName (
    col_1_name  col_1_type,
    ...
    col_n_name col_n_type
);
```
```sql
INSERT INTO tsheetName (col_1_name, ..., col_n_name) VALUES ( value_1_1, ... value_1_n);
...
INSERT INTO tsheetName (col_1_name, ..., col_n_name) VALUES ( value_m_1, ... value_m_n);
```