###### 1.软中断分类
1. **系统调用（System Calls）：** 程序通过执行系统调用来请求操作系统提供特定服务，例如文件操作、进程管理、网络通信等。系统调用是通过软中断来实现的。
2. **异常处理（Exception Handling）：** 当程序执行中发生异常情况时，操作系统可以通过软中断来捕获和处理异常，例如分页错误、浮点运算溢出等。
3. **任务切换（Task Switching）：** 操作系统使用软中断来实现任务切换，以在多任务系统中切换执行不同的任务或进程。
4. **信号处理（Signal Handling）：** 进程可以通过软中断来处理信号，例如**SIGTERM**、**SIGINT**等，以响应外部事件或通信。
5. **软中断机制（Software Interrupt Mechanism）：** 一些操作系统和内核使用软中断机制来执行特定的任务，例如Linux内核的软中断，用于执行高性能网络栈和其他异步任务。

应用：

- kill终止进程基于信号传递的软中断
###### 2.硬中断分类

1. 时钟中断（Timer Interrupt）： 由计时器硬件触发，用于定期产生定时器中断，以便操作系统可以进行时间管理和任务调度。
2. 硬件设备中断： 由硬件设备触发，例如键盘、鼠标、磁盘驱动器、网络适配器等。这些中断通常用于通知操作系统有新的输入或输出数据可用。
3. 异常中断： 由CPU内部硬件或指令执行引发的异常情况触发，例如除零异常、页面错误、非法指令等。这些中断用于处理错误和异常情况。
4. 外部中断： 由外部事件触发的中断，例如电源故障、硬件故障等。这些中断通常用于通知系统发生了不可恢复的故障。
5. 中断控制器中断： 用于处理和调度各种硬件中断的专用硬件，例如PIC（可编程中断控制器）或APIC（高级可编程中断控制器）

应用：

- 操作系统调度的时间片轮转法就是基于时钟硬中断完成的；
###### 3.没有中断的后果
程序一直执行，无法进行切换调度，无法完成硬件响应，同时由于操作系统被阻塞，画面暂停，操作系统api无法调用，该程序实际上可以看做os了，无法被抢占；
> ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1693989319661-cb0ccb7c-9890-43dd-8478-0f85a527b522.png#averageHue=%23f1efee&clientId=u7e0ec250-aff6-4&from=paste&height=53&id=ua5708008&originHeight=136&originWidth=2044&originalType=binary&ratio=2.559999942779541&rotation=0&showTitle=false&size=61057&status=done&style=none&taskId=u41ea5774-9b12-4214-8b38-ed3fe89a46f&title=&width=798.4375178464693)

###### 4.软中断实现原理

- 构成软中断机制的核心元素包括：

1、 软中断[状态寄存器](https://baike.baidu.com/item/%E7%8A%B6%E6%80%81%E5%AF%84%E5%AD%98%E5%99%A8?fromModule=lemma_inlink)soft interrupt state（irq_stat）
2、 软[中断向量表](https://baike.baidu.com/item/%E4%B8%AD%E6%96%AD%E5%90%91%E9%87%8F%E8%A1%A8?fromModule=lemma_inlink)（softirq_vec）
3、 软中断守护daemon

- 软中断的工作工程模拟了实际的[中断处理](https://baike.baidu.com/item/%E4%B8%AD%E6%96%AD%E5%A4%84%E7%90%86?fromModule=lemma_inlink)过程，当某一软中断事件发生后，首先需要设置对应的中断标记位，触发中断事务，然后唤醒守护线程去检测中断[状态寄存器](https://baike.baidu.com/item/%E7%8A%B6%E6%80%81%E5%AF%84%E5%AD%98%E5%99%A8/2477799?fromModule=lemma_inlink)，如果通过查询发现有软中断事务发生，那么通过查询软中断向量表调用相应的软中断服务程序action（）。这就是软中断的过程，与[硬件中断](https://baike.baidu.com/item/%E7%A1%AC%E4%BB%B6%E4%B8%AD%E6%96%AD?fromModule=lemma_inlink)唯一不同的地方是从中断标记到[中断服务程序](https://baike.baidu.com/item/%E4%B8%AD%E6%96%AD%E6%9C%8D%E5%8A%A1%E7%A8%8B%E5%BA%8F?fromModule=lemma_inlink)的映射过程。在CPU的硬件中断发生之后，CPU需要将硬件[中断请求](https://baike.baidu.com/item/%E4%B8%AD%E6%96%AD%E8%AF%B7%E6%B1%82?fromModule=lemma_inlink)通过向量表映射成具体的服务程序，这个过程是硬件自动完成的，但是软中断不是，其需要守护线程去实现这一过程，这也就是软件模拟的中断，故称之为软中断。
- 一个软中断不会去抢占另一个软中断，只有硬件中断才可以抢占软中断，所以硬中断能够保证对时间的严格要求。
###### 5.附录

- kill程序详细内容

[操作系统笔记(4):通过信号signal进行进程间通信——kill()系统调用实现的软中断_如何用kill函数和signal函数进行两个客户之间的连续通信-CSDN博客](https://blog.csdn.net/Cake_C/article/details/116943692)
首先，信号处理是一种进程间通信的方式，允许一个进程通知另一个进程发生了特定事件。这些事件可以包括用户请求终止进程、重新加载配置、重新启动等。进程可以使用signal()或sigaction()等函数来设置信号处理程序，以定义在接收到信号时应采取的操作。
关于非强制kil信号：SIGTERM，这个信号处理函数是可以被程序员重定义的，而且
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26575180/1693991315477-654dfae0-8e76-4ca5-8da1-7bf89d3ce42f.png#averageHue=%23474a58&clientId=uee441abd-9f5c-4&from=paste&height=234&id=uefd5f754&originHeight=724&originWidth=1969&originalType=binary&ratio=2.559999942779541&rotation=0&showTitle=false&size=233699&status=done&style=none&taskId=u3984abc6-6a20-40cd-939f-8ccf992aa44&title=&width=636)

- 其他信号补充

signal 11 (SIGSEGV) ：

   - 段错误通常发生在访问非法内存地址的时候。系统会发送一个SIGSEGV11号信号告诉当前进程，进程采取默认的捕获方式，即终止进程。
   1. 野指针
   2. 试图修改字符串常量的内容

- 0x80软中断：系统调用先陷入内核态的转换指令

其中断的处理程序是system-call.s，后续可以继续看；
简单来说，会把系统调用函数所需要的参数通过寄存器先保存，之后再执行sys_call();
> 在用户空间和内核空间之间，有一个叫做Syscall(系统调用, system call)的中间层，是连接用户态和内核态的桥梁。这样即提高了内核的安全型，也便于移植，只需实现同一套接口即可。Linux系统，用户空间通过向内核空间发出Syscall，产生[软中断](https://so.csdn.net/so/search?q=%E8%BD%AF%E4%B8%AD%E6%96%AD&spm=1001.2101.3001.7020)，从而让程序陷入内核态，执行相应的操作。

- 0x32时钟中断：硬件中断，内核程序里才允许存在

