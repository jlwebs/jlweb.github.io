---
title: 网站点滴1
tag:
- 历史
- 杂谈
- jemoji
- ruby
layout: post
comments: true
excerpt: |-
  :yum:干货少，纯记录
   1. 过期续费Transfer
   2. Jemoji自定义
---

**干货少，纯记录**
# 网站点滴

最近网站域名到期了，但是续费高达60+Dollar，

百般无奈查询后发现可以试试 Transfer（转移）这条路，转移完成有效期自动+1年，但是是基于过期时间计算，而不是转移日期

*注意：【如果域名过期45天后不续费将进入 赎回期*

       whois英文状态：REDEMPTION-PERIOD 

*这个阶段赎回费用极高且不允许Transfer，然后进入6天删除待决期，之后*

*CANN（The Internet Corporation for Assigned Names and Numbers * 将夺走你的域名，重新开放注册】*

> 向域名服务商在线提出域名转入申请，完整填报有关域名注册资料，原注册商同意，同意域名的转出。同意后便可转入。向域名服务商在线提出域名转出申请，完整填报有关域名注册资料，注册商同意，同意域名的转出。同意后便可转出到新的域名注册商。

*注意：虽然转移域名可以解决续费问题，但是如果时期不对，会造成 **掉年** 问题*
*比如我在国内便宜域名商买了9年域名，然后马上转移到godaddy去，年限不会加1，=转移费白交了*
*，一般要求Transfer或者购买域名后60天再进行Transfer才妥当*


很奇怪这个域名国外商最低Transfer价格都在15D以上，来自namesoil(域名泥土)，

后来选了家国内域名商转过去了（转移过程↓），价格减半，虽然国内域名商限制较多，但不是国内的主机不会太麻烦，

再更改NS解析到cloudflare，又恢复生机勃勃的景象了，算是成功fix！

------------
转移过程：在域名商申请域名解锁unlock，解锁后email会收到Transfer Key，到待转移域名商填写
支付转移费，等待2小时-6天，自动就过户过去了，如果之前是godaddy，还可以多刷新会Transfers
列表，里面可以加速服务（Transfer ACCEPT），一般2小时就迁移过去了

------------
2018年10月28日

blog里使用jemoji，自己定制的话还是不太方便的，提供一种方法

定位gem 本地包位置：

gem environment gempath

=>C:/Ruby24-x64/lib/ruby/gems/2.4.0/gems/jemoji-0.10.1/lib/jemoji.rb

打开jemoji的gem目录找到lib中的jemoji.rb

```ruby
def filter_with_emoji(src)
	filters[src] ||= HTML::Pipeline.new([
	HTML::Pipeline::EmojiFilter,
	], :asset_root => src, :img_attrs => { :align => nil,:height => "48", :width => "48" })
end
```

[ Eg： ↑我修改了 `height => "48", :width => "48" ` 原来默认32xp有点小 ]

:img_attrs就是对应emoji替换函数的附加参数，可以给img加属性，比如style等等

 - 这是html_pipeline gem包内源码说明
 
```ruby
HTML::Pipeline.require_dependency("gemoji", "EmojiFilter")

module HTML
  class Pipeline
    # HTML filter that replaces :emoji: with images.
    #
    # Context:
    #   :asset_root (required) - base url to link to emoji sprite
    #   :asset_path (optional) - url path to link to emoji sprite. :file_name can be used as a placeholder for the sprite file name. If no asset_path is set "emoji/:file_name" is used.
    #   :ignored_ancestor_tags (optional) - Tags to stop the emojification. Node has matched ancestor HTML tags will not be emojified. Default to pre, code, and tt tags. Extra tags please pass in the form of array, e.g., %w(blockquote summary).
    #   :img_attrs (optional) - Attributes for generated img tag. E.g. Pass { "draggble" => true, "height" => nil } to set draggable attribute to "true" and clear height attribute of generated img tag.
```

还有种方案，需要自行结合gemoji.rb（jemoji.rb中引用）配合修改url对应解析规则，比较复杂，读者自行研究

这里留两个推荐emoji源的cheat sheet，可以替换成自定义样式
:yum:

[iemoji](https://www.iemoji.com/emoji-cheat-sheet/smileys-people "iemoji")

[webpagefx](https://www.webpagefx.com/tools/emoji-cheat-sheet/ "webpagefx")

------------

`网站历史`-`2018年10月28日`