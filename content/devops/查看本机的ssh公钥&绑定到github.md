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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJHPDIC%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUtlsDz4S17P6LIRqqV1YsQxEuGsEQhxz3flk2WhVncQIgcijlSkhk0lqb91jawRndsAE1spVeSWza6tb4lzKtmr0q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDPO9HZExX2PW00VnZyrcAyw%2BE7D7LLSLDboNOwqNkxNMpuYfPXYV3HQsK5NVgIahmzD2aUAKe2pZu5kOMEvCrHwMD1LM9tBPZqRB9OdiIj9vba%2BuSuJjV3mdY%2FVgrxodh2BrUtVeOwfQkvh%2BY9yBD%2BkOA2VIDZmBqTOuWiq246rH6%2B6WtbTaIR0lJRlQM4ouNpu6pyp9UUK16L4VaoXPCriJaSChlg17n4t5mgjq%2FdhIXHi122xFN%2BeDutfzwzZuXQscvGuoxQDnD9QhTZps4drtXVDImSdN7kNCpy%2BZd0BlFX6bvekLtuhPgd60B2joaKznTOb4tqJj3GvP62DLbfhVQjOJGlJH2I%2F5osPp8LF9Fex7kRXKYq%2FofHi0L7YmMn2dVWBzMEHn4E5DwIsUuuoll57OPZd1DsOs8i43JrAomc4hO47vmXM%2B2r6RMSNlx6Nn8PEKi6j2P4mRT4cXYBT0u6ka47FwznTcKLmZ%2F2Vy3Fq2IZebNEfR%2FsYt5Xb053lGUtfaqpXbiHyeFHm1iHR%2Fuhc2a2UG%2F628ZHyybZpa01mIwl6mD9%2Bylbm0p0%2BVETQirrzNj%2BzgdlcUcKBMN621NVZykraZjaChMxMgST88rzyGv3%2BhNSB%2FJj4pvf87H2%2FYXO%2Bvxdjafg6wMO2yyM0GOqUBEAEohxTWd1uJCkfJrm6y134y6bzQjSj7YSBDWqspzGMfjfo5bJ%2B0Q3rWlZlA9tAue77Y7VRkKLMHfXTkXumxLWNzcWHavxPbM3ATKI7S1q9LOXL4B6hQST0kmPK1jkcwde96u%2F6WSFFIvg14gecFVR5%2FD59FE8DGft1eLg2tC01z%2BnP%2BmxxNHuEzTkDTNbMdffgYixaYio8OffaSmOUAc1AHGgLw&X-Amz-Signature=a358835153d0db7fb2409f1995c9c19afd4eeae3475769105a007fcbdcd32fa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJHPDIC%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUtlsDz4S17P6LIRqqV1YsQxEuGsEQhxz3flk2WhVncQIgcijlSkhk0lqb91jawRndsAE1spVeSWza6tb4lzKtmr0q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDPO9HZExX2PW00VnZyrcAyw%2BE7D7LLSLDboNOwqNkxNMpuYfPXYV3HQsK5NVgIahmzD2aUAKe2pZu5kOMEvCrHwMD1LM9tBPZqRB9OdiIj9vba%2BuSuJjV3mdY%2FVgrxodh2BrUtVeOwfQkvh%2BY9yBD%2BkOA2VIDZmBqTOuWiq246rH6%2B6WtbTaIR0lJRlQM4ouNpu6pyp9UUK16L4VaoXPCriJaSChlg17n4t5mgjq%2FdhIXHi122xFN%2BeDutfzwzZuXQscvGuoxQDnD9QhTZps4drtXVDImSdN7kNCpy%2BZd0BlFX6bvekLtuhPgd60B2joaKznTOb4tqJj3GvP62DLbfhVQjOJGlJH2I%2F5osPp8LF9Fex7kRXKYq%2FofHi0L7YmMn2dVWBzMEHn4E5DwIsUuuoll57OPZd1DsOs8i43JrAomc4hO47vmXM%2B2r6RMSNlx6Nn8PEKi6j2P4mRT4cXYBT0u6ka47FwznTcKLmZ%2F2Vy3Fq2IZebNEfR%2FsYt5Xb053lGUtfaqpXbiHyeFHm1iHR%2Fuhc2a2UG%2F628ZHyybZpa01mIwl6mD9%2Bylbm0p0%2BVETQirrzNj%2BzgdlcUcKBMN621NVZykraZjaChMxMgST88rzyGv3%2BhNSB%2FJj4pvf87H2%2FYXO%2Bvxdjafg6wMO2yyM0GOqUBEAEohxTWd1uJCkfJrm6y134y6bzQjSj7YSBDWqspzGMfjfo5bJ%2B0Q3rWlZlA9tAue77Y7VRkKLMHfXTkXumxLWNzcWHavxPbM3ATKI7S1q9LOXL4B6hQST0kmPK1jkcwde96u%2F6WSFFIvg14gecFVR5%2FD59FE8DGft1eLg2tC01z%2BnP%2BmxxNHuEzTkDTNbMdffgYixaYio8OffaSmOUAc1AHGgLw&X-Amz-Signature=0f8d562fc85a20ef4a9570e58b2b18c6c9ac5d371ddaefcf5f2b118bcf06bab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

