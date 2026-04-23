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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JILGXD%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLLqTrpGxOiKZLwulF9gme9qH6JykON5Q4zElDnJdE2AIhAL5ICyc1PPgiffWeX5ZqoUPLFpv64NTEdvi9%2B%2Fq2ogFKKv8DCFwQABoMNjM3NDIzMTgzODA1IgwAJdz0VWW8yxzOU7Mq3ANJL3MzhE7rkMQoj48I%2FRSLmaaUO5aISnxghdIF3m5rmB8jSUMQOpDNlC4GgX7hUIc4N%2BShxoplk7jj6Dkkhx9vra4pH64RcHGGyuQqcHtr%2B0d5BZu4I6qz5Lu8WRBi3X11evqjR4i5r6pJBp2rQDx%2FTybULvIBN2KfrHifMlPOfllnmufsW41dqB8CWo5rJwNR%2BPWoiAqaq2cdpItWJ8eH1DGqO42UMow0Y2d%2BKioaN956wONs0GDueyjlM6Zt5ijkgNSzEI2bYJJH3fuR1c2x6iBae9PoJ%2BdWKO3rkOENIdpP660G%2BUCO0iBkciOp%2BxB2wVVzI97iieqjFalrq9uEae2m8IgLEB31kcFwTN958bVUzZ1gUFH8UXNOBfUR6fgByEQfCeh0NASbmaj%2BQ7MlBo14j4468lN0PYmb0Nl3y05f2JND32FRbaEZYKOPWfPDR%2BUCFC9R%2F%2Bk%2BOkz1PH%2Bn0oC9fEIQm4xLjmqj7vl6%2BYjo7pVqgd2gbtY%2BMUlecQRSaawq996%2FvCyR59aW%2FtGrag9vN4TSynMYNUTM5t6sBslkXgag6k8%2BtE3iRgiTejfuH63ijxbrgF%2BWJSKh8gIImxRpVn%2FbHSZ6opuB8awsKZSqTFlUs%2BI3mKX%2FQjCkm6bPBjqkAeQpuVzQ%2BcSMK7up5%2F5mu9gH012jFggJHkKhBKLxu%2BprXtU5i29mztE7gp3LT1RxuFNumMe68wuyVkCqN5pc00D85pcXh%2BR3E48PMVURO9ID%2BGxRGtBU8YTIZiYiCm%2F%2BZx936DoPHwuoWQi7UGZQ46%2BF3lrQ4B%2F4Y%2BfwQz1iGJ8aew3Z15kn0M0PG0gYbkR6uVK9FU9KsB9VLqEW5QJbU9owK6U8&X-Amz-Signature=f7c6a0aef0168a0decee26c657a89de63b207608d391e6459292a832eadf9b13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JILGXD%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLLqTrpGxOiKZLwulF9gme9qH6JykON5Q4zElDnJdE2AIhAL5ICyc1PPgiffWeX5ZqoUPLFpv64NTEdvi9%2B%2Fq2ogFKKv8DCFwQABoMNjM3NDIzMTgzODA1IgwAJdz0VWW8yxzOU7Mq3ANJL3MzhE7rkMQoj48I%2FRSLmaaUO5aISnxghdIF3m5rmB8jSUMQOpDNlC4GgX7hUIc4N%2BShxoplk7jj6Dkkhx9vra4pH64RcHGGyuQqcHtr%2B0d5BZu4I6qz5Lu8WRBi3X11evqjR4i5r6pJBp2rQDx%2FTybULvIBN2KfrHifMlPOfllnmufsW41dqB8CWo5rJwNR%2BPWoiAqaq2cdpItWJ8eH1DGqO42UMow0Y2d%2BKioaN956wONs0GDueyjlM6Zt5ijkgNSzEI2bYJJH3fuR1c2x6iBae9PoJ%2BdWKO3rkOENIdpP660G%2BUCO0iBkciOp%2BxB2wVVzI97iieqjFalrq9uEae2m8IgLEB31kcFwTN958bVUzZ1gUFH8UXNOBfUR6fgByEQfCeh0NASbmaj%2BQ7MlBo14j4468lN0PYmb0Nl3y05f2JND32FRbaEZYKOPWfPDR%2BUCFC9R%2F%2Bk%2BOkz1PH%2Bn0oC9fEIQm4xLjmqj7vl6%2BYjo7pVqgd2gbtY%2BMUlecQRSaawq996%2FvCyR59aW%2FtGrag9vN4TSynMYNUTM5t6sBslkXgag6k8%2BtE3iRgiTejfuH63ijxbrgF%2BWJSKh8gIImxRpVn%2FbHSZ6opuB8awsKZSqTFlUs%2BI3mKX%2FQjCkm6bPBjqkAeQpuVzQ%2BcSMK7up5%2F5mu9gH012jFggJHkKhBKLxu%2BprXtU5i29mztE7gp3LT1RxuFNumMe68wuyVkCqN5pc00D85pcXh%2BR3E48PMVURO9ID%2BGxRGtBU8YTIZiYiCm%2F%2BZx936DoPHwuoWQi7UGZQ46%2BF3lrQ4B%2F4Y%2BfwQz1iGJ8aew3Z15kn0M0PG0gYbkR6uVK9FU9KsB9VLqEW5QJbU9owK6U8&X-Amz-Signature=be800a742be92af66898d2371bc657db97df146bfa287b371c9bc875057bb06d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JILGXD%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLLqTrpGxOiKZLwulF9gme9qH6JykON5Q4zElDnJdE2AIhAL5ICyc1PPgiffWeX5ZqoUPLFpv64NTEdvi9%2B%2Fq2ogFKKv8DCFwQABoMNjM3NDIzMTgzODA1IgwAJdz0VWW8yxzOU7Mq3ANJL3MzhE7rkMQoj48I%2FRSLmaaUO5aISnxghdIF3m5rmB8jSUMQOpDNlC4GgX7hUIc4N%2BShxoplk7jj6Dkkhx9vra4pH64RcHGGyuQqcHtr%2B0d5BZu4I6qz5Lu8WRBi3X11evqjR4i5r6pJBp2rQDx%2FTybULvIBN2KfrHifMlPOfllnmufsW41dqB8CWo5rJwNR%2BPWoiAqaq2cdpItWJ8eH1DGqO42UMow0Y2d%2BKioaN956wONs0GDueyjlM6Zt5ijkgNSzEI2bYJJH3fuR1c2x6iBae9PoJ%2BdWKO3rkOENIdpP660G%2BUCO0iBkciOp%2BxB2wVVzI97iieqjFalrq9uEae2m8IgLEB31kcFwTN958bVUzZ1gUFH8UXNOBfUR6fgByEQfCeh0NASbmaj%2BQ7MlBo14j4468lN0PYmb0Nl3y05f2JND32FRbaEZYKOPWfPDR%2BUCFC9R%2F%2Bk%2BOkz1PH%2Bn0oC9fEIQm4xLjmqj7vl6%2BYjo7pVqgd2gbtY%2BMUlecQRSaawq996%2FvCyR59aW%2FtGrag9vN4TSynMYNUTM5t6sBslkXgag6k8%2BtE3iRgiTejfuH63ijxbrgF%2BWJSKh8gIImxRpVn%2FbHSZ6opuB8awsKZSqTFlUs%2BI3mKX%2FQjCkm6bPBjqkAeQpuVzQ%2BcSMK7up5%2F5mu9gH012jFggJHkKhBKLxu%2BprXtU5i29mztE7gp3LT1RxuFNumMe68wuyVkCqN5pc00D85pcXh%2BR3E48PMVURO9ID%2BGxRGtBU8YTIZiYiCm%2F%2BZx936DoPHwuoWQi7UGZQ46%2BF3lrQ4B%2F4Y%2BfwQz1iGJ8aew3Z15kn0M0PG0gYbkR6uVK9FU9KsB9VLqEW5QJbU9owK6U8&X-Amz-Signature=866a3479b228f0ff4d426e604bff0924b46b93ca7476995e1c74768b0dbff67b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

