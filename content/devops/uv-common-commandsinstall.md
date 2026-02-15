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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5PAWG%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHnSDvFxhS8kVmItj6EdqiY0Jz74%2FUnsZ7zbEEwUGCYtAiEArchBVl6ait8alSfB80YLmNioTQsuRFqXt0zOwdzEZw0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDhpbOF9IZJYcCKTXyrcA8cnjHLnGghPUyKU%2Fq8BO7x4EAkB6Ohxy1Fhkcg9OtrNWtORcPZkcLGD6fmqfXIkuuJtkQHsZ4KGYqlqo9H6ozwm9QxWdmF59qleApf%2BrbqdfMBDpcQTS6kyfmHCmhq3aGhFl1l1uY2p1uBtyLt%2BafuyUqTEJ6ls6pRzQ2XpZDXAXSrSIAS%2BVWVWO9zM465vhK2vOyT2AfhLh60fitS7tMablVHNFTop4ynQ5pCik6Gq%2FP3IOFAY7N5ve5GbZexXuHbDBzVEFI2dxjhvYe05kCS0H%2FWMBP5Q4cbQKwtMnBGEDAv41a%2BzzedjkRlZ28Zl%2BcFjrjQ1Om6TtAncYRZbMV%2BwusX8IAD%2FD0erHkXBnnX384iXpzCDKFiaasizYpRWRASWpW1I01Py2aD6zyawXJtgZ%2Bnk%2F6Xt%2BHkVZJ6J49KPuQA2BwjrWjlOvi%2BrnQsqLTksHcE%2F6uF0uZhCPFEdr4wyoj%2F2VgV4KnXUJJkhz6LTPaEEjewSuw3GLUajML91Pa%2BDAO1ZiR4loB6ZBTEE8mDZA7%2BfLNgGAbW2%2Ff36bkxDtSc3fV5ZXieNRsHtZZn6S5CYdv7zBJyQtm3sda5Uu0xaiM7FaV1bGuCivroEWTbq9ryvw2%2BD0i7EIUKeMKuexMwGOqUB1fqwhfrx0qQJxHchMZTCSsPSjc7fjw1Ik%2F52uhdWJW%2FQcvYDW1zjM1Pttp3ecLWQR18xrcViFqIX0k6KlpDx7IG%2F8DPhOsUkYOz1vKfWhx1bSSTVzJ3AvJvD%2Fbph3x%2B4TniTbh%2Bt6Jq%2BaG%2BwHUDHWIhiWQ%2FmPZ6hTVTbtj3pYPcjKUk67d4xthr1zZi%2B0iLD8EV86D%2BOFWqXCn3kAMk3HrJ98%2BIL&X-Amz-Signature=fb4888eb23e5907e6334ba93d4c28d93ae18093ae806a3391d5715b4265e5ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5PAWG%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHnSDvFxhS8kVmItj6EdqiY0Jz74%2FUnsZ7zbEEwUGCYtAiEArchBVl6ait8alSfB80YLmNioTQsuRFqXt0zOwdzEZw0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDhpbOF9IZJYcCKTXyrcA8cnjHLnGghPUyKU%2Fq8BO7x4EAkB6Ohxy1Fhkcg9OtrNWtORcPZkcLGD6fmqfXIkuuJtkQHsZ4KGYqlqo9H6ozwm9QxWdmF59qleApf%2BrbqdfMBDpcQTS6kyfmHCmhq3aGhFl1l1uY2p1uBtyLt%2BafuyUqTEJ6ls6pRzQ2XpZDXAXSrSIAS%2BVWVWO9zM465vhK2vOyT2AfhLh60fitS7tMablVHNFTop4ynQ5pCik6Gq%2FP3IOFAY7N5ve5GbZexXuHbDBzVEFI2dxjhvYe05kCS0H%2FWMBP5Q4cbQKwtMnBGEDAv41a%2BzzedjkRlZ28Zl%2BcFjrjQ1Om6TtAncYRZbMV%2BwusX8IAD%2FD0erHkXBnnX384iXpzCDKFiaasizYpRWRASWpW1I01Py2aD6zyawXJtgZ%2Bnk%2F6Xt%2BHkVZJ6J49KPuQA2BwjrWjlOvi%2BrnQsqLTksHcE%2F6uF0uZhCPFEdr4wyoj%2F2VgV4KnXUJJkhz6LTPaEEjewSuw3GLUajML91Pa%2BDAO1ZiR4loB6ZBTEE8mDZA7%2BfLNgGAbW2%2Ff36bkxDtSc3fV5ZXieNRsHtZZn6S5CYdv7zBJyQtm3sda5Uu0xaiM7FaV1bGuCivroEWTbq9ryvw2%2BD0i7EIUKeMKuexMwGOqUB1fqwhfrx0qQJxHchMZTCSsPSjc7fjw1Ik%2F52uhdWJW%2FQcvYDW1zjM1Pttp3ecLWQR18xrcViFqIX0k6KlpDx7IG%2F8DPhOsUkYOz1vKfWhx1bSSTVzJ3AvJvD%2Fbph3x%2B4TniTbh%2Bt6Jq%2BaG%2BwHUDHWIhiWQ%2FmPZ6hTVTbtj3pYPcjKUk67d4xthr1zZi%2B0iLD8EV86D%2BOFWqXCn3kAMk3HrJ98%2BIL&X-Amz-Signature=dd6f0b5b8feeac89a41afd6b8f6ed126cc061c11b47a1d89a3885e9c9aeca279&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5PAWG%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHnSDvFxhS8kVmItj6EdqiY0Jz74%2FUnsZ7zbEEwUGCYtAiEArchBVl6ait8alSfB80YLmNioTQsuRFqXt0zOwdzEZw0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDhpbOF9IZJYcCKTXyrcA8cnjHLnGghPUyKU%2Fq8BO7x4EAkB6Ohxy1Fhkcg9OtrNWtORcPZkcLGD6fmqfXIkuuJtkQHsZ4KGYqlqo9H6ozwm9QxWdmF59qleApf%2BrbqdfMBDpcQTS6kyfmHCmhq3aGhFl1l1uY2p1uBtyLt%2BafuyUqTEJ6ls6pRzQ2XpZDXAXSrSIAS%2BVWVWO9zM465vhK2vOyT2AfhLh60fitS7tMablVHNFTop4ynQ5pCik6Gq%2FP3IOFAY7N5ve5GbZexXuHbDBzVEFI2dxjhvYe05kCS0H%2FWMBP5Q4cbQKwtMnBGEDAv41a%2BzzedjkRlZ28Zl%2BcFjrjQ1Om6TtAncYRZbMV%2BwusX8IAD%2FD0erHkXBnnX384iXpzCDKFiaasizYpRWRASWpW1I01Py2aD6zyawXJtgZ%2Bnk%2F6Xt%2BHkVZJ6J49KPuQA2BwjrWjlOvi%2BrnQsqLTksHcE%2F6uF0uZhCPFEdr4wyoj%2F2VgV4KnXUJJkhz6LTPaEEjewSuw3GLUajML91Pa%2BDAO1ZiR4loB6ZBTEE8mDZA7%2BfLNgGAbW2%2Ff36bkxDtSc3fV5ZXieNRsHtZZn6S5CYdv7zBJyQtm3sda5Uu0xaiM7FaV1bGuCivroEWTbq9ryvw2%2BD0i7EIUKeMKuexMwGOqUB1fqwhfrx0qQJxHchMZTCSsPSjc7fjw1Ik%2F52uhdWJW%2FQcvYDW1zjM1Pttp3ecLWQR18xrcViFqIX0k6KlpDx7IG%2F8DPhOsUkYOz1vKfWhx1bSSTVzJ3AvJvD%2Fbph3x%2B4TniTbh%2Bt6Jq%2BaG%2BwHUDHWIhiWQ%2FmPZ6hTVTbtj3pYPcjKUk67d4xthr1zZi%2B0iLD8EV86D%2BOFWqXCn3kAMk3HrJ98%2BIL&X-Amz-Signature=df77a01dc7579c9b95461be815ab892044165d778897b5dfae3df243a1d802ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

