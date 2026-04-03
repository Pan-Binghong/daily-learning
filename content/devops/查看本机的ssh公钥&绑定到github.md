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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5XGEW3L%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkHS1VZf37JbQI4FJOyvzYLo6NWpJ8jl3g4QxX1BWiUQIgHnqruJ%2BmpJQSvypu7uz8%2FsUvMCC5fueCmr%2B31zJOipgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDMJ52ecC0UJ5jBFejCrcA1Q5ZxIA%2FA6eTiFe1%2Bdfudx%2BSe2COPrnHdo%2BkBtJQkkprZJBeWn3ZrUmuY7ETYXSQkMEG0XbF2SGNP9m%2BzdGldi30FmhOQH2QSYl3NgabK27E%2BpIpTHj7uH913w9YJjiVYvG0KM%2F4XXV6slMK6%2BrwblieY59canADv2sWvzeDffomHCfIs%2F3RIii2%2FeiZI9L8qHh8WT7laoNAjR9NsSRRWeCFK1Quo6RWBqdf5Lp4Fcm1jG9v%2F%2BIUS%2Fcwp8KWgQtPBjaJ3S36cDFObNBLtVS2mPZYxAZFwSGQ4kvC%2Bg1xqB2kifPhLf5rEvfv0tfxJEXpD6wzPflLjy%2Fyec1jA7spHfAQFbXRh53Kt8a5ctdsEHU%2F2qAAJlWr6MwJ%2F4ly%2BWjftsGlnrD557hZEqyr7lTd0xe7TXmHNOau5HmxMvcfefOuzn9RRp2KObZ7AkeuP1a%2FVmsQB6Z72NHRsrJV6t5%2FNoOPqfWCqFoddqZ7%2BxKumwH8fvect3iZxlveFaI%2FjtHYjIGHiB3OzT75stYAcGIj4n4HYX8Kiy6iJ92NxnQtXZM7bXB9nAdGyJBoOGxrFfY40F8AVUb9FEHxR4yGVxwktARrY39trM4z7SSKq1uyER0QBFpsczg%2BeiPAYT%2FMKOtvc4GOqUBI7ua6mdSkadykjI7CxFNvUgBLKECbp1MgOBXidu57AvQuKZVqcoCRKmjGl3%2FclBIHq8oqdBlW0no1gg7aYOp%2FOqPlJBDSme%2BHHRQy4a%2FedLkS1aYLed%2FkpMRa%2ByYCE5JJeZ9vJ7SsK0GiKw1TyyDs63FF8Pakt1JOPkutHGVEDgn%2FqCC2sgjy%2B8lix9Pk8SfbjUdSr3p%2FN64yxWyNtcB9D5FroYJ&X-Amz-Signature=43f0f367bd03dbb04892a3366467f96cc55f7445c544c878529102f2b90433f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5XGEW3L%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkHS1VZf37JbQI4FJOyvzYLo6NWpJ8jl3g4QxX1BWiUQIgHnqruJ%2BmpJQSvypu7uz8%2FsUvMCC5fueCmr%2B31zJOipgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDMJ52ecC0UJ5jBFejCrcA1Q5ZxIA%2FA6eTiFe1%2Bdfudx%2BSe2COPrnHdo%2BkBtJQkkprZJBeWn3ZrUmuY7ETYXSQkMEG0XbF2SGNP9m%2BzdGldi30FmhOQH2QSYl3NgabK27E%2BpIpTHj7uH913w9YJjiVYvG0KM%2F4XXV6slMK6%2BrwblieY59canADv2sWvzeDffomHCfIs%2F3RIii2%2FeiZI9L8qHh8WT7laoNAjR9NsSRRWeCFK1Quo6RWBqdf5Lp4Fcm1jG9v%2F%2BIUS%2Fcwp8KWgQtPBjaJ3S36cDFObNBLtVS2mPZYxAZFwSGQ4kvC%2Bg1xqB2kifPhLf5rEvfv0tfxJEXpD6wzPflLjy%2Fyec1jA7spHfAQFbXRh53Kt8a5ctdsEHU%2F2qAAJlWr6MwJ%2F4ly%2BWjftsGlnrD557hZEqyr7lTd0xe7TXmHNOau5HmxMvcfefOuzn9RRp2KObZ7AkeuP1a%2FVmsQB6Z72NHRsrJV6t5%2FNoOPqfWCqFoddqZ7%2BxKumwH8fvect3iZxlveFaI%2FjtHYjIGHiB3OzT75stYAcGIj4n4HYX8Kiy6iJ92NxnQtXZM7bXB9nAdGyJBoOGxrFfY40F8AVUb9FEHxR4yGVxwktARrY39trM4z7SSKq1uyER0QBFpsczg%2BeiPAYT%2FMKOtvc4GOqUBI7ua6mdSkadykjI7CxFNvUgBLKECbp1MgOBXidu57AvQuKZVqcoCRKmjGl3%2FclBIHq8oqdBlW0no1gg7aYOp%2FOqPlJBDSme%2BHHRQy4a%2FedLkS1aYLed%2FkpMRa%2ByYCE5JJeZ9vJ7SsK0GiKw1TyyDs63FF8Pakt1JOPkutHGVEDgn%2FqCC2sgjy%2B8lix9Pk8SfbjUdSr3p%2FN64yxWyNtcB9D5FroYJ&X-Amz-Signature=8ebc8dc38147900366807a3808f1c76196e2e637f0e949edaa4e7d1be56f3d34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

