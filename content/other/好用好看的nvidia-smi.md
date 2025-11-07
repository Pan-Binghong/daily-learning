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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PKDWY7T%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMipPbW%2BdTPYT09DUDuVNE1DsLtiQzIw9QLZM57LPxVAIhAKT5Pmf1Wn5uB7HYZQEbACbOgyTTCBUlHVeP0XJnc%2F5GKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyUTpr9F%2BCE%2F%2BbHYQq3AP6354te8V8B%2BE2Jg%2FijFPPFuPVgjQiNI%2BJaSi0wmsbeVY9ICfa0TyYs9UyxC8OU5turGe%2BOzNuffc4HiwIqC7%2BBWhIoaH%2BeElbpHu3QLD%2BpF%2BWg5kqFDh4MOszhq0zRZO1a%2F3o0OrUp4EzFxWT7qSERkBbQzq%2FjK%2FapDaxoh5GdgFWgx6uyZdDdb1Kjq%2FHm%2BfMMlneupkUeyClEStmkAHhb%2FDq0En1cXexqoaxYivfQxRMVQog4ya82SyZp7Z22ShvOhHotbXIo2vt%2BW2mcGZ6THoruLzzk7UmGWm%2BJSafQn9GxT%2BOOjdMIHJE506VAmPYtThAM2GOq3aG2NualFqStLaiC00K4HWV7gvGrA3bFG1%2FdV2tbWo8S5JF%2FL8NPUDyZa%2F7UULW3SK3TGxz62%2FJ5LNtKWS3EM68FoMyIfzjnwsvbw2o4UQWV2haIQ4IHbUGK%2BELYwIbbnynKoNpEcUbSguaVGp%2FM74NsMX%2FlD%2BZHwZsOUOJPwBt8eGFsUzhePJFCByijJACkOwcgmwKtaDFd7OR%2FNtzSguVYv3f28zJHU6MXKjAXaIU8aSWhe28Jf0rpGi1nWZQCnsSFRXfmG%2Biv%2BZq35puMG8zo8%2Fsj2VEonAH640Q4yXgLKIeBjCOtbXIBjqkAXShFw4w%2FRU4kA6E3sJyd7K%2BSu6JtfWe4lCga8C3t9iP9GbHJyfXhZ%2BoVFx7gzdH6Z7O%2F%2BfOe4Iii6XU64wjm3V%2FG8Wl91rtYwroEtTHWsHuSwFN6hwT%2BZXZONIY6K7lo0IuXlQsPSWnrHyypj%2BHdxTEj5OH5CFaZETmcvsac1QLqlu2vzOhcVBOwDT6olOhvQYNAWTzBliLu7XOf0sYUYc4AQ71&X-Amz-Signature=b6ef7bf899aa7c58e8fcdedef820d1bdeaf0234385326608c02ff276993aef93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PKDWY7T%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMipPbW%2BdTPYT09DUDuVNE1DsLtiQzIw9QLZM57LPxVAIhAKT5Pmf1Wn5uB7HYZQEbACbOgyTTCBUlHVeP0XJnc%2F5GKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyUTpr9F%2BCE%2F%2BbHYQq3AP6354te8V8B%2BE2Jg%2FijFPPFuPVgjQiNI%2BJaSi0wmsbeVY9ICfa0TyYs9UyxC8OU5turGe%2BOzNuffc4HiwIqC7%2BBWhIoaH%2BeElbpHu3QLD%2BpF%2BWg5kqFDh4MOszhq0zRZO1a%2F3o0OrUp4EzFxWT7qSERkBbQzq%2FjK%2FapDaxoh5GdgFWgx6uyZdDdb1Kjq%2FHm%2BfMMlneupkUeyClEStmkAHhb%2FDq0En1cXexqoaxYivfQxRMVQog4ya82SyZp7Z22ShvOhHotbXIo2vt%2BW2mcGZ6THoruLzzk7UmGWm%2BJSafQn9GxT%2BOOjdMIHJE506VAmPYtThAM2GOq3aG2NualFqStLaiC00K4HWV7gvGrA3bFG1%2FdV2tbWo8S5JF%2FL8NPUDyZa%2F7UULW3SK3TGxz62%2FJ5LNtKWS3EM68FoMyIfzjnwsvbw2o4UQWV2haIQ4IHbUGK%2BELYwIbbnynKoNpEcUbSguaVGp%2FM74NsMX%2FlD%2BZHwZsOUOJPwBt8eGFsUzhePJFCByijJACkOwcgmwKtaDFd7OR%2FNtzSguVYv3f28zJHU6MXKjAXaIU8aSWhe28Jf0rpGi1nWZQCnsSFRXfmG%2Biv%2BZq35puMG8zo8%2Fsj2VEonAH640Q4yXgLKIeBjCOtbXIBjqkAXShFw4w%2FRU4kA6E3sJyd7K%2BSu6JtfWe4lCga8C3t9iP9GbHJyfXhZ%2BoVFx7gzdH6Z7O%2F%2BfOe4Iii6XU64wjm3V%2FG8Wl91rtYwroEtTHWsHuSwFN6hwT%2BZXZONIY6K7lo0IuXlQsPSWnrHyypj%2BHdxTEj5OH5CFaZETmcvsac1QLqlu2vzOhcVBOwDT6olOhvQYNAWTzBliLu7XOf0sYUYc4AQ71&X-Amz-Signature=224e7be006eb5515f0b8dc3aced377e29f8959750a18ab1913fa44cc1c615cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









