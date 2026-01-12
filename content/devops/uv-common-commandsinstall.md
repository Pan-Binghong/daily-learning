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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVA3QBE5%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDxy1hoejFVAS646DbUHO5mC%2Bdm%2F9DmkjWT%2ByHAwgCU2gIgOeoSW9HrkbciDGyIW4h8nZWSveBtQ26UHbbbvySTYMIqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNl6%2FdjKRA0Fx6zHCrcAyhGadMdk4SrwIGf5hPglzsCSQDdW%2Fu5B9iVHyBkkZzeGxQqPHBIk5J3PUkPd5JuH9FJyg5jG2hEcyRMC9Zi%2B2%2BCY766phFuxv6ZcZG4Pwp%2BydPOiWIjDv0qBz%2B5AtQZvuug%2FgEuo0JwQr0FpSVaydX29Yh2ybwhGzoE1UXzLaPKtE3WU1SBcqCQ1f%2Bf6MzgKhrRu5s2f%2FD2VARVqf3iPZKRHWy3e6Sbqx3VYdVvcJaduvD%2FJiM2%2FsPlEu3jqPJPg2IUTi6WHS3z%2BPp9U%2FhyBPK6iu006b9llFQr4pABHatnAoUDUspI2A2MKpLQep8B3ViBZjFwp8frJeBDcpvMDVwP2gZt0nB%2BB5%2B8R81OVYUhZRvvMOlVjKJ%2F8hHY9wNZ4vzkLjwrhgnNMxZcS9gjDVtGf5Ey0%2F2QxKLE23b6YYGv4nZrFggDiHGUmBRw7Ij2fb%2F7wbRD4HP4WQdzkRjctKU%2FBSS%2FODhQJ93U44tChHRjQQMHZpAfiVXa1UzNFuZfzqu6sHzyBedyH1zYkyV0qzEzmrqx%2F52Cxp0YtLQHDuSRHNshvx457WhjAxBxXWpgxK5CwBN7joc2jTJSdFbU%2B6qMLPQlykYVRYU30%2BZoDOXX1gYa14q5fINTR68NMPL3kMsGOqUBhLzjtQM%2Fltofazv%2FnLj2OKaounLetvQJqC1%2B5UrjfBepYvfS1eBTO2NZTWAMkXjqVmxC8gwQkv%2Fzseirpq4z1oRAgIUdolrmcD3bNG8vkgAL853UH99HSFXWuJAb4dF8nI1FcnbUSE82FAgdAs5Cf0PlosLZKCWVlWrEjbUaC5ojvntVrsqbZn1Eeq09yeC4hj2F7V1aXZBU%2BDt4fDDatctIv5x%2F&X-Amz-Signature=572e128c1827b013b727d942e9397fad67147f7bef84f15480e0549d0ec55ad2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVA3QBE5%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDxy1hoejFVAS646DbUHO5mC%2Bdm%2F9DmkjWT%2ByHAwgCU2gIgOeoSW9HrkbciDGyIW4h8nZWSveBtQ26UHbbbvySTYMIqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNl6%2FdjKRA0Fx6zHCrcAyhGadMdk4SrwIGf5hPglzsCSQDdW%2Fu5B9iVHyBkkZzeGxQqPHBIk5J3PUkPd5JuH9FJyg5jG2hEcyRMC9Zi%2B2%2BCY766phFuxv6ZcZG4Pwp%2BydPOiWIjDv0qBz%2B5AtQZvuug%2FgEuo0JwQr0FpSVaydX29Yh2ybwhGzoE1UXzLaPKtE3WU1SBcqCQ1f%2Bf6MzgKhrRu5s2f%2FD2VARVqf3iPZKRHWy3e6Sbqx3VYdVvcJaduvD%2FJiM2%2FsPlEu3jqPJPg2IUTi6WHS3z%2BPp9U%2FhyBPK6iu006b9llFQr4pABHatnAoUDUspI2A2MKpLQep8B3ViBZjFwp8frJeBDcpvMDVwP2gZt0nB%2BB5%2B8R81OVYUhZRvvMOlVjKJ%2F8hHY9wNZ4vzkLjwrhgnNMxZcS9gjDVtGf5Ey0%2F2QxKLE23b6YYGv4nZrFggDiHGUmBRw7Ij2fb%2F7wbRD4HP4WQdzkRjctKU%2FBSS%2FODhQJ93U44tChHRjQQMHZpAfiVXa1UzNFuZfzqu6sHzyBedyH1zYkyV0qzEzmrqx%2F52Cxp0YtLQHDuSRHNshvx457WhjAxBxXWpgxK5CwBN7joc2jTJSdFbU%2B6qMLPQlykYVRYU30%2BZoDOXX1gYa14q5fINTR68NMPL3kMsGOqUBhLzjtQM%2Fltofazv%2FnLj2OKaounLetvQJqC1%2B5UrjfBepYvfS1eBTO2NZTWAMkXjqVmxC8gwQkv%2Fzseirpq4z1oRAgIUdolrmcD3bNG8vkgAL853UH99HSFXWuJAb4dF8nI1FcnbUSE82FAgdAs5Cf0PlosLZKCWVlWrEjbUaC5ojvntVrsqbZn1Eeq09yeC4hj2F7V1aXZBU%2BDt4fDDatctIv5x%2F&X-Amz-Signature=85ea5081754afe3e65f97ad51a7cff4a8c1323193f3b6b6a15ee7caa184f702b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVA3QBE5%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDxy1hoejFVAS646DbUHO5mC%2Bdm%2F9DmkjWT%2ByHAwgCU2gIgOeoSW9HrkbciDGyIW4h8nZWSveBtQ26UHbbbvySTYMIqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNl6%2FdjKRA0Fx6zHCrcAyhGadMdk4SrwIGf5hPglzsCSQDdW%2Fu5B9iVHyBkkZzeGxQqPHBIk5J3PUkPd5JuH9FJyg5jG2hEcyRMC9Zi%2B2%2BCY766phFuxv6ZcZG4Pwp%2BydPOiWIjDv0qBz%2B5AtQZvuug%2FgEuo0JwQr0FpSVaydX29Yh2ybwhGzoE1UXzLaPKtE3WU1SBcqCQ1f%2Bf6MzgKhrRu5s2f%2FD2VARVqf3iPZKRHWy3e6Sbqx3VYdVvcJaduvD%2FJiM2%2FsPlEu3jqPJPg2IUTi6WHS3z%2BPp9U%2FhyBPK6iu006b9llFQr4pABHatnAoUDUspI2A2MKpLQep8B3ViBZjFwp8frJeBDcpvMDVwP2gZt0nB%2BB5%2B8R81OVYUhZRvvMOlVjKJ%2F8hHY9wNZ4vzkLjwrhgnNMxZcS9gjDVtGf5Ey0%2F2QxKLE23b6YYGv4nZrFggDiHGUmBRw7Ij2fb%2F7wbRD4HP4WQdzkRjctKU%2FBSS%2FODhQJ93U44tChHRjQQMHZpAfiVXa1UzNFuZfzqu6sHzyBedyH1zYkyV0qzEzmrqx%2F52Cxp0YtLQHDuSRHNshvx457WhjAxBxXWpgxK5CwBN7joc2jTJSdFbU%2B6qMLPQlykYVRYU30%2BZoDOXX1gYa14q5fINTR68NMPL3kMsGOqUBhLzjtQM%2Fltofazv%2FnLj2OKaounLetvQJqC1%2B5UrjfBepYvfS1eBTO2NZTWAMkXjqVmxC8gwQkv%2Fzseirpq4z1oRAgIUdolrmcD3bNG8vkgAL853UH99HSFXWuJAb4dF8nI1FcnbUSE82FAgdAs5Cf0PlosLZKCWVlWrEjbUaC5ojvntVrsqbZn1Eeq09yeC4hj2F7V1aXZBU%2BDt4fDDatctIv5x%2F&X-Amz-Signature=91fef04d8ade4b552968cf8ba882e01f0a06cb336273bf030a7f9ea24558b602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

