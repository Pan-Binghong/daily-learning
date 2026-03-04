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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV5WBAPP%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCR9M5er%2B%2BhIBDrBX0p9OG1Rsa%2FAPDGlpy%2BHDMWspxyagIgKyyUlBqw%2BSrfplF0jifJC6DQZKeGjtsBjxUul%2FDb1UwqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGtGtXqmEBCG47UOFircA%2BtZlE2tQk1iJOEFMZ9%2FYPLmjUKo6osuoa9Lqi%2FKW4dnXzgg3DOROqMM%2B3DVjGXeVYpyTtpTNrxvHPMIrEzNine1OtDWEtgwKhOneoOvEHTRAyvqcdBbmpsOGzrFugEauBTXZmMbP2OW%2BFdBTo9qkZn4EqPLhPR4Rt7NNHISSOfxr4Dqusn7fWjoTsjsVlsed0ts12BGQLEaUnxEVs7alPfGsuqY4D8YBj2ZzxAqY4%2BQ1GY%2BlUYxEMHfR6WIui4AOFb7hxK%2FWV8xjs0LShc1jaRzigtls1MOJvNf5UQHgLwkx10HJaiYaVRoRtqdsBPDS2FysSQo%2BKlLQTJDS2KaTN8BTglVhCgVEHTRnCycYm7EQGFyhx2Sj7SSJ6FE5ibBFPR2K8ijMwPF72I0kMBhWdRBCshVrjXhhHt%2BHPDuewLWvx4vdACcutLsUOYkJXZl5t2pN%2FaeeWtFdUZa22I9LCgUTGzgCpdVsqn0wAqyciJysiGr%2BxzONSFe%2FDCf8nmSYVs9ZQgqattYdXrlACAgkullpTuZn6W3U6pOx1ovs6iEGCdSWBqRpVulKxMMrBa7wccSJ6Sq%2FMwjK04A8mybSjj9PTxe2TNHYGWl%2F9RgQZj2P%2FJ3V%2B1M%2FCq5UU3cMJuans0GOqUBEKTZ7nbuVz6Za9gQz8IgnW0gvGpQLvNaMyAUzCRlsk%2Bk1SqBrigVc0dPwG2zmiaPMHbHeYOkCVVxMughTt0WCBku2Rs5rQASU1Mf7PS1PDHEFLdwmTs5dNB944pMMlKeGd6JQhFGsHECfe1%2B1HFNYfK%2BKwDNYoYucUFZRWzphPhAx5lkhlnY%2B7Y8xh%2FfMUeBWhV45plLrP5P07UNh1uBc%2BHW%2FPDg&X-Amz-Signature=413fd1c39166d47bd528aadab7299d9ec6f297b0d0bc051dfe53c0e9d11185ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV5WBAPP%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCR9M5er%2B%2BhIBDrBX0p9OG1Rsa%2FAPDGlpy%2BHDMWspxyagIgKyyUlBqw%2BSrfplF0jifJC6DQZKeGjtsBjxUul%2FDb1UwqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGtGtXqmEBCG47UOFircA%2BtZlE2tQk1iJOEFMZ9%2FYPLmjUKo6osuoa9Lqi%2FKW4dnXzgg3DOROqMM%2B3DVjGXeVYpyTtpTNrxvHPMIrEzNine1OtDWEtgwKhOneoOvEHTRAyvqcdBbmpsOGzrFugEauBTXZmMbP2OW%2BFdBTo9qkZn4EqPLhPR4Rt7NNHISSOfxr4Dqusn7fWjoTsjsVlsed0ts12BGQLEaUnxEVs7alPfGsuqY4D8YBj2ZzxAqY4%2BQ1GY%2BlUYxEMHfR6WIui4AOFb7hxK%2FWV8xjs0LShc1jaRzigtls1MOJvNf5UQHgLwkx10HJaiYaVRoRtqdsBPDS2FysSQo%2BKlLQTJDS2KaTN8BTglVhCgVEHTRnCycYm7EQGFyhx2Sj7SSJ6FE5ibBFPR2K8ijMwPF72I0kMBhWdRBCshVrjXhhHt%2BHPDuewLWvx4vdACcutLsUOYkJXZl5t2pN%2FaeeWtFdUZa22I9LCgUTGzgCpdVsqn0wAqyciJysiGr%2BxzONSFe%2FDCf8nmSYVs9ZQgqattYdXrlACAgkullpTuZn6W3U6pOx1ovs6iEGCdSWBqRpVulKxMMrBa7wccSJ6Sq%2FMwjK04A8mybSjj9PTxe2TNHYGWl%2F9RgQZj2P%2FJ3V%2B1M%2FCq5UU3cMJuans0GOqUBEKTZ7nbuVz6Za9gQz8IgnW0gvGpQLvNaMyAUzCRlsk%2Bk1SqBrigVc0dPwG2zmiaPMHbHeYOkCVVxMughTt0WCBku2Rs5rQASU1Mf7PS1PDHEFLdwmTs5dNB944pMMlKeGd6JQhFGsHECfe1%2B1HFNYfK%2BKwDNYoYucUFZRWzphPhAx5lkhlnY%2B7Y8xh%2FfMUeBWhV45plLrP5P07UNh1uBc%2BHW%2FPDg&X-Amz-Signature=ae2c153221dbe3a2e6de5b7b73513324b5b0aa8c7b1dc0fef06e5b94e5b27e3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

