---
title: 'PHP Code'
date: 2020-01-20
permalink: /posts/notes/php_code/
---

- [Basic](#basic)
  - [Array](#array)
  - [Gerenal](#gerenal)
  - [Date and Time](#date-and-time)
  - [read/write file](#readwrite-file)
  - [string](#string)
- [Cookie](#cookie)
- [password](#password)
- [json](#json)
- [GET and POST](#get-and-post)
- [xml](#xml)
- [insert DB](#insert-db)


#PHP CODE

## Basic
### Array
1. new array
```php 
$a=array();
$a=array('寒冷'=>3);
```
2. append an element to array
```php
array_push($a, "apple");
```

2. append two array
```php
$new_ary=$array1+$array2;
```
3. merge
```php
$arr12 = array_merge($arr1, $arr2); 
```

4. get keys and values of an arrary
```php
array_keys($tmp); 
array_values($tmp); 
```
5. Count rows of array
```php
$num_row=count($result);
```
6. Check if key/values in array
```php
array_key_exists('first', $search_array)
in_array('first', $search_array)
```

### Gerenal

1. foreach
```php
foreach($this->elem as $chinese=>$eng)
{
    your code here
}
```

2. string length
```php
strlen("John")
```

### Date and Time
1. get sever time
```php
$today=date("Y-m-d H:i:s");
$three_day_ago = date("Y-m-d H:i:s", strtotime("-3 day"));
```
2. get sever UTC time
```php
$log_dt=gmdate("Ymd");
```

3. set defaut timezone
```php
date_default_timezone_set('Asia/Macau');
```

### read/write file
1. file exist?
```php
file_exists($path)
```
2. write file
```php
    $log_file="log/log_xml_".$log_dt.".txt";
    if (file_exists($log_file))
    {
      // a+ read/write append file
        $myxmlfile = fopen($log_file, "a+") or die("Unable to open file!");
    }
    else{
      // c+ read/write/create  file
        $myxmlfile = fopen($log_file, "c+") or die("Unable to create file!");
    }
    fwrite($myxmlfile, "-------\n".$xml."\n");
    fclose($myxmlfile);
```

### string
1. replace
```php
echo str_replace("world","Peter","Hello world!");
// Hello world!-> Hello Peter!
```
2. substring
```php
$rest = substr("abcdef", -1);    // returns "f"
$rest = substr("abcdef", -2);    // returns "ef"
$rest = substr("abcdef", -3, 1); // returns "d"
$rest = substr("abcdef", 0, -1);  // returns "abcde"
$rest = substr("abcdef", 2, -1);  // returns "cde"
$rest = substr("abcdef", 4, -4);  // returns false
$rest = substr("abcdef", -3, -1); // returns "de"
```

3. split
```php
explode( ',', $input1 );
```

## Cookie
1. check isset cookie
```
isset($_COOKIE["user"]);
```
2. set cookie
```php
setcookie('user', $json_str,0,'/' );
```
3. delete cookie
```php
setcookie('user', '', time() - 3600,"/");
```
## password
```php
$password= hash( 'sha256', $password);
```




## json
1. encode array
```php 
// result in unicode
json_encode($arr);
//canot show chinese
json_encode($arr,JSON_UNESCAPED_UNICODE);
```
2. write json
```php
$fp = fopen($json_path, 'wb');
// utf8_encode($myString)
fputs($fp, json_encode($backup_ary,JSON_UNESCAPED_UNICODE));
fclose($fp);
```

3. read json as array
```php
$json_path='/home/vip004/zf1/msgboard/public/json/config_from_php.json';
$json = file_get_contents($json_path, true);
// echo $json;
$config_ary=json_decode($json, true);
```

4. read cookie
```php
$json_get_str=$_COOKIE["user"];
```

## GET and POST
```php
$i = $_GET["i"];  //取得網址列傳來的變數i  
$j = $_POST["j"];  //取得網址列傳來的變數j  
// check if Post
isset($_POST["i"]) 
```

## xml

1. gen_xml
```php
function create_xml($public_dt,$status,$notice_str,$dt)
{
    /* create a dom document with encoding utf8 */
    $domtree = new DOMDocument('1.0', 'UTF-8');
    $domtree->preserveWhiteSpace = false;
    $domtree->formatOutput = true;
    /* create the root element of the xml tree */
    $xmlRoot = $domtree->createElement("SpecialNotice");
    /* append it to the document created */
    $xmlRoot = $domtree->appendChild($xmlRoot);
    $system = $domtree->createElement("System");
    $system = $xmlRoot->appendChild($system);
    /* you should enclose the following two lines in a cicle */
    $system->appendChild($domtree->createElement("SysAuthor",'AMO'));
    $system->appendChild($domtree->createElement('SysPubdate',$public_dt));
    $system->appendChild($domtree->createElement('SysLanguage','3'));
    $Custom = $domtree->createElement("Custom");
    $Custom = $xmlRoot->appendChild($Custom);
    $WarmNotice = $domtree->createElement("WarmNotice");
    $WarmNotice = $Custom->appendChild($WarmNotice);
    $WarmNotice->appendChild($domtree->createElement("Status",$status));
    $WarmNotice->appendChild($domtree->createElement('Description',$notice_str));
    $WarmNotice->appendChild($domtree->createElement('IssuedAt',$dt));
    /* get the xml printed */
    $xml=$domtree->saveXML();
    return $xml;
}
```

2. output:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<SpecialNotice>
  <System>
    <SysAuthor>AMO</SysAuthor>
    <SysPubdate>2019-08-28 08:42 +0000</SysPubdate>
    <SysLanguage>3</SysLanguage>
  </System>
  <Custom>
    <WarmNotice>
      <Status>0</Status>
      <Description>In the next few hours, an area of thunderstorm may affect MIA. Please pay attention to the message issued by AMC.</Description>
      <IssuedAt>2019-08-28 08:42 GMT</IssuedAt>
    </WarmNotice>
  </Custom>
</SpecialNotice>
```

3. write xml
```php
function wt_xml_file($xml)
{
    $myxmlfile = fopen("/datacenter/products/cmae/warnings/e_aeronotice.xml", "w+") or die("Unable to open file!");

    fwrite($myxmlfile, $xml);
    fclose($myxmlfile);

    $myxmlfile = fopen("output/xml.txt", "w+") or die("Unable to open file!");
    fwrite($myxmlfile, $xml);
    fclose($myxmlfile);

    $log_dt=gmdate("Ymd");
    $log_file="log/log_xml_".$log_dt.".txt";
    if (file_exists($log_file))
    {
      // a+ read/write append file
        $myxmlfile = fopen($log_file, "a+") or die("Unable to open file!");
    }
    else{
      // c+ read/write/create  file
        $myxmlfile = fopen($log_file, "c+") or die("Unable to create file!");
    }
    fwrite($myxmlfile, "-------\n".$xml."\n");
    fclose($myxmlfile);
}
```

## insert DB

```php

function insert_db($dt_db,$notice_str,$status,$user)
{
    $servername = "localhost";
    $username = "cptmain";
    $password = "Idced@11ic";
    $dbname = "test";
    $log_dt=gmdate("Ymd");
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    $sql = "INSERT INTO amo_notice (ISSUE_TIME, MESSAGE, STATUS,USER)
    VALUES ('$dt_db', '$notice_str', $status,'$user')";

    if ($conn->query($sql) === TRUE) {
        // echo "New record created successfully";
        echo "TRUE";
    } else {
        echo "FALSE";
        // echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
```