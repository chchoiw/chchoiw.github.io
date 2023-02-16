## donet 6 install


[MicroSoft install](https://learn.microsoft.com/en-us/dotnet/core/install/linux-opensuse)


## donet 6 create new project

[create new project](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new)

```
dotnet new console -o skyViewSql
```


## add package to nutget

[MicroSoft-add packages](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-nuget-add-source)

```
dotnet add package System.Data.SqlClient
```

## build

```
dotnet build
```


##

```
dotnet run
```

##  ASP.NET Core

[網頁](https://ithelp.ithome.com.tw/articles/10234296?sc=hot)


## install sql server driver on suse

[2022安裝教學](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?view=sql-server-ver16)


## install

[官方網站安裝方法](https://learn.microsoft.com/en-us/sql/connect/php/installation-tutorial-linux-mac?view=sql-server-ver16)


## install sql odbc on suse

1. [官方網站安裝方法](https://learn.microsoft.com/de-de/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)好像找不到msodbcsql18, mssql-tools18
2. 所以找到了.rmp, 直接安裝
   
```
 sudo zypper install https://packages.microsoft.com/sles/15/prod/msodbcsql18-18.1.2.1-1.x86_64.rpm
```


```
sudo zypper install https://packages.microsoft.com/sles/15/prod/mssql-tools18-18.1.1.1-1.x86_64.rpm
```


## 安裝 php7-devel
```
https://download.opensuse.org/repositories/devel:/languages:/php/openSUSE_Leap_15.4/devel:languages:php.repo
```


## sqlcmd 的用法

```
sqlcmd -S SMGSQL01 -U skyview -P Idced@11ic -d SkyView -C
```

```
select top(1) * from tghokobs_input;
```




## dotnet and  svelte

- [link](https://khalidabuhakmeh.com/add-svelte-to-aspnet-core-projects)