---
layout: post
title: "IP包、TCP包、MTU、MSS"
date: 2023-12-10
categories: jekyll
tags: ['🥁-Network']
comments: true
---

1.MTU 与 MSS
只有UDP包才会在IP包时候被分片、TCP早在传输层就被MSS分段了
> 1.IP分片产生的原因是网络层的MTU；TCP分段产生原因是MSS.
> 2.IP分片由网络层完成，也在网络层进行重组；TCP分段是在传输层完成，并在传输层进行重组.   //透明性
> 3.对于以太网，MSS为1460字节，而MTU往往会大于MSS.
> 故采用TCP协议进行数据传输，是不会造成IP分片的。若数据过大，只会在传输层进行数据分段，到了IP层就不用分片。
> 所以可以看成是这种情况：传输层协议想发送一个超过了MTI的数据报，这个时候网络层就需要对其进行分片，一般UDP和ICMP会出现分片情况，但是TCP不会出现这种情况！因为TCP使用了MSS来避免分片！
> IP分片只有第一个带有传输层或ICMP首部，其余的分片只有IP头。至于怎么重组就是到对端以后IP层的事情了。
> 若TCP报文非常长那么在IP层传输时就有可能要分解成多个短数据报片。（计算机网络谢希仁）
> TCP分段每个都有完整首部。
> PS:所以我觉得是这样的，TCP的分段是针对应用层的数据来说的，比如使用TCP发送70KB的数据，这个时候就需要将70KB分成若干个MSS，到了网络层就不需要分片了。MSS的存在就避免了网络层分片的发生，

2.IP包分片（如UDP）后如何组装回的
基于字段“标识符”、“标志位”、“段偏移量”三位合一
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692166951653-561f71db-86da-4b70-8d3a-726d4226ee92.png#averageHue=%23e6e4e6&clientId=u72a71e38-1a8d-4&from=paste&id=u0a215f2f&originHeight=348&originWidth=874&originalType=url&ratio=2.5999999046325684&rotation=0&showTitle=false&size=549581&status=done&style=none&taskId=u3d64872b-d1a5-42eb-a19f-d19b246a6be&title=)

- 标志位

含有三位bit
第一位永远为零 未启用
第二位 0 1 如果为0 就是分配了分片
如果为1 就是未分配我就这一个帧 我没有兄弟姐妹
第三位 0 1
思考一下接收端怎么看有多少分片呢 就是标志位的最后一位表面我是不是最后一个分片
为1是就是还有后续分片
为0就是最后一个分片了
有一种攻击：段偏移量攻击—不断伪造ip包他就没法重组，然后就一直进行不断的重组，cpu就炸了（现在防火墙 中间位为0的都不让通过 只有010的能通过，重组都让应用层软件端重组，应用层发的时候分好片，交给应用层了）
[对抓包和ip包头以及路由原理分析_路由器抓包_Ech_0的博客-CSDN博客](https://blog.csdn.net/u011407763/article/details/104951675/)

- 标识符

标识符也就是id，是发送端随机生成的，主要是为了避免两个ip分片大包中的相同段偏移量子包的区分，具体而言就是标记这一片数据属于哪一个group id

- 段偏移量

决定ip分片的先后顺序
3.NAT转换示意图
[TCP Nagle算法、NAT 和 NAT 穿透](https://www.yuque.com/u26180163/gd4gdh/epis0ggvb0lfgl4y?view=doc_embed&inner=Plo2r)
4.UDP和TCP数据包大小规范

- UDP 协议的数据报不应该超过 MTU - 28 字节，一旦超过该限制，IP 协议的分片机制会增加 UDP 数据报无法重组的可能性
- IP 协议会分片传输过大的数据包（Packet）避免物理设备的限制；
- TCP 协议会分段传输过大的数据段（Segment）保证传输的性能；

5.不同MTU多设备传输路径上的妥协处理

- 路径上的网络设备根据数据包的大小和自己的 MTU 做出不同的决定：
   - 如果数据包大于设备的 MTU，就会丢弃数据包并发回一个包含该设备 MTU 的 ICMP 消息；
   - 如果数据包小于设备的 MTU，就会继续向目的主机传递数据包；
- 源主机收到 ICMP 消息后，会不断使用新的 MTU 发送 IP 数据包，直到 IP 数据包达到目的主机；

6.DNS为什么要求512字节数据以内
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1691988198585-fba685e5-10cb-4a90-99c5-a9bfc27077bc.png#averageHue=%23f2f0e3&clientId=ua8091143-6926-4&from=paste&id=ue0db0d46&originHeight=169&originWidth=1070&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=93144&status=done&style=none&taskId=ue06b2753-b1ae-4c7a-a5e3-b5c04b581fb&title=)

- 以太网帧在局域网中的MTU是1500byte，但是在非局域网环境，如：internet下的时候，MTU是各个[路由器](https://so.csdn.net/so/search?q=%E8%B7%AF%E7%94%B1%E5%99%A8&spm=1001.2101.3001.7020)进行一个配置的。所以，通常路由器默认的MTU为576字节。所以，为了适应网络环境，DNS协议在返回的数据报大于512的时候，就转化为了TCP协议。
- 512并不是严格上界，而是考虑损耗的妥协量，最大传数据最大值应该是548=576-20-18（网络层IP数据报首部20字节，UDP报文首部8字节）
- 

