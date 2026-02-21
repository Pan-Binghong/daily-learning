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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z3WVI4Y%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSTApAkkwnEM%2F3afXdgCqjEzAZBH2UN%2B%2FZKNBCVnYYzAiEAkLCYRwxlp7FMyMNCTEFQ2IKxgR85ab7ReHje3hoSxuUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzobVh4uTHRWUfykCrcA6Ro%2BWLW%2Bt2rVq4gLZB%2BrDHgkGjjy%2FUAKp8MxNf6rrkRaG%2BSqaUqhW13J50B3no3aCmjvD%2BLxWlZWQtM%2Bi8EmaT24QoTNDn1O1K2zMefDPIQO7k1DbziaJvDvV1Aoy6nKX5%2FBqhJsk2WUlOxXlzyYq7btVmRxGJHSxInPs2nvt3yahi3q2IP01xejW0AGXigaSn7VexdO9QE8E5dS86Xl1y5Hb32PIxikH%2Fi3isp5ynzl%2FQihNzayCFY2kUHSEJAmQWsAzbps%2FDRxXCw9P3FGSY1Rs74WmLQABkbcELH1ns676oqqD4l9clwcJzLBgvwp9qypbeMqo0AQAiMsaKioqEoLgBuNocqdA8jGa7Pims6GEuy8dQkBgRCre1wwCPU0xH5hf2nCqBQeDkyv2wtWyTURjhE34kYMoPp3hbZLu%2FDHpbiddNTOXkWR46IZfTiM9wXlNpDYPRKk%2B7J3WmMoWkwRcN8DuOtFcYibRbMEDtYrxqdDiGzG%2F97JTu0GRSQUBIJhTPhr80M7UbDFLEFUqMgUAkc7qBLgnNHjGAbljHckXvTSSrWl%2F3NWLHO%2FO9FtKuxUqoZaiSasye%2B1dbM7BpODZrZZ6egeWYXvclhRy6vdd%2FxhsVJkBT4QTwmMMm85MwGOqUBjePmI1nX9pBYQvvkHte5cprj%2FbM54qnAlutXNJzS7J4WvCMs8UYT%2FtrklP%2FU1lsAmWVRDhPu59TDPQ2zICOem%2BGL%2BeCFHvWfp9GpySw54k0tLm5yvKrYnSZ4FJ1gYQR%2BOf3LsKr4cTPRdS4Dtkvc58bYOktKxEEIxghbWyZ7prpkZUD7mhdsxbJfcZ6UhRO%2F0ohS%2FTgz2cf5pwSunk7vpgk%2FTXx8&X-Amz-Signature=43697c671904c0777364156dc3ab9cb1a2b3e75bb21474b320640ccc185d67d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z3WVI4Y%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSTApAkkwnEM%2F3afXdgCqjEzAZBH2UN%2B%2FZKNBCVnYYzAiEAkLCYRwxlp7FMyMNCTEFQ2IKxgR85ab7ReHje3hoSxuUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzobVh4uTHRWUfykCrcA6Ro%2BWLW%2Bt2rVq4gLZB%2BrDHgkGjjy%2FUAKp8MxNf6rrkRaG%2BSqaUqhW13J50B3no3aCmjvD%2BLxWlZWQtM%2Bi8EmaT24QoTNDn1O1K2zMefDPIQO7k1DbziaJvDvV1Aoy6nKX5%2FBqhJsk2WUlOxXlzyYq7btVmRxGJHSxInPs2nvt3yahi3q2IP01xejW0AGXigaSn7VexdO9QE8E5dS86Xl1y5Hb32PIxikH%2Fi3isp5ynzl%2FQihNzayCFY2kUHSEJAmQWsAzbps%2FDRxXCw9P3FGSY1Rs74WmLQABkbcELH1ns676oqqD4l9clwcJzLBgvwp9qypbeMqo0AQAiMsaKioqEoLgBuNocqdA8jGa7Pims6GEuy8dQkBgRCre1wwCPU0xH5hf2nCqBQeDkyv2wtWyTURjhE34kYMoPp3hbZLu%2FDHpbiddNTOXkWR46IZfTiM9wXlNpDYPRKk%2B7J3WmMoWkwRcN8DuOtFcYibRbMEDtYrxqdDiGzG%2F97JTu0GRSQUBIJhTPhr80M7UbDFLEFUqMgUAkc7qBLgnNHjGAbljHckXvTSSrWl%2F3NWLHO%2FO9FtKuxUqoZaiSasye%2B1dbM7BpODZrZZ6egeWYXvclhRy6vdd%2FxhsVJkBT4QTwmMMm85MwGOqUBjePmI1nX9pBYQvvkHte5cprj%2FbM54qnAlutXNJzS7J4WvCMs8UYT%2FtrklP%2FU1lsAmWVRDhPu59TDPQ2zICOem%2BGL%2BeCFHvWfp9GpySw54k0tLm5yvKrYnSZ4FJ1gYQR%2BOf3LsKr4cTPRdS4Dtkvc58bYOktKxEEIxghbWyZ7prpkZUD7mhdsxbJfcZ6UhRO%2F0ohS%2FTgz2cf5pwSunk7vpgk%2FTXx8&X-Amz-Signature=a24070e3e363f9833aead84117e82a8064637e7187424b9df683cd2e673eecbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z3WVI4Y%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSTApAkkwnEM%2F3afXdgCqjEzAZBH2UN%2B%2FZKNBCVnYYzAiEAkLCYRwxlp7FMyMNCTEFQ2IKxgR85ab7ReHje3hoSxuUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzobVh4uTHRWUfykCrcA6Ro%2BWLW%2Bt2rVq4gLZB%2BrDHgkGjjy%2FUAKp8MxNf6rrkRaG%2BSqaUqhW13J50B3no3aCmjvD%2BLxWlZWQtM%2Bi8EmaT24QoTNDn1O1K2zMefDPIQO7k1DbziaJvDvV1Aoy6nKX5%2FBqhJsk2WUlOxXlzyYq7btVmRxGJHSxInPs2nvt3yahi3q2IP01xejW0AGXigaSn7VexdO9QE8E5dS86Xl1y5Hb32PIxikH%2Fi3isp5ynzl%2FQihNzayCFY2kUHSEJAmQWsAzbps%2FDRxXCw9P3FGSY1Rs74WmLQABkbcELH1ns676oqqD4l9clwcJzLBgvwp9qypbeMqo0AQAiMsaKioqEoLgBuNocqdA8jGa7Pims6GEuy8dQkBgRCre1wwCPU0xH5hf2nCqBQeDkyv2wtWyTURjhE34kYMoPp3hbZLu%2FDHpbiddNTOXkWR46IZfTiM9wXlNpDYPRKk%2B7J3WmMoWkwRcN8DuOtFcYibRbMEDtYrxqdDiGzG%2F97JTu0GRSQUBIJhTPhr80M7UbDFLEFUqMgUAkc7qBLgnNHjGAbljHckXvTSSrWl%2F3NWLHO%2FO9FtKuxUqoZaiSasye%2B1dbM7BpODZrZZ6egeWYXvclhRy6vdd%2FxhsVJkBT4QTwmMMm85MwGOqUBjePmI1nX9pBYQvvkHte5cprj%2FbM54qnAlutXNJzS7J4WvCMs8UYT%2FtrklP%2FU1lsAmWVRDhPu59TDPQ2zICOem%2BGL%2BeCFHvWfp9GpySw54k0tLm5yvKrYnSZ4FJ1gYQR%2BOf3LsKr4cTPRdS4Dtkvc58bYOktKxEEIxghbWyZ7prpkZUD7mhdsxbJfcZ6UhRO%2F0ohS%2FTgz2cf5pwSunk7vpgk%2FTXx8&X-Amz-Signature=306fb2393aa9d456ecfaeb2b165bd4342cbcfab1313b0673419c0cae005ac28b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

