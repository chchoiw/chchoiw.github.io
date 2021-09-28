---
title: '02331-數據結構'
date: 2021-09-28
permalink: /posts/2021/09/02331/
tags:
  - 數據結構
category:
  - Computer Science
---


# 第三章

## 隊列

### 數組隊列
- 空隊列時
  - font=0, rear=0
- 非空隊列時
  - font是出隊,非空隊列是有內容
  - rear是入隊,非空隊列是最後有內容的後一個位置

### 鏈隊列

- 空隊列時
  
```
Q->font=head=Q->rear
head->next=Null
```

- 非空隊列時
  - font的指針指向head,但head沒有內容
  - rear的指針指向隊尾,p->rear->data是有內容的