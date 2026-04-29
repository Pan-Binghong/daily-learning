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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG6YRLN%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCGkrCm8ciMykrJqnqAH%2Bp%2B9YZljzfvLEKwg4I8O7cdYAIhAJEI1q0wsZP%2B3Mosha%2F%2Bi1Ws6EzzcVrPzknRJW5Xe%2FadKogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwz5H9ORa1x5fW7kMwq3AM4reQtJyPApUx%2BHjE6H%2BQCCzgO4%2FJQSIDdYK9QUkJVgzheBRbccryt570wZRju9LAXIEFhsgIeCSNhfo6sbJTaPOAD%2FTX73XR%2FiRrXKNLugpV0yhVTWIGePhP2Xx%2F0y8JIbe4%2B7ntnx%2FJugk19xpDhRV8rq5cMpe1VjXSwTGyse3Cc2yfx5lFH6HrMRoImGcf3VbTqlaPL18aUlhakj%2BtSqzO4yG0piw2GnrTjgWLmRrhQbLT9%2BR78B192co1ozyBrUKezJZRQe5W6%2FpwxCssmTS5lu3IJA7ScYlT0vgbXsWtAKhrkzXhnN5%2Fev7UsWH2jcIBW%2BACiqdZUuZYtJbyZAIwBW2as3kxpVTpa0nxp8CPAj6oog3Wxfkt8Wb1waMHAJevCdbysFPI1qmeO%2FFTLvab0lul%2BFI5jRStoE2keli5RvoYEkHvnabAiQ6bBQlz4A%2FVPfqiGuk53r43Zg3bNhTIaeVw0jak9u%2B6hjMtCMR6c7qURmvqLJoPAAKBLx6mudTYzuS8AjmzIFwNFMCOmOpoi6y0q8gUHNJahVIU3PAbxmN2Yof%2FmtCoCicxvM3Pe%2FSIl5qzD8aNoXAiv1gJjuP47sGQ5PRFJHrrt37%2BYLf6Yng7SChAaFci2xzCFksbPBjqkAcgIVJD0fyHnNQqR5XAexjmZLSMHKh8aRtbZ0rj88cySlTaoOLzbRAuTM7wQoqTNreUGJME9AasHcnyDBnRr7B6i7NaRaMoghRAejRWbg%2BhTRD%2BEUCxxKGXKqbLsSL5PuT6IPISX3i3sLQdO8vZcd51zI8jxskcEDWhJwD%2Fn18FBQfw4EqxmnFUdR0VfyxU91Rp2X25lyK5ZiRxPCcvzp5c5dLzr&X-Amz-Signature=1507f5c929ddfe932112dbe604299d68ec8e018d80f37590f9b8a724b192ce3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG6YRLN%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCGkrCm8ciMykrJqnqAH%2Bp%2B9YZljzfvLEKwg4I8O7cdYAIhAJEI1q0wsZP%2B3Mosha%2F%2Bi1Ws6EzzcVrPzknRJW5Xe%2FadKogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwz5H9ORa1x5fW7kMwq3AM4reQtJyPApUx%2BHjE6H%2BQCCzgO4%2FJQSIDdYK9QUkJVgzheBRbccryt570wZRju9LAXIEFhsgIeCSNhfo6sbJTaPOAD%2FTX73XR%2FiRrXKNLugpV0yhVTWIGePhP2Xx%2F0y8JIbe4%2B7ntnx%2FJugk19xpDhRV8rq5cMpe1VjXSwTGyse3Cc2yfx5lFH6HrMRoImGcf3VbTqlaPL18aUlhakj%2BtSqzO4yG0piw2GnrTjgWLmRrhQbLT9%2BR78B192co1ozyBrUKezJZRQe5W6%2FpwxCssmTS5lu3IJA7ScYlT0vgbXsWtAKhrkzXhnN5%2Fev7UsWH2jcIBW%2BACiqdZUuZYtJbyZAIwBW2as3kxpVTpa0nxp8CPAj6oog3Wxfkt8Wb1waMHAJevCdbysFPI1qmeO%2FFTLvab0lul%2BFI5jRStoE2keli5RvoYEkHvnabAiQ6bBQlz4A%2FVPfqiGuk53r43Zg3bNhTIaeVw0jak9u%2B6hjMtCMR6c7qURmvqLJoPAAKBLx6mudTYzuS8AjmzIFwNFMCOmOpoi6y0q8gUHNJahVIU3PAbxmN2Yof%2FmtCoCicxvM3Pe%2FSIl5qzD8aNoXAiv1gJjuP47sGQ5PRFJHrrt37%2BYLf6Yng7SChAaFci2xzCFksbPBjqkAcgIVJD0fyHnNQqR5XAexjmZLSMHKh8aRtbZ0rj88cySlTaoOLzbRAuTM7wQoqTNreUGJME9AasHcnyDBnRr7B6i7NaRaMoghRAejRWbg%2BhTRD%2BEUCxxKGXKqbLsSL5PuT6IPISX3i3sLQdO8vZcd51zI8jxskcEDWhJwD%2Fn18FBQfw4EqxmnFUdR0VfyxU91Rp2X25lyK5ZiRxPCcvzp5c5dLzr&X-Amz-Signature=64fa788845f5690664a4b2e49f37fc5f048928fa91465b2faa2032dddf36cf74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

