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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWNP33TK%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD%2BW8WyoS5nCjzhZzWFhxA0byrKmF%2BjS8PTXUGAe2S2vAIgIUjMiTN29M%2BXXQBUugrxwMQ1y%2BhB1pitRg6lIQoVwu0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPeM0eFbPoHgBw3JXircA3m%2BRUEKQkVS3HJlnqbFrGbtQwaZ1xk2PumbCUifyZrk2dsIqlVtHHcSiWcIXmsBBiy%2BnPfrV9Tj8pPmlKQM9UzYizeS5o1n6JEYCwgrsod4nZi8JR9GVllfLKh4jNd0qGhkdpFFDmZg%2FboBBbtyNHnC7jGswYkQ6%2B9kgBazsYHP3qxs2tFrgTSSIfSUn4KPZMJCeagBGSGIlJQKT7WBIMWkKMQdc6yaZmMcHtrtgjjCFk5MB%2FVyENgSlbs2Fa1wAQO0Uo2iwvgUgDddbAworqRnxUszvmBzAlbOU0vo6U%2FQbMA708mB5Safk4zAGQihGcA5Rjzhli677%2FUDN%2BOVFLcVk9kJ2%2FG%2FLd%2FflVkAANaP9%2BAKnwqmJINeNM52Bf551tP%2FFJeJ1HUUYi975FJ20tdEPuefv%2BMhqsMFn%2FAMjPIU9x%2F2lo1obUl7cKfRQxer3ZLVK7g5FAevKHSV28fIPQLNeGNrZdqw518bEJBZk4UGoPNRn7PQSQiaaeMSjS66dQ8BjNg5hCWMfkdlpvmy1akv0GA6mOzb%2BV943dLYSBNsupkmvIOGxonAUVRhfL2QdRf7mm%2Bo%2FVVjhCCxDSnXCSiKF%2BEDVUDuNBd%2FlIJVV%2BxcT4jOFUc4%2FMQtzAfpMNHvrM4GOqUBfaO5AeZa9SEWvGHGUSGVVe0H66V6dA2T%2FVHU6UUceeQw%2Fqo5uYdg%2BH5OLrwr59kmTPGwfC8aHVdXqqbnOZIyETrFfh2qbLZXIvN3pj0wOjdpa0DDQh3TekUMQRWHRrwjw8ukC5mlKYsJ7YyT624sQZZsVJzHuBAveY2uDJPHtdO9WI6G88ZJDARKH2VbWi%2BirFVM4NwAiJAe9DtPW6KB48pkfa2i&X-Amz-Signature=f6c15403b7a5d88656598ab05115bc600222b7e9a35da0b1857c5bb4419e2037&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWNP33TK%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD%2BW8WyoS5nCjzhZzWFhxA0byrKmF%2BjS8PTXUGAe2S2vAIgIUjMiTN29M%2BXXQBUugrxwMQ1y%2BhB1pitRg6lIQoVwu0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPeM0eFbPoHgBw3JXircA3m%2BRUEKQkVS3HJlnqbFrGbtQwaZ1xk2PumbCUifyZrk2dsIqlVtHHcSiWcIXmsBBiy%2BnPfrV9Tj8pPmlKQM9UzYizeS5o1n6JEYCwgrsod4nZi8JR9GVllfLKh4jNd0qGhkdpFFDmZg%2FboBBbtyNHnC7jGswYkQ6%2B9kgBazsYHP3qxs2tFrgTSSIfSUn4KPZMJCeagBGSGIlJQKT7WBIMWkKMQdc6yaZmMcHtrtgjjCFk5MB%2FVyENgSlbs2Fa1wAQO0Uo2iwvgUgDddbAworqRnxUszvmBzAlbOU0vo6U%2FQbMA708mB5Safk4zAGQihGcA5Rjzhli677%2FUDN%2BOVFLcVk9kJ2%2FG%2FLd%2FflVkAANaP9%2BAKnwqmJINeNM52Bf551tP%2FFJeJ1HUUYi975FJ20tdEPuefv%2BMhqsMFn%2FAMjPIU9x%2F2lo1obUl7cKfRQxer3ZLVK7g5FAevKHSV28fIPQLNeGNrZdqw518bEJBZk4UGoPNRn7PQSQiaaeMSjS66dQ8BjNg5hCWMfkdlpvmy1akv0GA6mOzb%2BV943dLYSBNsupkmvIOGxonAUVRhfL2QdRf7mm%2Bo%2FVVjhCCxDSnXCSiKF%2BEDVUDuNBd%2FlIJVV%2BxcT4jOFUc4%2FMQtzAfpMNHvrM4GOqUBfaO5AeZa9SEWvGHGUSGVVe0H66V6dA2T%2FVHU6UUceeQw%2Fqo5uYdg%2BH5OLrwr59kmTPGwfC8aHVdXqqbnOZIyETrFfh2qbLZXIvN3pj0wOjdpa0DDQh3TekUMQRWHRrwjw8ukC5mlKYsJ7YyT624sQZZsVJzHuBAveY2uDJPHtdO9WI6G88ZJDARKH2VbWi%2BirFVM4NwAiJAe9DtPW6KB48pkfa2i&X-Amz-Signature=d7567d5d5c74b4a8e48c09bde7d709c51e400706a31f0cd9887a13c957f690a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

