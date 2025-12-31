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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EKDVE3I%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUD0wKffSC%2BgaWRgE5m46e6Ad6JndmIRoagxwC7zb17gIhAO9e82w%2FAGS2xuF8jUOYeA%2FNT%2FIFnEFiXSlCtcvolJfUKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjjlsPilT74bABdYq3AN5RdKvQqTPsP%2FirrWtQ%2BxERrVC9kbWY%2BOY5%2F9fd3mKEfv2kv%2F8TikCGhsjE8djh6Nrny9QrBQhnqP86YNn4q%2BgodCcjULig0HEmqkiUzPpo7e5Xs%2FLdCeTa1AnCQoP%2Fj259qMSh9c5L4yDg0mdOYf%2BB1hsmA%2BQx%2B1bgOQKVJ0Y3n2ztRcEiUnYrBPQVzUlrCXe6JYAs4D9vG6Hnx4imCwnJBwjOFrJqkWGBxaPcIGsd4hH6eCDCM%2F8akuLzicEb3%2BuPa1AX6ldj08yB%2BbQ1aQDaJGbJm%2FaOUmJTNdblFGdXbdkRDSDynHYNhPjVHNXfV7Zb0SqFq7d4fEahsAYEKis2imm65gdH0pVLTZA%2BF7Cr2NAW2PAjcyM3lvuydSD2YGpoTk7fMp6irmx7tCJ4qoEevvo56N8nTbt90eHw5jdp5OoVdhKK%2BuQlF0pev%2BgfJg5JOsAkp%2BIKaxRDh9%2BrJgrMoMNYdbUo36HfZD1WTSGD12z%2Fw8O3ctL3rLT2%2BLfMHu6pFt8phIFmhYa%2BcD%2Bg43SSMhUZ4ZQsjAOskzwjj3IQbvVVHWrt6dGqSvQc552sc1U1MKfcR4tqgTONl0wJI8yn%2B7occp%2B%2BIkzETvxcZlIGPBUPNu04kBeErSPCjDE8tHKBjqkAbrn7wqlDuABb7zIm62rjFdBsk99iyd9wDuSYV3SH7lavBUXT4hk1D2j8Yi%2FIZFwEXPtFpL8vdwBM8r4HXSIDo2fI0%2BYWelztQ22xcKXpPEgkkpX5wDLjXi5bbrbje5tyvS%2B5YP9zBF3a6nECqBDMHzaKs6ucNjI6BWKD2R0B1a88OjyUAibosVAMCvKAeL5J5p%2BbtIyTaupkLhGSPY6uEXvpXYl&X-Amz-Signature=29e965bbe940fa4875dfbefa41c5975ce71968fa397e8bffed5af3319a85681e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EKDVE3I%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUD0wKffSC%2BgaWRgE5m46e6Ad6JndmIRoagxwC7zb17gIhAO9e82w%2FAGS2xuF8jUOYeA%2FNT%2FIFnEFiXSlCtcvolJfUKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjjlsPilT74bABdYq3AN5RdKvQqTPsP%2FirrWtQ%2BxERrVC9kbWY%2BOY5%2F9fd3mKEfv2kv%2F8TikCGhsjE8djh6Nrny9QrBQhnqP86YNn4q%2BgodCcjULig0HEmqkiUzPpo7e5Xs%2FLdCeTa1AnCQoP%2Fj259qMSh9c5L4yDg0mdOYf%2BB1hsmA%2BQx%2B1bgOQKVJ0Y3n2ztRcEiUnYrBPQVzUlrCXe6JYAs4D9vG6Hnx4imCwnJBwjOFrJqkWGBxaPcIGsd4hH6eCDCM%2F8akuLzicEb3%2BuPa1AX6ldj08yB%2BbQ1aQDaJGbJm%2FaOUmJTNdblFGdXbdkRDSDynHYNhPjVHNXfV7Zb0SqFq7d4fEahsAYEKis2imm65gdH0pVLTZA%2BF7Cr2NAW2PAjcyM3lvuydSD2YGpoTk7fMp6irmx7tCJ4qoEevvo56N8nTbt90eHw5jdp5OoVdhKK%2BuQlF0pev%2BgfJg5JOsAkp%2BIKaxRDh9%2BrJgrMoMNYdbUo36HfZD1WTSGD12z%2Fw8O3ctL3rLT2%2BLfMHu6pFt8phIFmhYa%2BcD%2Bg43SSMhUZ4ZQsjAOskzwjj3IQbvVVHWrt6dGqSvQc552sc1U1MKfcR4tqgTONl0wJI8yn%2B7occp%2B%2BIkzETvxcZlIGPBUPNu04kBeErSPCjDE8tHKBjqkAbrn7wqlDuABb7zIm62rjFdBsk99iyd9wDuSYV3SH7lavBUXT4hk1D2j8Yi%2FIZFwEXPtFpL8vdwBM8r4HXSIDo2fI0%2BYWelztQ22xcKXpPEgkkpX5wDLjXi5bbrbje5tyvS%2B5YP9zBF3a6nECqBDMHzaKs6ucNjI6BWKD2R0B1a88OjyUAibosVAMCvKAeL5J5p%2BbtIyTaupkLhGSPY6uEXvpXYl&X-Amz-Signature=a7f8b842b08fb7561f1be723345b7c05aaa6bf490c580d9a47ecaaef75920e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EKDVE3I%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUD0wKffSC%2BgaWRgE5m46e6Ad6JndmIRoagxwC7zb17gIhAO9e82w%2FAGS2xuF8jUOYeA%2FNT%2FIFnEFiXSlCtcvolJfUKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjjlsPilT74bABdYq3AN5RdKvQqTPsP%2FirrWtQ%2BxERrVC9kbWY%2BOY5%2F9fd3mKEfv2kv%2F8TikCGhsjE8djh6Nrny9QrBQhnqP86YNn4q%2BgodCcjULig0HEmqkiUzPpo7e5Xs%2FLdCeTa1AnCQoP%2Fj259qMSh9c5L4yDg0mdOYf%2BB1hsmA%2BQx%2B1bgOQKVJ0Y3n2ztRcEiUnYrBPQVzUlrCXe6JYAs4D9vG6Hnx4imCwnJBwjOFrJqkWGBxaPcIGsd4hH6eCDCM%2F8akuLzicEb3%2BuPa1AX6ldj08yB%2BbQ1aQDaJGbJm%2FaOUmJTNdblFGdXbdkRDSDynHYNhPjVHNXfV7Zb0SqFq7d4fEahsAYEKis2imm65gdH0pVLTZA%2BF7Cr2NAW2PAjcyM3lvuydSD2YGpoTk7fMp6irmx7tCJ4qoEevvo56N8nTbt90eHw5jdp5OoVdhKK%2BuQlF0pev%2BgfJg5JOsAkp%2BIKaxRDh9%2BrJgrMoMNYdbUo36HfZD1WTSGD12z%2Fw8O3ctL3rLT2%2BLfMHu6pFt8phIFmhYa%2BcD%2Bg43SSMhUZ4ZQsjAOskzwjj3IQbvVVHWrt6dGqSvQc552sc1U1MKfcR4tqgTONl0wJI8yn%2B7occp%2B%2BIkzETvxcZlIGPBUPNu04kBeErSPCjDE8tHKBjqkAbrn7wqlDuABb7zIm62rjFdBsk99iyd9wDuSYV3SH7lavBUXT4hk1D2j8Yi%2FIZFwEXPtFpL8vdwBM8r4HXSIDo2fI0%2BYWelztQ22xcKXpPEgkkpX5wDLjXi5bbrbje5tyvS%2B5YP9zBF3a6nECqBDMHzaKs6ucNjI6BWKD2R0B1a88OjyUAibosVAMCvKAeL5J5p%2BbtIyTaupkLhGSPY6uEXvpXYl&X-Amz-Signature=97d363d2ffac77ae2ccb6cdea39ea2c75094f41bd0e0572d883d77e2975c9933&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

