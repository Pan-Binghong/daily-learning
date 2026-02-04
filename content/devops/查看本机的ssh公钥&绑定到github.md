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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2GR4COP%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCKs3AgoH6A0FJdA4IgvqHgB38mzgJbBMI%2FCu%2BpiguhtwIhAN4ivEPO4HptPFbBcYmyKH8HFfOAAYQIhQnYV0vo%2BzaUKv8DCAwQABoMNjM3NDIzMTgzODA1Igwb%2BSKnN4GC2FCeWB0q3ANErfE3hEWa95S5iGwQKH0h8Om8gAd32rmX7SKVXpG9ro1isQyf%2F0erhzcjGphzi8LfWISSftb3i6MyL3aPlH6Y77SVdWJMwRF9MxGzELfXAFZzeF1v5789o%2Fh4aBKG8RV8R5paRowLhBuI9aT1ZE6l3nZOQNZ6%2BKL%2FXgIxTf9JYHelvEGhl3TrQjlQW685q3Bj52dgyFNnyVEPNB4e%2FkFQNY7x3j0A6UXUV23dIaKBxs%2FCD4F7PQt5mkpFCkLUoWGVPjoWr77qJN%2BiPTqxL700aweYdKevRLOOFxG4Wx2M0Y8wgvIRX%2BqK1PJWOWSW%2B2jii2Jtrq00w2uYT9HvAVnGa0cH3iqLSAcE51r8Bvn%2BdZwJefkemXScBjMTzkIL7AVRgBjvHlgo295F1eHojG2sFOkvsctKFsYNa36nBTfe11%2F7cBVhP52WmzxzdWiPcSxZdzJy1L6lHBeciBJN73Pa01lDA1G%2FGPQYsLlDsFlPb5nOUmEBEKDQEa8Snkx3lyOU0PsJSD186T3L1IR0Hv0W5nt0xTDVhUqT0SLDbdM%2FtY9EOnlq3DCL2EEC6eO4CHtymLzZHZxaWrK7xA%2B52OCxTOVuHJvt66jF9uixf%2BEbZACIB739LH%2BCOUBSbTDX6IrMBjqkAem%2FOCYO3cJNQV8gQB67wfMVUh1BbhusMfKP9nF85IaD0BIKaLIoCws5WjTjJDugtOfdfi%2F0bwmKNSGYm64NGZnaDaW%2BHYZnuzUm%2BDGBCCyeI%2Be7aDv7fDdsOqr4E7N3ohShpF9Y2qtGEPgiEmRHPIJ0r70X4QNVGtaTPlBV6AS0XhCKUZaDd0ecKMmD%2FFm4lymMaQ4hEN2OQFxo36kUep%2BoEGq6&X-Amz-Signature=b400b19e79fc298139b7128e329a8adf1e0020686fa9356a0939990d661b614a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2GR4COP%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCKs3AgoH6A0FJdA4IgvqHgB38mzgJbBMI%2FCu%2BpiguhtwIhAN4ivEPO4HptPFbBcYmyKH8HFfOAAYQIhQnYV0vo%2BzaUKv8DCAwQABoMNjM3NDIzMTgzODA1Igwb%2BSKnN4GC2FCeWB0q3ANErfE3hEWa95S5iGwQKH0h8Om8gAd32rmX7SKVXpG9ro1isQyf%2F0erhzcjGphzi8LfWISSftb3i6MyL3aPlH6Y77SVdWJMwRF9MxGzELfXAFZzeF1v5789o%2Fh4aBKG8RV8R5paRowLhBuI9aT1ZE6l3nZOQNZ6%2BKL%2FXgIxTf9JYHelvEGhl3TrQjlQW685q3Bj52dgyFNnyVEPNB4e%2FkFQNY7x3j0A6UXUV23dIaKBxs%2FCD4F7PQt5mkpFCkLUoWGVPjoWr77qJN%2BiPTqxL700aweYdKevRLOOFxG4Wx2M0Y8wgvIRX%2BqK1PJWOWSW%2B2jii2Jtrq00w2uYT9HvAVnGa0cH3iqLSAcE51r8Bvn%2BdZwJefkemXScBjMTzkIL7AVRgBjvHlgo295F1eHojG2sFOkvsctKFsYNa36nBTfe11%2F7cBVhP52WmzxzdWiPcSxZdzJy1L6lHBeciBJN73Pa01lDA1G%2FGPQYsLlDsFlPb5nOUmEBEKDQEa8Snkx3lyOU0PsJSD186T3L1IR0Hv0W5nt0xTDVhUqT0SLDbdM%2FtY9EOnlq3DCL2EEC6eO4CHtymLzZHZxaWrK7xA%2B52OCxTOVuHJvt66jF9uixf%2BEbZACIB739LH%2BCOUBSbTDX6IrMBjqkAem%2FOCYO3cJNQV8gQB67wfMVUh1BbhusMfKP9nF85IaD0BIKaLIoCws5WjTjJDugtOfdfi%2F0bwmKNSGYm64NGZnaDaW%2BHYZnuzUm%2BDGBCCyeI%2Be7aDv7fDdsOqr4E7N3ohShpF9Y2qtGEPgiEmRHPIJ0r70X4QNVGtaTPlBV6AS0XhCKUZaDd0ecKMmD%2FFm4lymMaQ4hEN2OQFxo36kUep%2BoEGq6&X-Amz-Signature=27da4009319bf5c072c90184bb68ea328b87c5f30fbf9572511eee4493f89417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

