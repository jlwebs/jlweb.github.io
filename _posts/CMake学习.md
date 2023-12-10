##### 1.基础命令
创建指定名的项目
project(BankStealer Ver 1.0) 

2.常用参数学习
gcc atomic.c -lpthread -o atomic

1. **-lpthread**： 这是一个编译器选项，用于告诉编译器链接 POSIX 线程库（Pthreads）。在这里，"-lpthread" 表示链接程序时需要包括 pthread 库，以支持多线程编程。Pthreads 是一种用于多线程编程的标准库。
2. **-o atomic**： 这是一个编译器选项，用于指定生成的可执行文件的名称。在这里，"-o atomic" 表示生成的可执行文件将被命名为 "atomic"。



