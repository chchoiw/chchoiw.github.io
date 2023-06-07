# SMS  command
- 測試: testCPT


```bash
sendSMS -i cptv02.smg.net -s a.xml
```

- xml format

```xml
<?xml version='1.0' encoding='UTF-8'?>
<sms>
  <smsGroup>testCPT</smsGroup>
  <smsLanguage>2</smsLanguage>
  <smsMessage>測試海潚用</smsMessage>
</sms>
```

- xml location

```
/datacenter/temp/zf1311_output/swfdata/sweather/smsUTF8/tn/
```



## alert
- 測試: alert_test_test


```
sendAlert -i tra007.smg.net -p alert_template.xml
```


```xml
<?xml version='1.0' encoding='UTF-8'?>
<alert>
  <cmd>playsound</cmd>
  <clientIp></clientIp>
  <group>alert_test_test</group>
  <playlist path="wav">
    <soundfile>cuckoo.wav</soundfile>
  </playlist>
  <alertText>alert 測試</alertText>
  <refURL></refURL>
</alert>
```

- DB

tra007.smg.net>CPT> alertGroup
tra007.smg.net>CPT> alertRecvLog