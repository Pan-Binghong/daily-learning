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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AYXFCNY%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC2aNQOtLhiVuHZmIzTq2d4R3ucbXEELtOGi368ejSk%2FQIgSUN8p%2F6NW%2FyLH5Mf0R8Bu%2FpuQYsjVb9SeARfdBtLMrgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDHOwjzOZGs23acoqqircA731vzVI4FAYRqTtEz6Nnrwgblby8xwwTjBizPuveMeFbP%2BSH79%2FwyzzUYP1z%2BwZo5wgE92bei9jKk4LE3F5sPkCizJ9ade8c83f4%2FgImTWf7HHIuD2ZdPrcsJY6ol97ciWmRvZk5l8DbXcBADavEWRU5p7WCjkY89rVcYLwxO3Pj5ntsRmAdkAldq30yEAwRlbeZFi8JfmrJusV0p3ZAR6tz74NgjcVM5i5s0paix0Z%2FHOERr3ai2s8Fq068oYAQJcuKI4nY%2FTFt0B2hIMWH%2FNgl9fZ840LUx06N0XAu4bmPIP9bZAvAfbKiV697x0arjYyESMbxlzXfiKyeNwel5vHdr0vSY7gZjZjC%2FHf0cKLTjYvImTRig9oI8bXwrBPgzom7aF81DaPI4Gx3HYzqk%2BM%2BnZK06cQ1%2B1%2FgaigrBJnZNIXlqQfH8INDlb1%2FSMbCanxw1GA5Gjw7cLMb9hbaf6jNFcP%2FUt5Uj3BkNhv7tOBuy6zB1gWm9uZTSP1AiM84HsMUDpf8mcwMzPZHgfVzKscQAQxqDAYqodiH92uFNvi4YkW%2BN%2BKsYowCwEz84Kf0gk7vtAU6ujH5oVpSwjewsv%2BkjbRWb4O6fTEzwoaUkwsDsxcKPPqvcxx61iFMMrjz8gGOqUB9GejUwhK2n63vVXu7pGmy8PxH4iMDsEfrwa%2FfrmGo9VixFML3Dmc4dwtUpfy0xlVs92bjJ9gYWx0E%2ButCjfs7CVS7jqRVHJzMo9Q4elHlHYWrsSn3RY0waRpwiSHz2BAK9kcZ3RF4PsMMxzZHtaHSOcCKIKV2JAX0W%2FGmP1sPvAjkrPVBkydUqe4GTAaURVJ0tVi0XEZZ3DpR%2FGnq%2FLz2FlFqrke&X-Amz-Signature=dbd5ed0a1f066ffb045764ca0ee03af59cdc69ff2e8435de05ad8dbb7f8256ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AYXFCNY%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC2aNQOtLhiVuHZmIzTq2d4R3ucbXEELtOGi368ejSk%2FQIgSUN8p%2F6NW%2FyLH5Mf0R8Bu%2FpuQYsjVb9SeARfdBtLMrgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDHOwjzOZGs23acoqqircA731vzVI4FAYRqTtEz6Nnrwgblby8xwwTjBizPuveMeFbP%2BSH79%2FwyzzUYP1z%2BwZo5wgE92bei9jKk4LE3F5sPkCizJ9ade8c83f4%2FgImTWf7HHIuD2ZdPrcsJY6ol97ciWmRvZk5l8DbXcBADavEWRU5p7WCjkY89rVcYLwxO3Pj5ntsRmAdkAldq30yEAwRlbeZFi8JfmrJusV0p3ZAR6tz74NgjcVM5i5s0paix0Z%2FHOERr3ai2s8Fq068oYAQJcuKI4nY%2FTFt0B2hIMWH%2FNgl9fZ840LUx06N0XAu4bmPIP9bZAvAfbKiV697x0arjYyESMbxlzXfiKyeNwel5vHdr0vSY7gZjZjC%2FHf0cKLTjYvImTRig9oI8bXwrBPgzom7aF81DaPI4Gx3HYzqk%2BM%2BnZK06cQ1%2B1%2FgaigrBJnZNIXlqQfH8INDlb1%2FSMbCanxw1GA5Gjw7cLMb9hbaf6jNFcP%2FUt5Uj3BkNhv7tOBuy6zB1gWm9uZTSP1AiM84HsMUDpf8mcwMzPZHgfVzKscQAQxqDAYqodiH92uFNvi4YkW%2BN%2BKsYowCwEz84Kf0gk7vtAU6ujH5oVpSwjewsv%2BkjbRWb4O6fTEzwoaUkwsDsxcKPPqvcxx61iFMMrjz8gGOqUB9GejUwhK2n63vVXu7pGmy8PxH4iMDsEfrwa%2FfrmGo9VixFML3Dmc4dwtUpfy0xlVs92bjJ9gYWx0E%2ButCjfs7CVS7jqRVHJzMo9Q4elHlHYWrsSn3RY0waRpwiSHz2BAK9kcZ3RF4PsMMxzZHtaHSOcCKIKV2JAX0W%2FGmP1sPvAjkrPVBkydUqe4GTAaURVJ0tVi0XEZZ3DpR%2FGnq%2FLz2FlFqrke&X-Amz-Signature=ed86f8fb77fa228551f9bdc865c40bfccabf55f2e2cb9e2c2f874fefb2e161d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









