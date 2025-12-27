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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLXMXN5X%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBV0T4MjR%2Bu1MZmqJs8uO8qzcxf%2FG8xYsEmulqCauJCDAiEAqe8OfJ9h8RFWBViRZ9iS%2FiaKOKbdJBoJSvg1ctwlwBEq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCWSm%2Bzkc88rrcZMYyrcAyar6j4k4wT3v6BXDvGRq4pwZDnDgVl1skcWz9rMHRMf%2B9y6SVWhCiv0Wwh0ieGmTiLtH%2B6NYlhYXENlfLAR9V0beVRNk29EvY4Au%2Byduz3%2Fb05VNdbutO00U9MUjb4YZ7%2FZ27ZS0nwCgJaex2YSQmqqPqgwxRPZ2Vu7F3DgxTELTtAVg9CeJjmMt4mxUA7vyIAVj4Tmr5RHUvFSFnsX6SbOuXyDtx9123GCK%2FHmKzK23LeiplUuP%2BokY5gOgb466nrzvM6PmbFlxT3vvwr7bEh8Yl0H%2FfDq3r9F9mDH3LJJYrKxRkFB8g8t1CSKQWTckpSwKNGzYwU1xAVl5QziUOfss9WUH8uwn4VZIz3jLz6%2Fl8XR1jBOep%2FMe8f7Cuw9%2FJlQlXc8EXk4dsnidRpjfJVxDqSOBLyy0nxF%2F6GaVJ0rVkh2NRFPc8lp9GqcA1D2FEcDAKh5GiZlpV1S8QVkln2%2BAvQTsQ74jcTWVgqIRcV7rzVrNE14HKNJj45q2ybIEY5wkSadKnN%2BOJabCpfylfPI8If%2FNz41TWDkMHSZ6TBCljCMkngHQMQroS%2Bt7tFw8%2Fi%2B026QpHgCaCYhQSZE8Uoo7g14ZKM1MoQzeb%2BQAFXWsAj%2Fvh54rxSdU8MGMN7rvMoGOqUBuNM9Txjje74kegsUjVqOpo6hz%2Fh%2BHnOJL39ODJ4G9wQgMEyAeamvo8Bj3O46U9w1cdsj8sx4ZcTfacQSKbUDxf6E6NKPMIHCG94OLQzFL1etmjxyKqr0qft7JNGxbp4%2B%2FcdH1N1ElJZxX6WXKjt5efNb6%2Bv3ymDl8lHdW432q1Z06fi2RyqryS83L%2BmJ%2B9jNTti%2FkllkZMslyx7rXkYp54ONJHdf&X-Amz-Signature=5d6d6b20f9df8fe2c25c8694788411f5749d0c5d7dc52d1cd60fb2564d3c05a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLXMXN5X%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBV0T4MjR%2Bu1MZmqJs8uO8qzcxf%2FG8xYsEmulqCauJCDAiEAqe8OfJ9h8RFWBViRZ9iS%2FiaKOKbdJBoJSvg1ctwlwBEq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCWSm%2Bzkc88rrcZMYyrcAyar6j4k4wT3v6BXDvGRq4pwZDnDgVl1skcWz9rMHRMf%2B9y6SVWhCiv0Wwh0ieGmTiLtH%2B6NYlhYXENlfLAR9V0beVRNk29EvY4Au%2Byduz3%2Fb05VNdbutO00U9MUjb4YZ7%2FZ27ZS0nwCgJaex2YSQmqqPqgwxRPZ2Vu7F3DgxTELTtAVg9CeJjmMt4mxUA7vyIAVj4Tmr5RHUvFSFnsX6SbOuXyDtx9123GCK%2FHmKzK23LeiplUuP%2BokY5gOgb466nrzvM6PmbFlxT3vvwr7bEh8Yl0H%2FfDq3r9F9mDH3LJJYrKxRkFB8g8t1CSKQWTckpSwKNGzYwU1xAVl5QziUOfss9WUH8uwn4VZIz3jLz6%2Fl8XR1jBOep%2FMe8f7Cuw9%2FJlQlXc8EXk4dsnidRpjfJVxDqSOBLyy0nxF%2F6GaVJ0rVkh2NRFPc8lp9GqcA1D2FEcDAKh5GiZlpV1S8QVkln2%2BAvQTsQ74jcTWVgqIRcV7rzVrNE14HKNJj45q2ybIEY5wkSadKnN%2BOJabCpfylfPI8If%2FNz41TWDkMHSZ6TBCljCMkngHQMQroS%2Bt7tFw8%2Fi%2B026QpHgCaCYhQSZE8Uoo7g14ZKM1MoQzeb%2BQAFXWsAj%2Fvh54rxSdU8MGMN7rvMoGOqUBuNM9Txjje74kegsUjVqOpo6hz%2Fh%2BHnOJL39ODJ4G9wQgMEyAeamvo8Bj3O46U9w1cdsj8sx4ZcTfacQSKbUDxf6E6NKPMIHCG94OLQzFL1etmjxyKqr0qft7JNGxbp4%2B%2FcdH1N1ElJZxX6WXKjt5efNb6%2Bv3ymDl8lHdW432q1Z06fi2RyqryS83L%2BmJ%2B9jNTti%2FkllkZMslyx7rXkYp54ONJHdf&X-Amz-Signature=5c996c75b8eea00ddcfb852c8fbd7f379ca7ae04912469a4d0d2e6702a082efe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









