---
title: 'SMG Window live mail set internal account'
date: 2017-07-26
permalink: /posts/notes/smg_window_live_mail/
---


# SMG Window live mail set internal account


* copy all folder to local computer
```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```
* if account cannot be connected again, try rename folder

```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```

and open ```Window Live Mail``` app again

* there will be new folder with the same path
```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail
```

* reset account 
```
pop3.smg.net 110
smtp.smg.net 25
```
![](/images/window_live_mail/1.png)
![](/images/window_live_mail/2.png)

* only copy inbox respect to the same account, for example:
```
C:\Users\chchoi\AppData\Local\Microsoft\Windows Live Mail\smg_internal\Inbox
```
here smg_ineternal is my account name