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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGO6ML4A%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFVeiDe3GwyPBtGM7T%2F8PGuWMZ3PI3QoNYJzEU7sLylQIgPTqZX%2FfeQ6PvDoEiWv0%2BFseg8KQlCxTdD4sT1N7zAfwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQd6kMONpSHOaG6QircAztgalet9XSgyqw%2B%2BB776T6O%2Bjgcg8n49SCtvLWNvMQlDTpYQjVKbnfDu%2FRR9YIySw8q7D216ge3SQVLFFsRELeMcYNaH5tWX%2FeLxO4hpW7LQp6r61uPUJNR7Us%2B3%2BwViK1f9SRTxMmVuBosUlShk2ykpvnMuUsImjDiNw9pnh6k2MI7OPmRPjbW5jq10nSPkbDCYPIsjR7AQWr1rCeE519rA2rBUKSgei%2BICZPLzmt8Sd3%2BnAZyKPI%2FnvnHWoeERsjFG5NoyWlzPXOp92xeq17UtDd8O2EbLaSkgqWbBSTgeDDJ783ycm43vsmHBXWy6SG%2BiOm%2FjIKjMX4TG4RXqWDnj7lu2D%2BrmgtL5S2K3PGyhHt3JrBGN2zxlk3IPVkuog1QP%2BDCTXpO4NXVILxG36ZjUqBuiBswwBAzWzbAMQaFwljAGAmkds%2Fb8vd6wCDF%2Bqg3ueX5Fln8dZ%2B21Y0%2BjwW3J%2B0owJshNAk9fsiR%2BszVAL%2Fl4kOJCA%2BA4lqk0GeJmphrvMfpr4XvFhfqY%2FIB6Lb4emzC2zwSXvdpFiLpBNErFA8iQ3UWDQVMP%2FUoq%2FHe7yzfYVlPoyHTXj17wlEqUiWwz9NFNRgzj8WLA4aYGxl9nyynMYziZvbBGPeXMLjDqswGOqUBtK%2BlgobMANJn9X8NiyM%2Bnw0NSMKHHIkrjupz9WD0IX6MqUOUPHTU35r3%2FkZk64%2B5Z8TjIg2%2Fia6a06FVUXLTGbVOWUfip8jwdQCu3iTYEh8pcTaxLimH4nvIbE2SypkKj%2FI5np1IA9ZoO1PRM4GgEO7DnnketxvnAbgN14WsWXUfP6yEdq3LmwA42gq26fXqRxsXJPZaqj6zsbLPnSswKtw9DLif&X-Amz-Signature=f442e0d115a2ccd14990d53fc64df12ecb4e614c86bb26ede783727309367ea0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGO6ML4A%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFVeiDe3GwyPBtGM7T%2F8PGuWMZ3PI3QoNYJzEU7sLylQIgPTqZX%2FfeQ6PvDoEiWv0%2BFseg8KQlCxTdD4sT1N7zAfwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQd6kMONpSHOaG6QircAztgalet9XSgyqw%2B%2BB776T6O%2Bjgcg8n49SCtvLWNvMQlDTpYQjVKbnfDu%2FRR9YIySw8q7D216ge3SQVLFFsRELeMcYNaH5tWX%2FeLxO4hpW7LQp6r61uPUJNR7Us%2B3%2BwViK1f9SRTxMmVuBosUlShk2ykpvnMuUsImjDiNw9pnh6k2MI7OPmRPjbW5jq10nSPkbDCYPIsjR7AQWr1rCeE519rA2rBUKSgei%2BICZPLzmt8Sd3%2BnAZyKPI%2FnvnHWoeERsjFG5NoyWlzPXOp92xeq17UtDd8O2EbLaSkgqWbBSTgeDDJ783ycm43vsmHBXWy6SG%2BiOm%2FjIKjMX4TG4RXqWDnj7lu2D%2BrmgtL5S2K3PGyhHt3JrBGN2zxlk3IPVkuog1QP%2BDCTXpO4NXVILxG36ZjUqBuiBswwBAzWzbAMQaFwljAGAmkds%2Fb8vd6wCDF%2Bqg3ueX5Fln8dZ%2B21Y0%2BjwW3J%2B0owJshNAk9fsiR%2BszVAL%2Fl4kOJCA%2BA4lqk0GeJmphrvMfpr4XvFhfqY%2FIB6Lb4emzC2zwSXvdpFiLpBNErFA8iQ3UWDQVMP%2FUoq%2FHe7yzfYVlPoyHTXj17wlEqUiWwz9NFNRgzj8WLA4aYGxl9nyynMYziZvbBGPeXMLjDqswGOqUBtK%2BlgobMANJn9X8NiyM%2Bnw0NSMKHHIkrjupz9WD0IX6MqUOUPHTU35r3%2FkZk64%2B5Z8TjIg2%2Fia6a06FVUXLTGbVOWUfip8jwdQCu3iTYEh8pcTaxLimH4nvIbE2SypkKj%2FI5np1IA9ZoO1PRM4GgEO7DnnketxvnAbgN14WsWXUfP6yEdq3LmwA42gq26fXqRxsXJPZaqj6zsbLPnSswKtw9DLif&X-Amz-Signature=d632150d0d42bb2ee183a54b7d83f8b5f4681600aecb1b2df1d82478ce518903&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGO6ML4A%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFVeiDe3GwyPBtGM7T%2F8PGuWMZ3PI3QoNYJzEU7sLylQIgPTqZX%2FfeQ6PvDoEiWv0%2BFseg8KQlCxTdD4sT1N7zAfwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQd6kMONpSHOaG6QircAztgalet9XSgyqw%2B%2BB776T6O%2Bjgcg8n49SCtvLWNvMQlDTpYQjVKbnfDu%2FRR9YIySw8q7D216ge3SQVLFFsRELeMcYNaH5tWX%2FeLxO4hpW7LQp6r61uPUJNR7Us%2B3%2BwViK1f9SRTxMmVuBosUlShk2ykpvnMuUsImjDiNw9pnh6k2MI7OPmRPjbW5jq10nSPkbDCYPIsjR7AQWr1rCeE519rA2rBUKSgei%2BICZPLzmt8Sd3%2BnAZyKPI%2FnvnHWoeERsjFG5NoyWlzPXOp92xeq17UtDd8O2EbLaSkgqWbBSTgeDDJ783ycm43vsmHBXWy6SG%2BiOm%2FjIKjMX4TG4RXqWDnj7lu2D%2BrmgtL5S2K3PGyhHt3JrBGN2zxlk3IPVkuog1QP%2BDCTXpO4NXVILxG36ZjUqBuiBswwBAzWzbAMQaFwljAGAmkds%2Fb8vd6wCDF%2Bqg3ueX5Fln8dZ%2B21Y0%2BjwW3J%2B0owJshNAk9fsiR%2BszVAL%2Fl4kOJCA%2BA4lqk0GeJmphrvMfpr4XvFhfqY%2FIB6Lb4emzC2zwSXvdpFiLpBNErFA8iQ3UWDQVMP%2FUoq%2FHe7yzfYVlPoyHTXj17wlEqUiWwz9NFNRgzj8WLA4aYGxl9nyynMYziZvbBGPeXMLjDqswGOqUBtK%2BlgobMANJn9X8NiyM%2Bnw0NSMKHHIkrjupz9WD0IX6MqUOUPHTU35r3%2FkZk64%2B5Z8TjIg2%2Fia6a06FVUXLTGbVOWUfip8jwdQCu3iTYEh8pcTaxLimH4nvIbE2SypkKj%2FI5np1IA9ZoO1PRM4GgEO7DnnketxvnAbgN14WsWXUfP6yEdq3LmwA42gq26fXqRxsXJPZaqj6zsbLPnSswKtw9DLif&X-Amz-Signature=2a27458f4498863a6ed30df8c81bfda755f5861a3f221b29c3b6cc2cf524b5dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

