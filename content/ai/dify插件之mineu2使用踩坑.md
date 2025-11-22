---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OWRPYW6%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIAu8B3nvfY%2FwwUlZ7BC8m%2FDjfd4fqhMn%2FpUrjHC8UQIDAiBqIvckn6GDw7k0AHL3qtwg4g63BXG6%2FwPYT36q9Tpdoir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIM11%2F5SDi%2Fhzsg7MgcKtwDzILW47ReqTJlCATai8DdGVr4OX7aKnRSqmAWBuZVbs9MsiNj%2B9PqIZbj7BsIwKVwTnE6Adz%2FuC7FQfovR6FFyY74lVy2%2Bpzi2wEg%2Fa9m9%2BPXw2iqVmrCF7jQ5tHdvk6O0XUMgndI1buhdROf1PpECEjZdt3o257OfSUb%2FuNB4oI0q27aXCRjURTRLzNHN9Mk9UCTXMIvFp8QIUcgEsNdY2Jr4SEf2K92jf8i63R1tBNMy212c27JERXPaqeVz0UzZ3U%2BOtW7Jm0uak0T2SJXfKOXEpXceg3aUcZJmb8PqEIgelVWm%2B%2FGtHCwJk70hUcVN39rtouG0F5VqxvsXNcMEVLdQz9A7GBZ7J8Vtg2A0bBMeCz6B%2B2V19bzSFi6zU%2BHc4cA0NeQL0wFDXoaNpoo9Iu6%2Bft%2B1Qd%2BI8uAddlRYLRHanfJ%2Fx2EaWnypZIb36j6cFXrHgUB%2Bo2oxJ8uikloAeGlaMcyb3%2BauGJq0di9flJjQR6ViAkz4Kd6iGd1Jm%2B5nFyB2uIPL%2BYHyk6MVc3Ec6Rmm9XIuq3UnCf5yNFZeOqnhwR5aWb%2Ff6KhYolkCcu03HA34JBWnPaeWIyGCZDEW2dCh06Lum0cwYQeyTtl8vrhQBJ%2FiCuycx38kyIwyaCEyQY6pgGzIha58hNr%2FVgfEyOsboDNNET5m4gMLoKY0LJkDTiBNxnjYE33tEFEknTW7UKeOqi506b74xWY2kmnJoP2Fsp341zBdL%2FCWAnvd0l8huriUYSytFqI7NGlcxIpbslBVQjrmd3n1zXmz9A2h8K3AO2A%2FIj0ehB5zWCe2PPysQA1oEtMA3n%2Bi97ZwUrmfSZH%2Fa%2Ft2%2Byrov7VPj5fJOW8BN28d10Qnlzt&X-Amz-Signature=086038f148aa410ba7ea55f667a448492952ff17e7841990e1b796036aaee3f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OWRPYW6%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIAu8B3nvfY%2FwwUlZ7BC8m%2FDjfd4fqhMn%2FpUrjHC8UQIDAiBqIvckn6GDw7k0AHL3qtwg4g63BXG6%2FwPYT36q9Tpdoir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIM11%2F5SDi%2Fhzsg7MgcKtwDzILW47ReqTJlCATai8DdGVr4OX7aKnRSqmAWBuZVbs9MsiNj%2B9PqIZbj7BsIwKVwTnE6Adz%2FuC7FQfovR6FFyY74lVy2%2Bpzi2wEg%2Fa9m9%2BPXw2iqVmrCF7jQ5tHdvk6O0XUMgndI1buhdROf1PpECEjZdt3o257OfSUb%2FuNB4oI0q27aXCRjURTRLzNHN9Mk9UCTXMIvFp8QIUcgEsNdY2Jr4SEf2K92jf8i63R1tBNMy212c27JERXPaqeVz0UzZ3U%2BOtW7Jm0uak0T2SJXfKOXEpXceg3aUcZJmb8PqEIgelVWm%2B%2FGtHCwJk70hUcVN39rtouG0F5VqxvsXNcMEVLdQz9A7GBZ7J8Vtg2A0bBMeCz6B%2B2V19bzSFi6zU%2BHc4cA0NeQL0wFDXoaNpoo9Iu6%2Bft%2B1Qd%2BI8uAddlRYLRHanfJ%2Fx2EaWnypZIb36j6cFXrHgUB%2Bo2oxJ8uikloAeGlaMcyb3%2BauGJq0di9flJjQR6ViAkz4Kd6iGd1Jm%2B5nFyB2uIPL%2BYHyk6MVc3Ec6Rmm9XIuq3UnCf5yNFZeOqnhwR5aWb%2Ff6KhYolkCcu03HA34JBWnPaeWIyGCZDEW2dCh06Lum0cwYQeyTtl8vrhQBJ%2FiCuycx38kyIwyaCEyQY6pgGzIha58hNr%2FVgfEyOsboDNNET5m4gMLoKY0LJkDTiBNxnjYE33tEFEknTW7UKeOqi506b74xWY2kmnJoP2Fsp341zBdL%2FCWAnvd0l8huriUYSytFqI7NGlcxIpbslBVQjrmd3n1zXmz9A2h8K3AO2A%2FIj0ehB5zWCe2PPysQA1oEtMA3n%2Bi97ZwUrmfSZH%2Fa%2Ft2%2Byrov7VPj5fJOW8BN28d10Qnlzt&X-Amz-Signature=a1cdf222f0ca2689933a21fb7d84f047e2e7895c2820ac384f02f8e09641a916&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



