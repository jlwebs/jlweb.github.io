---
layout: post
title: "16_32_64位系统下int 、指针、long、long long大小"
date: 2023-12-10
categories: jekyll
tags: ['🥁-OS']
comments: true
---

指针类型void* 大小和第二行一致，和操作系统位数完全一致
其他就是记下long 和int 。
1、32位系统的最大寻址空间是2的32次方=4294967296（bit）= 4（GB）左右（一般是可以用3.25G左右就满了）。
2、64位系统的最大寻址空间为2的64次方=4294967296（bit）的32次方，数值大于1亿GB
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692107879058-1841eb14-82de-432e-824f-b2b311387a44.png#averageHue=%23fafafb&clientId=u94f75aa3-4b80-4&from=paste&height=277&id=u48406a2e&originHeight=506&originWidth=1763&originalType=binary&ratio=1.8300000429153442&rotation=0&showTitle=false&size=13929&status=done&style=none&taskId=ud0fce9af-8c14-4b47-bbcc-9614e53330e&title=&width=963.387955549658)
