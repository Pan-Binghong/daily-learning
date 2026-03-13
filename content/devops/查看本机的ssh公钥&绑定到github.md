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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6Z7SIFS%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKl1LUxyWBWaGgJ3YOrAttfXf7Pe78M6I6Vjd3BjUzeAiEAuC4ogK8rZulmA9EIqEBcyEGZouWzSYnbfyB17ZARJ9gqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BVaB0e67I5veZObSrcA7lt%2Bfa9iypAZ4cPno1Wg05WRYqO%2Fmqw6ejRa%2BNU2QV2Ly8Ko0r5SbKgbqZAxcoLP79WULU891ugwAJk5b2Og4phtrDxjKKgI99AOG86l0O3I1WFpsNCJP9ef9oCSWFTLK6CoQ2gRNrih4RQkNQ4BWq1RvZWyTW1IdhAs3phpQ5%2BG5p9alw4wMK%2BcwVSKgZ5r7%2Fpi2ztfCvUJEO%2Br%2BMIgTz9IZddzVAGrNaQ9CZ699vXHGYj4WkkBM2uf9YJdGcLKDXXHxD6hcgSUHdxoA9SvlHVvbeYD7BWO5DyBWy3Eg4C3wx13goXKpfwvblQBybfSFw0rbhjhRrw9ltn5pessRrnV1jtAutxpgpBMJbv9%2FcDLQDGNF6Q4DDKvoo6ksXO8jMPhW0Yq8br6qgG9rHlGoPQILjbTqkCjoy61oiHJbSrjOnb%2B9eoovlyY4lZq6fH29eWdTCcK3FevOgFCV80i0AkO%2FMmKDT9keCs5TydJoOsDYfzB%2BTIlf%2FgfqEZv0IhxoYn%2BthhHyM050lqY43eVXlmlXJPbtL50tglE45nkgS1XXSQEQnsHQT0vPNzyhHKtZRqmXnOV7VnEGEzA8ywQAA1bfuBatMdD4EshhrwxCtQXGaMo6inzlJkpxnwMN%2B4zc0GOqUBXSyZAyDO4FvrMgpYzkXdhiplKSHC2iWecmxcwPDIfh6HfDwdH8Z8DRPoHJT7tcI1%2Fvpc9TSLDGtmasF3xUd9Y0qd9zeMKoG%2FeyCj%2FYjBjJq8CV2ftp9vL8XaqoOlY3afVpaSe0LCYVttQUVzuqG7y1GI5gYfzzffyhuq4KM7uNkHVtEeZFUWfkV9UmujqJX%2FkMg1BgEC4terFUTt6dIhL6%2FzrTu%2F&X-Amz-Signature=ceb37424fdba8659670b8e06aba0504eaab42d497926c793badbd06b41899276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6Z7SIFS%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKl1LUxyWBWaGgJ3YOrAttfXf7Pe78M6I6Vjd3BjUzeAiEAuC4ogK8rZulmA9EIqEBcyEGZouWzSYnbfyB17ZARJ9gqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BVaB0e67I5veZObSrcA7lt%2Bfa9iypAZ4cPno1Wg05WRYqO%2Fmqw6ejRa%2BNU2QV2Ly8Ko0r5SbKgbqZAxcoLP79WULU891ugwAJk5b2Og4phtrDxjKKgI99AOG86l0O3I1WFpsNCJP9ef9oCSWFTLK6CoQ2gRNrih4RQkNQ4BWq1RvZWyTW1IdhAs3phpQ5%2BG5p9alw4wMK%2BcwVSKgZ5r7%2Fpi2ztfCvUJEO%2Br%2BMIgTz9IZddzVAGrNaQ9CZ699vXHGYj4WkkBM2uf9YJdGcLKDXXHxD6hcgSUHdxoA9SvlHVvbeYD7BWO5DyBWy3Eg4C3wx13goXKpfwvblQBybfSFw0rbhjhRrw9ltn5pessRrnV1jtAutxpgpBMJbv9%2FcDLQDGNF6Q4DDKvoo6ksXO8jMPhW0Yq8br6qgG9rHlGoPQILjbTqkCjoy61oiHJbSrjOnb%2B9eoovlyY4lZq6fH29eWdTCcK3FevOgFCV80i0AkO%2FMmKDT9keCs5TydJoOsDYfzB%2BTIlf%2FgfqEZv0IhxoYn%2BthhHyM050lqY43eVXlmlXJPbtL50tglE45nkgS1XXSQEQnsHQT0vPNzyhHKtZRqmXnOV7VnEGEzA8ywQAA1bfuBatMdD4EshhrwxCtQXGaMo6inzlJkpxnwMN%2B4zc0GOqUBXSyZAyDO4FvrMgpYzkXdhiplKSHC2iWecmxcwPDIfh6HfDwdH8Z8DRPoHJT7tcI1%2Fvpc9TSLDGtmasF3xUd9Y0qd9zeMKoG%2FeyCj%2FYjBjJq8CV2ftp9vL8XaqoOlY3afVpaSe0LCYVttQUVzuqG7y1GI5gYfzzffyhuq4KM7uNkHVtEeZFUWfkV9UmujqJX%2FkMg1BgEC4terFUTt6dIhL6%2FzrTu%2F&X-Amz-Signature=1bf888e319f5010aba3084fa10fe27f7b484dcefd1b93f4c715507ec57331061&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

