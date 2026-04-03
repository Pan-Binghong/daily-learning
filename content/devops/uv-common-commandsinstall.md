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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLC33XRP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOOtQFpwYja95lwgBrt6%2FZ0BKoDE6ZRCAehFEUsp9xKAiBxdPwlIolLOJJnyHZvXiOeo2hj8gQegE7lb%2BpTw21tCir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMbm3coPxkYuEsB9ipKtwD3D1hEDSElVeAwI539oFjzTl4%2BTAFYTaV8VmyVrKO0xZMhiaX1f%2BVuAFQQZrLYIYchW8y1AzJfGElyRRcv7ptbjwiYUri%2FHEEBZ8p2ZtBXkQubr78SY2afq%2BB23wvjP7YMaRL8KR5MQWmkL%2FSnnx1ZYeeMH%2BCdrl2Y9UQi81CwnioQfVXiY7i4khyaejMHkS1bdrePc%2Ff8TYOv6qb%2B34%2FuzyTY%2FuOEA2ZO59tG8nsX%2FW1lsgDr2KvtufJcOX4PQWE1Vst3JwaLtME8f17khWLD1hbW3ryTe80pOVteLFYs6DU9Er2%2BSGPv1N66Gl3PiXYhM83ca%2FfVxJt7lYoEd5HronUhIqcOo5jkyoe0h0TcsCmG00nh4mdTCFvJp7tlFIpKcDHS6qrDaxBfZB84GbEKWtf5Op%2FBOKq8lhd0oI6unsaiSOM6lvIf7eJpbo6F0ujGVbGUhIuVhfZMteeZYvfiBQ3UAwhNvRMIK0BhSqOXB2upETpPHkeuwE4sB7u6p2zWY%2Bzv%2BekIHlJ1kt%2FD1KuzqlLqVdSGx31JpTlkiK917SXQl2sYJpHv1UinkZmsJPblAQfXRhwy8pHEccmkYEXauInUkCIGRUQrkeSJAxy0vmo8zOkX3H6fIFe17kw%2FOe8zgY6pgFimCeNN9Nlg5FRsyKabC%2FtfPdFktZtw7tqhrRSUMQQf6AjAMUWhzGEz5G63XHCqeJsu68HI%2FRqomckZ481XmitAo1ZMFiVcpAuE6iVtrCctdTuVpv96hwebVVXXPRmogbcV%2BjKICxJxsNstF29b5rroxkkctgcpmV51qQqHgGvbVl1wz56mZCRbMMzyqDMVsMSlI4nqtuH2p4Hc%2BxmM3O51KVwN0%2Fq&X-Amz-Signature=caee629ac4c3a6a2dadb39eec311f0b242a02762344d3815d2f11f2940ea8ba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLC33XRP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOOtQFpwYja95lwgBrt6%2FZ0BKoDE6ZRCAehFEUsp9xKAiBxdPwlIolLOJJnyHZvXiOeo2hj8gQegE7lb%2BpTw21tCir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMbm3coPxkYuEsB9ipKtwD3D1hEDSElVeAwI539oFjzTl4%2BTAFYTaV8VmyVrKO0xZMhiaX1f%2BVuAFQQZrLYIYchW8y1AzJfGElyRRcv7ptbjwiYUri%2FHEEBZ8p2ZtBXkQubr78SY2afq%2BB23wvjP7YMaRL8KR5MQWmkL%2FSnnx1ZYeeMH%2BCdrl2Y9UQi81CwnioQfVXiY7i4khyaejMHkS1bdrePc%2Ff8TYOv6qb%2B34%2FuzyTY%2FuOEA2ZO59tG8nsX%2FW1lsgDr2KvtufJcOX4PQWE1Vst3JwaLtME8f17khWLD1hbW3ryTe80pOVteLFYs6DU9Er2%2BSGPv1N66Gl3PiXYhM83ca%2FfVxJt7lYoEd5HronUhIqcOo5jkyoe0h0TcsCmG00nh4mdTCFvJp7tlFIpKcDHS6qrDaxBfZB84GbEKWtf5Op%2FBOKq8lhd0oI6unsaiSOM6lvIf7eJpbo6F0ujGVbGUhIuVhfZMteeZYvfiBQ3UAwhNvRMIK0BhSqOXB2upETpPHkeuwE4sB7u6p2zWY%2Bzv%2BekIHlJ1kt%2FD1KuzqlLqVdSGx31JpTlkiK917SXQl2sYJpHv1UinkZmsJPblAQfXRhwy8pHEccmkYEXauInUkCIGRUQrkeSJAxy0vmo8zOkX3H6fIFe17kw%2FOe8zgY6pgFimCeNN9Nlg5FRsyKabC%2FtfPdFktZtw7tqhrRSUMQQf6AjAMUWhzGEz5G63XHCqeJsu68HI%2FRqomckZ481XmitAo1ZMFiVcpAuE6iVtrCctdTuVpv96hwebVVXXPRmogbcV%2BjKICxJxsNstF29b5rroxkkctgcpmV51qQqHgGvbVl1wz56mZCRbMMzyqDMVsMSlI4nqtuH2p4Hc%2BxmM3O51KVwN0%2Fq&X-Amz-Signature=6fe5aa49624c3dc28e5be0621337fb40bcf7b52fe40e2247ef7373af857f76dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLC33XRP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOOtQFpwYja95lwgBrt6%2FZ0BKoDE6ZRCAehFEUsp9xKAiBxdPwlIolLOJJnyHZvXiOeo2hj8gQegE7lb%2BpTw21tCir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMbm3coPxkYuEsB9ipKtwD3D1hEDSElVeAwI539oFjzTl4%2BTAFYTaV8VmyVrKO0xZMhiaX1f%2BVuAFQQZrLYIYchW8y1AzJfGElyRRcv7ptbjwiYUri%2FHEEBZ8p2ZtBXkQubr78SY2afq%2BB23wvjP7YMaRL8KR5MQWmkL%2FSnnx1ZYeeMH%2BCdrl2Y9UQi81CwnioQfVXiY7i4khyaejMHkS1bdrePc%2Ff8TYOv6qb%2B34%2FuzyTY%2FuOEA2ZO59tG8nsX%2FW1lsgDr2KvtufJcOX4PQWE1Vst3JwaLtME8f17khWLD1hbW3ryTe80pOVteLFYs6DU9Er2%2BSGPv1N66Gl3PiXYhM83ca%2FfVxJt7lYoEd5HronUhIqcOo5jkyoe0h0TcsCmG00nh4mdTCFvJp7tlFIpKcDHS6qrDaxBfZB84GbEKWtf5Op%2FBOKq8lhd0oI6unsaiSOM6lvIf7eJpbo6F0ujGVbGUhIuVhfZMteeZYvfiBQ3UAwhNvRMIK0BhSqOXB2upETpPHkeuwE4sB7u6p2zWY%2Bzv%2BekIHlJ1kt%2FD1KuzqlLqVdSGx31JpTlkiK917SXQl2sYJpHv1UinkZmsJPblAQfXRhwy8pHEccmkYEXauInUkCIGRUQrkeSJAxy0vmo8zOkX3H6fIFe17kw%2FOe8zgY6pgFimCeNN9Nlg5FRsyKabC%2FtfPdFktZtw7tqhrRSUMQQf6AjAMUWhzGEz5G63XHCqeJsu68HI%2FRqomckZ481XmitAo1ZMFiVcpAuE6iVtrCctdTuVpv96hwebVVXXPRmogbcV%2BjKICxJxsNstF29b5rroxkkctgcpmV51qQqHgGvbVl1wz56mZCRbMMzyqDMVsMSlI4nqtuH2p4Hc%2BxmM3O51KVwN0%2Fq&X-Amz-Signature=e5044d48b25c0dd0783db48fedaea187d92019ef2dc4c688e85692f7be578150&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

