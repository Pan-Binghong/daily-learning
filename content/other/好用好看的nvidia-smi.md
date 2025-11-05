---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
标签:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGENS3XY%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BjidxD9BXW9iF1iUIP6CXRkB4SieTKXRWJ%2FjdtD%2FUygIgXdZBVBlvI%2FVlMlKRuvSsMoxthUioH8XFBiWE39f8gwQqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiALh9Y1ayV9vgdXircA2A5B1ZgkQzOHUEQB8MNQRk%2FYaI5g%2FtrVbl1%2FizzbFwVmL3llDR2IoM3%2F%2Btq62M7l5N7CnCfA3Mm93HQYBWe5JQQRfRoYQIOpo%2FCRL9T19bnIHtFoywNZcMauXrjuS64R%2BQh2V2F3c7Izc2%2BpIVtBagn6lqg2MDqWXq%2FRr0QU4JRHpDZhKQK3cVIyP2Srmfyt4DEZNQjNkVfS5JzhXUOAWbxOplVbx85u2bDyKdW8UpD1U2fJmyyPVmPYXSAH%2FqyyWugrr%2Bdowu2NQPaW3npyvf7v3007BH6O4a9RFRKkAd529GKSCp8G%2FLTgqAdmgaHnKyiUdBfyKfcTB6Jcc%2BUxhfs2Qyr4pwOWDMSs6EZUwx2Qgqj8fCQ6zwCxb%2FzGt%2FHesXBrO2adQh69s%2B9QZ1Mx3Y7bpmbVYOyGKMD1J%2Fep3Qo0lPRnFqw9hE1Z06D8ubo%2BtB68Hf%2BU%2BbVaS0OxcJJfyCf0g%2BMVeiAuFYsZkOsOc2Ii94spZ%2Bw0go7aiXJ3kR3aG7X7NBR9JH8lTmfe9bycpzxF0cq1RcVwgW1HUNF4LMY3USdUkmLxgV%2FCiBJibwR7dyS6d7XYMFMYwTNtQ2PyWTYj%2BnX%2FsnfHXvz6Hv8vtwzncUf7T6hVJmaENGpMLiirMgGOqUBSUehOFuYJx%2BkI6sQykKNV67Z1OpAZ8mefPPO22%2FM1sWppENoDW9kyfMAKHIZSuFN8VZpeIrmBsoUoa0zBymJj%2BXGAhUQ1nkDAfMELJPzcJf1B%2FfqBDKpKSGLd1ugi95IJMOa%2Fe%2BPBed17%2FBWIwHDBuu0tqZZi7IOQpCf%2BZacfE5ZmKbtInWAHslItajgJYpgq94OKWRMUDydki%2BIle6b6012Qdma&X-Amz-Signature=4467b9ac2712c95105b50d723f3af9ecbbd9634e837474e584a64eb2b065e3f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGENS3XY%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BjidxD9BXW9iF1iUIP6CXRkB4SieTKXRWJ%2FjdtD%2FUygIgXdZBVBlvI%2FVlMlKRuvSsMoxthUioH8XFBiWE39f8gwQqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiALh9Y1ayV9vgdXircA2A5B1ZgkQzOHUEQB8MNQRk%2FYaI5g%2FtrVbl1%2FizzbFwVmL3llDR2IoM3%2F%2Btq62M7l5N7CnCfA3Mm93HQYBWe5JQQRfRoYQIOpo%2FCRL9T19bnIHtFoywNZcMauXrjuS64R%2BQh2V2F3c7Izc2%2BpIVtBagn6lqg2MDqWXq%2FRr0QU4JRHpDZhKQK3cVIyP2Srmfyt4DEZNQjNkVfS5JzhXUOAWbxOplVbx85u2bDyKdW8UpD1U2fJmyyPVmPYXSAH%2FqyyWugrr%2Bdowu2NQPaW3npyvf7v3007BH6O4a9RFRKkAd529GKSCp8G%2FLTgqAdmgaHnKyiUdBfyKfcTB6Jcc%2BUxhfs2Qyr4pwOWDMSs6EZUwx2Qgqj8fCQ6zwCxb%2FzGt%2FHesXBrO2adQh69s%2B9QZ1Mx3Y7bpmbVYOyGKMD1J%2Fep3Qo0lPRnFqw9hE1Z06D8ubo%2BtB68Hf%2BU%2BbVaS0OxcJJfyCf0g%2BMVeiAuFYsZkOsOc2Ii94spZ%2Bw0go7aiXJ3kR3aG7X7NBR9JH8lTmfe9bycpzxF0cq1RcVwgW1HUNF4LMY3USdUkmLxgV%2FCiBJibwR7dyS6d7XYMFMYwTNtQ2PyWTYj%2BnX%2FsnfHXvz6Hv8vtwzncUf7T6hVJmaENGpMLiirMgGOqUBSUehOFuYJx%2BkI6sQykKNV67Z1OpAZ8mefPPO22%2FM1sWppENoDW9kyfMAKHIZSuFN8VZpeIrmBsoUoa0zBymJj%2BXGAhUQ1nkDAfMELJPzcJf1B%2FfqBDKpKSGLd1ugi95IJMOa%2Fe%2BPBed17%2FBWIwHDBuu0tqZZi7IOQpCf%2BZacfE5ZmKbtInWAHslItajgJYpgq94OKWRMUDydki%2BIle6b6012Qdma&X-Amz-Signature=f0bc6a482ccdc72fb0b6f8a4ed6213c49d895bb28ec8b0fd23d8cf6973032572&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









