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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MT42MCS%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0wrch%2FMYClDcc8eYo5F0OfA2XVNU6rtdtEQZ3KjWNCAIgMo3kQ9aRuEFJWJxoaTingTgN1XOOC0M0l3yVy3kfas4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMUKQPWYSmtjSsydpyrcA4gpa77tA%2FMFdKliJwYarvRzxYdyj%2BcwEls5HF87H1iYLjx4AD5rkZFURgoaWkOp%2FujCkQp97%2ByfTvUrnMwig6ZPK42KgonFysgx5AAsmnU5I94jXWgib4HdvczT2k3hfgnW2QQQU%2BqxLH8qonzYfQvDzEd2k6GV53rfqXvtZWpQ7v2uj%2BjqbIBmfpifTg44LyBMmksrHqAlNQzAroLfaiXwPRhRHuyB1F7KVNbLiSUGy4CM2keAgzTQGA0SWeVdpy0LfVmPMW14yPvUHtrfQ5Ni3wM0LzfzHLW1ZA4nVXtaXii9BerpotjUWFPzFfttUoCGNM0G64xZcSKRSI9FPlmO5QrZw4%2BGN3rKNTXqKD3P8PpjyL5%2FBpPrfPGJsxo9lEYra1QCJH3VZOW%2BFqSXtUcqDHbPyUkFUkxmgNh4iKRBshe8TpIwFjMJoS2wRPZ8r0GbADou%2Bcp3cMlcxx1e%2FNY9MWMoKgJtImCfZmqOWOEos2KMuAb2brzOCloye65CxwChAVNA2kqfeHZDShkrW%2BSriNO3PgL%2F41mfAK9VRI2Jv4J3oH8BKW5reWD84D3kAUgeJlL0Xj%2BhTh77zBh7Ds8dZV3l78tUsyCBR%2BeGWomrZs9BglNm9L2O7lNyMKiex84GOqUBAyX4fbVk7ZQWQA2tkbeuNV%2FHzFMD61Ikpx57%2BafWvs7RNnHKO%2BBcwsTurclQtBXn%2FH5gNAiWW91iPqMAu9AIWiKJc%2B398JE%2F9YIBAdT76jjs5EGOlnF2mDBRx6Ybu%2F%2FAUM3kMJ3r6BJ55Dcl5JIWrNj3kS0F2GKT2VeqjG3hhVAT1zKYmSncvv1RMiMcFMyxolH4WyUsTRLVOLqNqOfNG%2BuYZ64N&X-Amz-Signature=de1bb443705a5cf08a07af858edb0bc03db9df986f2b2fab63205a64ecaa11df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MT42MCS%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0wrch%2FMYClDcc8eYo5F0OfA2XVNU6rtdtEQZ3KjWNCAIgMo3kQ9aRuEFJWJxoaTingTgN1XOOC0M0l3yVy3kfas4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMUKQPWYSmtjSsydpyrcA4gpa77tA%2FMFdKliJwYarvRzxYdyj%2BcwEls5HF87H1iYLjx4AD5rkZFURgoaWkOp%2FujCkQp97%2ByfTvUrnMwig6ZPK42KgonFysgx5AAsmnU5I94jXWgib4HdvczT2k3hfgnW2QQQU%2BqxLH8qonzYfQvDzEd2k6GV53rfqXvtZWpQ7v2uj%2BjqbIBmfpifTg44LyBMmksrHqAlNQzAroLfaiXwPRhRHuyB1F7KVNbLiSUGy4CM2keAgzTQGA0SWeVdpy0LfVmPMW14yPvUHtrfQ5Ni3wM0LzfzHLW1ZA4nVXtaXii9BerpotjUWFPzFfttUoCGNM0G64xZcSKRSI9FPlmO5QrZw4%2BGN3rKNTXqKD3P8PpjyL5%2FBpPrfPGJsxo9lEYra1QCJH3VZOW%2BFqSXtUcqDHbPyUkFUkxmgNh4iKRBshe8TpIwFjMJoS2wRPZ8r0GbADou%2Bcp3cMlcxx1e%2FNY9MWMoKgJtImCfZmqOWOEos2KMuAb2brzOCloye65CxwChAVNA2kqfeHZDShkrW%2BSriNO3PgL%2F41mfAK9VRI2Jv4J3oH8BKW5reWD84D3kAUgeJlL0Xj%2BhTh77zBh7Ds8dZV3l78tUsyCBR%2BeGWomrZs9BglNm9L2O7lNyMKiex84GOqUBAyX4fbVk7ZQWQA2tkbeuNV%2FHzFMD61Ikpx57%2BafWvs7RNnHKO%2BBcwsTurclQtBXn%2FH5gNAiWW91iPqMAu9AIWiKJc%2B398JE%2F9YIBAdT76jjs5EGOlnF2mDBRx6Ybu%2F%2FAUM3kMJ3r6BJ55Dcl5JIWrNj3kS0F2GKT2VeqjG3hhVAT1zKYmSncvv1RMiMcFMyxolH4WyUsTRLVOLqNqOfNG%2BuYZ64N&X-Amz-Signature=bf1cbfc747cc28afe6e7cf4315f8f17d32ea2b982f6c3d10126de488c58395a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

