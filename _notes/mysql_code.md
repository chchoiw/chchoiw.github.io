---
title: 'Mysql Code'
date: 2020-01-20
permalink: /posts/notes/mysql_code/
---

- [Mysql Code](#mysql-code)
  - [Enter to db host](#enter-to-db-host)
  - [Create table](#create-table)
  - [Add column](#add-column)
  - [Modife column](#modife-column)
  - [Drop column](#drop-column)
  - [Copy structre from old table to new table](#copy-structre-from-old-table-to-new-table)
  - [Copy structure and data from old to new](#copy-structure-and-data-from-old-to-new)
  - [Update Data](#update-data)
  - [remove UNQIUE constraint](#remove-unqiue-constraint)
  - [Time Zone](#time-zone)
  - [Select command](#select-command)
    - [Not in array](#not-in-array)
    - [Like](#like)
    - [Time range](#time-range)
    - [Insert Data](#insert-data)
    - [Update Data](#update-data-1)
    - [Null Value](#null-value)
    - [Unique Value](#unique-value)
    - [Rename Column Name](#rename-column-name)
# Mysql Code

## Enter to db host
```bash
mysql -hmssv08 -ucptmain -pcpt123
use CPTMAIN
```

## Create table
```sql
CREATE TABLE check_alert (
    ID int NOT NULL AUTO_INCREMENT,
    CHECK_TIME DATETIME, 
    TYPE VARCHAR(20), 
    STATIONCODE VARCHAR(20), 
    OBS_TIME DATETIME,
    ELEMENT VARCHAR(50),
    GRADE int, 
    PRIMARY KEY (ID)
    )
    CHARACTER SET utf8;
```

## Add column
```sql
ALTER TABLE MSGboard ADD COLUMN GenSMS INT(11) NOT NULL DEFAULT 0 AFTER OBS_TIME;
```

## Modife column
```sql
ALTER TABLE check_alert MODIFY COLUMN UNIT VARCHAR(20) NOT NULL DEFAULT ''  AFTER THRESHOLD_VALUE;
```

## Drop column
```sql
ALTER TABLE check_alert DROP COLUMN FIRST_FOUND;
```
## Copy structre from old table to new table
```sql
CREATE TABLE check_alert_test  LIKE check_alert;
```

## Copy structure and data from old to new
ref: [link](https://stackoverflow.com/questions/3280006/duplicating-a-mysql-table-indices-and-data)
```sql
CREATE TABLE newtable LIKE oldtable; 
INSERT newtable SELECT * FROM oldtable;
-- or 
CREATE TABLE tbl_new AS SELECT * FROM tbl_old;
```

## Update Data
```sql
UPDATE check_alert SET THRESHOLD_VALUE= NULL where id=99;
```

## remove UNQIUE constraint
[link](https://stackoverflow.com/questions/3487691/dropping-unique-constraint-from-mysql-table)
```sql
SHOW INDEX FROM tbl_name
-- then
ALTER TABLE tbl_name DROP INDEX index_name
```

## Time Zone
```sql
select * from table_name where Time>=  DATE_SUB(CONVERT_TZ(Now(),'+00:00','+8:00'), INTERVAL 3 DAY) AND Time <= CONVERT_TZ(Now(),'+00:00','+8:00')
```

## Select command

### Not in array
```sql
SELECT * FROM albums WHERE name NOT IN ('Wall', 'Profile', 'Cover', 'Instagram')
```

### Like
1. %: unknown lengths of  unknown characters. If searching aXXXX
```sql
SELECT * FROM albums WHERE CustomerName LIKE 'a%'
```

2. "_" : one unknown character. If searching "aXbXXX"
```sql
SELECT * FROM albums WHERE CustomerName LIKE 'a_b___'
```

### Time range

```sql
SELECT DATE_SUB("2017-06-15 09:34:21", INTERVAL 15 MINUTE);
SELECT DATE_SUB("2017-06-15 09:34:21", INTERVAL 3 HOUR);
SELECT DATE_SUB("2017-06-15", INTERVAL -2 MONTH);
```

### Insert Data
```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
```

### Update Data
```sql
UPDATE Customers SET ContactName='Juan' WHERE Country='Mexico';
```

### Null Value
```sql
SELECT column_names FROM table_name WHERE column_name IS NULL;
SELECT column_names FROM table_name WHERE column_name IS NOT NULL;
```

### Unique Value
```sql
SELECT DISTINCT Country FROM Customers;
```

### Rename Column Name
```sql
SELECT CustomerID AS ID, CustomerName AS Customer FROM Customers;
```
