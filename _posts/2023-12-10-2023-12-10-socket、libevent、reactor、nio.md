---
layout: post
title: "2023-12-10-socket、libevent、reactor、nio"
date: 2023-12-10
categories: jekyll
tags: ['output']
comments: true
---

---
layout: post
title: "Socket、libevent、Reactor、NIO"
date: 2023-12-10
categories: jekyll
tags: ['🥁-Network']
comments: true
---

1**_.Socket_**
两台计算机之间数据传输，要通过[网卡](https://www.zhihu.com/search?q=%E7%BD%91%E5%8D%A1&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A1181105689%7D)。网卡归谁管？操作系统。socket也是这么一个接口，用于程序和操作系统之间，进行网络数据收发的接口。在面向过程的语言中，socket是一个[函数](https://www.zhihu.com/search?q=%E5%87%BD%E6%95%B0&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A1181105689%7D)，在面向对象的语言中，socket是一个class，无论哪样，都是程序和操作系统之间的一个接口。在调用socket时，我们是需要指定协议的，如果指定tcp，那么这个socket就用tcp跟对方通信，如果指定udp，那么socket就用udp跟对方通信，其实还有unix-domain和raw类型的socket。
基于 Linux 一切皆文件的理念，在内核中 Socket 也是以「文件」的形式存在的，也是有对应的文件描述符。由下可知，processes[id].task_struct.fds[socket_file_descriptor] = Socket ， 其中socket_file_descriptor是Socket对象对应的文件描述符，在fds（文件描述符数组）中对应与数组下标；
> 文件描述符的作用是什么？每一个进程都有一个数据结构 task_struct，该结构体里有一个指向「文件描述符数组」的成员指针。该数组里列出这个进程打开的所有文件的文件描述符。数组的下标是文件描述符，是一个整数，而数组的内容是一个指针，指向内核中所有打开的文件的列表，也就是说内核可以通过文件描述符找到对应打开的文件。

由下可知，Socket.inode = Windows.global.TheSocket;
> 然后每个文件都有一个 inode，Socket 文件的 inode 指向了内核中的 Socket 结构，在这个结构体里有两个队列，分别是**发送队列**和**接收队列**，这个两个队列里面保存的是一个个 struct sk_buff，用链表的组织形式串起来。sk_buff 可以表示各个层的数据包，在应用层数据包叫 data，在 TCP 层我们称为 segment，在 IP 层我们叫 packet，在数据链路层称为 frame。



2.libevent
ibevent 是一个事件通知库，libevent 被设计为跨平台的库，支持在多种操作系统上运行

3.Reactor
