###### 0.关闭同步流 笔试提高输入输出速度模板
 ` int main() {`
`   std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);`
`  }  `
###### 1.c++从标准输入读取一行数据
string line; 
getline(cin, line);
getline(std::istream& is, std::string& str, char delim); 
//每次取delim前的一个string（delim不能为string）
> 可选参数，表示分隔符，默认为换行符 **\n**。当遇到该分隔符时，**std::getline** 将停止读取，将读取的内容存储在 **str** 中。

但回车符在输入流中是被剔除了的，不会像cin>>int后需要手动getchar();去除
```cpp
stringstream s
istringstream is
ostringstream os 
```
###### 2.万能头文件 
#include<bits/stdc++.h>

3.手动头文件引入
```cpp
#include <iostream>     // 输入输出流
#include <vector>       // 动态数组容器
#include <string>       // 字符串处理
#include <queue>        // 队列容器
#include <stack>        // 栈容器
#include <list>         // 双向链表容器
#include <map>          // 有序映射
#include <unordered_map>  // 哈希表容器（无序映射）
#include <set>          // 有序集合
#include <unordered_set>  // 哈希集合容器（无序集合）
#include <algorithm>    // 常见算法（排序、查找等）
#include <utility>      // 常用工具函数（pair类模板等）
#include <bitset>       // 位集容器
#include <cmath>        // 数学函数库
#include <cstdlib>      // 标准库函数
#include <cstring>      // 字符串处理函数库
#include <iomanip>      // 输入输出格式控制
#include <sstream>      // 字符串流，用于字符串处理
#include <fstream>      // 文件流，用于文件操作
#include <numeric>      // 数值算法，如部分和、累加等
#include <functional>   // 函数对象，用于自定义排序、比较等
#include <ctime>        // 时间和日期处理
#include <chrono>       // 高精度时间库
#include <random>       // 随机数库
#include <numeric>
```

4.处理回车符号
int n; cin >> n; 
cin.ignore(); // To ignore the newline character after reading 'n'

5.while暴读逻辑
如果输入中包含回车、制表符（Tab）或其他转义符，cin >> n 默认情况下会跳过它们并继续读取下一个有效的输入。对于输入中包含的空格，cin >> n 也会将它们视为分隔符，因此会忽略它们。
cin>>str 字符串只能接收一个单词

6.带浮点数的输出
printf("%.2f\n", sum / count);

7.完整案例
```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    int nn;

    while(cin >> n){
        string s;
        std::vector<int> v; 
        getchar();
        while(n--){
            cin >> nn ;
            getchar();
            getline(cin, s);
            stringstream ss(s);
            string each;
            while(getline(ss, each, ' ')){
                v.push_back(stoi(each));
            }
            cout<<accumulate(v.begin(), v.end(), 0);
            if(n!=0) cout<<endl<<endl;
            else cout<<endl;
            v.clear();
        }
    }
    return 0;
}


```
除非像此题告诉了求和元素有多少个，可以用cin>>int不断读入并计次减少，不然只能实现一个C++版本的split函数
```cpp
string s;
getline(cin,s);
getchar() //如果有遗留缓冲区需要处理的\n或者空格需要执行
stringstream ss(s);
// istream ss(s)
string substr;
getline(ss, substr, ' ') //delimeter 是空格
stoi(substr) //转整数
```
8.二叉树和单链表定义
```cpp
struct ListNode{
    int val;
    ListNode* next;
    ListNode() :val(0), next(nullptr) {}
};

//优化↓
struct ListNode{
    int val;
    ListNode* next;
    ListNode(int v=0) :val(v), next(nullptr) {}
};
```
```cpp
struct TreeNode{
    int val;
    TreeNode* left;
	TreeNode* right;
    ListNode() :val(0), left(nullptr), right(nullptr) {}
};
```
