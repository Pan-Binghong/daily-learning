---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5KEYIBN%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BQuFSmcHVzo0vLAysr4rwlON%2B%2BjqhUjepXYZzfDoZ9gIgXOcb6nMb0gRJ7CgspQ57u1LArhaP0ocF7Gp6c8%2BeocAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDJx%2FV8K9L70YpJZ3CrcA66LzgIXIKSUn18mudHjawDt9DjdY%2B1itB4haRmROqhPIKEKwAkxrBvWmH2vnUIJcEUBwaivr742Kc8PECqaZw10107ifZYciGbmbmZirb76bx6PbrmhG8GQ4SC308FPu4LtBeZTpAaxI5Rapz%2B849Udh80AaVQnB%2B4D9viNv%2BVKSh9eP0E6GOVwQlHa9ppPboXtkbXDCfh22gK1UVxbrQAzBdHVGSpLwpj5Z4mOSU0WYJArtIlJ0Wu1aEfMmrS5r4iwNT4LcRbIPJH8NrHoyV3pDpwSQKmzzO6eLrYaU%2Fe5ahRQdhwL4dyzD37ujxzFbCNcFVwRe87laKKc51gymyJenceeQPHu%2F8VEOGxbLHNZRaMGd513sNSm9AY%2BTs1gNO5799uPi2Iqp8dVG8g%2BXxVDaeg1U6Lf8xPZQfBNr%2FXdgRsnuR5yut3i1sqdIABJxDYXsVHX8%2BMHiRofdvB3cEIDyxKDx2e0CAQjhsn7Z%2F9qCqAe8j6Scc4fVpFOL4v6jJcUCP%2BZM8eRlO1fg2EIK5C42jG1U8oarhqk764Wdd29oBIpsEBPsPZUkZ84IYf16rlMidqbhPTRKmLmZcI82kQcX35B0JkEaLsCdP5kpXc8qRwCBSbhvRQV%2FFgMMMzvvMoGOqUB1%2FEim9MHITORgy74h7wk5RuZZO%2FEujCen2kGDQlsu01JfNMmIlE9lD3zpBDAz1y4zWbBRO7Fc6EmDDTr6EXpSYa8lceNiNBnHO2aUjkpOOi%2FugU3xawzJKd2NKsgnbvxhkBmJo63pn4lYmFOBrOa5xOXiXkLZV8%2FkISpynhrMRFvBqZe8UJuqNQ908bwz7kmXlsd%2BGWBjTdC5nzzdGmhM8wPwYNA&X-Amz-Signature=f8813bce773fbb507ee4da98cd900512bf5b9b53934c5800dfa683c84e262240&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

