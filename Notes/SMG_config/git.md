


[git server](https://tfs002.smg.net/DefaultCollection/)

[add ssh key to server](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
window cmd

```
ssh-keygen -C "chchoi@smg.gov.mo"

```

- 開啟C:\Users\chchoi/.ssh/id_rsa.pub
- 再copy到git server 的add key
  


open git core

```
git config --global user.name "chchoi"
git config --global user.email "chchoi@smg.gov.mo"
git init
git clone ssh://tfs002.smg.net:22/DefaultCollection/Station%20Maintain%20Config/_git/Station%20Maintain%20Config

```



```
https://tfs002.smg.net/DefaultCollection/
```

再在clone 的 folder上加入新檔

git core

```
git add .
git commit -m 'your message'
git remote add origin ssh://tfs002.smg.net/DefaultCollection/Station%20Maintain%20Config/_git/Station%20Maintain%20Config
git push -u origin main
```