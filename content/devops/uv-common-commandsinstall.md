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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVP7WMH%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZQFnh%2B1CiHChll7GBB%2Bk8z90O8rjPUIU357rSrIMdowIhAMABoZTBz6iuV7kiZ%2BDe9GJ7qFslpEQaS02ncskYYQIkKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDPnXGTZgIj1wdcNQq3APjW8sYtJXJU5N7I1MSNVssPD01bmJF6z0TeGg4HFcK1vFN0WGVPDKCqUyGHZcgxmEajT4hCfvg%2BzPevh2rEU6eyTto5Qsg7UnIr4FMbZBbe9DQc2ARbjAneoY9IDsVjuELoZPAfofhGgC%2BAeo5l9mq1qa44iC81y8ZSnSVYqkuoeTr9siAOkZON%2FIxXkCwnP68LI36zcRbts3Kr%2FgSmOrod90e%2FAU0Y1OOiZL4vXOptUq4HH8XjbvV0B5ZMYqfR%2F%2FoU%2Fpb1M2xUhHKI1HGPP2DMEqXmmgE4K3iF0pncfqSmWxwFHuBsyQPVtIVv%2Fpw58ah7Vmi0LLEZIkywxVd%2FCoBclopJAYVwLM8V9ah8EuzL2mo7u9q5z0xYYVkACP9Uf4IWctTUNH0nd4FwQTH4EGDVzDUDfXTsOo%2BI66VuosvRWq1f%2BHE%2B%2BhyVFkk6OwUQPDjyXqL4SXlcdLnUYA8ozrtqa%2B5UNc1WMI2LC11myPTg7cS0%2F2IaJ0ryJjG5J2maDX%2F%2BSijMx44yq62%2B3VFbmWc1zkWvXvS7DkmRFqaauaPm5L3Us7w9x3tdZpGvY8Hnc4Covz4%2Bgf38UzBe2CKbpx3EaLjxNy0bImFSBIAoh8CXCiKzqzdU3MLCZlpsjC8tIHPBjqkAXQP11aXY8mk%2Bx4bM0t6o3UGmcbY%2BFh0IjDH1WhvHzPxeUzAKKCpWfFUY9QSTBzEikL7NFpuBwdP1RTpJ%2BWSXJDjoxt8WVwFOl2Ewswyd9P5V7FRjqg16CCf6LEvOeOAY5e58IHFj7jZqAIHnwl8AoKGn%2FoYsHQofEt7AE38XQGrx67DGQ%2Bsz9UdUMHs1Y58ZwFNwYOPFm%2BRw0iAnQwqU3np2t6f&X-Amz-Signature=36acdaac0ea357058f683ab42416ed0a9dca1797fbbb60b2159c2fe1b80010f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVP7WMH%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZQFnh%2B1CiHChll7GBB%2Bk8z90O8rjPUIU357rSrIMdowIhAMABoZTBz6iuV7kiZ%2BDe9GJ7qFslpEQaS02ncskYYQIkKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDPnXGTZgIj1wdcNQq3APjW8sYtJXJU5N7I1MSNVssPD01bmJF6z0TeGg4HFcK1vFN0WGVPDKCqUyGHZcgxmEajT4hCfvg%2BzPevh2rEU6eyTto5Qsg7UnIr4FMbZBbe9DQc2ARbjAneoY9IDsVjuELoZPAfofhGgC%2BAeo5l9mq1qa44iC81y8ZSnSVYqkuoeTr9siAOkZON%2FIxXkCwnP68LI36zcRbts3Kr%2FgSmOrod90e%2FAU0Y1OOiZL4vXOptUq4HH8XjbvV0B5ZMYqfR%2F%2FoU%2Fpb1M2xUhHKI1HGPP2DMEqXmmgE4K3iF0pncfqSmWxwFHuBsyQPVtIVv%2Fpw58ah7Vmi0LLEZIkywxVd%2FCoBclopJAYVwLM8V9ah8EuzL2mo7u9q5z0xYYVkACP9Uf4IWctTUNH0nd4FwQTH4EGDVzDUDfXTsOo%2BI66VuosvRWq1f%2BHE%2B%2BhyVFkk6OwUQPDjyXqL4SXlcdLnUYA8ozrtqa%2B5UNc1WMI2LC11myPTg7cS0%2F2IaJ0ryJjG5J2maDX%2F%2BSijMx44yq62%2B3VFbmWc1zkWvXvS7DkmRFqaauaPm5L3Us7w9x3tdZpGvY8Hnc4Covz4%2Bgf38UzBe2CKbpx3EaLjxNy0bImFSBIAoh8CXCiKzqzdU3MLCZlpsjC8tIHPBjqkAXQP11aXY8mk%2Bx4bM0t6o3UGmcbY%2BFh0IjDH1WhvHzPxeUzAKKCpWfFUY9QSTBzEikL7NFpuBwdP1RTpJ%2BWSXJDjoxt8WVwFOl2Ewswyd9P5V7FRjqg16CCf6LEvOeOAY5e58IHFj7jZqAIHnwl8AoKGn%2FoYsHQofEt7AE38XQGrx67DGQ%2Bsz9UdUMHs1Y58ZwFNwYOPFm%2BRw0iAnQwqU3np2t6f&X-Amz-Signature=cdc6aa38170bf966946c87e16534f5c9638d97d2150650a429f26e7ea13fb23f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVP7WMH%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZQFnh%2B1CiHChll7GBB%2Bk8z90O8rjPUIU357rSrIMdowIhAMABoZTBz6iuV7kiZ%2BDe9GJ7qFslpEQaS02ncskYYQIkKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDPnXGTZgIj1wdcNQq3APjW8sYtJXJU5N7I1MSNVssPD01bmJF6z0TeGg4HFcK1vFN0WGVPDKCqUyGHZcgxmEajT4hCfvg%2BzPevh2rEU6eyTto5Qsg7UnIr4FMbZBbe9DQc2ARbjAneoY9IDsVjuELoZPAfofhGgC%2BAeo5l9mq1qa44iC81y8ZSnSVYqkuoeTr9siAOkZON%2FIxXkCwnP68LI36zcRbts3Kr%2FgSmOrod90e%2FAU0Y1OOiZL4vXOptUq4HH8XjbvV0B5ZMYqfR%2F%2FoU%2Fpb1M2xUhHKI1HGPP2DMEqXmmgE4K3iF0pncfqSmWxwFHuBsyQPVtIVv%2Fpw58ah7Vmi0LLEZIkywxVd%2FCoBclopJAYVwLM8V9ah8EuzL2mo7u9q5z0xYYVkACP9Uf4IWctTUNH0nd4FwQTH4EGDVzDUDfXTsOo%2BI66VuosvRWq1f%2BHE%2B%2BhyVFkk6OwUQPDjyXqL4SXlcdLnUYA8ozrtqa%2B5UNc1WMI2LC11myPTg7cS0%2F2IaJ0ryJjG5J2maDX%2F%2BSijMx44yq62%2B3VFbmWc1zkWvXvS7DkmRFqaauaPm5L3Us7w9x3tdZpGvY8Hnc4Covz4%2Bgf38UzBe2CKbpx3EaLjxNy0bImFSBIAoh8CXCiKzqzdU3MLCZlpsjC8tIHPBjqkAXQP11aXY8mk%2Bx4bM0t6o3UGmcbY%2BFh0IjDH1WhvHzPxeUzAKKCpWfFUY9QSTBzEikL7NFpuBwdP1RTpJ%2BWSXJDjoxt8WVwFOl2Ewswyd9P5V7FRjqg16CCf6LEvOeOAY5e58IHFj7jZqAIHnwl8AoKGn%2FoYsHQofEt7AE38XQGrx67DGQ%2Bsz9UdUMHs1Y58ZwFNwYOPFm%2BRw0iAnQwqU3np2t6f&X-Amz-Signature=0870f8dac7eab23509b6f35acbda1a7ead1857e861a5d462a1fc016a17d292d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

