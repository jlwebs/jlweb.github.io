---
title: gWSL2+Vnc一键访问ubuntu桌面
feature: https://img2.baidu.com/it/u=1538308069,3004453526&fm=253&fmt=auto&app=138&f=JPEG?w=788&h=500
tag:
- 运维
- WSL
- shell
file: http://jlwebs.github.io/assets/img/about.jpeg
layout: post
---

WSL2子系统最终舒服使用捣鼓出来了。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692715572021-8b7fecdf-ef3e-4b98-97f7-5e14072a9bfe.png#averageHue=%23cf582e&clientId=u19241a42-f0c5-4&from=paste&height=91&id=u7f1d4892&originHeight=218&originWidth=474&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=59990&status=done&style=none&taskId=u840cbaae-02cc-4a84-b2b3-37dccf6da6f&title=&width=197.49999215205543)<br />首先说明：个人测试RDP很卡，可能是调整过加速，而且是win11家庭版暴力解锁的远程估计有bug，最后感觉VNC才是最快的，这次使用的是Xvfc + Vnc4server + （TigerVnc-viewer + gWSL GUI）

（安装尽量用外网环境，因为比较需要socks全局透明代理，会顺便把v2ray+hysteria的方案也分享一下，也是个人感觉最优的体验。）

XVfc基本上算Ubuntu桌面程序轻量化t0级别的了，此外的没有尝试了，这次目的就是把linux桌面的臃肿去掉，借助gWSL高效的访问桌面+自身安装的软件。

这里默认你已经装好了WSL2，且具备gWSL开启能力，建议使用22.04 lts ubuntu 商店版本；<br />不建议使用root用户进行下面操作，用sudo就好。

直接开始步骤：

1. ` sudo apt update -y && sudo apt upgrade -y `
2. ` sudo apt install xfce4 -y `
3.  ` sudo apt install xrdp -y `
4.  ` echo xfce4-session > ~/.xsession `
5.  ` sudo apt install net-tools -y`
6.  ` sudo service xrdp restart `
7.  ` sudo apt install ifconfig `
8.  ` apt install tigervncviwer `
9.  ` sudo apt-get update `

   	` sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32`<br />      	` sudo apt-get update `<br /> ` apt install vnc4server `

10.  ` vi ~/root/.vnc/xstartup`
```
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &
#x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
#x-window-manager &
sesion-manager & xfdesktop & xfce4-panel &
xfce4-menu-plugin &
xfsettingsd &
xfconfd &
xfwm4 &
```

11. 去掉一般用户sudo密码输入要求

` sudo vim /etc/sudoers.d/你的用户名 `<br /> 改为` dexter ALL=(ALL) NOPASSWD: ALL`, 执行sudo命令输入密码的了

12. `sudo apt install gedit`

 `mkdir ~/.local/bin -p `<br /> `sudo gedit ~/.local/bin/remote.sh `
```
sudo /usr/bin/vncserver :3  #使用虚拟屏幕3号投影
sleep 2    # 强制等待一秒,否则可能出现xrdp启动没完成导致无法连接
cd ~
sudo nohup /usr/bin/xtigervncviewer -passwd=mypass 127.0.0.1:3 
# mstsc.exe /v:172.23.83.252:3389 一开始别人用的mstsc需要还要指定物理机的ip才行，果断改之。
```

13. 开启gWSL

wsl --update 一下，具体不会可以google一下。<br />开启后，开始菜单里Ubuntu文件夹里就会列出当前所有gui应用，现在可以直接访问了。我们把TigerVNC Viewer图标单独复制一份，下一步进行改造。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692713533613-af77f85c-136c-4ae1-a003-d9a62b51fe2f.png#averageHue=%23866b4b&clientId=u19241a42-f0c5-4&from=paste&height=278&id=u339919d9&originHeight=667&originWidth=538&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=327508&status=done&style=none&taskId=u9dabb4ab-50ce-4747-a57e-e286304f610&title=&width=224.166657759084)

