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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNQEHKR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCv7qGQkJ9kMuyoXJj9RsJs1Ddi0z79lSDhjZIluT8iOQIhANRPlFwSoPmMU6UlVsdSiIpVJD1EXkLwZPSYDw7J0FeQKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVcbamzDwuB3xb%2FoAq3AOkJdVJNwFhlpQPb3j3I9bdKW07Vq3peyHZaayriq6KvqvgOzoPD7J%2FFMhdOIyPJyzgowkB6K1Z8ELpHEdR8ShqrLDHWnn%2F7pVJ%2Bs0kLNBiO2Hqy1T7HHk1gvImz098soRZyteEl9HO2YoRy0njhHOpnAbkwTsaOC6Z7kuOa2GR2RzPrAAiAosuRMQJVraR%2FDgssJhExYOKMHDq803TZ3YztF%2BoYx4rbgf%2F3iDr01s1xJ9BXdL0p2K3il6pBiSk0zYk%2FSfgTy%2B5yOHgoAoR5%2Bhm%2FRgUIjJgKF519Chc8ph4sIqQZr03MvLnFS7nbMOHpaLU1kobhTNSJDyMb4DuBWuU7n%2F7PRHipPkc0u9cd2nmNxlxkS%2FLt5sj0y0ygVoJrbwCq3rRzuuMZQy6SsuMsvKgWvwTMhf5%2BvPk15vfqL8iZH4iRdcat3RScee4WuHyGZT%2Bnbo27%2F%2BFHe%2FIUGwiG%2ByOPlI6R%2BDMCFq8zcyTZiRB3UdP%2FJe4rFUfSeXcX0zDEssAexOICnWlmOrmH%2BllIuoX8kU2dGJAjf1F4VFyelCTZI9eOVyHDVdTLEHqpnAGP5PCd9iguiw7o1DQ%2Bidbxy6U0O9KB4amHJVG5Y16sRHiv67o%2F%2BFxpqR6l1YkfDD8tbXIBjqkAW00qR8sSqe2u0Vdk0E9CheMlKO1JZ8SeqZACD%2F7EI6nFQEcwa5W3ntnJrTdJ%2BmRwFI8yH%2Boi4w3RJwFzVFFjqhlMT%2FuWtt02h%2B%2BT6UTXw6m32N6PNbW8Qd4NQ3gDtSCssGUYB8yWNFuUFW%2FAGb7xC5wUqK35LSK5DQEsvE5JbYPkEu12edTswboyc5oICu4HYK2yTYdkXmQnGLxrm%2B64ZDRdLVN&X-Amz-Signature=a300a7aa57a78c332d4f4f3f7c88ba84456808334b59b1cb7b43e01fc9923339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNQEHKR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCv7qGQkJ9kMuyoXJj9RsJs1Ddi0z79lSDhjZIluT8iOQIhANRPlFwSoPmMU6UlVsdSiIpVJD1EXkLwZPSYDw7J0FeQKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVcbamzDwuB3xb%2FoAq3AOkJdVJNwFhlpQPb3j3I9bdKW07Vq3peyHZaayriq6KvqvgOzoPD7J%2FFMhdOIyPJyzgowkB6K1Z8ELpHEdR8ShqrLDHWnn%2F7pVJ%2Bs0kLNBiO2Hqy1T7HHk1gvImz098soRZyteEl9HO2YoRy0njhHOpnAbkwTsaOC6Z7kuOa2GR2RzPrAAiAosuRMQJVraR%2FDgssJhExYOKMHDq803TZ3YztF%2BoYx4rbgf%2F3iDr01s1xJ9BXdL0p2K3il6pBiSk0zYk%2FSfgTy%2B5yOHgoAoR5%2Bhm%2FRgUIjJgKF519Chc8ph4sIqQZr03MvLnFS7nbMOHpaLU1kobhTNSJDyMb4DuBWuU7n%2F7PRHipPkc0u9cd2nmNxlxkS%2FLt5sj0y0ygVoJrbwCq3rRzuuMZQy6SsuMsvKgWvwTMhf5%2BvPk15vfqL8iZH4iRdcat3RScee4WuHyGZT%2Bnbo27%2F%2BFHe%2FIUGwiG%2ByOPlI6R%2BDMCFq8zcyTZiRB3UdP%2FJe4rFUfSeXcX0zDEssAexOICnWlmOrmH%2BllIuoX8kU2dGJAjf1F4VFyelCTZI9eOVyHDVdTLEHqpnAGP5PCd9iguiw7o1DQ%2Bidbxy6U0O9KB4amHJVG5Y16sRHiv67o%2F%2BFxpqR6l1YkfDD8tbXIBjqkAW00qR8sSqe2u0Vdk0E9CheMlKO1JZ8SeqZACD%2F7EI6nFQEcwa5W3ntnJrTdJ%2BmRwFI8yH%2Boi4w3RJwFzVFFjqhlMT%2FuWtt02h%2B%2BT6UTXw6m32N6PNbW8Qd4NQ3gDtSCssGUYB8yWNFuUFW%2FAGb7xC5wUqK35LSK5DQEsvE5JbYPkEu12edTswboyc5oICu4HYK2yTYdkXmQnGLxrm%2B64ZDRdLVN&X-Amz-Signature=5ccea2f15c6d48073ede64e347b007b413efddc5d67d30f8195d34e6d0bfe47b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFNQEHKR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCv7qGQkJ9kMuyoXJj9RsJs1Ddi0z79lSDhjZIluT8iOQIhANRPlFwSoPmMU6UlVsdSiIpVJD1EXkLwZPSYDw7J0FeQKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVcbamzDwuB3xb%2FoAq3AOkJdVJNwFhlpQPb3j3I9bdKW07Vq3peyHZaayriq6KvqvgOzoPD7J%2FFMhdOIyPJyzgowkB6K1Z8ELpHEdR8ShqrLDHWnn%2F7pVJ%2Bs0kLNBiO2Hqy1T7HHk1gvImz098soRZyteEl9HO2YoRy0njhHOpnAbkwTsaOC6Z7kuOa2GR2RzPrAAiAosuRMQJVraR%2FDgssJhExYOKMHDq803TZ3YztF%2BoYx4rbgf%2F3iDr01s1xJ9BXdL0p2K3il6pBiSk0zYk%2FSfgTy%2B5yOHgoAoR5%2Bhm%2FRgUIjJgKF519Chc8ph4sIqQZr03MvLnFS7nbMOHpaLU1kobhTNSJDyMb4DuBWuU7n%2F7PRHipPkc0u9cd2nmNxlxkS%2FLt5sj0y0ygVoJrbwCq3rRzuuMZQy6SsuMsvKgWvwTMhf5%2BvPk15vfqL8iZH4iRdcat3RScee4WuHyGZT%2Bnbo27%2F%2BFHe%2FIUGwiG%2ByOPlI6R%2BDMCFq8zcyTZiRB3UdP%2FJe4rFUfSeXcX0zDEssAexOICnWlmOrmH%2BllIuoX8kU2dGJAjf1F4VFyelCTZI9eOVyHDVdTLEHqpnAGP5PCd9iguiw7o1DQ%2Bidbxy6U0O9KB4amHJVG5Y16sRHiv67o%2F%2BFxpqR6l1YkfDD8tbXIBjqkAW00qR8sSqe2u0Vdk0E9CheMlKO1JZ8SeqZACD%2F7EI6nFQEcwa5W3ntnJrTdJ%2BmRwFI8yH%2Boi4w3RJwFzVFFjqhlMT%2FuWtt02h%2B%2BT6UTXw6m32N6PNbW8Qd4NQ3gDtSCssGUYB8yWNFuUFW%2FAGb7xC5wUqK35LSK5DQEsvE5JbYPkEu12edTswboyc5oICu4HYK2yTYdkXmQnGLxrm%2B64ZDRdLVN&X-Amz-Signature=cae6097555b0efe8bf1f62c6c9301cb9e77497f910432e0dc04261ad463dcbff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

