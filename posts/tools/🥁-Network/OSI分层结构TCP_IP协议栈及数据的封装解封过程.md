0.ip数据报中的ip怎么来的
是通过OS协议栈
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1691982150469-90d7e85b-9713-4987-a987-fc52eb5738a5.png#averageHue=%23c7deab&clientId=u1641288c-b969-4&from=paste&id=ucdb61c05&originHeight=623&originWidth=908&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=109276&status=done&style=none&taskId=ufd3aa05f-d469-44f7-9a91-e966eda00f6&title=)
[网络层 IP 首部中的目的 IP 地址是怎么获取的？ - 拾月凄辰 - 博客园](https://www.cnblogs.com/FengZeng666/p/15610870.html)
[TCP Socket 编程原理详解 - 拾月凄辰 - 博客园](https://www.cnblogs.com/FengZeng666/p/15610953.html)
0.报文剥离
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1691926170648-fc644175-a319-426b-a0fa-544a671a4018.png#averageHue=%230b0b0b&clientId=u1641288c-b969-4&from=paste&height=102&id=u00a4a341&originHeight=171&originWidth=1006&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=19122&status=done&style=none&taskId=u674462c8-164f-49b8-af4c-cd1a0e98fe9&title=&width=600.3624267578125)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1691926176324-bedf3e29-529b-421e-a5a8-f4c2666b6ff3.png#averageHue=%2344a748&clientId=u1641288c-b969-4&from=paste&height=384&id=u8b59b4f6&originHeight=561&originWidth=973&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=60308&status=done&style=none&taskId=uccaa1ee7-121f-420d-9aaf-3dec1d62d6c&title=&width=665.3624267578125)
1.数据封装与解包逻辑
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1690540993917-ff8b0a53-932e-4235-a7aa-5bb632dd5e49.png#averageHue=%23f5f2ef&clientId=u3bf2242c-6998-4&from=paste&id=u48b49e41&originHeight=257&originWidth=433&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=97056&status=done&style=none&taskId=u9b57102e-95a3-4782-955f-96c241e0734&title=)
封装：由于通信数据包需要在往底层流动，以便承载二进制流的物理网线或信号上进行远程沟通，越靠近底层数据越返璞归真，失去语义和抽象文字，回归二进制流，这个过程中需要不断对各层报文加入新的字段以便在数据洪流中正确区分个体或者完整校验等用途。我们从应用层HTTP的文本信息里的特征id（如QQ号）作为不同个体独立标识，到传输、网络层的IP和端口作为标识，到链路层的MAC作为标识、到物理层无标识的0、1数据流
解包：0、1数据流经过帧标识解析给数据链路层，然后由MAC字段解析后发送给网络层、然后借助IP头部(包含souce、destination ip)划分后把数据分发给传输层，传输层通过TCP头部（含端口）的划分传给应用层，各个应用协议解析后返回给请求自身的应用程序中。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1690541196850-882f455f-4f97-40fe-9f1c-f6c07646222a.png#averageHue=%23f4f4f4&clientId=u3bf2242c-6998-4&from=paste&id=u0075151e&originHeight=1140&originWidth=1166&originalType=url&ratio=2.134999990463257&rotation=0&showTitle=false&size=188716&status=done&style=none&taskId=u96a77b32-104c-4779-9a5b-f1a862d5bf8&title=)
