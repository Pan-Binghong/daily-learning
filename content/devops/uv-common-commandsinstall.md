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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEJJD2H%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHumqUb8wP36N7k5b5Ddznt209XyNnMl7gKPYin0tXJAAiAjarIlGqB149vimKzFry6teoY8HS9QVnRr9nOowz8pcCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMbpHEYQMC7r4lnX61KtwD5ynnn5LIjVmjCA791FRCncws3FShY0S4YmbxfzXqCpFWLQIqT9dBFWIwy5dTzUIdmWPzcIDYJP9BPGfXo7g6sCONmo%2FGrBPj59nCiDk%2BOzO%2F2k09BsHEdMaAAWTHoLSlwn%2FntDkEX3d7U03jyI8p48NiV6NEGpTphhm72339sikTY4qyaZIMFGx0gb7H2EVYZtjSWcfrmCcUz%2FaUAqZDAknf%2Fuku76mcuCjMtu7J%2FhG23Op3AdJ4XcjJH5WqEej0nMaO8g2NjnFyfLN2fkesoJgPWICVAjvD5hsVumyOr6Wc%2Bz%2BA78sHVtMfGg9PpSWrZSr78GOx8Qbj%2BQTllM9%2BLHfsx%2BfTSTfgaZCKNKqYAbmj2kJ4kRGjrtvLp54wjjdjsfFq1gA4kiW9sCvz%2FIXAl9hJ4yHOpx5%2BnifKuDyLLOvBfzVupj2%2B9rJbe3txWc%2B3cxudMAmTzqPkS0ERyjajooqVOWax3QkcgG3%2BASxzUfmGddcdXlokHRSs4wRZe5ByArWCFxD4050Oan5RhLmmzVH%2FORUmtO1%2FwTjTARhGyzDJFmK%2FdoaDYI7BtLJ7oJwDyxJk8lRkLzg3hVgZcO%2FvDjDm4PeSIvnWEwuukSQTtapWACt%2FTj1AhVl07cYwoM6OzQY6pgGhQOUGRvMv0CK0%2B8Lnoa4VyU%2FY4tm4L1lGzDJJ42i%2FWwT%2FCMEd9FPomPIVJXKxoY5J1XbLjZWyDXg0D%2FivizVY%2B%2FKxLup2gxJmQPKFULRDwPKzPpSeFuF%2BruI%2BcAmSSdUp%2BL9w55ZHE7Cuc%2FyuONSC7mIdhuCaVhVqPHCRFIvAhc9RhhOZB91UeD%2FVvv6pGUukiFJC2lcGcL2oG5SgsCfu44JoenFE&X-Amz-Signature=d163af36fbfa0f70cefd74b290bd35ca1f3b2c07d90448cd4a3721c0dd46ae83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEJJD2H%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHumqUb8wP36N7k5b5Ddznt209XyNnMl7gKPYin0tXJAAiAjarIlGqB149vimKzFry6teoY8HS9QVnRr9nOowz8pcCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMbpHEYQMC7r4lnX61KtwD5ynnn5LIjVmjCA791FRCncws3FShY0S4YmbxfzXqCpFWLQIqT9dBFWIwy5dTzUIdmWPzcIDYJP9BPGfXo7g6sCONmo%2FGrBPj59nCiDk%2BOzO%2F2k09BsHEdMaAAWTHoLSlwn%2FntDkEX3d7U03jyI8p48NiV6NEGpTphhm72339sikTY4qyaZIMFGx0gb7H2EVYZtjSWcfrmCcUz%2FaUAqZDAknf%2Fuku76mcuCjMtu7J%2FhG23Op3AdJ4XcjJH5WqEej0nMaO8g2NjnFyfLN2fkesoJgPWICVAjvD5hsVumyOr6Wc%2Bz%2BA78sHVtMfGg9PpSWrZSr78GOx8Qbj%2BQTllM9%2BLHfsx%2BfTSTfgaZCKNKqYAbmj2kJ4kRGjrtvLp54wjjdjsfFq1gA4kiW9sCvz%2FIXAl9hJ4yHOpx5%2BnifKuDyLLOvBfzVupj2%2B9rJbe3txWc%2B3cxudMAmTzqPkS0ERyjajooqVOWax3QkcgG3%2BASxzUfmGddcdXlokHRSs4wRZe5ByArWCFxD4050Oan5RhLmmzVH%2FORUmtO1%2FwTjTARhGyzDJFmK%2FdoaDYI7BtLJ7oJwDyxJk8lRkLzg3hVgZcO%2FvDjDm4PeSIvnWEwuukSQTtapWACt%2FTj1AhVl07cYwoM6OzQY6pgGhQOUGRvMv0CK0%2B8Lnoa4VyU%2FY4tm4L1lGzDJJ42i%2FWwT%2FCMEd9FPomPIVJXKxoY5J1XbLjZWyDXg0D%2FivizVY%2B%2FKxLup2gxJmQPKFULRDwPKzPpSeFuF%2BruI%2BcAmSSdUp%2BL9w55ZHE7Cuc%2FyuONSC7mIdhuCaVhVqPHCRFIvAhc9RhhOZB91UeD%2FVvv6pGUukiFJC2lcGcL2oG5SgsCfu44JoenFE&X-Amz-Signature=086b39c35300357f9d051d2f6008cad6dcdb6aa063784303a1498e3ba2c843d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEJJD2H%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHumqUb8wP36N7k5b5Ddznt209XyNnMl7gKPYin0tXJAAiAjarIlGqB149vimKzFry6teoY8HS9QVnRr9nOowz8pcCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMbpHEYQMC7r4lnX61KtwD5ynnn5LIjVmjCA791FRCncws3FShY0S4YmbxfzXqCpFWLQIqT9dBFWIwy5dTzUIdmWPzcIDYJP9BPGfXo7g6sCONmo%2FGrBPj59nCiDk%2BOzO%2F2k09BsHEdMaAAWTHoLSlwn%2FntDkEX3d7U03jyI8p48NiV6NEGpTphhm72339sikTY4qyaZIMFGx0gb7H2EVYZtjSWcfrmCcUz%2FaUAqZDAknf%2Fuku76mcuCjMtu7J%2FhG23Op3AdJ4XcjJH5WqEej0nMaO8g2NjnFyfLN2fkesoJgPWICVAjvD5hsVumyOr6Wc%2Bz%2BA78sHVtMfGg9PpSWrZSr78GOx8Qbj%2BQTllM9%2BLHfsx%2BfTSTfgaZCKNKqYAbmj2kJ4kRGjrtvLp54wjjdjsfFq1gA4kiW9sCvz%2FIXAl9hJ4yHOpx5%2BnifKuDyLLOvBfzVupj2%2B9rJbe3txWc%2B3cxudMAmTzqPkS0ERyjajooqVOWax3QkcgG3%2BASxzUfmGddcdXlokHRSs4wRZe5ByArWCFxD4050Oan5RhLmmzVH%2FORUmtO1%2FwTjTARhGyzDJFmK%2FdoaDYI7BtLJ7oJwDyxJk8lRkLzg3hVgZcO%2FvDjDm4PeSIvnWEwuukSQTtapWACt%2FTj1AhVl07cYwoM6OzQY6pgGhQOUGRvMv0CK0%2B8Lnoa4VyU%2FY4tm4L1lGzDJJ42i%2FWwT%2FCMEd9FPomPIVJXKxoY5J1XbLjZWyDXg0D%2FivizVY%2B%2FKxLup2gxJmQPKFULRDwPKzPpSeFuF%2BruI%2BcAmSSdUp%2BL9w55ZHE7Cuc%2FyuONSC7mIdhuCaVhVqPHCRFIvAhc9RhhOZB91UeD%2FVvv6pGUukiFJC2lcGcL2oG5SgsCfu44JoenFE&X-Amz-Signature=37ddb623a750eb24ef268798861696e25b41c666f3f204c9652fae9e6b64d406&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

