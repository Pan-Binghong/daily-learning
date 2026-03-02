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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKM6DHXV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCd0zeZgv3k6lrYBJurFIgA%2BzghfBkRh%2FLC9tcsFcGlAiBG2mflDzZa7NX8f9Sr%2Fby17QumC6%2FOfZ%2FboaN56BouGCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM04qBwwA6mHODvhB7KtwDCq1PxkIArhVFdduR0PO%2Bw6myO4L8A5XXooPfhbB0Fow%2Fd9%2BnypMLV2clXwX5wppraUPGVlKZd4Y%2Fn6pxtpey2xxSdL1n4VahBHG9kEjf1cgTy6qofF60p2scxRtUCrW3cZQp0UURPyw8gprSUsKiK7PNw60IwTkb9UOeMUqelI1uyeFp3lR4tnPGwKaM8kAdrScBrq7oTuIYjnSm1u736hIxa3MVc0cAtZs7KrTmK0OA5FYfby1cAxQvetvL6HxE%2BLcrWNlmBatdS%2BP6RBa%2Box%2Bh0CPRsKi2b4fOWe34prrynBsocPfqgI4CRHq%2B3z2KjuWn5cgZ7JHSkNjUCzdFK2af8a98TMVu5cgYQXck%2F3BMy7k4X7aZGJqvFFeIpudb5eHOK3pkjE9gSOPFxsaVoMhxmklR4zcmLGl4vzoTVK55gfuWn%2BT1%2F9eOmwWFQivefmI%2FC1URGvB%2BVVnX7YkvjRcY%2F1TM4hxBHrPzmbat%2FSzEBZ4xEKqoVriF0YzgK0hSOWvYkFIOiwvKPzYYsNVvkUJoDaN6Wzh%2F%2FQ%2FZN3jZ%2BqUZq7XtdKOqlQwAWJsmfGl1NAx7%2FzbLAOiiAi9wGh%2B9fYx4nVgmBTqiAhBaBc7YFrcgZ15qezOvBrRD8Wowhv2TzQY6pgFFqsl8rpoy0YNrkvJ0CXiu4qpUA0%2BpBoXE%2BSA8PpdwaZX31A8ir4sqM1scb3C8QGT4Kg%2FvB6vgxDqgVPeRTv9nv9zNTviIUkDG5SRA3hIv6EJWkZqI1qhIEl5xz6V5Zy45pCznYdh1Bm1QzU3pXR7MvhsHaplRMD%2Fr0fwsPevJLI1pUFJZr%2FQ9KFUgKQRXpa2ywWI1yqaCK8jrWIP%2FxQm5kabQXVFs&X-Amz-Signature=274b080242074e9bd92a684b0906559f9bc774d9c0d48871f2c09fc30689ba63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKM6DHXV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCd0zeZgv3k6lrYBJurFIgA%2BzghfBkRh%2FLC9tcsFcGlAiBG2mflDzZa7NX8f9Sr%2Fby17QumC6%2FOfZ%2FboaN56BouGCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM04qBwwA6mHODvhB7KtwDCq1PxkIArhVFdduR0PO%2Bw6myO4L8A5XXooPfhbB0Fow%2Fd9%2BnypMLV2clXwX5wppraUPGVlKZd4Y%2Fn6pxtpey2xxSdL1n4VahBHG9kEjf1cgTy6qofF60p2scxRtUCrW3cZQp0UURPyw8gprSUsKiK7PNw60IwTkb9UOeMUqelI1uyeFp3lR4tnPGwKaM8kAdrScBrq7oTuIYjnSm1u736hIxa3MVc0cAtZs7KrTmK0OA5FYfby1cAxQvetvL6HxE%2BLcrWNlmBatdS%2BP6RBa%2Box%2Bh0CPRsKi2b4fOWe34prrynBsocPfqgI4CRHq%2B3z2KjuWn5cgZ7JHSkNjUCzdFK2af8a98TMVu5cgYQXck%2F3BMy7k4X7aZGJqvFFeIpudb5eHOK3pkjE9gSOPFxsaVoMhxmklR4zcmLGl4vzoTVK55gfuWn%2BT1%2F9eOmwWFQivefmI%2FC1URGvB%2BVVnX7YkvjRcY%2F1TM4hxBHrPzmbat%2FSzEBZ4xEKqoVriF0YzgK0hSOWvYkFIOiwvKPzYYsNVvkUJoDaN6Wzh%2F%2FQ%2FZN3jZ%2BqUZq7XtdKOqlQwAWJsmfGl1NAx7%2FzbLAOiiAi9wGh%2B9fYx4nVgmBTqiAhBaBc7YFrcgZ15qezOvBrRD8Wowhv2TzQY6pgFFqsl8rpoy0YNrkvJ0CXiu4qpUA0%2BpBoXE%2BSA8PpdwaZX31A8ir4sqM1scb3C8QGT4Kg%2FvB6vgxDqgVPeRTv9nv9zNTviIUkDG5SRA3hIv6EJWkZqI1qhIEl5xz6V5Zy45pCznYdh1Bm1QzU3pXR7MvhsHaplRMD%2Fr0fwsPevJLI1pUFJZr%2FQ9KFUgKQRXpa2ywWI1yqaCK8jrWIP%2FxQm5kabQXVFs&X-Amz-Signature=53a659651b8dac448be939167737496368b58981771dfe3fa249bea02ee9090b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKM6DHXV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCd0zeZgv3k6lrYBJurFIgA%2BzghfBkRh%2FLC9tcsFcGlAiBG2mflDzZa7NX8f9Sr%2Fby17QumC6%2FOfZ%2FboaN56BouGCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM04qBwwA6mHODvhB7KtwDCq1PxkIArhVFdduR0PO%2Bw6myO4L8A5XXooPfhbB0Fow%2Fd9%2BnypMLV2clXwX5wppraUPGVlKZd4Y%2Fn6pxtpey2xxSdL1n4VahBHG9kEjf1cgTy6qofF60p2scxRtUCrW3cZQp0UURPyw8gprSUsKiK7PNw60IwTkb9UOeMUqelI1uyeFp3lR4tnPGwKaM8kAdrScBrq7oTuIYjnSm1u736hIxa3MVc0cAtZs7KrTmK0OA5FYfby1cAxQvetvL6HxE%2BLcrWNlmBatdS%2BP6RBa%2Box%2Bh0CPRsKi2b4fOWe34prrynBsocPfqgI4CRHq%2B3z2KjuWn5cgZ7JHSkNjUCzdFK2af8a98TMVu5cgYQXck%2F3BMy7k4X7aZGJqvFFeIpudb5eHOK3pkjE9gSOPFxsaVoMhxmklR4zcmLGl4vzoTVK55gfuWn%2BT1%2F9eOmwWFQivefmI%2FC1URGvB%2BVVnX7YkvjRcY%2F1TM4hxBHrPzmbat%2FSzEBZ4xEKqoVriF0YzgK0hSOWvYkFIOiwvKPzYYsNVvkUJoDaN6Wzh%2F%2FQ%2FZN3jZ%2BqUZq7XtdKOqlQwAWJsmfGl1NAx7%2FzbLAOiiAi9wGh%2B9fYx4nVgmBTqiAhBaBc7YFrcgZ15qezOvBrRD8Wowhv2TzQY6pgFFqsl8rpoy0YNrkvJ0CXiu4qpUA0%2BpBoXE%2BSA8PpdwaZX31A8ir4sqM1scb3C8QGT4Kg%2FvB6vgxDqgVPeRTv9nv9zNTviIUkDG5SRA3hIv6EJWkZqI1qhIEl5xz6V5Zy45pCznYdh1Bm1QzU3pXR7MvhsHaplRMD%2Fr0fwsPevJLI1pUFJZr%2FQ9KFUgKQRXpa2ywWI1yqaCK8jrWIP%2FxQm5kabQXVFs&X-Amz-Signature=889302b2722e68c365dd9f6022ab279fe87c1410c110cc4f5bdc86082c38fb22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

