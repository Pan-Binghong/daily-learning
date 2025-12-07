---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QM5UKM3%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBavv5q641Hv2JaBAgj%2FEIWUbHzNdvUkm3JnRUnwpjr5AiBXOZOp6rLlvWCA7IO71s9bqjCr22gvf1lYvN6S%2FawvZSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVn2lppatFsoRCGRMKtwD3oxAvIaeFhZ%2Fm1oICNCqVP0AlaODa1cjXRp3TBp9mOpyQ%2FAG0eVTGEaOLALQ%2BrRnB%2FzETUbzV2xEIXqs8lVcfuTpykSkmPhVqoCe8%2Bw6chiUItomWsl03yi%2FMqz6dwq5RzfLOL6Kz7BTCPRbp2Yc0CdR8HmD9sh8U1eEUHL36xX%2B4LSXzLVZzfPF%2BNi1P5GEBRLkWBNxIKslX00%2BNJoPgyV4Bd1Z53BxfdfV%2FSCl3vTediyK9eSO2hHNN%2FYVk%2Bz8ilD%2FfN1kZydbf7yc%2BcYfKNHwu%2FBw5Az5ih6ANg5XlPKmgaWhdyj%2FPEnGCEUJ%2F83m4lPjzzaVy%2FaphMB3LDzV052Y64iM63uK1BWhEAPJiwUG5nEQExFZvvMzmCWu2PCk3F%2BQfAS8EgiZB6xIo6HHlTKtcR6DzW11u5vehWiNM8sLwDOgRowpHQBtt%2Fj4soHuv6jTIy8%2BdMjTO7MfYql1SOD9zvLmOS%2F77t2zFM3WotRhSISojJwBzDenGJUzHdkFK1%2F9Xm8urZ31GluePMJEQfEtXlRh8LqQ2yagie8MfhgbRJ%2BPbPb3ZkG3nDZd5TGr8IqVeuCs6%2BM%2Fadru5X3z7D7NkduWnWTOxoij4q%2BZML3g0J6CPUjpLOxtlIYwqv3SyQY6pgEp%2FXQuhub2gh5G8TfD9nRdU71vy0UHctk29D%2B0foOO8%2FZsqixeBpkNjzL2EO5XYKo%2BKpz%2B5org3z%2BICNva8f7XYGFjKnmPMLZ%2BenoPMBer4h00kIdFAiAEAyUPSo4lfAUuWfjn9KtGtVqzrF9sxQhE4x1bDUvN1q%2F%2BIb50AtiK0xSwv4w9vRb3KSeJFqiMDq0v6z%2FPfhrib4RoI%2F8NXj7qqwlvmFyM&X-Amz-Signature=40838ed91e6cf779e1d777cacb779d107260c067de3c94721e10daaddec033dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QM5UKM3%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBavv5q641Hv2JaBAgj%2FEIWUbHzNdvUkm3JnRUnwpjr5AiBXOZOp6rLlvWCA7IO71s9bqjCr22gvf1lYvN6S%2FawvZSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVn2lppatFsoRCGRMKtwD3oxAvIaeFhZ%2Fm1oICNCqVP0AlaODa1cjXRp3TBp9mOpyQ%2FAG0eVTGEaOLALQ%2BrRnB%2FzETUbzV2xEIXqs8lVcfuTpykSkmPhVqoCe8%2Bw6chiUItomWsl03yi%2FMqz6dwq5RzfLOL6Kz7BTCPRbp2Yc0CdR8HmD9sh8U1eEUHL36xX%2B4LSXzLVZzfPF%2BNi1P5GEBRLkWBNxIKslX00%2BNJoPgyV4Bd1Z53BxfdfV%2FSCl3vTediyK9eSO2hHNN%2FYVk%2Bz8ilD%2FfN1kZydbf7yc%2BcYfKNHwu%2FBw5Az5ih6ANg5XlPKmgaWhdyj%2FPEnGCEUJ%2F83m4lPjzzaVy%2FaphMB3LDzV052Y64iM63uK1BWhEAPJiwUG5nEQExFZvvMzmCWu2PCk3F%2BQfAS8EgiZB6xIo6HHlTKtcR6DzW11u5vehWiNM8sLwDOgRowpHQBtt%2Fj4soHuv6jTIy8%2BdMjTO7MfYql1SOD9zvLmOS%2F77t2zFM3WotRhSISojJwBzDenGJUzHdkFK1%2F9Xm8urZ31GluePMJEQfEtXlRh8LqQ2yagie8MfhgbRJ%2BPbPb3ZkG3nDZd5TGr8IqVeuCs6%2BM%2Fadru5X3z7D7NkduWnWTOxoij4q%2BZML3g0J6CPUjpLOxtlIYwqv3SyQY6pgEp%2FXQuhub2gh5G8TfD9nRdU71vy0UHctk29D%2B0foOO8%2FZsqixeBpkNjzL2EO5XYKo%2BKpz%2B5org3z%2BICNva8f7XYGFjKnmPMLZ%2BenoPMBer4h00kIdFAiAEAyUPSo4lfAUuWfjn9KtGtVqzrF9sxQhE4x1bDUvN1q%2F%2BIb50AtiK0xSwv4w9vRb3KSeJFqiMDq0v6z%2FPfhrib4RoI%2F8NXj7qqwlvmFyM&X-Amz-Signature=acc48142861bed5aa818a65e7221ad771582d7253aee7d7be07a57d120093863&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QM5UKM3%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBavv5q641Hv2JaBAgj%2FEIWUbHzNdvUkm3JnRUnwpjr5AiBXOZOp6rLlvWCA7IO71s9bqjCr22gvf1lYvN6S%2FawvZSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVn2lppatFsoRCGRMKtwD3oxAvIaeFhZ%2Fm1oICNCqVP0AlaODa1cjXRp3TBp9mOpyQ%2FAG0eVTGEaOLALQ%2BrRnB%2FzETUbzV2xEIXqs8lVcfuTpykSkmPhVqoCe8%2Bw6chiUItomWsl03yi%2FMqz6dwq5RzfLOL6Kz7BTCPRbp2Yc0CdR8HmD9sh8U1eEUHL36xX%2B4LSXzLVZzfPF%2BNi1P5GEBRLkWBNxIKslX00%2BNJoPgyV4Bd1Z53BxfdfV%2FSCl3vTediyK9eSO2hHNN%2FYVk%2Bz8ilD%2FfN1kZydbf7yc%2BcYfKNHwu%2FBw5Az5ih6ANg5XlPKmgaWhdyj%2FPEnGCEUJ%2F83m4lPjzzaVy%2FaphMB3LDzV052Y64iM63uK1BWhEAPJiwUG5nEQExFZvvMzmCWu2PCk3F%2BQfAS8EgiZB6xIo6HHlTKtcR6DzW11u5vehWiNM8sLwDOgRowpHQBtt%2Fj4soHuv6jTIy8%2BdMjTO7MfYql1SOD9zvLmOS%2F77t2zFM3WotRhSISojJwBzDenGJUzHdkFK1%2F9Xm8urZ31GluePMJEQfEtXlRh8LqQ2yagie8MfhgbRJ%2BPbPb3ZkG3nDZd5TGr8IqVeuCs6%2BM%2Fadru5X3z7D7NkduWnWTOxoij4q%2BZML3g0J6CPUjpLOxtlIYwqv3SyQY6pgEp%2FXQuhub2gh5G8TfD9nRdU71vy0UHctk29D%2B0foOO8%2FZsqixeBpkNjzL2EO5XYKo%2BKpz%2B5org3z%2BICNva8f7XYGFjKnmPMLZ%2BenoPMBer4h00kIdFAiAEAyUPSo4lfAUuWfjn9KtGtVqzrF9sxQhE4x1bDUvN1q%2F%2BIb50AtiK0xSwv4w9vRb3KSeJFqiMDq0v6z%2FPfhrib4RoI%2F8NXj7qqwlvmFyM&X-Amz-Signature=d07b32e21b42f0c194fab886d902ff2d7ef66972f1112b31c250c534115a024a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

