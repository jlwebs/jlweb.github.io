##### redis的跳表 Vs mysql的B+树
先说结论：B+树是为了减少磁盘I/O， 查询利好，实现复杂；跳表实现简单，无磁盘I/O时写入占优；
具体分析：先看结构定义
![](https://cdn.nlark.com/yuque/0/2023/png/26575180/1695091757294-a6323d6c-725c-45ee-921e-87c88c1caefd.png#averageHue=%23dae4e5&clientId=ueb419e01-cfd7-4&from=paste&height=311&id=u48d9b8d7&originHeight=617&originWidth=1080&originalType=url&ratio=2.559999942779541&rotation=0&showTitle=false&status=done&style=none&taskId=uda70b985-7673-4fbc-8811-b130e20ebc6&title=&width=544.00830078125)
![](https://cdn.nlark.com/yuque/0/2023/png/26575180/1695091781738-a3af848d-928a-4141-9982-f3bca304900f.png#averageHue=%23e9edef&clientId=ueb419e01-cfd7-4&from=paste&height=163&id=u41475e58&originHeight=309&originWidth=1080&originalType=url&ratio=2.559999942779541&rotation=0&showTitle=false&status=done&style=none&taskId=u0460208d-167d-4d50-884e-1630706ae6e&title=&width=570.00830078125)
B+树：

      - B+ 树是多叉树结构，每个叶节点都是一个 16k 的数据页
