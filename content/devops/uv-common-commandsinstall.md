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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL7342OO%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAv806x3dykK%2Bsj2Q6saktMPAeCaKe0CUZ1NYBJD71p%2BAiBxkhePhh99BWi%2BBFkmL%2B35LChBkzQvnGrEwwGxkpzF%2FCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMslGjL4g8JOYHKg5wKtwD5ATxrJ5SSSyYTFK5OOo%2BpCvC96sD6k9WRGD6ByD6IO7ILUNR%2FG%2BxhOKR8iCnhS6c3DdtED03NCphgVyNqZbST7ySYqrPmcRiaxB79YWswWCYDhRWJtP7LAUNzF3zC5Gq1HEBC0eCmVS%2FBd8OatGQ6hbC4yOYUCIuabs2XZ3tCOaT7Y8PtZtw%2BNFkKPWjJznHiystuu1TtNVSDOYKFNN4IxVS85kaNcHcvTPd9yPfeI%2B3emQHS20ziQDTKimAOSBfz0fXDyAGpH%2FpZTMVijgEGWvyUPBgFZEy0WQLXVv74HNZJppy7IIDFDagN7pFrHRtXQiMEsztIyKlnoL100Lbp10LVw3RGCDh219amjzv9TRRzdvZRgKGfOIQcqLciEs3bSEYz0s6ATbycgwhNA%2B7Ys7sfL3IVl6mZAae08ovfZix1RfdOafJIwEqLzriQsNOD6EmzE%2FtsPMAlzEO%2Bdy19m2cjeidatHjJDEzSlZ0syMzBu4NTD9RfG7fD17YeqagQe2K6od8ad%2BS28xn5zeZ0LNxFaegAKKboQyYtYrIfjtnPqD95%2F3d1rF1MS0MqwMDpOiMk%2Bzv%2FoJdeO%2Bj2%2BN6xi0CT7JML3%2FJKBrvk6c52Y1Au2R%2B9hNN7M48m7gw6rDMzgY6pgF70ccSTSC1J319W%2BH51pKrKKZ4N2VW6MruGadQD8OSJzjuSrjs3vJRRCIGb0Cw8%2BVW%2BWXKqYFxzg4yaz3kFfabCQm8EzEAf7uOyno2E3t8RzlkXCYdDYnD9QkuI3OZv3txWcF8jLaR5ZHKIPtNdngGTXH4ItQxevGu0Rou1dvUAYgGjy3WNZFMNvM0cts%2Fc8r9dwyhrjjAeBsLDyehzR6ufjV7PkQn&X-Amz-Signature=6f8bfc3388659833003a10b15c77defe65b2913898a00ecb082b7b2f4f550fdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL7342OO%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAv806x3dykK%2Bsj2Q6saktMPAeCaKe0CUZ1NYBJD71p%2BAiBxkhePhh99BWi%2BBFkmL%2B35LChBkzQvnGrEwwGxkpzF%2FCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMslGjL4g8JOYHKg5wKtwD5ATxrJ5SSSyYTFK5OOo%2BpCvC96sD6k9WRGD6ByD6IO7ILUNR%2FG%2BxhOKR8iCnhS6c3DdtED03NCphgVyNqZbST7ySYqrPmcRiaxB79YWswWCYDhRWJtP7LAUNzF3zC5Gq1HEBC0eCmVS%2FBd8OatGQ6hbC4yOYUCIuabs2XZ3tCOaT7Y8PtZtw%2BNFkKPWjJznHiystuu1TtNVSDOYKFNN4IxVS85kaNcHcvTPd9yPfeI%2B3emQHS20ziQDTKimAOSBfz0fXDyAGpH%2FpZTMVijgEGWvyUPBgFZEy0WQLXVv74HNZJppy7IIDFDagN7pFrHRtXQiMEsztIyKlnoL100Lbp10LVw3RGCDh219amjzv9TRRzdvZRgKGfOIQcqLciEs3bSEYz0s6ATbycgwhNA%2B7Ys7sfL3IVl6mZAae08ovfZix1RfdOafJIwEqLzriQsNOD6EmzE%2FtsPMAlzEO%2Bdy19m2cjeidatHjJDEzSlZ0syMzBu4NTD9RfG7fD17YeqagQe2K6od8ad%2BS28xn5zeZ0LNxFaegAKKboQyYtYrIfjtnPqD95%2F3d1rF1MS0MqwMDpOiMk%2Bzv%2FoJdeO%2Bj2%2BN6xi0CT7JML3%2FJKBrvk6c52Y1Au2R%2B9hNN7M48m7gw6rDMzgY6pgF70ccSTSC1J319W%2BH51pKrKKZ4N2VW6MruGadQD8OSJzjuSrjs3vJRRCIGb0Cw8%2BVW%2BWXKqYFxzg4yaz3kFfabCQm8EzEAf7uOyno2E3t8RzlkXCYdDYnD9QkuI3OZv3txWcF8jLaR5ZHKIPtNdngGTXH4ItQxevGu0Rou1dvUAYgGjy3WNZFMNvM0cts%2Fc8r9dwyhrjjAeBsLDyehzR6ufjV7PkQn&X-Amz-Signature=57798a117ba5f43870813f98061c01edaeb10556c8d0e705ed92cace53febf78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL7342OO%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAv806x3dykK%2Bsj2Q6saktMPAeCaKe0CUZ1NYBJD71p%2BAiBxkhePhh99BWi%2BBFkmL%2B35LChBkzQvnGrEwwGxkpzF%2FCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMslGjL4g8JOYHKg5wKtwD5ATxrJ5SSSyYTFK5OOo%2BpCvC96sD6k9WRGD6ByD6IO7ILUNR%2FG%2BxhOKR8iCnhS6c3DdtED03NCphgVyNqZbST7ySYqrPmcRiaxB79YWswWCYDhRWJtP7LAUNzF3zC5Gq1HEBC0eCmVS%2FBd8OatGQ6hbC4yOYUCIuabs2XZ3tCOaT7Y8PtZtw%2BNFkKPWjJznHiystuu1TtNVSDOYKFNN4IxVS85kaNcHcvTPd9yPfeI%2B3emQHS20ziQDTKimAOSBfz0fXDyAGpH%2FpZTMVijgEGWvyUPBgFZEy0WQLXVv74HNZJppy7IIDFDagN7pFrHRtXQiMEsztIyKlnoL100Lbp10LVw3RGCDh219amjzv9TRRzdvZRgKGfOIQcqLciEs3bSEYz0s6ATbycgwhNA%2B7Ys7sfL3IVl6mZAae08ovfZix1RfdOafJIwEqLzriQsNOD6EmzE%2FtsPMAlzEO%2Bdy19m2cjeidatHjJDEzSlZ0syMzBu4NTD9RfG7fD17YeqagQe2K6od8ad%2BS28xn5zeZ0LNxFaegAKKboQyYtYrIfjtnPqD95%2F3d1rF1MS0MqwMDpOiMk%2Bzv%2FoJdeO%2Bj2%2BN6xi0CT7JML3%2FJKBrvk6c52Y1Au2R%2B9hNN7M48m7gw6rDMzgY6pgF70ccSTSC1J319W%2BH51pKrKKZ4N2VW6MruGadQD8OSJzjuSrjs3vJRRCIGb0Cw8%2BVW%2BWXKqYFxzg4yaz3kFfabCQm8EzEAf7uOyno2E3t8RzlkXCYdDYnD9QkuI3OZv3txWcF8jLaR5ZHKIPtNdngGTXH4ItQxevGu0Rou1dvUAYgGjy3WNZFMNvM0cts%2Fc8r9dwyhrjjAeBsLDyehzR6ufjV7PkQn&X-Amz-Signature=346ad6852ba5d8c5abca348fc3f3f3822ad3721dbb14f3dc151d40182dc1b80c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

