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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXRZPBWX%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwKUBVMyKPMmYlV%2FjaoUYEImm3yBCxHYB2Zw7IxnHlkQIhAJPs229TWLq4W4ojORz3PrRd%2BtFhriD%2FVqMFm72A8roaKv8DCFsQABoMNjM3NDIzMTgzODA1IgyRUs2lOCtvVjOuTv0q3AN%2FEmJYZrjzXhrz5JxzNvZjq%2FOxM6Cx7wZMlGCSbr1p6IdQnEi83GlZqND5rsGLGxJHMI33%2BOSl%2BjZEcAgQL46wE2UuQu0QA06IrQMDjsd2jMutFtMmYldWhobCM3QBujAwA6r6G49ynnjj7vrMsQplPyMHlHXL8W4ZEOKzYmzTDVoJBTQsDAjCwlWXPsbFtsOGidLaL3NNTNyOoxUU1ZspfYmc3c4mE%2BwwhMZ4famDgg2cy%2F2IThgaN7owcyMqv8reFk2gkiZGGsI0Wvz9f%2B9XS6GR9j5XNvBkjM29RRq7xtTDQpUBeFTz96ZE2PY34Nh9ph5HM2csJ3dtorD7qRDJnBxBHnZDZ29GqD5zwPHCLEvWdOvTi1ECM25LwiQjGreXkqJc31P9wAdt%2FrOccgXxAJNCf4ahc7lcqzVFSSns9kSJBxtSsglvUM7ijZzZLKJ52NKiDpejCYRiAeCcFoMm92TVK7bouGP4uHYUQjv0FHHiZqT59TvlJ6RrU0SY5YSvhmtKsqwmEm%2BGv3VuRilwdI9AmlbZEJ0ktRvOIvjgFsPJ75nHJ5I2BYlgBR0Szz6lKWrjGcd1VeghVYpVirsCXy2ojm9ub8skPJq5wq8hA2h7SYPZklZldQLOTTCC0qvLBjqkAaqk4mY1cA0FO06BvGFGrnLyw2hIhkLe0wbLJBTr7yGCwr6sEt%2FugLBSd5KEgS4Cl%2FgeM1q%2Bri2Vqu06NIp7hlpgCB07Wa%2BEF5yUKQTAc5VphoHFBGwCJm8ctprgn3KZMdEy%2FO2TxsZguPGh3Y0oxn2NmuXIG5w1TOI4o4uZ8EGPNhri2ZC8nCqS9eI3iFL6qNgVssSzUv3U8oDsnLmI6JV%2Bzcul&X-Amz-Signature=e8e2623a0d43efafdc18bf6ea6a63c2e2717bc56a4b562af7b3e1f6da895d187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXRZPBWX%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwKUBVMyKPMmYlV%2FjaoUYEImm3yBCxHYB2Zw7IxnHlkQIhAJPs229TWLq4W4ojORz3PrRd%2BtFhriD%2FVqMFm72A8roaKv8DCFsQABoMNjM3NDIzMTgzODA1IgyRUs2lOCtvVjOuTv0q3AN%2FEmJYZrjzXhrz5JxzNvZjq%2FOxM6Cx7wZMlGCSbr1p6IdQnEi83GlZqND5rsGLGxJHMI33%2BOSl%2BjZEcAgQL46wE2UuQu0QA06IrQMDjsd2jMutFtMmYldWhobCM3QBujAwA6r6G49ynnjj7vrMsQplPyMHlHXL8W4ZEOKzYmzTDVoJBTQsDAjCwlWXPsbFtsOGidLaL3NNTNyOoxUU1ZspfYmc3c4mE%2BwwhMZ4famDgg2cy%2F2IThgaN7owcyMqv8reFk2gkiZGGsI0Wvz9f%2B9XS6GR9j5XNvBkjM29RRq7xtTDQpUBeFTz96ZE2PY34Nh9ph5HM2csJ3dtorD7qRDJnBxBHnZDZ29GqD5zwPHCLEvWdOvTi1ECM25LwiQjGreXkqJc31P9wAdt%2FrOccgXxAJNCf4ahc7lcqzVFSSns9kSJBxtSsglvUM7ijZzZLKJ52NKiDpejCYRiAeCcFoMm92TVK7bouGP4uHYUQjv0FHHiZqT59TvlJ6RrU0SY5YSvhmtKsqwmEm%2BGv3VuRilwdI9AmlbZEJ0ktRvOIvjgFsPJ75nHJ5I2BYlgBR0Szz6lKWrjGcd1VeghVYpVirsCXy2ojm9ub8skPJq5wq8hA2h7SYPZklZldQLOTTCC0qvLBjqkAaqk4mY1cA0FO06BvGFGrnLyw2hIhkLe0wbLJBTr7yGCwr6sEt%2FugLBSd5KEgS4Cl%2FgeM1q%2Bri2Vqu06NIp7hlpgCB07Wa%2BEF5yUKQTAc5VphoHFBGwCJm8ctprgn3KZMdEy%2FO2TxsZguPGh3Y0oxn2NmuXIG5w1TOI4o4uZ8EGPNhri2ZC8nCqS9eI3iFL6qNgVssSzUv3U8oDsnLmI6JV%2Bzcul&X-Amz-Signature=2d9a7c0c97758b86e648cd979dd5b1c4b2cab409c64f5cf87d8fc8879dc48d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









