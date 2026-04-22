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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVQ4EQGZ%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBZXtiKddgubgiImy3kU4QYFMmfcaYYqlyiVhBT0xH9rAiEA%2BXirjoJ%2Fe01Yt4L6wM2C3e35peNJDYh8WtYJ2%2B6GEhkq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDJarR11cPWmeyNi%2BtyrcA7uyYfyo77SI6232WbuJYsDPNXItsR3NAdhS5SIDZ19OUV7dl5Zpz88MFCttLmQ2Ro27pAX1iubaKWBAnfE235KlGKv1dcHPNGfmDSY4xVodPkd7ETm5KTxBmZzxY1MFtvcN8n2QKFqWJbX1WGiQrl2AaU1D5C%2FTSZ8Hw3dRwBTV2RLiCSS6%2F20EiLoJzm2q2L37DwDeC9CKuLlTU1qEjOcJl7FA9ebpB7SfOr6ghezXKj8ICAHnCa3enHTvU4MHVfR82gdeBqF%2BaBDKofPMscbaAWLacGk5EjryVPEQO1rfTrJNRH6fyC%2BvMqvc53%2F3vARBfNhhlFfWV8i8w2iaJYZXBlY5XRqVK0MX%2FEmSYRLo0hxf2CfvBs07ASED5FYyUGrUdmgxP90mh1NQwgaw5IxlM08iKTJo4bgmb%2BFQ2tf3sNHIrOnTvHo06F3KRRpR5nOXbROkcrx8mGhvbTv%2FZ3jf2%2By6s3IGdq2krVhwcUQE%2BlIc51HaAo6AwWNW%2FWNGv7S8VtY6wWHXYg7PbzWAHoi6A%2F9IAkgD2bD2kOvvPHeT08eVi9s0rL%2B6V7fAp1Ru1vsgzaXTvTCS6q%2Bt8%2FbStI7D1%2BpLkjzzV8%2FVxWNqyeAevWykVJI4AQXYhgdVMIz8oM8GOqUBbShwhrQlT5eTd4%2BWIFvkvEMMfKE13PxbzoNvF5RekiUXqWG4pnQ97D56y6LxcEynKJDQLb%2FjmKJajttWlumhUTd88iWqLJNjBFnuWGuoKcyc5eBSLYJr%2FIB6jk65XFEmiHSd3YbgZ4v%2FuZGnN1MhlzIZvIz5vRfOsNz4E4ClyVEseCn8nTa7u6v8AePgWqtQXuLbMrm0Dz4wmS0NMeICJ7pEezNU&X-Amz-Signature=7f32e43cde192b828292e45fed9504026630a76c7beaf2627d3bf8d5d377840a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVQ4EQGZ%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBZXtiKddgubgiImy3kU4QYFMmfcaYYqlyiVhBT0xH9rAiEA%2BXirjoJ%2Fe01Yt4L6wM2C3e35peNJDYh8WtYJ2%2B6GEhkq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDJarR11cPWmeyNi%2BtyrcA7uyYfyo77SI6232WbuJYsDPNXItsR3NAdhS5SIDZ19OUV7dl5Zpz88MFCttLmQ2Ro27pAX1iubaKWBAnfE235KlGKv1dcHPNGfmDSY4xVodPkd7ETm5KTxBmZzxY1MFtvcN8n2QKFqWJbX1WGiQrl2AaU1D5C%2FTSZ8Hw3dRwBTV2RLiCSS6%2F20EiLoJzm2q2L37DwDeC9CKuLlTU1qEjOcJl7FA9ebpB7SfOr6ghezXKj8ICAHnCa3enHTvU4MHVfR82gdeBqF%2BaBDKofPMscbaAWLacGk5EjryVPEQO1rfTrJNRH6fyC%2BvMqvc53%2F3vARBfNhhlFfWV8i8w2iaJYZXBlY5XRqVK0MX%2FEmSYRLo0hxf2CfvBs07ASED5FYyUGrUdmgxP90mh1NQwgaw5IxlM08iKTJo4bgmb%2BFQ2tf3sNHIrOnTvHo06F3KRRpR5nOXbROkcrx8mGhvbTv%2FZ3jf2%2By6s3IGdq2krVhwcUQE%2BlIc51HaAo6AwWNW%2FWNGv7S8VtY6wWHXYg7PbzWAHoi6A%2F9IAkgD2bD2kOvvPHeT08eVi9s0rL%2B6V7fAp1Ru1vsgzaXTvTCS6q%2Bt8%2FbStI7D1%2BpLkjzzV8%2FVxWNqyeAevWykVJI4AQXYhgdVMIz8oM8GOqUBbShwhrQlT5eTd4%2BWIFvkvEMMfKE13PxbzoNvF5RekiUXqWG4pnQ97D56y6LxcEynKJDQLb%2FjmKJajttWlumhUTd88iWqLJNjBFnuWGuoKcyc5eBSLYJr%2FIB6jk65XFEmiHSd3YbgZ4v%2FuZGnN1MhlzIZvIz5vRfOsNz4E4ClyVEseCn8nTa7u6v8AePgWqtQXuLbMrm0Dz4wmS0NMeICJ7pEezNU&X-Amz-Signature=641573d2fa09a290978b872fb01baf0a682795051dc561609dee6fea9e73a124&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

