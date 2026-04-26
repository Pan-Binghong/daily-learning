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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GR3STAU%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeVci9GqdZDW2jxBMqf6RLbCJaq3UNmABZ8nuOBLTUOgIgB1Ix2JpV9BgRufwrv7HTe5E5uELcpPRLS2muw1Vk5WQqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0OTRURCfiyyGjLkSrcA%2BsNPz32NmJsF2H%2FFSO78K%2Bs%2FrRn7y6V0oDqUqSwXi21Fynz0lIg1HA8Qi2dVxS2HHRyJIZzl%2FTKuceF5e7Rp2CaQ2%2FsSbZL0VAhqTiDy4xQCaZ8oGVZu69%2FCTorGbTCu%2BKDlV7OGpWC7vYn4xgFAiZod%2FklSLZwp29Vvdj8DtEuyrPqqpwxAnsHK8l%2BXxWcOxE9mJKXaiVZnjurZ6aURzwer4w03ZEb%2FAShI%2BbJKaX47jE75rWsOgN%2BFpDgV%2F7K4mXmnl1yY3YRRDFuMASsny2Td3uJxDSyUwLyeDkRIFhcjH5UPOMe9GHm0VJlZ3ajbQLpyuJG85Yr7PcrVAsJlxZQa3gjkHyIRG1RcJ%2BBaktT5c5saryH3N7CT%2FGvR7N8ztSQ354%2FqZdZthAz%2FDSlLCt6HruYognX6dlOa3scmKnvqXXDaoqZa9a%2BE92bH3Do%2Fy9iPd3pA6pDIlpyubKQlyRPpsUxBaEnFO0naFvdhABFSMChubakSVoQLscovGmGzpBotIVUmByMNNbWTbAXXu%2BUy78iYIvc1y0U536KsHDeAf8h%2FfB%2BU1jD5E%2B5%2BVvlYNJJV%2FOsx3YHQGn4xHfRGhh%2FIbTpovw8trhixkx68l6jMcSx4jnMc1PFR9krMJKPts8GOqUBpWAGRc5EIBILDRJH1mrQc3xGJpjSSC%2FwoViWn8U%2F8QXKRQ6i0gllixiMLM8WYJHiOxGm0oQbp2w9MFkHE%2FLcf8SV9HbK%2FcrLOCQJHGAzIHBHNVl7cErLsv3A9lH1ZL%2F53KBqc7I7X7e5RLBTdAG5MbeCdybTskoB8FZOcXt8299bGiQwzaBj9En46XUbTg9oMp7wlbP36DFsU85Ne%2BXFC69rlLQk&X-Amz-Signature=77be1f696d602ff3c53822b57854412ed3da015bbbf7db41fdbe5b1a17f604dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GR3STAU%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeVci9GqdZDW2jxBMqf6RLbCJaq3UNmABZ8nuOBLTUOgIgB1Ix2JpV9BgRufwrv7HTe5E5uELcpPRLS2muw1Vk5WQqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0OTRURCfiyyGjLkSrcA%2BsNPz32NmJsF2H%2FFSO78K%2Bs%2FrRn7y6V0oDqUqSwXi21Fynz0lIg1HA8Qi2dVxS2HHRyJIZzl%2FTKuceF5e7Rp2CaQ2%2FsSbZL0VAhqTiDy4xQCaZ8oGVZu69%2FCTorGbTCu%2BKDlV7OGpWC7vYn4xgFAiZod%2FklSLZwp29Vvdj8DtEuyrPqqpwxAnsHK8l%2BXxWcOxE9mJKXaiVZnjurZ6aURzwer4w03ZEb%2FAShI%2BbJKaX47jE75rWsOgN%2BFpDgV%2F7K4mXmnl1yY3YRRDFuMASsny2Td3uJxDSyUwLyeDkRIFhcjH5UPOMe9GHm0VJlZ3ajbQLpyuJG85Yr7PcrVAsJlxZQa3gjkHyIRG1RcJ%2BBaktT5c5saryH3N7CT%2FGvR7N8ztSQ354%2FqZdZthAz%2FDSlLCt6HruYognX6dlOa3scmKnvqXXDaoqZa9a%2BE92bH3Do%2Fy9iPd3pA6pDIlpyubKQlyRPpsUxBaEnFO0naFvdhABFSMChubakSVoQLscovGmGzpBotIVUmByMNNbWTbAXXu%2BUy78iYIvc1y0U536KsHDeAf8h%2FfB%2BU1jD5E%2B5%2BVvlYNJJV%2FOsx3YHQGn4xHfRGhh%2FIbTpovw8trhixkx68l6jMcSx4jnMc1PFR9krMJKPts8GOqUBpWAGRc5EIBILDRJH1mrQc3xGJpjSSC%2FwoViWn8U%2F8QXKRQ6i0gllixiMLM8WYJHiOxGm0oQbp2w9MFkHE%2FLcf8SV9HbK%2FcrLOCQJHGAzIHBHNVl7cErLsv3A9lH1ZL%2F53KBqc7I7X7e5RLBTdAG5MbeCdybTskoB8FZOcXt8299bGiQwzaBj9En46XUbTg9oMp7wlbP36DFsU85Ne%2BXFC69rlLQk&X-Amz-Signature=896e2d85190c6fce2e29eb29e2ae8e3cd799fb3951772809a4cd110e64a85059&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

