---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466324MNMKE%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIBx21yX%2FEZMnmsGYXR0Dq57n30I4pW9HJE0vB68te6m2AiEAnfvyHzYVp00bjpf9MXPLLzBKLuUo%2FDDIffEWtferuvQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqPfEZQd0atxV%2FzhircA9O2gZzP5wykX4m%2BYfgwI2zWui%2FF2efL4naEtVyVnMaeHC%2BjtSypMGYoCosbBCRfAuaTWX4QfVLtfq9XrZH%2FB3sPv1OEg82jmk0neMY%2BVWsMROykrNMACzi4pNcfrJgNhADiWCPIotS%2FiTnFoY%2FVsi5Mjt8kNhZ%2FqkAxeuHfyOfO7PC1BmFGONn4juHvRa6JIPqjUvV2C4sAlTVgTUrHqpht8KCKB7aU9VsaeqVwQgnlEE56q1oO7QkoIQF9G77eXy5BeANbKsVi0MW2Zpg5DdwJBKQw7Pm4LjmSd%2BzCk6QVsmb63Z%2BbKPtSol%2BO8Gpcs%2F8VcYStIclsAeowTQ38s3drowzG4HoeWSJnvIcq5ZwEnn7joABQugKA9xqO4OrnhLttnWkxBCWhbEzf5cLpJo%2F%2FgzmG%2FEGW7KJsQDbxWzcxm76s1LOxXlZ5HN%2BcDNVsdOcxjSEXiOqT0jOV4jCihYwo1inf1KFxC0aTb7Wjk0NGUpiNLZZu4lAY%2FlCw8MVkCT2US%2BkStELl%2FeuYXq6oSgm0BEYBJId2KeCn6ex8XgNAR3xU7e7%2Be4pGh1FDLRv6mnjWadsuBO%2BcrrhxByzNo3cStR%2F3BFqQswtgGbtWqQem2VKHDHhMsL2TMtdbMLCvy8sGOqUBlEl%2BuV61vm2VJFupQKpDc8TE2ELAjTOJ3Q5tO5e5Xue2PVWOXhReCZB1cKuW9JzX60VE%2B7ZaXRVBbbtaYWF2fljPClZt4rn54%2FlnAaD0k32MHhpOI4dn4n9sBbRwZikIvrdy1y1dIAET9DzTte7z6ascWMELBxNAX6iszN4oQaHgQqrCtelIcJwOlKWytLfDb2jK%2BNm1rIXU4OOS5qR%2FH1Bo4r7w&X-Amz-Signature=6e98891786b09e5d753e0446f0ddd1750d1be0fb76ff98a4ae3480673c685985&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466324MNMKE%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIBx21yX%2FEZMnmsGYXR0Dq57n30I4pW9HJE0vB68te6m2AiEAnfvyHzYVp00bjpf9MXPLLzBKLuUo%2FDDIffEWtferuvQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqPfEZQd0atxV%2FzhircA9O2gZzP5wykX4m%2BYfgwI2zWui%2FF2efL4naEtVyVnMaeHC%2BjtSypMGYoCosbBCRfAuaTWX4QfVLtfq9XrZH%2FB3sPv1OEg82jmk0neMY%2BVWsMROykrNMACzi4pNcfrJgNhADiWCPIotS%2FiTnFoY%2FVsi5Mjt8kNhZ%2FqkAxeuHfyOfO7PC1BmFGONn4juHvRa6JIPqjUvV2C4sAlTVgTUrHqpht8KCKB7aU9VsaeqVwQgnlEE56q1oO7QkoIQF9G77eXy5BeANbKsVi0MW2Zpg5DdwJBKQw7Pm4LjmSd%2BzCk6QVsmb63Z%2BbKPtSol%2BO8Gpcs%2F8VcYStIclsAeowTQ38s3drowzG4HoeWSJnvIcq5ZwEnn7joABQugKA9xqO4OrnhLttnWkxBCWhbEzf5cLpJo%2F%2FgzmG%2FEGW7KJsQDbxWzcxm76s1LOxXlZ5HN%2BcDNVsdOcxjSEXiOqT0jOV4jCihYwo1inf1KFxC0aTb7Wjk0NGUpiNLZZu4lAY%2FlCw8MVkCT2US%2BkStELl%2FeuYXq6oSgm0BEYBJId2KeCn6ex8XgNAR3xU7e7%2Be4pGh1FDLRv6mnjWadsuBO%2BcrrhxByzNo3cStR%2F3BFqQswtgGbtWqQem2VKHDHhMsL2TMtdbMLCvy8sGOqUBlEl%2BuV61vm2VJFupQKpDc8TE2ELAjTOJ3Q5tO5e5Xue2PVWOXhReCZB1cKuW9JzX60VE%2B7ZaXRVBbbtaYWF2fljPClZt4rn54%2FlnAaD0k32MHhpOI4dn4n9sBbRwZikIvrdy1y1dIAET9DzTte7z6ascWMELBxNAX6iszN4oQaHgQqrCtelIcJwOlKWytLfDb2jK%2BNm1rIXU4OOS5qR%2FH1Bo4r7w&X-Amz-Signature=e6a0c6fd42a2ac306538c963e68d8dd68a780b29ce38bb6c0ab979c674f50a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466324MNMKE%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIBx21yX%2FEZMnmsGYXR0Dq57n30I4pW9HJE0vB68te6m2AiEAnfvyHzYVp00bjpf9MXPLLzBKLuUo%2FDDIffEWtferuvQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqPfEZQd0atxV%2FzhircA9O2gZzP5wykX4m%2BYfgwI2zWui%2FF2efL4naEtVyVnMaeHC%2BjtSypMGYoCosbBCRfAuaTWX4QfVLtfq9XrZH%2FB3sPv1OEg82jmk0neMY%2BVWsMROykrNMACzi4pNcfrJgNhADiWCPIotS%2FiTnFoY%2FVsi5Mjt8kNhZ%2FqkAxeuHfyOfO7PC1BmFGONn4juHvRa6JIPqjUvV2C4sAlTVgTUrHqpht8KCKB7aU9VsaeqVwQgnlEE56q1oO7QkoIQF9G77eXy5BeANbKsVi0MW2Zpg5DdwJBKQw7Pm4LjmSd%2BzCk6QVsmb63Z%2BbKPtSol%2BO8Gpcs%2F8VcYStIclsAeowTQ38s3drowzG4HoeWSJnvIcq5ZwEnn7joABQugKA9xqO4OrnhLttnWkxBCWhbEzf5cLpJo%2F%2FgzmG%2FEGW7KJsQDbxWzcxm76s1LOxXlZ5HN%2BcDNVsdOcxjSEXiOqT0jOV4jCihYwo1inf1KFxC0aTb7Wjk0NGUpiNLZZu4lAY%2FlCw8MVkCT2US%2BkStELl%2FeuYXq6oSgm0BEYBJId2KeCn6ex8XgNAR3xU7e7%2Be4pGh1FDLRv6mnjWadsuBO%2BcrrhxByzNo3cStR%2F3BFqQswtgGbtWqQem2VKHDHhMsL2TMtdbMLCvy8sGOqUBlEl%2BuV61vm2VJFupQKpDc8TE2ELAjTOJ3Q5tO5e5Xue2PVWOXhReCZB1cKuW9JzX60VE%2B7ZaXRVBbbtaYWF2fljPClZt4rn54%2FlnAaD0k32MHhpOI4dn4n9sBbRwZikIvrdy1y1dIAET9DzTte7z6ascWMELBxNAX6iszN4oQaHgQqrCtelIcJwOlKWytLfDb2jK%2BNm1rIXU4OOS5qR%2FH1Bo4r7w&X-Amz-Signature=0bc2373476acd05e685f872a2c8456abdea94a947a4b9b6cf20e100e4aa93e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

