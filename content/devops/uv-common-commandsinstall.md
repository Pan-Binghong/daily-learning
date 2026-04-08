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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BCXZQCD%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIAUWTjLC98NHDo2rSQw%2BrqhUbWjBvPSKgVAxaEAxbh4KAiEApYAoxDTScjMWqJZLsFMFbMzlPqUU67JW97UoO2i%2BbEUqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHL0dBl%2F1UDiXcDQzyrcA0YdBkUC0Yw1Zw6oy6i3sjx%2BzeRx2RcJcq6xCeK305CNYgVzH0ZA0xy2m13d41CUBLyHh%2F25FWwjgLo%2B%2BIEDQWr7m6hDRtl6nXhSzZXHMi0xjpxzwLASb4wx8YtmoyMFlZ2K7eQJLOUJvdbYPbKNoB565vdesX%2FoIZ0IiTQBMRl2wDC6xv95yLh38GHF9oMCItG7pQvJI2qLAfHK64xri0LbCWMhuK4gk6eL7Et0G15fSO8MtfkSxY00VyN8OEyl19vGF30vnXuJJISVYHSnH8bZWAdayabE0MlcLvYz%2BF2tq1H3M12xdGkK%2BjD6Eyk7Vp8j3OyodFvS%2FLNaJTmIh%2FmmB9eQsrTYWIzI1ES1mHqbJXy46oJ9SM0wOYjFBZJ%2F0sJHeGeMm9mlQ5RrXUhAwPx%2BgMvIw1J1688OsaWFc83rGCJJ31YlB%2BzVaUVuqP0TUM48sXYEZzgGT2WdJPzc5LKxYRhMT0Zkj8LDYt0DNKxHeZDGCeaUYZnKy18ilxpu0XST3gb5Xh%2BTBnGNfGfdVNuZUK6ktUslrD3e3wrNKgtv1Xs6asUT7eciZWYk1bkToJR24hmdSW%2FKvIP%2FtKPPiruLRfwBbdu6xt9u6yvwy0BalXdt3%2F5piTK6OoU7MM%2BI184GOqUByuZQ1E%2BFriTfscIooUsps0iDQm3RCU0VlR3enOyE3hXBaMVK4Zs4qv%2FGUSj%2FXlEbwA5Ehfj8n6N3JUMZkjRAgvwpqi6OCJaA8ugtTeZCF4oj3nIoJBMp9myptwMgmyw4p53riR1GJTNXZWjKqHtEteu0DnL%2FwBPw3O6n9ZddFB9AKAm36jB21PHCsxeLW3txKKE%2BIXs4wa0uN8oHNKINWiWFYUB%2F&X-Amz-Signature=eac97c9358253f9926c837bceb2c3e3061ff378e1ec9238c5b5a7328c51e3349&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BCXZQCD%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIAUWTjLC98NHDo2rSQw%2BrqhUbWjBvPSKgVAxaEAxbh4KAiEApYAoxDTScjMWqJZLsFMFbMzlPqUU67JW97UoO2i%2BbEUqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHL0dBl%2F1UDiXcDQzyrcA0YdBkUC0Yw1Zw6oy6i3sjx%2BzeRx2RcJcq6xCeK305CNYgVzH0ZA0xy2m13d41CUBLyHh%2F25FWwjgLo%2B%2BIEDQWr7m6hDRtl6nXhSzZXHMi0xjpxzwLASb4wx8YtmoyMFlZ2K7eQJLOUJvdbYPbKNoB565vdesX%2FoIZ0IiTQBMRl2wDC6xv95yLh38GHF9oMCItG7pQvJI2qLAfHK64xri0LbCWMhuK4gk6eL7Et0G15fSO8MtfkSxY00VyN8OEyl19vGF30vnXuJJISVYHSnH8bZWAdayabE0MlcLvYz%2BF2tq1H3M12xdGkK%2BjD6Eyk7Vp8j3OyodFvS%2FLNaJTmIh%2FmmB9eQsrTYWIzI1ES1mHqbJXy46oJ9SM0wOYjFBZJ%2F0sJHeGeMm9mlQ5RrXUhAwPx%2BgMvIw1J1688OsaWFc83rGCJJ31YlB%2BzVaUVuqP0TUM48sXYEZzgGT2WdJPzc5LKxYRhMT0Zkj8LDYt0DNKxHeZDGCeaUYZnKy18ilxpu0XST3gb5Xh%2BTBnGNfGfdVNuZUK6ktUslrD3e3wrNKgtv1Xs6asUT7eciZWYk1bkToJR24hmdSW%2FKvIP%2FtKPPiruLRfwBbdu6xt9u6yvwy0BalXdt3%2F5piTK6OoU7MM%2BI184GOqUByuZQ1E%2BFriTfscIooUsps0iDQm3RCU0VlR3enOyE3hXBaMVK4Zs4qv%2FGUSj%2FXlEbwA5Ehfj8n6N3JUMZkjRAgvwpqi6OCJaA8ugtTeZCF4oj3nIoJBMp9myptwMgmyw4p53riR1GJTNXZWjKqHtEteu0DnL%2FwBPw3O6n9ZddFB9AKAm36jB21PHCsxeLW3txKKE%2BIXs4wa0uN8oHNKINWiWFYUB%2F&X-Amz-Signature=bdd3b59ae543b85860dc7c2068eec69088dddadb45f249dce1e9656232af07ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BCXZQCD%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIAUWTjLC98NHDo2rSQw%2BrqhUbWjBvPSKgVAxaEAxbh4KAiEApYAoxDTScjMWqJZLsFMFbMzlPqUU67JW97UoO2i%2BbEUqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHL0dBl%2F1UDiXcDQzyrcA0YdBkUC0Yw1Zw6oy6i3sjx%2BzeRx2RcJcq6xCeK305CNYgVzH0ZA0xy2m13d41CUBLyHh%2F25FWwjgLo%2B%2BIEDQWr7m6hDRtl6nXhSzZXHMi0xjpxzwLASb4wx8YtmoyMFlZ2K7eQJLOUJvdbYPbKNoB565vdesX%2FoIZ0IiTQBMRl2wDC6xv95yLh38GHF9oMCItG7pQvJI2qLAfHK64xri0LbCWMhuK4gk6eL7Et0G15fSO8MtfkSxY00VyN8OEyl19vGF30vnXuJJISVYHSnH8bZWAdayabE0MlcLvYz%2BF2tq1H3M12xdGkK%2BjD6Eyk7Vp8j3OyodFvS%2FLNaJTmIh%2FmmB9eQsrTYWIzI1ES1mHqbJXy46oJ9SM0wOYjFBZJ%2F0sJHeGeMm9mlQ5RrXUhAwPx%2BgMvIw1J1688OsaWFc83rGCJJ31YlB%2BzVaUVuqP0TUM48sXYEZzgGT2WdJPzc5LKxYRhMT0Zkj8LDYt0DNKxHeZDGCeaUYZnKy18ilxpu0XST3gb5Xh%2BTBnGNfGfdVNuZUK6ktUslrD3e3wrNKgtv1Xs6asUT7eciZWYk1bkToJR24hmdSW%2FKvIP%2FtKPPiruLRfwBbdu6xt9u6yvwy0BalXdt3%2F5piTK6OoU7MM%2BI184GOqUByuZQ1E%2BFriTfscIooUsps0iDQm3RCU0VlR3enOyE3hXBaMVK4Zs4qv%2FGUSj%2FXlEbwA5Ehfj8n6N3JUMZkjRAgvwpqi6OCJaA8ugtTeZCF4oj3nIoJBMp9myptwMgmyw4p53riR1GJTNXZWjKqHtEteu0DnL%2FwBPw3O6n9ZddFB9AKAm36jB21PHCsxeLW3txKKE%2BIXs4wa0uN8oHNKINWiWFYUB%2F&X-Amz-Signature=5e372fa69d22d5db970a5ef284bfa18cfce59a66884adec2f37e5bc6038372e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

