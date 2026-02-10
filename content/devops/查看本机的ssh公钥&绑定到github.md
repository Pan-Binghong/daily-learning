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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQGG7OST%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1uc4qGJ1oMA2ZpFlhwfrsEGSYehCNGKkumfSzVwvfmAiBwqJM1tcygT9dyMh1Yvw6jP42nHbn51nX5BkOMMyJ2kSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCi6KWLZHizSbddMEKtwDr04Wj01IZQ3dEs%2FTn8COJQO3HHY8zd5U5sOR2QrbkffyiuVy6WV5%2FfHep1mazTZ03auxBnuP38qPM%2FPfq8phQJkmyIQd4GpGZv3%2BngQ5DEUVTuuVsNh7ASRbEmX3Be%2F%2BHgD8gR2xi5IncYPhKAOKYLOUbsTJv9llo7rsc36qqaRt4bcYwDZ5SVvyBHgFaMmU%2FMfQZx1ZdgsMgZuL91%2BhK5EfEEcp7x1OIKqYnVeF%2FpHuCxvRMLfqG10PBH2LHoIzE588NAJ%2BYQdnvgDHlED6S6GrM1loqsDtlt3pbVrgRIHEl3AWS6P1n3NCWnVA9lzGA6Qiddesfz2slqa%2B8%2FXfWOocx5L%2BN3slio0TzC3Ijn6UAYvURcTIFN466FQKLsXvGA%2BWNQZEsXm0NvYpN8p1f%2FG0cuYStDmJIm0RECuNlYOXvaUeDLb%2B6rmjzp6mVx6%2F54QWqFAlJxODU1zokwiEVsxD8SnMNLJQPaOPmXDeubpyFZYKosbWR9UrGHevjPKmj0csOTAR9KU2jyVj49%2FYIgZe%2Bu5b6OkdSjL%2FSv4KEl9itwn3aSBTsm%2Fznw5RAYAQAjUYJ5GN5p7Q67TxHou21bv%2FW5CRt%2BLJ8Ou2EcVKRrPJgJcsEkSPdh%2FG4WMwmcOqzAY6pgHPRWRK%2FPdz6DH%2BMWAkbKhcjeVHHZHnyl4r7M9dQHRuANqCb%2B1TIJDw%2FEJ9Fotp%2FyEIjM64h4tDTMcS3ln%2FHPpMVj9KqY1daVSMFTOWgvPPa2SYbF%2Bs6zqntyZV%2F1VypkNk0PM%2F0PD2kIeZFfK%2FJocE6HKQDVVOAZBK6hOJPHZXJAXchz6h2d02Am0YPUG9oOeanfEZTmdc1Lb4FuSkUpN5Ko5wv%2BOP&X-Amz-Signature=abe123a4c389e3dbefbaf6ddc4ecfeb6c37b5bcced11fb59eca535177cd95e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQGG7OST%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1uc4qGJ1oMA2ZpFlhwfrsEGSYehCNGKkumfSzVwvfmAiBwqJM1tcygT9dyMh1Yvw6jP42nHbn51nX5BkOMMyJ2kSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCi6KWLZHizSbddMEKtwDr04Wj01IZQ3dEs%2FTn8COJQO3HHY8zd5U5sOR2QrbkffyiuVy6WV5%2FfHep1mazTZ03auxBnuP38qPM%2FPfq8phQJkmyIQd4GpGZv3%2BngQ5DEUVTuuVsNh7ASRbEmX3Be%2F%2BHgD8gR2xi5IncYPhKAOKYLOUbsTJv9llo7rsc36qqaRt4bcYwDZ5SVvyBHgFaMmU%2FMfQZx1ZdgsMgZuL91%2BhK5EfEEcp7x1OIKqYnVeF%2FpHuCxvRMLfqG10PBH2LHoIzE588NAJ%2BYQdnvgDHlED6S6GrM1loqsDtlt3pbVrgRIHEl3AWS6P1n3NCWnVA9lzGA6Qiddesfz2slqa%2B8%2FXfWOocx5L%2BN3slio0TzC3Ijn6UAYvURcTIFN466FQKLsXvGA%2BWNQZEsXm0NvYpN8p1f%2FG0cuYStDmJIm0RECuNlYOXvaUeDLb%2B6rmjzp6mVx6%2F54QWqFAlJxODU1zokwiEVsxD8SnMNLJQPaOPmXDeubpyFZYKosbWR9UrGHevjPKmj0csOTAR9KU2jyVj49%2FYIgZe%2Bu5b6OkdSjL%2FSv4KEl9itwn3aSBTsm%2Fznw5RAYAQAjUYJ5GN5p7Q67TxHou21bv%2FW5CRt%2BLJ8Ou2EcVKRrPJgJcsEkSPdh%2FG4WMwmcOqzAY6pgHPRWRK%2FPdz6DH%2BMWAkbKhcjeVHHZHnyl4r7M9dQHRuANqCb%2B1TIJDw%2FEJ9Fotp%2FyEIjM64h4tDTMcS3ln%2FHPpMVj9KqY1daVSMFTOWgvPPa2SYbF%2Bs6zqntyZV%2F1VypkNk0PM%2F0PD2kIeZFfK%2FJocE6HKQDVVOAZBK6hOJPHZXJAXchz6h2d02Am0YPUG9oOeanfEZTmdc1Lb4FuSkUpN5Ko5wv%2BOP&X-Amz-Signature=ee739d6f328b39705b7ca22052dba71de26f149c4b7d3e1a35b40b073517d21b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

