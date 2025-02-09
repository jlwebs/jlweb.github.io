[搞懂RPC的基本原理和层次架构](https://www.yuque.com/xujunze/backend/sthbl7?view=doc_embed)
###### 1.测试

- stress 压力测试部分
   - 压力测试不是并发压力测试，只是模拟系统高负载下是否能监控到正确数值
   - 对cpu、磁盘、内存进行压测，可以高负载下测试自己程序
      - -c 6    多核榨干，不断计算随机数平方根
- 并发监控数量
   - 简单通过线性机器池和自定义业务逻辑完成异常与正常的判断，在本地网络测试模拟多台机器下是否正常使用，由于远程调用依赖网络，这里本地测试模拟简易情况并发量，本地受限于进程占用内存，因此只简单测试了几百台机器（进程）
###### 2.工作流程
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1694625458510-02dcda41-90ff-43bd-bb6a-27563d5a704e.png#averageHue=%23fbfbfb&clientId=u552a0c5e-a1df-4&from=paste&height=242&id=u5a19916b&originHeight=920&originWidth=1463&originalType=binary&ratio=2.879999876022339&rotation=0&showTitle=false&size=113557&status=done&style=none&taskId=u6af22f0b-1dbc-411f-bd85-7c43d7ea24e&title=&width=384.98614501953125)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1694657477329-ea83380b-26e6-4819-a4f0-39bed0f4f397.png#averageHue=%23f7e8cb&clientId=u0aa4ed35-ef71-4&from=paste&height=222&id=uc5ecdb24&originHeight=739&originWidth=1467&originalType=binary&ratio=2.879999876022339&rotation=0&showTitle=false&size=481162&status=done&style=none&taskId=u7d945977-3c83-4033-b2ff-b6f228bf6b1&title=&width=440.3750305175781)
 
###### 3.面试问题

- 监控参数怎么读取的，详细说下
1. **系统信息**："/proc"目录包含了许多文件，提供了关于系统硬件和内核状态的信息，如CPU信息、内存信息、网络配置、加载的模块等。
2. **虚拟文件**：在"/proc"中的大多数文件都不是实际存在的磁盘文件，而是内核提供的虚拟文件，用于在运行时访问系统状态和内核数据结构。
3. "/proc"是一个虚拟文件系统，不占用实际的磁盘空间，而是在内存中动态生成的。因此，它提供了一个方便的接口，使用户和系统可以轻松地访问和管理运行时的系统和进程信息。

/proc/mem_info  	内存相关
/proc/net/dev      	网络相关
/proc/stat           	CPU相关：计算CPU的user和sys占用率
根据获取内容次序，组织专门结构体，用file.ReadLine和 stoll把每一行数据存入struct

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1694768569037-7832349a-4c10-43e9-8ee7-9cacedb752d8.png#averageHue=%23fefefe&clientId=u290b1e72-5fe0-4&from=paste&height=80&id=ubf1a8138&originHeight=205&originWidth=1608&originalType=binary&ratio=2.559999942779541&rotation=0&showTitle=false&size=30462&status=done&style=none&taskId=u682740af-d23a-4ce8-a0a1-0e4aca6b4d0&title=&width=628.1250140396882)
###### 4.grpc框架工作原理
gRPC 是一个高性能、跨语言的远程过程调用（RPC）框架，由Google开发，基于HTTP/2协议和Protocol Buffers（protobuf）序列化协议。

以下是gRPC框架的工作原理：

定义服务和消息类型：

使用 Protocol Buffers 定义服务接口和消息类型。服务接口定义了可以远程调用的方法，消息类型定义了方法的参数和返回值的格式。
编写服务实现：

在服务端编写实现服务接口的代码。这些代码包括处理客户端请求、执行相应的逻辑并返回结果。
生成代码：

使用 Protocol Buffers 编译器（protoc）来生成客户端和服务端的代码，包括消息类型、服务接口和一些辅助代码。
启动gRPC服务器：

在服务端应用程序中创建一个gRPC服务器，并将实现了服务接口的服务对象注册到服务器中。
启动gRPC客户端：

在客户端应用程序中创建一个gRPC通道，该通道用于连接到远程服务器。
客户端调用服务：

在客户端中创建一个服务的存根（Stub），然后使用存根来调用远程服务。调用过程会将请求序列化成Protocol Buffers格式，并通过HTTP/2协议发送到服务器。
服务端处理请求：

服务端接收到请求后，会将请求解析并传递给实现了相应服务接口的对象进行处理。处理过程会将返回值序列化成Protocol Buffers格式，并通过HTTP/2协议返回给客户端。
客户端接收响应：

客户端接收到响应后，会将响应解析成相应的消息类型，并将其传递给应用程序。
关闭连接：

当请求和响应处理完毕后，客户端和服务器会关闭连接。
总的来说，gRPC框架基于HTTP/2协议和Protocol Buffers序列化协议实现了高效的跨语言远程过程调用，使得客户端和服务器可以像调用本地方法一样调用远程方法。同时，gRPC提供了许多功能，如流式处理、认证、拦截器等，使得它成为一个强大的RPC框架。
