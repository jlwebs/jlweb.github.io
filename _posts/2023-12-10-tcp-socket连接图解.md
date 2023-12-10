---
layout: post
title: "tcp socket连接图解"
date: 2023-12-10
categories: jekyll
tags: ['🥁-Network']
comments: true
---

![](https://cdn.nlark.com/yuque/0/2023/jpeg/26575180/1699164916039-80d5750a-4145-4ae3-9879-ed9010125c2b.jpeg#averageHue=%23dee4cc&clientId=u1ef7964f-b871-4&from=paste&height=294&id=zP3So&originHeight=714&originWidth=640&originalType=url&ratio=2.640000104904175&rotation=0&showTitle=false&status=done&style=shadow&taskId=u506d6170-67d5-4d00-8a23-1862fe20090&title=&width=263.3006591796875)![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699164999066-cbab5b88-326e-455d-8f79-d53c06bd7b36.png#averageHue=%23378b14&clientId=u1ef7964f-b871-4&from=paste&height=147&id=u1ad3f20b&originHeight=285&originWidth=673&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=136662&status=done&style=shadow&taskId=u76d28433-a338-47a2-886d-20d044a4aad&title=&width=347.9242401123047)
![](https://cdn.nlark.com/yuque/0/2023/webp/26575180/1699166025265-9f6aef88-1aa4-4883-8033-52cb895076fc.webp#averageHue=%23f9f9f9&clientId=ue349ab1b-ceff-4&from=paste&height=167&id=u1d55206d&originHeight=675&originWidth=1440&originalType=url&ratio=2.640000104904175&rotation=0&showTitle=false&status=done&style=shadow&taskId=u1186b4a9-d13e-4ddc-a01a-830d3297653&title=&width=356.2840881347656)![socket编程接口](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699171093781-84c534b4-98a1-4c8c-ba6f-4ce32eecfe3a.png#averageHue=%23f6f6f6&clientId=ud864c216-927e-4&from=paste&height=100&id=pZBtQ&originHeight=443&originWidth=1158&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=true&size=171557&status=done&style=shadow&taskId=u30c238aa-7474-4207-92da-ab6c62ef88a&title=socket%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3&width=261.62310791015625 "socket编程接口")
https TLS握手+会话密钥过程 （图解）![](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699410307585-71d5cbbc-e022-4bc3-b2d1-93adf1cc3cd9.png#averageHue=%23fbf6e5&clientId=ud864c216-927e-4&from=paste&height=803&id=u1352b305&originHeight=2807&originWidth=1545&originalType=url&ratio=2.640000104904175&rotation=0&showTitle=false&status=done&style=shadow&taskId=u72895000-9f8c-4eee-84e5-0811981e050&title=&width=442.0272216796875)

- 握手过程：

客户端connect 开启第一次握手
listen()获取到结果 第二次握手，进入半连接队列
最后一次ack后进入established，进入全连接队列（内核通过**五元组**绑定找到对应的半连接队列，然后搬迁）
 

- 挥手过程：

recv返回0代表开始关闭，前两次挥手已完成
close()开始第三次挥手；
请求关闭端进入TIME_WAIT阶段
（为了清空历史连接，开启新的连接![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699168627887-4c1d9bd1-c7f7-499e-b087-7203e4df72f3.png#averageHue=%23e8e6e4&clientId=ue349ab1b-ceff-4&from=paste&height=38&id=u0d8ce4f0&originHeight=135&originWidth=1772&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=62677&status=done&style=shadow&taskId=u04ab2741-aea4-40c8-a0db-23c088a638d&title=&width=497.21209716796875)）

- backlog两种理解
   - 1.全连接队列长度（linux最新版本）
   - 2.全连接+半连接队列长度

[异常]

- TIME_WAIT分别客户端、服务端出现大量，什么原因？

客户端主动关闭情况下： 高并发+短连接过多。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699513050903-b3ec2cfd-a141-4025-a7d7-66acbc6064e5.png#averageHue=%23f6f5f4&clientId=ud864c216-927e-4&from=paste&height=222&id=u3c58e253&originHeight=1020&originWidth=1414&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=307512&status=done&style=shadow&taskId=ufa1336b7-d057-4159-8fb7-b98e1d56794&title=&width=307.6020202636719)
server主动关闭下，主要是代码逻辑问题，导致大量连接主动关闭；

- 客户端出现大量FIN_WAIT原因？

等同于服务端进入大量![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1699168057822-827db988-e0c3-48d4-b825-ba9e01328586.png#averageHue=%23e2c7b0&clientId=ue349ab1b-ceff-4&from=paste&height=19&id=u91c66ffd&originHeight=50&originWidth=140&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=10514&status=done&style=shadow&taskId=ue4301d59-6f39-44c3-af12-a2b2f6125bf&title=&width=53.0303009230682)状态，等于服务端没有及时调用close函数；


[问题]

- 能否TCP\UDP绑定相同端口下同时通信

![](https://cdn.nlark.com/yuque/0/2023/jpeg/26575180/1699241415180-3366e0f3-afcc-4143-a205-3839d0c7990e.jpeg#averageHue=%23dddbc7&clientId=ud864c216-927e-4&from=paste&height=350&id=u6e7b4c89&originHeight=1197&originWidth=952&originalType=url&ratio=2.640000104904175&rotation=0&showTitle=false&status=done&style=shadow&taskId=u28586b03-41b6-45cb-bea5-64dd1c29ae4&title=&width=278.0085144042969)  可以，五元组区别。

- 端口复用

有时候重启服务器会出现：**Address already in use**
说明还在4次挥手结束后的Time_wait阶段；可以开启端口复用option： 
SO_REUSEADDR 作用是：**如果当前启动进程绑定的 IP+PORT 与处于TIME_WAIT 状态的连接占用的 IP+PORT 存在冲突，但是新启动的进程使用了 SO_REUSEADDR 选项，那么该进程就可以绑定成功**

