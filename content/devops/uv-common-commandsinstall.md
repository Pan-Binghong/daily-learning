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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FIR2CBN%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCEP5chGF3fPTbzYbiaMm46uB%2FU1AP8aXA4T6UcgpyfQgIhAKNEZZmQXVc%2FAwe11tm3Gwgyn%2FydmqsqqfawMUqLD0sbKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3w4m3NqQo4yvkfaYq3APSnPT7Y1%2BLoTgF1kR3kAXWYEhaRlQBAUO4SsAlvNugxkeIyPRyOUa4mOeLP95mPw%2Bx1V3CmgIditc%2FSGU7R3HnYCquJcYWGG9%2BrXBhE%2FSuQJRO0gFC%2FqJJ3sDEh2c7NnaJ8DYrwn0Rq3TzQAmNKZ1Uh5naOgDYgM6V5jdbML4j2eQgC8ieIpUqGDgumSmL283Vo50o1%2Blsrvfq5TZa4gq7MufUzJ8R4Z%2ByR3yau64fwPUIHwTkJ%2FNnJkiXBDLp7dLCSd1DtjNKZ7Bx2dGk1%2BncjpPrNRABceOFF%2FG45T8K7UWa%2BRIfvvm%2BXKl9%2FheEFKYEfe2nSFV993gOGCOgVvz1eSSoBb0WMC4z1yIZ4we0XpQCk3l42Sjp9ZbYNK97D5t2gaTCbJrACgNcHUgKOZneIyUWmNfPAzLZmyXRgn7ANHyiRNroNbcVKkuMfR9jDb%2BZjeugACIKKwIOj5IDHW0gHrshNtmrsUtpMs8Lnj6ntdGP33O9Xuba4u%2BSXZXa2dpPWCLsUUjkKHcounDCdew%2BnA%2FO0C7HTHYQBVuCfYNGbkj%2BQebWSGB4koomfftw9jWCc22rCU6uFZyXxt40nbfW0IlHlJeJRFx8r2ivDdmItgZw6rullMtZj0bL%2FjCN2IXMBjqkARGBThz%2ByseNM8zw6OL6n%2BgPbUza%2FXA4ntkU52UmIrBD19zGY%2B3p08zMT%2BWXdJ8cvcfBvoxDrNoA%2FKmBnekdoGDzC2dVdhR%2FPeD3EtYgwUG5D3JxdE9OCboChtylAsZwsyxxbV4YJuAlsjpakU8oSEUYRSfmWvGWNj29hI6jyBhQqFWkSqt2PG5PgqOPa7zg76puvFw4tFduMiH93McjigYZLNQu&X-Amz-Signature=8381bcf2488bd37939a224364db62da2c6d0067bd0a092be10817c2ea10513ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FIR2CBN%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCEP5chGF3fPTbzYbiaMm46uB%2FU1AP8aXA4T6UcgpyfQgIhAKNEZZmQXVc%2FAwe11tm3Gwgyn%2FydmqsqqfawMUqLD0sbKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3w4m3NqQo4yvkfaYq3APSnPT7Y1%2BLoTgF1kR3kAXWYEhaRlQBAUO4SsAlvNugxkeIyPRyOUa4mOeLP95mPw%2Bx1V3CmgIditc%2FSGU7R3HnYCquJcYWGG9%2BrXBhE%2FSuQJRO0gFC%2FqJJ3sDEh2c7NnaJ8DYrwn0Rq3TzQAmNKZ1Uh5naOgDYgM6V5jdbML4j2eQgC8ieIpUqGDgumSmL283Vo50o1%2Blsrvfq5TZa4gq7MufUzJ8R4Z%2ByR3yau64fwPUIHwTkJ%2FNnJkiXBDLp7dLCSd1DtjNKZ7Bx2dGk1%2BncjpPrNRABceOFF%2FG45T8K7UWa%2BRIfvvm%2BXKl9%2FheEFKYEfe2nSFV993gOGCOgVvz1eSSoBb0WMC4z1yIZ4we0XpQCk3l42Sjp9ZbYNK97D5t2gaTCbJrACgNcHUgKOZneIyUWmNfPAzLZmyXRgn7ANHyiRNroNbcVKkuMfR9jDb%2BZjeugACIKKwIOj5IDHW0gHrshNtmrsUtpMs8Lnj6ntdGP33O9Xuba4u%2BSXZXa2dpPWCLsUUjkKHcounDCdew%2BnA%2FO0C7HTHYQBVuCfYNGbkj%2BQebWSGB4koomfftw9jWCc22rCU6uFZyXxt40nbfW0IlHlJeJRFx8r2ivDdmItgZw6rullMtZj0bL%2FjCN2IXMBjqkARGBThz%2ByseNM8zw6OL6n%2BgPbUza%2FXA4ntkU52UmIrBD19zGY%2B3p08zMT%2BWXdJ8cvcfBvoxDrNoA%2FKmBnekdoGDzC2dVdhR%2FPeD3EtYgwUG5D3JxdE9OCboChtylAsZwsyxxbV4YJuAlsjpakU8oSEUYRSfmWvGWNj29hI6jyBhQqFWkSqt2PG5PgqOPa7zg76puvFw4tFduMiH93McjigYZLNQu&X-Amz-Signature=1398a988de5fbe21d6f10f09d6514348a62ba62f37a484f2c6c1243e201d5ca8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FIR2CBN%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCEP5chGF3fPTbzYbiaMm46uB%2FU1AP8aXA4T6UcgpyfQgIhAKNEZZmQXVc%2FAwe11tm3Gwgyn%2FydmqsqqfawMUqLD0sbKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3w4m3NqQo4yvkfaYq3APSnPT7Y1%2BLoTgF1kR3kAXWYEhaRlQBAUO4SsAlvNugxkeIyPRyOUa4mOeLP95mPw%2Bx1V3CmgIditc%2FSGU7R3HnYCquJcYWGG9%2BrXBhE%2FSuQJRO0gFC%2FqJJ3sDEh2c7NnaJ8DYrwn0Rq3TzQAmNKZ1Uh5naOgDYgM6V5jdbML4j2eQgC8ieIpUqGDgumSmL283Vo50o1%2Blsrvfq5TZa4gq7MufUzJ8R4Z%2ByR3yau64fwPUIHwTkJ%2FNnJkiXBDLp7dLCSd1DtjNKZ7Bx2dGk1%2BncjpPrNRABceOFF%2FG45T8K7UWa%2BRIfvvm%2BXKl9%2FheEFKYEfe2nSFV993gOGCOgVvz1eSSoBb0WMC4z1yIZ4we0XpQCk3l42Sjp9ZbYNK97D5t2gaTCbJrACgNcHUgKOZneIyUWmNfPAzLZmyXRgn7ANHyiRNroNbcVKkuMfR9jDb%2BZjeugACIKKwIOj5IDHW0gHrshNtmrsUtpMs8Lnj6ntdGP33O9Xuba4u%2BSXZXa2dpPWCLsUUjkKHcounDCdew%2BnA%2FO0C7HTHYQBVuCfYNGbkj%2BQebWSGB4koomfftw9jWCc22rCU6uFZyXxt40nbfW0IlHlJeJRFx8r2ivDdmItgZw6rullMtZj0bL%2FjCN2IXMBjqkARGBThz%2ByseNM8zw6OL6n%2BgPbUza%2FXA4ntkU52UmIrBD19zGY%2B3p08zMT%2BWXdJ8cvcfBvoxDrNoA%2FKmBnekdoGDzC2dVdhR%2FPeD3EtYgwUG5D3JxdE9OCboChtylAsZwsyxxbV4YJuAlsjpakU8oSEUYRSfmWvGWNj29hI6jyBhQqFWkSqt2PG5PgqOPa7zg76puvFw4tFduMiH93McjigYZLNQu&X-Amz-Signature=63ed40c17619f5d37909400b8a7b6a61e53facd5c121770bb211d68c54d2e19d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

