---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOQSCS4Z%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQCSAM8cH6f5PdNWeoZTTxlcJRcwNgDr2Jw6VYM%2BLnbHsAIgaC1eOZ9hL5sFJVLJLe%2Fhp14EFbo7%2F15V%2F4HKUJpDORkqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDASN8n%2B9%2F051rfDtTyrcA0ae0x1NYadVs7m8AcYiWmWR%2BiOeUgJ8STYiOVC7loexwsVclgYPj81VEzL85htWPVxW8n8rVu%2FDD6BObmH%2FM8LF5DuLdpWL0n2jeDxgKa2So%2FT%2Fi5mOCZKkYT2bYFYL9fQ5e1KlVqVFNu5y%2BGmKjFir1kfJAUsfzEcJfUM4v1ZHAHgflHrbu%2FbvdZZpPb5aAKFYI5O%2BVYeSx1OIABDNjtBhNpK6lAunqaACSs%2BXfi7%2FKWmZJ5B4nx1MENFHDfipT5FxtW1PGdADLzR%2Ft5mdJvaSbgnH5GrtdMkqyR%2FJQ99Dks%2Fktiz2Vj1SjwIz7q%2BXMlo%2FcvSQEDtiQ2iVRIPGsI%2Fr6VB4AY%2Ftb5CMmv2nUe%2B8TG4Gokfmy2eDE3UuB5MAX%2Bvzg0aEYlHOmxaDGpXGGBABMMrD8y0vRmPk9bkzF6rxPl1ct25CjU3zx0fMoEfC9eTxCMaGI4BUae1LIDpi3P8x%2FVqkwFwtL6Fz8I5eIKGdmmguR5qFXUdksI2u4hklsTb3QmV61JY%2BvD6vJ2XHR7r3%2FsSvgxgXjhrFfK3plfy99tDkMHAMgztxnX2PTWgMcOLJs%2BztlMj2di1dJ3iWbs5rr%2B96HgnO7UT3kOssrHDdxjUFOdSIjEVayB3qMLDlosoGOqUB%2FEH1q09vusb3inOgXDaoMjci0AtJIWhGOHfN4ubDHCPUJ40HJDVwSN23izoSeYF8%2F09VLlxYNetjjAttaPSCwobWTnVXMFy082Gz0axmrk5CHO93mrABaONcRNxCGaOTFK0%2BGAGENTI92ohnSA6s5j045OR2DzyvAcgPMutCtEH3jVmkmSHUT%2FASGkxjPfKSPAq5zMStrHDIHG2eT3%2FZpOg87yBD&X-Amz-Signature=8f71ae7dc17388a3773b312dbd3d1eb543fcf83b83d1655320b8b281b985a881&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOQSCS4Z%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQCSAM8cH6f5PdNWeoZTTxlcJRcwNgDr2Jw6VYM%2BLnbHsAIgaC1eOZ9hL5sFJVLJLe%2Fhp14EFbo7%2F15V%2F4HKUJpDORkqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDASN8n%2B9%2F051rfDtTyrcA0ae0x1NYadVs7m8AcYiWmWR%2BiOeUgJ8STYiOVC7loexwsVclgYPj81VEzL85htWPVxW8n8rVu%2FDD6BObmH%2FM8LF5DuLdpWL0n2jeDxgKa2So%2FT%2Fi5mOCZKkYT2bYFYL9fQ5e1KlVqVFNu5y%2BGmKjFir1kfJAUsfzEcJfUM4v1ZHAHgflHrbu%2FbvdZZpPb5aAKFYI5O%2BVYeSx1OIABDNjtBhNpK6lAunqaACSs%2BXfi7%2FKWmZJ5B4nx1MENFHDfipT5FxtW1PGdADLzR%2Ft5mdJvaSbgnH5GrtdMkqyR%2FJQ99Dks%2Fktiz2Vj1SjwIz7q%2BXMlo%2FcvSQEDtiQ2iVRIPGsI%2Fr6VB4AY%2Ftb5CMmv2nUe%2B8TG4Gokfmy2eDE3UuB5MAX%2Bvzg0aEYlHOmxaDGpXGGBABMMrD8y0vRmPk9bkzF6rxPl1ct25CjU3zx0fMoEfC9eTxCMaGI4BUae1LIDpi3P8x%2FVqkwFwtL6Fz8I5eIKGdmmguR5qFXUdksI2u4hklsTb3QmV61JY%2BvD6vJ2XHR7r3%2FsSvgxgXjhrFfK3plfy99tDkMHAMgztxnX2PTWgMcOLJs%2BztlMj2di1dJ3iWbs5rr%2B96HgnO7UT3kOssrHDdxjUFOdSIjEVayB3qMLDlosoGOqUB%2FEH1q09vusb3inOgXDaoMjci0AtJIWhGOHfN4ubDHCPUJ40HJDVwSN23izoSeYF8%2F09VLlxYNetjjAttaPSCwobWTnVXMFy082Gz0axmrk5CHO93mrABaONcRNxCGaOTFK0%2BGAGENTI92ohnSA6s5j045OR2DzyvAcgPMutCtEH3jVmkmSHUT%2FASGkxjPfKSPAq5zMStrHDIHG2eT3%2FZpOg87yBD&X-Amz-Signature=95117178e0b854583c8299ce1b8a744364d2568b4e60a805fc1b30a18aa19a6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









