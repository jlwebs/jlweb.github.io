---
layout: post
title: "select 、 poll =_ epoll的演变与区别"
date: 2023-12-10
categories: jekyll
tags: ['🥁-Network']
comments: true
---

###### 1.前世今生
Unix最早只有select，在其后期对select的改进poll出现、后来很多年后才改进出了epoll，其过程是一个耦合较高的过程优化解耦提升了性能，现在linux网络编程已经通通使用epoll了。
###### 2.基础功能

1. epoll
###### 3.区别总结

