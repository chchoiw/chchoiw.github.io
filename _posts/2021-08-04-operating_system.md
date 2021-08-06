---
title: '04741-操作系統'
date: 2021-05-21
permalink: /posts/2021/07/02326/
tags:
  - 操作系統
category:
  - Computer Science
---


# 簡介
- 這是我[自考](http://eea.gd.gov.cn/zxks/index.html)計算機科學與應用中操作系統(02326)的複習要點
- 開始學習是使用[網上教學視頻](https://www.bilibili.com/video/BV1P4411z7cH?from=search&seid=3564874264541170958)
- [複習視頻](https://www.bilibili.com/video/BV1ty4y177wU?p=1)                                       
- [完成真題](https://drive.google.com/drive/folders/11Q28HN94vHKmIWU3VQynMXRGqgtvuueW?usp=sharing)
  

# 操作系統概論
- 操作系統是一種複雜的系統軟件，是不同程序代碼、數據結構、數據初始化文件的集合，可執行
- 操作系統屏



# 進程與線程

## 程序
- 順序性
- 封閉性:計算結果只取決於程序自身
- 確定性:與運行速度無
- 可再現性:與不同時間執行無關
  
## 並發與並行
- 並行:微觀與宏觀都是同時
- 並發:微觀是順序執行, 宏觀是同時

## 多道程序
- P.80
- 獨立性:與其他程多無閞
- 隨機性:執行開始時間和數據輸入時間都是隨機
- 資源共享性


- 缺點
  - 時間延長:對實時要求的程序不合適
  - 系統效率提高有一定限度
  

## 進程
- P.81
- 進程:<span style="color:red">系統進行資源分配和調度的一個獨立單位</span>
- 進程是由<span style="color:red">程序、數據和進程控制塊</span>組成
- 進程和程序分別:程序是靜態,進程是動態
- 特徵:
  - 井發性
  - 動態性
  - 獨立性
  - 交往性
  - 異步性
  - 結構性
### 進程控制塊(PCB)
- PCB 組織
  - 線性
  - 索引
  - 鏈接

- 進程的隊列
  - 就緒
  - 等待
  - 運行

- 進程控制
  - P.90
  - 創建原語
    
    ```mermaid
    graph LR
    A[申請PCB區域]-->B[有關信息填入PCB]
    B-->C[設進程狀態為就緒]
    C-->D[把進程放進就緒隊列]
    ```

  - 撤銷原語

    ```mermaid
    graph LR
    A[找撤銷進程的PCB]-->B[進程所在隊列消去]
    B-->C[𢸈銷它的子進程]
    C-->D[釋放占用的資源]
    D-->E[消去PCB]
    ```

  - 阻塞原語
  - 喚醒原語




### 可再入程序
- 可再入程序:被多個用戶同時調用的程序,與數據區分離


-- to be continuous