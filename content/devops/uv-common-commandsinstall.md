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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3ICXW7V%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCH00u6sasVAdjCmGjQyhXGm1AnZ0TyqGnmgjyAve%2BZNgIgTYUEZjaec8W8vxrBu%2FPQwNRg3ecE2JJq1Fpys6IGEsgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDGTEUYxubNReqH1VmyrcA%2FiFT%2FkFuHLHnyff8ZBLQizmGwQgSKDhHCkhH4coWeCfsImy87sxfC0yL9o%2FtG9rVFyIq1Y%2FepJ8YCx6G0SqgAy8lMzNayRtg2Dn5Ko5ZM%2F9uupkXXFJUNktJYT%2FkzM8X9D9JexSfT8KYeaS6hAj2E1wPqgWzYiANxarTk767LDHR7GaO2%2Fk1L6B76ISqYUbK2ZPUvdrUiPHETJZMg3DoluD3%2Br2kGAfySIE62MS%2Fq57dPm6Ixl3RiPP7eRRfpR%2BuYTLr6kKo4XwEJTiEadhjNiem1FJmPGwVBi%2FebNmhc9QkVzzeuE%2Fx4J0pFl0GNnVGIBz%2FOPOmiBNBDyNiwnt7UpFgAUIAVxRMpUHrg8%2Fd4kTgJICQAd9shJPyR85Al189tuu0%2FbtabBZgYGNy4trfwomBLE%2FbvF%2FkQFKm3GyEzGsLYCkoA%2FmUUmPwEGRTmZ2XZC65gc%2FKdCLTQ16d6FGcOAbpVacLRAxcbolZj%2FERLNgvYZa5emJwC9jcBXbDVjy9OzH9MG1K3anBEyfQYKhAvlocisgDXz7jvfua6qvMtYKN7t8lb8%2BzeJjXU6x9bD6HNVT2OvdP62JLQRifhiOknBUJ%2FR8YVJpWACAwIgH5LpN1TC%2Fku08ZR3NOZZ4MIqz3M4GOqUBmqtntprjjvwUdjv18whvOwBAJJvLtfIVF%2BC0pmWQ7ain1nbD%2BrCC4nPa4z%2Fl0o8Y1D4zOX0rnZP5TRfCIwTkj%2FpStb6gi3IWprlTtn%2F645h%2FfVjunE5YuimFhkkHRkyEizbI%2B90NebvHfCz3zk2ef9OvN5oMWjYY0WphsdDTG0%2BW4TGXzkfHGT9gKE6j4rdai2EnrGg5zIhqFioxQ8wp9SUsmvAg&X-Amz-Signature=debfc17be38f029129cd98f6782745110c1f803a89fa1dbad6d689a16e07a5a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3ICXW7V%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCH00u6sasVAdjCmGjQyhXGm1AnZ0TyqGnmgjyAve%2BZNgIgTYUEZjaec8W8vxrBu%2FPQwNRg3ecE2JJq1Fpys6IGEsgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDGTEUYxubNReqH1VmyrcA%2FiFT%2FkFuHLHnyff8ZBLQizmGwQgSKDhHCkhH4coWeCfsImy87sxfC0yL9o%2FtG9rVFyIq1Y%2FepJ8YCx6G0SqgAy8lMzNayRtg2Dn5Ko5ZM%2F9uupkXXFJUNktJYT%2FkzM8X9D9JexSfT8KYeaS6hAj2E1wPqgWzYiANxarTk767LDHR7GaO2%2Fk1L6B76ISqYUbK2ZPUvdrUiPHETJZMg3DoluD3%2Br2kGAfySIE62MS%2Fq57dPm6Ixl3RiPP7eRRfpR%2BuYTLr6kKo4XwEJTiEadhjNiem1FJmPGwVBi%2FebNmhc9QkVzzeuE%2Fx4J0pFl0GNnVGIBz%2FOPOmiBNBDyNiwnt7UpFgAUIAVxRMpUHrg8%2Fd4kTgJICQAd9shJPyR85Al189tuu0%2FbtabBZgYGNy4trfwomBLE%2FbvF%2FkQFKm3GyEzGsLYCkoA%2FmUUmPwEGRTmZ2XZC65gc%2FKdCLTQ16d6FGcOAbpVacLRAxcbolZj%2FERLNgvYZa5emJwC9jcBXbDVjy9OzH9MG1K3anBEyfQYKhAvlocisgDXz7jvfua6qvMtYKN7t8lb8%2BzeJjXU6x9bD6HNVT2OvdP62JLQRifhiOknBUJ%2FR8YVJpWACAwIgH5LpN1TC%2Fku08ZR3NOZZ4MIqz3M4GOqUBmqtntprjjvwUdjv18whvOwBAJJvLtfIVF%2BC0pmWQ7ain1nbD%2BrCC4nPa4z%2Fl0o8Y1D4zOX0rnZP5TRfCIwTkj%2FpStb6gi3IWprlTtn%2F645h%2FfVjunE5YuimFhkkHRkyEizbI%2B90NebvHfCz3zk2ef9OvN5oMWjYY0WphsdDTG0%2BW4TGXzkfHGT9gKE6j4rdai2EnrGg5zIhqFioxQ8wp9SUsmvAg&X-Amz-Signature=a8f90c6835fc3d90b968de31be274a1a2eab4d80292526a0fbdebcc3ea476a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3ICXW7V%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCH00u6sasVAdjCmGjQyhXGm1AnZ0TyqGnmgjyAve%2BZNgIgTYUEZjaec8W8vxrBu%2FPQwNRg3ecE2JJq1Fpys6IGEsgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDGTEUYxubNReqH1VmyrcA%2FiFT%2FkFuHLHnyff8ZBLQizmGwQgSKDhHCkhH4coWeCfsImy87sxfC0yL9o%2FtG9rVFyIq1Y%2FepJ8YCx6G0SqgAy8lMzNayRtg2Dn5Ko5ZM%2F9uupkXXFJUNktJYT%2FkzM8X9D9JexSfT8KYeaS6hAj2E1wPqgWzYiANxarTk767LDHR7GaO2%2Fk1L6B76ISqYUbK2ZPUvdrUiPHETJZMg3DoluD3%2Br2kGAfySIE62MS%2Fq57dPm6Ixl3RiPP7eRRfpR%2BuYTLr6kKo4XwEJTiEadhjNiem1FJmPGwVBi%2FebNmhc9QkVzzeuE%2Fx4J0pFl0GNnVGIBz%2FOPOmiBNBDyNiwnt7UpFgAUIAVxRMpUHrg8%2Fd4kTgJICQAd9shJPyR85Al189tuu0%2FbtabBZgYGNy4trfwomBLE%2FbvF%2FkQFKm3GyEzGsLYCkoA%2FmUUmPwEGRTmZ2XZC65gc%2FKdCLTQ16d6FGcOAbpVacLRAxcbolZj%2FERLNgvYZa5emJwC9jcBXbDVjy9OzH9MG1K3anBEyfQYKhAvlocisgDXz7jvfua6qvMtYKN7t8lb8%2BzeJjXU6x9bD6HNVT2OvdP62JLQRifhiOknBUJ%2FR8YVJpWACAwIgH5LpN1TC%2Fku08ZR3NOZZ4MIqz3M4GOqUBmqtntprjjvwUdjv18whvOwBAJJvLtfIVF%2BC0pmWQ7ain1nbD%2BrCC4nPa4z%2Fl0o8Y1D4zOX0rnZP5TRfCIwTkj%2FpStb6gi3IWprlTtn%2F645h%2FfVjunE5YuimFhkkHRkyEizbI%2B90NebvHfCz3zk2ef9OvN5oMWjYY0WphsdDTG0%2BW4TGXzkfHGT9gKE6j4rdai2EnrGg5zIhqFioxQ8wp9SUsmvAg&X-Amz-Signature=d50cc37f5c7d5016b7853cbdab46cd49217616c0b9d6d02a7ff1289ea87c062f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

