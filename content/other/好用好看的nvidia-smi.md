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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKAYOUI5%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BKJRtMrXtAh%2FOkT%2FpOTW5K2dJBJtYuOTDYtWrEvYGKAIgSvboJUpJK225vJ0mMN3017D06nNhJCxjYqQ7Gz7Hp2Aq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNQ7MRW8gvP7Sz1hEircA1qEqvs%2BdLXz%2FxErIbkvtidUHgEjh%2FRwfMYlA0v42HHhwF9G85qVB8fWrGlAF93%2Bbu%2FqJ50ZThyu4ZXjXbgEcAHyyntlJzjFEMZkGLoHGp%2FAS5DO7IdWdSCM%2BG2%2BGOSFn6BYR0A%2FWY%2BrZcdAjJlaqOmIcNhNxzhhbQPXDJ3YpEs95QDnIf3Yc85Gs3ibsxtDNww6bd2bewxbJbHcAucELrrc4rTXOhplbxy2JfHAX03JzetnyVxWebelYmxRiDb%2FRUmWZ4pmMG%2Fr0uUueR25acry2lTTDBAduCkIlghZhUHLsW9F2sFanoYHBIqvcLkBDuKcvGTMjc8%2Fzq7SDDxBNuM3ODKwuTMqcqXXytwJj9XNPXDTGoOfJxBsIGZnN54OQE6scaVWtWbzqoroVaL9lvjmlIjcCVwrzMgxPmOjfDVccMO9WnS7%2BW3%2FQ1C97zPvalaQGmP9pv9lhW7DMHlCAr8uYezsdMuRYKqkms45PuPomtD5F023MTFQspPDXTrw6GezrEd%2B3WcopCOfVA3vr%2BQBi6JGVgQxYlPCbz%2FRkeP2gwiK5NhKsAnDhc6BIw0w4ojQV0zuUrFhchkFuZ0oLJdHwkVLVuI8xMGdPJph%2Br9xEDyMd%2F6U%2Blul18OwMPrkgs4GOqUBP2M9eG7ATocG73PhWKiD9ncDiahFaFJMBt%2BmLfK3um6wLf1zEspAjERC%2FbCib%2F7VyAk8excKTn%2BrFDkPUejcdGBQRa6Vc9AlBR3ta%2FfB0XpWOq4f9gXPR%2FY9YhWC2qgfjNqng7tb25BNYrif5uMRB63C5DHCkfLFd%2FLGMGbFb7htH6kUwVovIcGCWQY6saI3o9m6%2BUD%2Bjn6T4MSY%2BllZr%2BOgtQkx&X-Amz-Signature=8a641de836c9261e65036551998640c3a2b68d0ce9f9ee683c492a072dd1caa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKAYOUI5%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BKJRtMrXtAh%2FOkT%2FpOTW5K2dJBJtYuOTDYtWrEvYGKAIgSvboJUpJK225vJ0mMN3017D06nNhJCxjYqQ7Gz7Hp2Aq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNQ7MRW8gvP7Sz1hEircA1qEqvs%2BdLXz%2FxErIbkvtidUHgEjh%2FRwfMYlA0v42HHhwF9G85qVB8fWrGlAF93%2Bbu%2FqJ50ZThyu4ZXjXbgEcAHyyntlJzjFEMZkGLoHGp%2FAS5DO7IdWdSCM%2BG2%2BGOSFn6BYR0A%2FWY%2BrZcdAjJlaqOmIcNhNxzhhbQPXDJ3YpEs95QDnIf3Yc85Gs3ibsxtDNww6bd2bewxbJbHcAucELrrc4rTXOhplbxy2JfHAX03JzetnyVxWebelYmxRiDb%2FRUmWZ4pmMG%2Fr0uUueR25acry2lTTDBAduCkIlghZhUHLsW9F2sFanoYHBIqvcLkBDuKcvGTMjc8%2Fzq7SDDxBNuM3ODKwuTMqcqXXytwJj9XNPXDTGoOfJxBsIGZnN54OQE6scaVWtWbzqoroVaL9lvjmlIjcCVwrzMgxPmOjfDVccMO9WnS7%2BW3%2FQ1C97zPvalaQGmP9pv9lhW7DMHlCAr8uYezsdMuRYKqkms45PuPomtD5F023MTFQspPDXTrw6GezrEd%2B3WcopCOfVA3vr%2BQBi6JGVgQxYlPCbz%2FRkeP2gwiK5NhKsAnDhc6BIw0w4ojQV0zuUrFhchkFuZ0oLJdHwkVLVuI8xMGdPJph%2Br9xEDyMd%2F6U%2Blul18OwMPrkgs4GOqUBP2M9eG7ATocG73PhWKiD9ncDiahFaFJMBt%2BmLfK3um6wLf1zEspAjERC%2FbCib%2F7VyAk8excKTn%2BrFDkPUejcdGBQRa6Vc9AlBR3ta%2FfB0XpWOq4f9gXPR%2FY9YhWC2qgfjNqng7tb25BNYrif5uMRB63C5DHCkfLFd%2FLGMGbFb7htH6kUwVovIcGCWQY6saI3o9m6%2BUD%2Bjn6T4MSY%2BllZr%2BOgtQkx&X-Amz-Signature=3c0509d9acb7ad36afe6be0b9b2efeb8dc3d2e14ecf00467ce0be9e5cf719561&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









