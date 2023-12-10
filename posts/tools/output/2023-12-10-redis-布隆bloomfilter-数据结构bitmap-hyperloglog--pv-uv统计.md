---
layout: post
title: "redis 布隆bloomFilter 数据结构Bitmap Hyperloglog  PV UV统计"
date: 2023-12-10
categories: jekyll
tags: ['🥁-DB']
comments: true
---

布隆过滤器 
基于多个hash 实现，能保证判断不存在(其中一个hash映射位置为0就代表不存在)，但不保证1存在判断正确率(多个hash位置终究会被其他映射冲突填满，全1并不一定存在，在数据装填越来越多后，此正确率持续下跌)

布谷鸟过滤器(鸠占鹊巢设计思想)，一个数组多个hash映射到不同位置，代表巢穴个数(默认2个)，一旦满了就踢走替换，能解决布隆过滤器无法删除只能重新新建的缺点，以及判存的错误率问题
[一文读懂Redis的布隆过滤器与布谷鸟过滤器](https://zhuanlan.zhihu.com/p/516733225)
