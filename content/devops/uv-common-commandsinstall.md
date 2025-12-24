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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOMCCWOB%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCh%2Bm0bE%2BrQiGalURlQ3f%2B6HoR%2FDUq%2BRpQBPuM5mrekPQIhALXitOy%2FUswud%2B5opxeGzPGbkXaVAsqfAkShtUqpJ4kOKv8DCBkQABoMNjM3NDIzMTgzODA1IgxAU4I3eAqUw59lrVMq3AM%2BYFwWbTtEZImc7WeLMqcPnLabo8bs64XhbsU7ySYol8DtcMGRuhWYEtBsvut1xS4pOxjCY4YCihPr4uDxx3%2BTEI91JJMy2kZkt6AFPUewJFu9myfzt%2F5yUz4Rkz0GZL3nwm7FfGsVjaN4rRrmABLavZY%2BuFJWkt6Id01Cg5zO0rGrEYXufe5Op%2BE36E8hflg8%2FJ5CDOARsrEhyMDojAh07L1WKLkLix88v9dQy9Obwb3doWYmrgvuaGBMcyjNLO5mJ%2B1XZeAVTFAZ4NE4NznLqpQaf4W8K9btH%2Bu9ZUNWRFf%2B5x2p5ypkwhtTcb5Sm22%2FKLbC3QeKryVI86pieT2ZU%2Bvu3f%2B4VJBq6LXgganCkOdsMresFBy5JHuzyT7Y9gAZXOBD4Wo6LawYsDfhGm0dNkRFHQoaW3SqKWS53MrrDS%2Bsjb0xBHXYKQ3GFrJdRNcn%2F%2Bb7h%2Fz%2F%2FvVOow2tzGYTfXO3K5WamZl19oiosVRMW7y%2FzpxSpvlLKS4oI4%2F%2B6U6vdKDm9%2FmDInvdV1dko7IrJN7A7NcW%2Fj%2FFa7IrWO4WxbqyQrFUO%2BZ60u%2F4fCinQcHZHOpv2kwY0%2FmjbKdSOYT2xmy2bokwEpp6g4p6VXQDJh2tMKSuQINNbAyuqjCr4KzKBjqkAfQPThXaQR7CVUqHR5BwYhG0ClQ9DFqAAW5oTCvUsTewtWyEF4G%2FNS0aq0dzP9SUbN24AMcBf9yFdsAJsOhaSRsmyjOfgZh%2BV8c8jHw979%2FwqxAkB3TvZEEo2aQIMMUfCqqep6nT311MEgFCTyC1Mx5eceJCh07GnLorTzapq71DRMd2TYuuUm%2BpVzn%2FKux0gOppobQTqxH%2B9c8ltvtgIBOxZLaY&X-Amz-Signature=f2f7e1427211559389aff3ee522e71c7996431c179ab7f9edc5984d64ec14899&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOMCCWOB%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCh%2Bm0bE%2BrQiGalURlQ3f%2B6HoR%2FDUq%2BRpQBPuM5mrekPQIhALXitOy%2FUswud%2B5opxeGzPGbkXaVAsqfAkShtUqpJ4kOKv8DCBkQABoMNjM3NDIzMTgzODA1IgxAU4I3eAqUw59lrVMq3AM%2BYFwWbTtEZImc7WeLMqcPnLabo8bs64XhbsU7ySYol8DtcMGRuhWYEtBsvut1xS4pOxjCY4YCihPr4uDxx3%2BTEI91JJMy2kZkt6AFPUewJFu9myfzt%2F5yUz4Rkz0GZL3nwm7FfGsVjaN4rRrmABLavZY%2BuFJWkt6Id01Cg5zO0rGrEYXufe5Op%2BE36E8hflg8%2FJ5CDOARsrEhyMDojAh07L1WKLkLix88v9dQy9Obwb3doWYmrgvuaGBMcyjNLO5mJ%2B1XZeAVTFAZ4NE4NznLqpQaf4W8K9btH%2Bu9ZUNWRFf%2B5x2p5ypkwhtTcb5Sm22%2FKLbC3QeKryVI86pieT2ZU%2Bvu3f%2B4VJBq6LXgganCkOdsMresFBy5JHuzyT7Y9gAZXOBD4Wo6LawYsDfhGm0dNkRFHQoaW3SqKWS53MrrDS%2Bsjb0xBHXYKQ3GFrJdRNcn%2F%2Bb7h%2Fz%2F%2FvVOow2tzGYTfXO3K5WamZl19oiosVRMW7y%2FzpxSpvlLKS4oI4%2F%2B6U6vdKDm9%2FmDInvdV1dko7IrJN7A7NcW%2Fj%2FFa7IrWO4WxbqyQrFUO%2BZ60u%2F4fCinQcHZHOpv2kwY0%2FmjbKdSOYT2xmy2bokwEpp6g4p6VXQDJh2tMKSuQINNbAyuqjCr4KzKBjqkAfQPThXaQR7CVUqHR5BwYhG0ClQ9DFqAAW5oTCvUsTewtWyEF4G%2FNS0aq0dzP9SUbN24AMcBf9yFdsAJsOhaSRsmyjOfgZh%2BV8c8jHw979%2FwqxAkB3TvZEEo2aQIMMUfCqqep6nT311MEgFCTyC1Mx5eceJCh07GnLorTzapq71DRMd2TYuuUm%2BpVzn%2FKux0gOppobQTqxH%2B9c8ltvtgIBOxZLaY&X-Amz-Signature=775a79d6095aea7b1a46554b16351684e4fd62e43fb7e48c5b78c56e48933415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOMCCWOB%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCh%2Bm0bE%2BrQiGalURlQ3f%2B6HoR%2FDUq%2BRpQBPuM5mrekPQIhALXitOy%2FUswud%2B5opxeGzPGbkXaVAsqfAkShtUqpJ4kOKv8DCBkQABoMNjM3NDIzMTgzODA1IgxAU4I3eAqUw59lrVMq3AM%2BYFwWbTtEZImc7WeLMqcPnLabo8bs64XhbsU7ySYol8DtcMGRuhWYEtBsvut1xS4pOxjCY4YCihPr4uDxx3%2BTEI91JJMy2kZkt6AFPUewJFu9myfzt%2F5yUz4Rkz0GZL3nwm7FfGsVjaN4rRrmABLavZY%2BuFJWkt6Id01Cg5zO0rGrEYXufe5Op%2BE36E8hflg8%2FJ5CDOARsrEhyMDojAh07L1WKLkLix88v9dQy9Obwb3doWYmrgvuaGBMcyjNLO5mJ%2B1XZeAVTFAZ4NE4NznLqpQaf4W8K9btH%2Bu9ZUNWRFf%2B5x2p5ypkwhtTcb5Sm22%2FKLbC3QeKryVI86pieT2ZU%2Bvu3f%2B4VJBq6LXgganCkOdsMresFBy5JHuzyT7Y9gAZXOBD4Wo6LawYsDfhGm0dNkRFHQoaW3SqKWS53MrrDS%2Bsjb0xBHXYKQ3GFrJdRNcn%2F%2Bb7h%2Fz%2F%2FvVOow2tzGYTfXO3K5WamZl19oiosVRMW7y%2FzpxSpvlLKS4oI4%2F%2B6U6vdKDm9%2FmDInvdV1dko7IrJN7A7NcW%2Fj%2FFa7IrWO4WxbqyQrFUO%2BZ60u%2F4fCinQcHZHOpv2kwY0%2FmjbKdSOYT2xmy2bokwEpp6g4p6VXQDJh2tMKSuQINNbAyuqjCr4KzKBjqkAfQPThXaQR7CVUqHR5BwYhG0ClQ9DFqAAW5oTCvUsTewtWyEF4G%2FNS0aq0dzP9SUbN24AMcBf9yFdsAJsOhaSRsmyjOfgZh%2BV8c8jHw979%2FwqxAkB3TvZEEo2aQIMMUfCqqep6nT311MEgFCTyC1Mx5eceJCh07GnLorTzapq71DRMd2TYuuUm%2BpVzn%2FKux0gOppobQTqxH%2B9c8ltvtgIBOxZLaY&X-Amz-Signature=0b9c6ff5e542d328bc28fd7770ec60ab5aa96de4d6b6d6d94bd6c86f7f70e0b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

