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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XTFBXSC%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchcll3b5sk4q7hOD1onUaFZF3JH1eSxeoJi%2F3wydEJAiEAz6Tf4mbxBxnCOlqH3bStT9OshTLURPYhraZR%2F9syHt0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLeRPhUNhGWq5qqmqyrcA4jRMdC33rwixpe9qHyeahva3P4oPgUjz4NnW%2FLq5Al3st%2FWECVQjUMcoATahifVlMXHCkhFsdruWdNqiCCjkFUy18qiDTq1QYHPzLAWn0pXl%2B6jhve7flZyWVpHJVCNrkSVZwpQNonPb%2FkRJhZV05lKopjn2GWfmAPXjGQbFD1i4gBnjemCiu3hH%2Fe2SP34as2EaINkXQd%2F%2FXt%2B6GHWOuAdNEpvt%2BDVFifcMAZBtNKyt4hlyQkNZvDInR8PRYqRwEVvC7xu0hR%2FjjjGcfTCClsHiiSaUHh7cq6H4C55aUDWuw7FO0qd0GRkuKr%2B9NC55b0tlABUWvOgUMiB43QsFPR17cdzL1SK5gey5TW%2B63Mz%2F6dCoqhizlhrnYOKG%2Bx1PgWDJZDVsDhsto%2FesqtCGP52tHXK4RaYeFCX0Lv4c5rQgcmHHvmlj0oy0ovVdR7Ly2WrGx%2FfxgoRjpxF5ypQ7oDioiAXB6%2F1nqkREa5bLorQIYdtlGSXP1ljGvSLKf4DjEQYxh%2FErQdJkrC%2BuD%2BZVZBaJ%2FRC58IJdeoxBda6%2BzGppGHJuDQ49bHleqdaOJG6o5Had%2FTiszbdaH%2B9%2FVjW0n5P%2FpINRSumLx1AsgnYGFS6YCrcfI2jALgXj9TJMLiyzM4GOqUBeJzjjYDh2uxsPbT9HgRAzVe61buaieVvG2n2G9njQysf2h0%2B4vuvt2bK5VMjIWp4Ao7jrAgEeYZ%2FB2i4bjoOTqLQfE7XF1NEENzeBq7WPAY%2Fe27fKjkrblrw%2Fe%2BdE6tEpSl0CDr5s8c3hbUCxd2vtRb%2F26ebRVFyo7TpW9T1YDP96i8xg4nQvo9u7jf55qR9%2FfEiF5j%2FcWWpVYqp5EM0EzWNt5WF&X-Amz-Signature=eb1b119f2546815bc99fa733658e7e3c5ce83dd073bd8def12c2d3cf111d2661&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XTFBXSC%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchcll3b5sk4q7hOD1onUaFZF3JH1eSxeoJi%2F3wydEJAiEAz6Tf4mbxBxnCOlqH3bStT9OshTLURPYhraZR%2F9syHt0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLeRPhUNhGWq5qqmqyrcA4jRMdC33rwixpe9qHyeahva3P4oPgUjz4NnW%2FLq5Al3st%2FWECVQjUMcoATahifVlMXHCkhFsdruWdNqiCCjkFUy18qiDTq1QYHPzLAWn0pXl%2B6jhve7flZyWVpHJVCNrkSVZwpQNonPb%2FkRJhZV05lKopjn2GWfmAPXjGQbFD1i4gBnjemCiu3hH%2Fe2SP34as2EaINkXQd%2F%2FXt%2B6GHWOuAdNEpvt%2BDVFifcMAZBtNKyt4hlyQkNZvDInR8PRYqRwEVvC7xu0hR%2FjjjGcfTCClsHiiSaUHh7cq6H4C55aUDWuw7FO0qd0GRkuKr%2B9NC55b0tlABUWvOgUMiB43QsFPR17cdzL1SK5gey5TW%2B63Mz%2F6dCoqhizlhrnYOKG%2Bx1PgWDJZDVsDhsto%2FesqtCGP52tHXK4RaYeFCX0Lv4c5rQgcmHHvmlj0oy0ovVdR7Ly2WrGx%2FfxgoRjpxF5ypQ7oDioiAXB6%2F1nqkREa5bLorQIYdtlGSXP1ljGvSLKf4DjEQYxh%2FErQdJkrC%2BuD%2BZVZBaJ%2FRC58IJdeoxBda6%2BzGppGHJuDQ49bHleqdaOJG6o5Had%2FTiszbdaH%2B9%2FVjW0n5P%2FpINRSumLx1AsgnYGFS6YCrcfI2jALgXj9TJMLiyzM4GOqUBeJzjjYDh2uxsPbT9HgRAzVe61buaieVvG2n2G9njQysf2h0%2B4vuvt2bK5VMjIWp4Ao7jrAgEeYZ%2FB2i4bjoOTqLQfE7XF1NEENzeBq7WPAY%2Fe27fKjkrblrw%2Fe%2BdE6tEpSl0CDr5s8c3hbUCxd2vtRb%2F26ebRVFyo7TpW9T1YDP96i8xg4nQvo9u7jf55qR9%2FfEiF5j%2FcWWpVYqp5EM0EzWNt5WF&X-Amz-Signature=0e8885abbed4ecde8c6a043ddfe664576920a2db9d4219dd518a849327257450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

