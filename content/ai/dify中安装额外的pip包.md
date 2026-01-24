---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNGA5S47%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIFpBUFIq9sW4USphyZ8IuIpjlkdvFekLAYK6gS46exmZAiBiRA%2FUq19rMeSKXeLIltItjzd0tLXU1MKVOen2j0EXbyr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMmfPzkSyvkDOBk4vSKtwDlysI%2FjWlIA8NpRTotmxSf3aikhwhcopY36EG%2FXwg7bXDL7TAHTjP19Hicqr4e6p5SeKNunHoA4B6FWY6G8Bop5TF2P%2FWjkGJd0WcHBuWcMPgAAdDfJ15WXuvPDJ%2Bd2o8fq2KaJe1O37HmelWYhqwW3Rv%2BiuVSVxra8AYgXPNUbmFEXm02awvGmo69uZVNVyJ5KfWWpGETiE5TsNQtXQF%2BYRk3ys35KaJgnscC0RQ2UmKODMHrJS7v31JLtTV4sKeiH3NmQSEvqnR3q96QCCzD63v0%2Bva8rMJ0GycNYCHbH0TPHShsuI9sea84gfvxL2F2%2B8EoPTJLiC5gAOqpnCepLkuVYSSpcXtBKF15covdWkGJVak%2BnP35BBVEiyRm6ku9VL6GZd7CCvm%2FkJ7Ob22Kgto8ITrNik%2BulP1v94bZK9aS2dT3GGKPFYHk0EsbStxQDzWSrlB8MNF%2BFxgSaEpJdMiiyJ0CvjGRgWmcdCrWhKWPs6Zy1CJLCmA7GRkwdcea9Cqpr2fNpvY%2FlQ9anRNCU1SPbPePiYRHuK%2BP0gKPn8u0BJ6GiwmtyrYtu6hlKg5MG6uCioZZV7VkeKnXIZkFE5zzbYi1bxe30qmee2X08HSTMZqu5WdL4e1NyYwnM7QywY6pgEguvZZeBUV9kzKU50xkx9s8AdcLToZswQ2gbNYozntttpkY98xF3SU70jbnAJOj2oLD%2F4f%2FbXTKXHj1XcvQ7ZkVf2laGIxHaSS2ZBefZmrll6O1SgMXiQU9yxOeOHaiENSj7o%2BPdW2J1Lhf13C4vDHLs1hFVRPdVuq%2BF3S5FtLmbHFy9zFMdd6owGuAS3Q0JwJBPj1KziYEAhSIkyuZeCW6oxUepRR&X-Amz-Signature=d24621a3f14b299e611900037fbcc88c43841c8b98a5f0add57ada429482b1a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

