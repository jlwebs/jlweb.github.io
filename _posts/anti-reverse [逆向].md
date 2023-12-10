###### 1.IAT表是什么，怎么作用生效的
比如User32.dll，MessageBoxA这个API函数来说吧,其入口地址为77D504EA（显然超过0xC0000000 属于kernel space）, 如果在操作系统版本或者User32.dll的版本跟我的不同童鞋的机器上运行,可能就会出错。这时IAT(Import Address Table:输入函数地址表)诞生，用于提供寻找系统api入口地址，提升程序的环境兼容性；
2^32 = 2^4^8 = 16^8 = 0xffffffff + 1
因此按照4GB的四等分：1GB=0x40000000 2GB=0x80000000 3GB=0xC0000000 4GB=0xFFFFFFFF+1

【动态链接库对应的api实际地址是如何被装载到程序里的？】

- 1. 以`user32.dll`里的 `MessageBoxA`api为例，首先dll有自己的导出表Export table（见PE结构），记录了api的函数名到地址的映射表；
- 2. os装载器首先解析**可执行文件的导入表**（Import Table），获得dll名称，以及指向IAT中对应所有api的起始项位置
- 3. 通过GetProcAddress获取API函数的地址并填充到IAT中；GetProcAddress会根据导入表的信息去定位对应的动态链接库，并通过**动态链接库的导出表**（Export Table）找到相应函数的入口地址，装载到.rodata段作为字符串常量；
   - ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1698168589785-cbb1ddb8-2279-4d77-b830-b2a1c7aed2fc.png#averageHue=%23d2d0c8&clientId=ud3801d77-ccbe-4&from=paste&height=171&id=ufde9663e&originHeight=452&originWidth=561&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=431742&status=done&style=none&taskId=u0807834a-c017-477d-9ffc-de0b3dcaac7&title=&width=212.49999155600898) （可以看到地址符合.rodata段布局，紧挨.text段的上方）
- 4.位于被加壳程序的OEP处,我们接下来可以将程序dump出来,但是在dump之前我们必须修复IAT,为什么要修复IAT呢？
   - 其实IAT指的是导入函数地址表，我们要修复的不是IAT而是，步骤3里装载的dll导出表函数清单字符串区域，IAT如下箭头所指处，是自动生成的（注意上面的汇编程序叫做间接调用，IAT表不是代码是内存片段，JMP区域可以叫做中转站，编译器把动态库调用自动转换为解引用call）；
   - ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1698169282026-5cc189b1-2a9e-49b9-b431-b5358976bfa6.png#averageHue=%23e1dfc3&clientId=ud3801d77-ccbe-4&from=paste&height=294&id=ub13874f6&originHeight=776&originWidth=1223&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=1126334&status=done&style=none&taskId=u70561dcc-8c58-4b50-ac3d-5b5914d0fc4&title=&width=463.25755734937434)
   - 在这片IAT区域右键 view in executable file↓，可以看到原始API的string名源头↓偏移地址
   - ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1698169635793-45ba029a-48f7-4550-bfea-91f03218543e.png#averageHue=%23d8d6c7&clientId=ud3801d77-ccbe-4&from=paste&height=165&id=uc70cd9c0&originHeight=435&originWidth=1067&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=769929&status=done&style=none&taskId=ud6c5f82c-5dc9-4798-b48a-64029e7eacc&title=&width=404.1666506065269)![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1698169705976-21158bd9-da2f-4cf4-98e2-ea1959561220.png#averageHue=%23d2cfc7&clientId=ud3801d77-ccbe-4&from=paste&height=167&id=ueddf184f&originHeight=441&originWidth=595&originalType=binary&ratio=2.640000104904175&rotation=0&showTitle=false&size=434727&status=done&style=none&taskId=u42940dcb-0443-4c2e-9138-ceffc9b8241&title=&width=225.37877892303985)
   - 壳子会把程序导入表函数名称清单放到哪个位置呢？取决于壳子loader，和传统程序载入类似 ，但是肯定尽量让其隐蔽了
###### 2.在linux下，为什么 i386 ELF可执行文件默认从地址（.text）0x08048000开始分配。 而 x64是0x400000
![](https://cdn.nlark.com/yuque/0/2023/png/26575180/1698164141354-60f4494e-236b-46de-8e0d-c43ddbcc1d48.png#averageHue=%23fbfaf8&clientId=ud3801d77-ccbe-4&from=paste&height=401&id=u4f3d65e0&originHeight=970&originWidth=1884&originalType=url&ratio=2.640000104904175&rotation=0&showTitle=false&status=done&style=none&taskId=ucbc5d443-a9c4-4b1b-9268-9e06ec4efe6&title=&width=779.0108642578125)
