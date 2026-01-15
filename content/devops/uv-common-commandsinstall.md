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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XW4UVJL%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICOdMK%2FtPQAIxbztai9t25uk%2FqFbX8G0aFWsQbsaZUvYAiAvOxokjLp%2F2%2FQEnYz2QQMt68QfWk0ZlO5myGqMflLpfir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMV95vwtVfkoxCt7YSKtwDkBn3b%2FI%2F%2BWv30vouN%2BWHhKq0tzen6HjglV%2Frabo0ZPKGoxMHLuYYvzwYYXXNr57%2Bhjh34M5ZCEW21N0sItIKXExwp%2FMScauir0RLQcFj7xIE95zC1LEtN3dQ%2F3CCvtR4VRtUmG5fbwov5RpWWqZisH5HnZ%2FlF%2Bn071H9zXFfxbpM%2FLbXXCtjb6tLoY5RGlMXY6LNp3C%2BQ1%2FmJq09fY47cAoLHSUDk5sw9pTuU9oqpD7CaAvC5rXUcyq04YaWyk7X0S2OptiP1KUP1OiEXop8gi6ABM2cQOZL2vXJyNHZSMgrv5bOhfZ9yg2h43e7oqAbzaXjL2hJi3Eq82fLzkOz6kZyR39RhWUh8xSjbFgPmirO4ixwy05HRW0Hiuai7KRNIk%2FEdXwB8YrnJKTiKmFkuiuKBqSLfC9YDwOpiSxfK3ACaIUzHFMII5YC%2F6QaPzhlVqrk0a1TG0Xjcj2YfAVzcoBC1KlsPz8Qg8GDGTXFN65ipA%2F1ZlGx7O7EMX0O2YVOqGT%2FpZ6ytaZRPs2X%2Bi35H0vz%2FchH%2BKiHg6AKIsg9gkxKmz00uoFYx9lHaNzuD6KN0rMFs2GDi7mMeJXMoaqnV70Z9bfaYfUoug735Ed4As0ydQcVdgUr%2F2PZVKUw7ZqhywY6pgEPl1GPovcBfP7ZZ6wdZi6sSNzRSJ8QWDlWPLai%2BrD1zuQMic1m27OyNbCViFWpzmTFRrJCilVvp8gf3v4jA%2FV1Ft4ueTTyGr4bepKF2H8FvidAJM%2Fr5Ir9SeoaRxbJfzM1gNQRKrBbzq8w5dsED3oiH%2BjpZFCUJ1YoFmq34AGGPc7RXB%2BPJQfji5UarsLKk803CLNrO%2FUGzD%2BFI01xf66UnWXKE%2FJ2&X-Amz-Signature=49cbce5e12b3b7885df0399e586830c0cb5639b60443794efca27668e265da8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XW4UVJL%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICOdMK%2FtPQAIxbztai9t25uk%2FqFbX8G0aFWsQbsaZUvYAiAvOxokjLp%2F2%2FQEnYz2QQMt68QfWk0ZlO5myGqMflLpfir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMV95vwtVfkoxCt7YSKtwDkBn3b%2FI%2F%2BWv30vouN%2BWHhKq0tzen6HjglV%2Frabo0ZPKGoxMHLuYYvzwYYXXNr57%2Bhjh34M5ZCEW21N0sItIKXExwp%2FMScauir0RLQcFj7xIE95zC1LEtN3dQ%2F3CCvtR4VRtUmG5fbwov5RpWWqZisH5HnZ%2FlF%2Bn071H9zXFfxbpM%2FLbXXCtjb6tLoY5RGlMXY6LNp3C%2BQ1%2FmJq09fY47cAoLHSUDk5sw9pTuU9oqpD7CaAvC5rXUcyq04YaWyk7X0S2OptiP1KUP1OiEXop8gi6ABM2cQOZL2vXJyNHZSMgrv5bOhfZ9yg2h43e7oqAbzaXjL2hJi3Eq82fLzkOz6kZyR39RhWUh8xSjbFgPmirO4ixwy05HRW0Hiuai7KRNIk%2FEdXwB8YrnJKTiKmFkuiuKBqSLfC9YDwOpiSxfK3ACaIUzHFMII5YC%2F6QaPzhlVqrk0a1TG0Xjcj2YfAVzcoBC1KlsPz8Qg8GDGTXFN65ipA%2F1ZlGx7O7EMX0O2YVOqGT%2FpZ6ytaZRPs2X%2Bi35H0vz%2FchH%2BKiHg6AKIsg9gkxKmz00uoFYx9lHaNzuD6KN0rMFs2GDi7mMeJXMoaqnV70Z9bfaYfUoug735Ed4As0ydQcVdgUr%2F2PZVKUw7ZqhywY6pgEPl1GPovcBfP7ZZ6wdZi6sSNzRSJ8QWDlWPLai%2BrD1zuQMic1m27OyNbCViFWpzmTFRrJCilVvp8gf3v4jA%2FV1Ft4ueTTyGr4bepKF2H8FvidAJM%2Fr5Ir9SeoaRxbJfzM1gNQRKrBbzq8w5dsED3oiH%2BjpZFCUJ1YoFmq34AGGPc7RXB%2BPJQfji5UarsLKk803CLNrO%2FUGzD%2BFI01xf66UnWXKE%2FJ2&X-Amz-Signature=c21141b48d132d0117d0d90f72bf33660f9265739d334b893157b36bc6d20b4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XW4UVJL%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICOdMK%2FtPQAIxbztai9t25uk%2FqFbX8G0aFWsQbsaZUvYAiAvOxokjLp%2F2%2FQEnYz2QQMt68QfWk0ZlO5myGqMflLpfir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMV95vwtVfkoxCt7YSKtwDkBn3b%2FI%2F%2BWv30vouN%2BWHhKq0tzen6HjglV%2Frabo0ZPKGoxMHLuYYvzwYYXXNr57%2Bhjh34M5ZCEW21N0sItIKXExwp%2FMScauir0RLQcFj7xIE95zC1LEtN3dQ%2F3CCvtR4VRtUmG5fbwov5RpWWqZisH5HnZ%2FlF%2Bn071H9zXFfxbpM%2FLbXXCtjb6tLoY5RGlMXY6LNp3C%2BQ1%2FmJq09fY47cAoLHSUDk5sw9pTuU9oqpD7CaAvC5rXUcyq04YaWyk7X0S2OptiP1KUP1OiEXop8gi6ABM2cQOZL2vXJyNHZSMgrv5bOhfZ9yg2h43e7oqAbzaXjL2hJi3Eq82fLzkOz6kZyR39RhWUh8xSjbFgPmirO4ixwy05HRW0Hiuai7KRNIk%2FEdXwB8YrnJKTiKmFkuiuKBqSLfC9YDwOpiSxfK3ACaIUzHFMII5YC%2F6QaPzhlVqrk0a1TG0Xjcj2YfAVzcoBC1KlsPz8Qg8GDGTXFN65ipA%2F1ZlGx7O7EMX0O2YVOqGT%2FpZ6ytaZRPs2X%2Bi35H0vz%2FchH%2BKiHg6AKIsg9gkxKmz00uoFYx9lHaNzuD6KN0rMFs2GDi7mMeJXMoaqnV70Z9bfaYfUoug735Ed4As0ydQcVdgUr%2F2PZVKUw7ZqhywY6pgEPl1GPovcBfP7ZZ6wdZi6sSNzRSJ8QWDlWPLai%2BrD1zuQMic1m27OyNbCViFWpzmTFRrJCilVvp8gf3v4jA%2FV1Ft4ueTTyGr4bepKF2H8FvidAJM%2Fr5Ir9SeoaRxbJfzM1gNQRKrBbzq8w5dsED3oiH%2BjpZFCUJ1YoFmq34AGGPc7RXB%2BPJQfji5UarsLKk803CLNrO%2FUGzD%2BFI01xf66UnWXKE%2FJ2&X-Amz-Signature=fc2dac57d84eb7cd4ae54d691e73e299c7dfd8388c28dfd3b245c1b12b648aaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

