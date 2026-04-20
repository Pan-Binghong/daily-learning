---
title: 查看本机的SSH公钥&绑定到Github
date: '2026-02-03T02:14:00.000Z'
lastmod: '2026-02-03T03:32:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 配置Git使用SSH方式, 本文环境：windows + powershell + git guissh 

---

## 查看

```json
ls  ~/.ssh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2LFQHPZ%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIFPyl5InR4M60I%2FTAWgPMhk1eGm6dgX5MoO%2B5oUlXfrcAiB9dUtn4ZJYTUJDnetKLy5zHbp0glZcVOjtqLelLjRUpyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMj%2Ft7IXsRElcskGEPKtwDcu856vH9kAI3kfcR04XbAkgC1Y%2BeLZHBz8oNN%2FxFlyL1QP0Um%2BwKz6W5dVInplqTwWuDUqWMr41XZHrQ0KL6Lp7%2FGaFDWJFEphuJ2yEGPati5Y8P6y77e%2FXzj8iVKNyNBvli%2B96ABpoKmoPWi%2FySBwhrFR8IOC0e1T7DZ5VXy2gOx35f57j4AwmDFcwhVXwzMUzfN8GrFyv7inM9zA%2B%2B6we2DCKgqX7IBRnrXr1iv7KeR7zl79VJA3jOyouP%2BdJApuywiJi5OByh12zTZ7cUpfBG03i7BOaS8LMJ17ZI91Md89jXmu16OgGv1AL3EQX%2BYURt6RTRH%2F3Ddp4GJIqJQFWdwiUIZnCon%2FqARSLVeMLyYjynuFXLceV92S9eFGWqDRzDgsJXe83S4wYUet2u%2Fsv6clr6CFX6a9rq7CkLgQH2D5RzGqbxDPcJccBRrKf1sIz3inBGUidunW4wM3pS1IyisqNW58hVAIzGpzJsXYxif7CfjKoayJyt4A6kFIliX7yeR9eY7Qhzwigw2s4MiY7kYr8XExwP5kI8K1SqaxUa5%2FGerPJM2HZ%2FVBpKdl2gz0gNhv0RMJzvY81O3WJiOrmd69xTb%2F5J2Dck%2BP2JvkEhVzbBi9WRTpp2T5UwxJaWzwY6pgGlOE7FuzdkXWocHCA5ItqJEOdu%2B1nxam0PE%2BgTIif8WIPW2bjn5EgV2qNIeOa8SIqB9PL0%2FCkC9xbUesvjojK5KaAFtZ%2Bx6E%2BzzbyIigJIgo0%2FWxrDHCSuEkvmlpZHNoTa8yfMIXQcynNz1jAVYZgpUkw6hyKR4cp%2FwBMwiKEn5hhfDs8CV2wsYqxk3V7u26eUbPV%2BagarfJ3pRnKVIlqYKCbCZL0K&X-Amz-Signature=f903a3a1d759ff7b93e6602962a1676cf4c9862b95428604289b65fd57317247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 创建

```json
# 推荐使用Ed25519算法
ssh-keygen -t ed25519 -C "your_email@example.com"

# 备选
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

## 配置

```json
# 将ssh密钥添加到ssh-agent
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add .\.ssh\id_ed25519

# 查看是否添加成功
ssh-add -l
```

### 安装gh（github cli）

```json
# 打开powershell
choco install gh

# 登录
gh auth login
```

## 打开GIT/提交

```json
gh ssh-key add ~/.ssh/id_ed25519.pub --title "公司主机"
```

## 验证

```json
ssh -T git@github.com
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2LFQHPZ%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIFPyl5InR4M60I%2FTAWgPMhk1eGm6dgX5MoO%2B5oUlXfrcAiB9dUtn4ZJYTUJDnetKLy5zHbp0glZcVOjtqLelLjRUpyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMj%2Ft7IXsRElcskGEPKtwDcu856vH9kAI3kfcR04XbAkgC1Y%2BeLZHBz8oNN%2FxFlyL1QP0Um%2BwKz6W5dVInplqTwWuDUqWMr41XZHrQ0KL6Lp7%2FGaFDWJFEphuJ2yEGPati5Y8P6y77e%2FXzj8iVKNyNBvli%2B96ABpoKmoPWi%2FySBwhrFR8IOC0e1T7DZ5VXy2gOx35f57j4AwmDFcwhVXwzMUzfN8GrFyv7inM9zA%2B%2B6we2DCKgqX7IBRnrXr1iv7KeR7zl79VJA3jOyouP%2BdJApuywiJi5OByh12zTZ7cUpfBG03i7BOaS8LMJ17ZI91Md89jXmu16OgGv1AL3EQX%2BYURt6RTRH%2F3Ddp4GJIqJQFWdwiUIZnCon%2FqARSLVeMLyYjynuFXLceV92S9eFGWqDRzDgsJXe83S4wYUet2u%2Fsv6clr6CFX6a9rq7CkLgQH2D5RzGqbxDPcJccBRrKf1sIz3inBGUidunW4wM3pS1IyisqNW58hVAIzGpzJsXYxif7CfjKoayJyt4A6kFIliX7yeR9eY7Qhzwigw2s4MiY7kYr8XExwP5kI8K1SqaxUa5%2FGerPJM2HZ%2FVBpKdl2gz0gNhv0RMJzvY81O3WJiOrmd69xTb%2F5J2Dck%2BP2JvkEhVzbBi9WRTpp2T5UwxJaWzwY6pgGlOE7FuzdkXWocHCA5ItqJEOdu%2B1nxam0PE%2BgTIif8WIPW2bjn5EgV2qNIeOa8SIqB9PL0%2FCkC9xbUesvjojK5KaAFtZ%2Bx6E%2BzzbyIigJIgo0%2FWxrDHCSuEkvmlpZHNoTa8yfMIXQcynNz1jAVYZgpUkw6hyKR4cp%2FwBMwiKEn5hhfDs8CV2wsYqxk3V7u26eUbPV%2BagarfJ3pRnKVIlqYKCbCZL0K&X-Amz-Signature=70e908ffaab45c9f08dabfb15520e1ca7253f6022af529b1f291ba4588121936&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

