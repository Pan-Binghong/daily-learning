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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656J5S3XK%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCY3c9AgUDL%2BOQvmlCIyzRW2FQtOVM4KadQItck3gpsUQIhAJmgIMY7g%2FTDoHrzGrtipM8%2FzjEdmsjW5%2FDdoWrUunJ%2BKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMTreXcOIRpe6T4P0q3APJkxqsiYiFIz2NdW8Hm44dWa2mDy5Q5PYHG%2B7YmdW16wSTCbcjWishMHw%2BbH4efhkpjeeXQsO7%2BDEjBO%2BgjFzrWfk31BdWjoiz92E59O9C2cKvZnpU1B%2F9A9lcwc1f%2BUUZrvJPiQSJK2%2F1rblS6Z6pEmybjGJ7R2tSY7EqTe4vvFbe0rxmIiNSnIxDlnAYq29PqOHfVqvCTsbJRNvlK7IeeE2wiKrGzb2C2VJjXVOdBzpJmwp2Pss9k0J7qyIuiTcJmz2tKzFf%2FsL5LTZUBEyj58u1pSqOr9wmJJcTWA8qOrhEuFXBbXgd1MyLVCKfQnHjK8yWwrzZ4YdPVKuM3bxPYixVQIt%2B16jBLh0enjPJDedZ4kb19j0ide3YoQ2CTqqv6bG%2FoFws20CqH%2BZgDCJmAbRi61RpgU93l5vD8RoPxnXGhIpwqdshAJG9GU6sbET3uv%2BKNeWiZwzFN%2FHxwfC7ro78Z5HsT67vtyUwbmkkdls8%2FJryalsMUV5bFuLE%2B%2BnGKgHZlxE7TlIiMyYtzaHKggkrboXcBy9osBgF8olxtnZMgOezXIGYH0MPcbiC1vA2KGzTvSox%2FvcvX6xdMRBQQ1BkYJFaS08AjNFbdnrbnKY9SqPw984225G9zjC%2Bkd%2FMBjqkAaEusLFcwvVsRUpi5MUPld5tPrmHnEKFfeHC2PILC0wRP8%2B0i7pmTU8P5pY31cA1JiLn4BpHtcCWOJKyXVx%2BTYUOwYIhS8vXBxbW9fOK%2F9d8suVokT6K3EUV6thVcfA56zGB5vdm%2FoNjf7YHRvu8hNwo6KHrN4%2BSCthe6JvCB8Rkc7ygnIDH23l3eQ2c%2FZh4ygLfqp3qzxbg9eBZUDwfPlN3wEkh&X-Amz-Signature=13ce350e9c906a1ab21d0e69573618fbc4394197b67dfa1b3e62c2250f587005&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656J5S3XK%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCY3c9AgUDL%2BOQvmlCIyzRW2FQtOVM4KadQItck3gpsUQIhAJmgIMY7g%2FTDoHrzGrtipM8%2FzjEdmsjW5%2FDdoWrUunJ%2BKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMTreXcOIRpe6T4P0q3APJkxqsiYiFIz2NdW8Hm44dWa2mDy5Q5PYHG%2B7YmdW16wSTCbcjWishMHw%2BbH4efhkpjeeXQsO7%2BDEjBO%2BgjFzrWfk31BdWjoiz92E59O9C2cKvZnpU1B%2F9A9lcwc1f%2BUUZrvJPiQSJK2%2F1rblS6Z6pEmybjGJ7R2tSY7EqTe4vvFbe0rxmIiNSnIxDlnAYq29PqOHfVqvCTsbJRNvlK7IeeE2wiKrGzb2C2VJjXVOdBzpJmwp2Pss9k0J7qyIuiTcJmz2tKzFf%2FsL5LTZUBEyj58u1pSqOr9wmJJcTWA8qOrhEuFXBbXgd1MyLVCKfQnHjK8yWwrzZ4YdPVKuM3bxPYixVQIt%2B16jBLh0enjPJDedZ4kb19j0ide3YoQ2CTqqv6bG%2FoFws20CqH%2BZgDCJmAbRi61RpgU93l5vD8RoPxnXGhIpwqdshAJG9GU6sbET3uv%2BKNeWiZwzFN%2FHxwfC7ro78Z5HsT67vtyUwbmkkdls8%2FJryalsMUV5bFuLE%2B%2BnGKgHZlxE7TlIiMyYtzaHKggkrboXcBy9osBgF8olxtnZMgOezXIGYH0MPcbiC1vA2KGzTvSox%2FvcvX6xdMRBQQ1BkYJFaS08AjNFbdnrbnKY9SqPw984225G9zjC%2Bkd%2FMBjqkAaEusLFcwvVsRUpi5MUPld5tPrmHnEKFfeHC2PILC0wRP8%2B0i7pmTU8P5pY31cA1JiLn4BpHtcCWOJKyXVx%2BTYUOwYIhS8vXBxbW9fOK%2F9d8suVokT6K3EUV6thVcfA56zGB5vdm%2FoNjf7YHRvu8hNwo6KHrN4%2BSCthe6JvCB8Rkc7ygnIDH23l3eQ2c%2FZh4ygLfqp3qzxbg9eBZUDwfPlN3wEkh&X-Amz-Signature=eb33003dc539731c5b9e543e7f7c50ea4d24ce1ed625741783e1f62429af52ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656J5S3XK%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCY3c9AgUDL%2BOQvmlCIyzRW2FQtOVM4KadQItck3gpsUQIhAJmgIMY7g%2FTDoHrzGrtipM8%2FzjEdmsjW5%2FDdoWrUunJ%2BKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMTreXcOIRpe6T4P0q3APJkxqsiYiFIz2NdW8Hm44dWa2mDy5Q5PYHG%2B7YmdW16wSTCbcjWishMHw%2BbH4efhkpjeeXQsO7%2BDEjBO%2BgjFzrWfk31BdWjoiz92E59O9C2cKvZnpU1B%2F9A9lcwc1f%2BUUZrvJPiQSJK2%2F1rblS6Z6pEmybjGJ7R2tSY7EqTe4vvFbe0rxmIiNSnIxDlnAYq29PqOHfVqvCTsbJRNvlK7IeeE2wiKrGzb2C2VJjXVOdBzpJmwp2Pss9k0J7qyIuiTcJmz2tKzFf%2FsL5LTZUBEyj58u1pSqOr9wmJJcTWA8qOrhEuFXBbXgd1MyLVCKfQnHjK8yWwrzZ4YdPVKuM3bxPYixVQIt%2B16jBLh0enjPJDedZ4kb19j0ide3YoQ2CTqqv6bG%2FoFws20CqH%2BZgDCJmAbRi61RpgU93l5vD8RoPxnXGhIpwqdshAJG9GU6sbET3uv%2BKNeWiZwzFN%2FHxwfC7ro78Z5HsT67vtyUwbmkkdls8%2FJryalsMUV5bFuLE%2B%2BnGKgHZlxE7TlIiMyYtzaHKggkrboXcBy9osBgF8olxtnZMgOezXIGYH0MPcbiC1vA2KGzTvSox%2FvcvX6xdMRBQQ1BkYJFaS08AjNFbdnrbnKY9SqPw984225G9zjC%2Bkd%2FMBjqkAaEusLFcwvVsRUpi5MUPld5tPrmHnEKFfeHC2PILC0wRP8%2B0i7pmTU8P5pY31cA1JiLn4BpHtcCWOJKyXVx%2BTYUOwYIhS8vXBxbW9fOK%2F9d8suVokT6K3EUV6thVcfA56zGB5vdm%2FoNjf7YHRvu8hNwo6KHrN4%2BSCthe6JvCB8Rkc7ygnIDH23l3eQ2c%2FZh4ygLfqp3qzxbg9eBZUDwfPlN3wEkh&X-Amz-Signature=a35561fbba892c63fe3a27b57effe46f689ea80b1cfe82ba871cc263cacb6a88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

