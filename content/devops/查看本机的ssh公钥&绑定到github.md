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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQEBG3IQ%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDB3AEwDkrzRVkSmu64t6b7sCRop%2BBy3F0jzt%2F%2BFHisLgIhAO3i92XtPHyAqsp%2FTmjs7P1pljiYirXRt7bLsJEaUaXRKv8DCFMQABoMNjM3NDIzMTgzODA1Igwh%2BDEyoD%2BgobUlw3Uq3APbRvYsKwdAwIMhIhto8ZbQtnNiqSZ8VN%2B61SSEXJ4hxDqxfRFIzAOcjzoMvAlJwa4SioDXMMVD4A3Yg0i%2B%2FeUhTj7R4znYMsWTCdYei%2FEw0W%2FlhcQRe7vwDi9E%2BzECPA84T7jWvEmbO%2Bf7sQ3gIyxoHKkTboeJqTfdKsqeGSZPns6EX8jVEQdcAZd4tWsDShmzXYw3s%2FTw6EPa49suHs7OLqCZajtHVkpBBc44AnDHnq%2F2LX6n17KK2z38PUFdxZXO08OBxrHLKozN0C06XTd6D0w8FoBj7p033QKctF5uguHMq3A6juwqi%2BxDjO4hmh%2BOEp95TtJI6nOf3rAKcRZWKQ2IOhITcp3qiUPhZTt6d5aQ2IvTw7Ayq3WqpBp9uNEuVZu5H4SAy129v9OCJWK60QBCOVlbf5MI9Np%2B5fxoM%2BmzPgxA2a%2BZwk5js4KiZpXpTrFo8nxeiElfNiRp61P2ZPShmsFsbc0pO9SvqMzfMFRv6F0W46AjAnawutygzAUuZHm9BeEzIE9GULvtbAlj0hyYK%2FXoKfhtCSdZN1gF%2FB4H7r4soCJqTV2h9OuaKv0KNi8guTlqNpMtm0fJYOyYhqF6xAoHGompM9rLEBWl5W66oCD7AOn6a%2FhZNzCqxJrMBjqkAZh9Rg5Bafs3h2NBCtsXV%2BCJG65hZT1ntNROmATicVfxMhnYwNSYUBNiqr4epFJKZ4SgL%2FnIWkQFXlx22%2FH1PgxZSOFg4hW%2Fw%2FcQg5KFuJg%2FeRHuxeg14ODde57B5y0pmlXCTMOrEKAZ3OqsC12EZYg2fxIviA5o7H4aSoTsxy7rzpW7Kw%2By%2FLLsCI94QlnM2xAfekM6kvMVW5zO%2BZsv2U3wVd1Y&X-Amz-Signature=24c1ea07d6e88c38172b38bba2b2a8d531753e354da245f9efde00cfa280002d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQEBG3IQ%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDB3AEwDkrzRVkSmu64t6b7sCRop%2BBy3F0jzt%2F%2BFHisLgIhAO3i92XtPHyAqsp%2FTmjs7P1pljiYirXRt7bLsJEaUaXRKv8DCFMQABoMNjM3NDIzMTgzODA1Igwh%2BDEyoD%2BgobUlw3Uq3APbRvYsKwdAwIMhIhto8ZbQtnNiqSZ8VN%2B61SSEXJ4hxDqxfRFIzAOcjzoMvAlJwa4SioDXMMVD4A3Yg0i%2B%2FeUhTj7R4znYMsWTCdYei%2FEw0W%2FlhcQRe7vwDi9E%2BzECPA84T7jWvEmbO%2Bf7sQ3gIyxoHKkTboeJqTfdKsqeGSZPns6EX8jVEQdcAZd4tWsDShmzXYw3s%2FTw6EPa49suHs7OLqCZajtHVkpBBc44AnDHnq%2F2LX6n17KK2z38PUFdxZXO08OBxrHLKozN0C06XTd6D0w8FoBj7p033QKctF5uguHMq3A6juwqi%2BxDjO4hmh%2BOEp95TtJI6nOf3rAKcRZWKQ2IOhITcp3qiUPhZTt6d5aQ2IvTw7Ayq3WqpBp9uNEuVZu5H4SAy129v9OCJWK60QBCOVlbf5MI9Np%2B5fxoM%2BmzPgxA2a%2BZwk5js4KiZpXpTrFo8nxeiElfNiRp61P2ZPShmsFsbc0pO9SvqMzfMFRv6F0W46AjAnawutygzAUuZHm9BeEzIE9GULvtbAlj0hyYK%2FXoKfhtCSdZN1gF%2FB4H7r4soCJqTV2h9OuaKv0KNi8guTlqNpMtm0fJYOyYhqF6xAoHGompM9rLEBWl5W66oCD7AOn6a%2FhZNzCqxJrMBjqkAZh9Rg5Bafs3h2NBCtsXV%2BCJG65hZT1ntNROmATicVfxMhnYwNSYUBNiqr4epFJKZ4SgL%2FnIWkQFXlx22%2FH1PgxZSOFg4hW%2Fw%2FcQg5KFuJg%2FeRHuxeg14ODde57B5y0pmlXCTMOrEKAZ3OqsC12EZYg2fxIviA5o7H4aSoTsxy7rzpW7Kw%2By%2FLLsCI94QlnM2xAfekM6kvMVW5zO%2BZsv2U3wVd1Y&X-Amz-Signature=3df4b2cceaf3de68828eff54329f0cee59e397395d463e5c20c6130e2fbb1a73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