14. 创建桌面快捷方式

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692713441987-acf98b40-da79-4f48-b958-e81a6233d3db.png#averageHue=%23f1f0ef&clientId=u19241a42-f0c5-4&from=paste&height=164&id=u69b76fc6&originHeight=563&originWidth=813&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=50177&status=done&style=none&taskId=ud3bd8d4a-5c03-415b-91c5-ba59f28ab58&title=&width=236.75)<br />`C:\Users\ding\AppData\Local\Microsoft\WindowsApps\MicrosoftCorporationII.WindowsSubsystemForLinux_8wekyb3d8bbwe\wslg.exe -d Ubuntu --cd "~" -- /home/你的用户名/.local/bin/remote.sh ` 【整个逻辑跳跃：mnt/C/快捷方式.lnk  → 子系统~目录 → remote.sh → xtigervncviewer】

15. 用tiger的密码生成器，生成密码文件

` cd ~`<br />` vncpasswd mypass`

15. 结束开始享受

`wsl --shut-down`<br />完全关掉wsl，然后双击快捷方式，时间10s内就弹出来了；![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692714256545-099d0a5d-0e8f-4633-805f-83e594e0b6aa.png#averageHue=%23837663&clientId=u19241a42-f0c5-4&from=paste&height=273&id=u1385572d&originHeight=909&originWidth=1917&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=429022&status=done&style=none&taskId=ucc9d33e9-2a79-4a72-a335-85389dea861&title=&width=576.0025634765625)<br />如果没有去特意解锁WSL的systemd权限，启动时间会更快（之前为了自制service试过，最后只是把vncserver启动起来了，但是内部调用还是有bug，才用了这个方案的）。

【附录章节】 <br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692715544823-ff993d63-7902-46d7-b429-87d60954db0c.png#averageHue=%23faf9f6&clientId=u19241a42-f0c5-4&from=paste&height=105&id=u69bd7449&originHeight=253&originWidth=1656&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=41131&status=done&style=none&taskId=ub41389fe-ef63-4a7c-b49d-d138ff19c4f&title=&width=689.9999725818645)<br />在折腾过程中也顺便把V2rayA 基于网页版本的透明代理装了，毕竟xfce没有gnome自带的全局socks代理，这里物理机已经搭好了hysteria 节点，使用`"socks5": {"listen": ":10808","timeout": 300,"disable_udp": false}`暴露给局域网机器使用，注意不要写成127.0.0.1:10808的ip了否则只能本地代理，（同时本机V2rayN软件设置打开：允许局域网连接，好让iptables 放行）。

1. v2ray-core安装

这个是最煎熬的，一键命令安装很慢容易network error，慢慢装吧，具体见github readme。

2. v2raya 用软件包安装即可比较轻松，参考github就行
3. 安装chrome浏览器，因为基于web的，火狐不好用吐槽下最后都连不上google
4. v2raya启动后自动进入后台面板，设置socks5代理 ：指向物理机ip，ipconfig看得到。
5. 测速启动，设置透明代理一条龙
6. 开个terminal测下 curl google.com没问题了。要用就设置去开透明代理，不用就关了，实时的，不用被全局代理变量临时版本煎熬，而且局限性较大：shell脚本里修改了也只作用于shell文件周期，没办法通过sh文件一键切换。

这里涉及很多外网地址，需要先借助蛋生鸡，鸡才能给你造好代理的蛋。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1692715476045-e4c29e3b-2122-4e65-85f6-bb340a3bf217.png#averageHue=%2348a2c8&clientId=u19241a42-f0c5-4&from=paste&height=100&id=u6cd97238&originHeight=239&originWidth=1023&originalType=binary&ratio=2.4000000953674316&rotation=0&showTitle=false&size=19588&status=done&style=none&taskId=ud53fb785-90a7-4736-8ee7-86d5c552fbb&title=&width=426.24998306234744)<br />**结论：**<br />这篇文章面向linux新手，老鸟一般会结合Window Manager进行键盘高效布局，但了解了一圈，并不能按我想象的和gWSL配合达到程序坞的，一开始想找一些GUI程序替代桌面xfce的，不知有人了解吗。<br />中间其实还折腾过 kali 发行版的 kex-win -s模式 和 kex 的seamless模式，前者是基于tigerVNC的，后者基于Vcxrv，还是前者稳定不易出问题，但是系统本身问题较多不推荐用wsl版本的kali，后者不仅要开防火墙，还有操作麻烦了（不能一键都是麻烦），而且很容易崩就不能用了。<br />溜了溜了，做开发去了，折腾太耗时间了。
