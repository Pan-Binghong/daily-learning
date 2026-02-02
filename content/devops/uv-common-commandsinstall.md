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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNS7LF4%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIHUZMxJkQxa3BWcNYmBHoAcmfM5hsRb9pbcWt%2F51%2B%2FbrAiEAmvJV97B9cxXOptyBW5LJNVGEhASAU2GDeXtHALXUTtAqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjty5KSv6CVY5cSnyrcAxafxUoGBFXkDgfKk6n45oOXKDyixx31qEHqxf5d5ZHAuVSbqMK2lX2jXarrf4y5a4zzLXU6UPSgmeD2JOMF%2BF5C%2FjhFnggPpOgEEnHxBTKHo6uNjkDFvmsDhqU5J8i1r5jyO2g3NhVkyIEA%2BYfuOxKfP%2FiX%2Foxy6uQlSDG6BLYIc6lsqsG7bnzchqUx05Vc5DXvr2YiwI8kiKgX7D%2Btla%2F42e4%2BgTlYL9sEEnJi0AeRLTs%2FqnXdJM2Sbh9m8rV12fqSfQW9%2BqxTdusnHOxx0blcbaK%2BXBEA5RfbmOJAU5%2BxoeO4SgrX7dFhKYnWZkSHn%2F9LDMQ1gawps8Wth8dpukWdPm52IfqzOqQ2idGEuIr7GnDIh3B4RvJ0jzva4i269BGG8wjlWAumU22GWt6kNomgAvlsz1rPe1YR4uDW%2B6a8%2BDXN%2FD7g29BF%2BzYIh3fpKQCw0Zzsc2nfCY0NRJG%2Bq1V48cOU16ypru%2BUwiWTw4nBcasBvAGhBO2Rpyhn2Zkkx3m7gTDm5ixcnn8PQYOwMYPkKGyBjqDOXcvOMFMS9VRfOGq3Y%2BEa9B%2Bx1oOSYpR291mSTSlT94B2bu50x%2FlUZhB%2B%2BesZCSoQYfrM8P3l3r2ntWKFArbNC9%2FMoxxIMIaIgMwGOqUBtjRSWJJC8ClK1HIpnf3SC7ylE%2FL04w2sfzsCoTDKrDq0PCeNZrW0Azoh85bZEzj5wK9qCgSbaGAZRmVP4hZbxD6l%2FlvzV%2Fs0qmpMmr18r%2FphBQhJ4Kcoj5i0SUf1IBvjxIs7y7KeOuII8G9SPrjhhA2Zn5C7l%2B1dsqCZ58H5PcK%2F76QxIPgHXMrBGxPdWlJUTHjj9m5sGlrmyPwVnZqyqqM91616&X-Amz-Signature=8c06542af187ae931aa897e0a189ce67f815c4a5273729f8b52afd41bf496aa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNS7LF4%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIHUZMxJkQxa3BWcNYmBHoAcmfM5hsRb9pbcWt%2F51%2B%2FbrAiEAmvJV97B9cxXOptyBW5LJNVGEhASAU2GDeXtHALXUTtAqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjty5KSv6CVY5cSnyrcAxafxUoGBFXkDgfKk6n45oOXKDyixx31qEHqxf5d5ZHAuVSbqMK2lX2jXarrf4y5a4zzLXU6UPSgmeD2JOMF%2BF5C%2FjhFnggPpOgEEnHxBTKHo6uNjkDFvmsDhqU5J8i1r5jyO2g3NhVkyIEA%2BYfuOxKfP%2FiX%2Foxy6uQlSDG6BLYIc6lsqsG7bnzchqUx05Vc5DXvr2YiwI8kiKgX7D%2Btla%2F42e4%2BgTlYL9sEEnJi0AeRLTs%2FqnXdJM2Sbh9m8rV12fqSfQW9%2BqxTdusnHOxx0blcbaK%2BXBEA5RfbmOJAU5%2BxoeO4SgrX7dFhKYnWZkSHn%2F9LDMQ1gawps8Wth8dpukWdPm52IfqzOqQ2idGEuIr7GnDIh3B4RvJ0jzva4i269BGG8wjlWAumU22GWt6kNomgAvlsz1rPe1YR4uDW%2B6a8%2BDXN%2FD7g29BF%2BzYIh3fpKQCw0Zzsc2nfCY0NRJG%2Bq1V48cOU16ypru%2BUwiWTw4nBcasBvAGhBO2Rpyhn2Zkkx3m7gTDm5ixcnn8PQYOwMYPkKGyBjqDOXcvOMFMS9VRfOGq3Y%2BEa9B%2Bx1oOSYpR291mSTSlT94B2bu50x%2FlUZhB%2B%2BesZCSoQYfrM8P3l3r2ntWKFArbNC9%2FMoxxIMIaIgMwGOqUBtjRSWJJC8ClK1HIpnf3SC7ylE%2FL04w2sfzsCoTDKrDq0PCeNZrW0Azoh85bZEzj5wK9qCgSbaGAZRmVP4hZbxD6l%2FlvzV%2Fs0qmpMmr18r%2FphBQhJ4Kcoj5i0SUf1IBvjxIs7y7KeOuII8G9SPrjhhA2Zn5C7l%2B1dsqCZ58H5PcK%2F76QxIPgHXMrBGxPdWlJUTHjj9m5sGlrmyPwVnZqyqqM91616&X-Amz-Signature=c46aebfd5625b6bffa858c7a7ed29c2711673edeaea2194abc8005bb662b8ab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNS7LF4%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIHUZMxJkQxa3BWcNYmBHoAcmfM5hsRb9pbcWt%2F51%2B%2FbrAiEAmvJV97B9cxXOptyBW5LJNVGEhASAU2GDeXtHALXUTtAqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjty5KSv6CVY5cSnyrcAxafxUoGBFXkDgfKk6n45oOXKDyixx31qEHqxf5d5ZHAuVSbqMK2lX2jXarrf4y5a4zzLXU6UPSgmeD2JOMF%2BF5C%2FjhFnggPpOgEEnHxBTKHo6uNjkDFvmsDhqU5J8i1r5jyO2g3NhVkyIEA%2BYfuOxKfP%2FiX%2Foxy6uQlSDG6BLYIc6lsqsG7bnzchqUx05Vc5DXvr2YiwI8kiKgX7D%2Btla%2F42e4%2BgTlYL9sEEnJi0AeRLTs%2FqnXdJM2Sbh9m8rV12fqSfQW9%2BqxTdusnHOxx0blcbaK%2BXBEA5RfbmOJAU5%2BxoeO4SgrX7dFhKYnWZkSHn%2F9LDMQ1gawps8Wth8dpukWdPm52IfqzOqQ2idGEuIr7GnDIh3B4RvJ0jzva4i269BGG8wjlWAumU22GWt6kNomgAvlsz1rPe1YR4uDW%2B6a8%2BDXN%2FD7g29BF%2BzYIh3fpKQCw0Zzsc2nfCY0NRJG%2Bq1V48cOU16ypru%2BUwiWTw4nBcasBvAGhBO2Rpyhn2Zkkx3m7gTDm5ixcnn8PQYOwMYPkKGyBjqDOXcvOMFMS9VRfOGq3Y%2BEa9B%2Bx1oOSYpR291mSTSlT94B2bu50x%2FlUZhB%2B%2BesZCSoQYfrM8P3l3r2ntWKFArbNC9%2FMoxxIMIaIgMwGOqUBtjRSWJJC8ClK1HIpnf3SC7ylE%2FL04w2sfzsCoTDKrDq0PCeNZrW0Azoh85bZEzj5wK9qCgSbaGAZRmVP4hZbxD6l%2FlvzV%2Fs0qmpMmr18r%2FphBQhJ4Kcoj5i0SUf1IBvjxIs7y7KeOuII8G9SPrjhhA2Zn5C7l%2B1dsqCZ58H5PcK%2F76QxIPgHXMrBGxPdWlJUTHjj9m5sGlrmyPwVnZqyqqM91616&X-Amz-Signature=502de681c60a26a7bef4c110d418a56672aefdf7083ee9c2910c825e4027116b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

