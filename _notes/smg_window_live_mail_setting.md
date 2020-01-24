---
title: "SMG replace computer setting"
date: 2020-01-20
permalink: /posts/notes/smg_setting/
---

# Window Live Mail

- copy all folder to local computer

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```

- if account cannot be connected again, try rename folder

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```

- open `Window Live Mail` app again, there will be new folder with the same path

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```

- copy [Contacts](https://drive.google.com/open?id=1Nr7wa7KxlBhi_hD2GECxOVD4fTcMKsrK) and replace the following location:

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live\Contacts
```

- reset account

```
pop3.smg.net 110
smtp.smg.net 25
```

![](/images/window_live_mail_png/1.png)
![](/images/window_live_mail_png/2.png)

- only copy inbox respect to the same account, for example:

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail\smg_internal\Inbox
```

here smg_ineternal is my account name

# Data Disk Connection

- [Download](/files/smg_replace_computer/dir_connect.vbs)
- click`window+r` open `cmd`
- key in

```
shell:startup
```

- copy `dir_connect.vbs` to

```
C:\Users\chchoi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

then will run it again for starting the computer.
