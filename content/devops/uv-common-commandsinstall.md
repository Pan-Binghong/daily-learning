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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5CXEZPA%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAqZ6anC%2BGoHlw6TU4eLPbDHiXS1%2BtzMMmNGH94otLK6AiB2Mvu83wLwpdcD9ccsP%2Bug98rh0h3t2msW5E21Y2hYeir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIM5A5YKHUHBW6eHg1HKtwD4pNid3PPXJ0I4BTZGHH7UINJ2TKqUdvZbVac9iJt7fWDxxKGTdJ6qDhljkDD55cyCyXcSg64s3480GgJq3MwGcxHSh4GS7Hde8Wi3gm93TIgyvEgEf2RNA3ht5ZxqaoJ1xN%2B4LHL60Qs8E5mqeqYtUTEnxej7xYa3PqxDQkeSPyKLLYigygOPZF1zPw%2FuGqzZ2KfySi4VMtKKM%2BYC7Dtv8OHzbh8uWV6g%2FEyztdlAFL4GQW5JqDxLW4Z9mPo0YINk%2BDMSUdiAAAfid7C4wmy3xIAT1As%2Fd%2BD1VM0LwvuOgJOkZZrQELwT4Xyc8qB17GsA3hBdob0yBUpE8urV4OEuCUWjtUg6%2BjXn12JApJWbUzKAHrk0%2F47Nu79bShtDo74JveSeRdfLgg%2FzzDSyocg7Co955IFIjc4F3lW7r2wsYpRJFe%2FbIDageqFTPFtZ4WHEuGJA%2FkixOh5yRgJsk31rup5S1tvdgpc8UglvWqr9Q3C%2BcLW9AJZWC42EfJEbLIYNEwjln0JjU7kmKA%2Bf7Ne8vXzN%2FsN1oYhvAx2CYxOgEMWws812%2F7l5PtlhHq7cGvn4V8515AjNKtiUYZ8GXOpxM5l9MSZjANInInkz68LCNlbnYHKpsq%2B%2F23OGAowtMLrygY6pgGuGpBeX64tOhVa2bFYNBpsCJppOtsk8Lnop1cdnZM1kwWvt%2FlqRKnrJAcZ%2BoN6KvEi65aDo8U219%2FSsbd%2FTPy6OhIXidlFYPovKUgvCh1uEWPjz7IhJOxkNLnRArwEwKgDBYDuTC0qpy%2BazIQUnJXCSP71HGr3LyM1hR8a5CIQNAvFzBWGLv67EqSXmBWayJNOQyf5sgJVfAqgQpsw1C0sl02R1MHV&X-Amz-Signature=ebec928890137dca34afca4823c0c259d84e80f5e45a9395d6d5ff0d398ca38f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5CXEZPA%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAqZ6anC%2BGoHlw6TU4eLPbDHiXS1%2BtzMMmNGH94otLK6AiB2Mvu83wLwpdcD9ccsP%2Bug98rh0h3t2msW5E21Y2hYeir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIM5A5YKHUHBW6eHg1HKtwD4pNid3PPXJ0I4BTZGHH7UINJ2TKqUdvZbVac9iJt7fWDxxKGTdJ6qDhljkDD55cyCyXcSg64s3480GgJq3MwGcxHSh4GS7Hde8Wi3gm93TIgyvEgEf2RNA3ht5ZxqaoJ1xN%2B4LHL60Qs8E5mqeqYtUTEnxej7xYa3PqxDQkeSPyKLLYigygOPZF1zPw%2FuGqzZ2KfySi4VMtKKM%2BYC7Dtv8OHzbh8uWV6g%2FEyztdlAFL4GQW5JqDxLW4Z9mPo0YINk%2BDMSUdiAAAfid7C4wmy3xIAT1As%2Fd%2BD1VM0LwvuOgJOkZZrQELwT4Xyc8qB17GsA3hBdob0yBUpE8urV4OEuCUWjtUg6%2BjXn12JApJWbUzKAHrk0%2F47Nu79bShtDo74JveSeRdfLgg%2FzzDSyocg7Co955IFIjc4F3lW7r2wsYpRJFe%2FbIDageqFTPFtZ4WHEuGJA%2FkixOh5yRgJsk31rup5S1tvdgpc8UglvWqr9Q3C%2BcLW9AJZWC42EfJEbLIYNEwjln0JjU7kmKA%2Bf7Ne8vXzN%2FsN1oYhvAx2CYxOgEMWws812%2F7l5PtlhHq7cGvn4V8515AjNKtiUYZ8GXOpxM5l9MSZjANInInkz68LCNlbnYHKpsq%2B%2F23OGAowtMLrygY6pgGuGpBeX64tOhVa2bFYNBpsCJppOtsk8Lnop1cdnZM1kwWvt%2FlqRKnrJAcZ%2BoN6KvEi65aDo8U219%2FSsbd%2FTPy6OhIXidlFYPovKUgvCh1uEWPjz7IhJOxkNLnRArwEwKgDBYDuTC0qpy%2BazIQUnJXCSP71HGr3LyM1hR8a5CIQNAvFzBWGLv67EqSXmBWayJNOQyf5sgJVfAqgQpsw1C0sl02R1MHV&X-Amz-Signature=fca808f9b86fd714f52a9aebf7af50541bb128114ef08031cd9ee180108e3865&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5CXEZPA%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAqZ6anC%2BGoHlw6TU4eLPbDHiXS1%2BtzMMmNGH94otLK6AiB2Mvu83wLwpdcD9ccsP%2Bug98rh0h3t2msW5E21Y2hYeir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIM5A5YKHUHBW6eHg1HKtwD4pNid3PPXJ0I4BTZGHH7UINJ2TKqUdvZbVac9iJt7fWDxxKGTdJ6qDhljkDD55cyCyXcSg64s3480GgJq3MwGcxHSh4GS7Hde8Wi3gm93TIgyvEgEf2RNA3ht5ZxqaoJ1xN%2B4LHL60Qs8E5mqeqYtUTEnxej7xYa3PqxDQkeSPyKLLYigygOPZF1zPw%2FuGqzZ2KfySi4VMtKKM%2BYC7Dtv8OHzbh8uWV6g%2FEyztdlAFL4GQW5JqDxLW4Z9mPo0YINk%2BDMSUdiAAAfid7C4wmy3xIAT1As%2Fd%2BD1VM0LwvuOgJOkZZrQELwT4Xyc8qB17GsA3hBdob0yBUpE8urV4OEuCUWjtUg6%2BjXn12JApJWbUzKAHrk0%2F47Nu79bShtDo74JveSeRdfLgg%2FzzDSyocg7Co955IFIjc4F3lW7r2wsYpRJFe%2FbIDageqFTPFtZ4WHEuGJA%2FkixOh5yRgJsk31rup5S1tvdgpc8UglvWqr9Q3C%2BcLW9AJZWC42EfJEbLIYNEwjln0JjU7kmKA%2Bf7Ne8vXzN%2FsN1oYhvAx2CYxOgEMWws812%2F7l5PtlhHq7cGvn4V8515AjNKtiUYZ8GXOpxM5l9MSZjANInInkz68LCNlbnYHKpsq%2B%2F23OGAowtMLrygY6pgGuGpBeX64tOhVa2bFYNBpsCJppOtsk8Lnop1cdnZM1kwWvt%2FlqRKnrJAcZ%2BoN6KvEi65aDo8U219%2FSsbd%2FTPy6OhIXidlFYPovKUgvCh1uEWPjz7IhJOxkNLnRArwEwKgDBYDuTC0qpy%2BazIQUnJXCSP71HGr3LyM1hR8a5CIQNAvFzBWGLv67EqSXmBWayJNOQyf5sgJVfAqgQpsw1C0sl02R1MHV&X-Amz-Signature=e2dfbc9fcaf66d5ce9c21c5325b4504f9cdeb932cd807b6446da376172547534&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

