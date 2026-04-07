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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MNP3WHY%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCl%2FWtNcfxYOm6bhbZHORnJOo2qnx4u7dl%2BhooeKrt8%2BgIgUUlER%2FvFdfya%2F0Vu1mldeJxl2E9UN%2Btsx6CiFApTVAYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOmWIvdo%2BYdCZdlBSrcA2HqVzvk05b6OEZEWLAxYKGYL%2Fo%2Bdb6RhUTUzhJnN2zB%2BDwyQpYBClF1ExTveqg6WbUQ34Xo%2BTwJ12dhfqbnz9R%2FY9pOTjwV%2B8fDg7h25j%2BayBOv5jNKOmvu6nRdQ2jgjMsxSuPLz0KG5dGC7e2iLJlWkEo9XfNCYLWYMUACdqvy4ihvCscPqakUiSbafl%2FF5bMTv2iGzpsJxWaOf5EA6NCysaFkOjFLkMPpzHVfwgMJWJOeTxKuXyzT8XIYzXhIp%2BVf%2BTdxsOCZaF%2FADy29ElB8%2FLUh7G%2BCIFMIDIEygYm%2FVR%2FZ4DB2cOwQ8Z4xh1H628JtaALtF2jtTUAQBfw758k61nsU9rqilpcJIlIpO%2BXGpKlHwSs9SxwHUYgSXWKq%2BmcBjOjM3BMjSsEw4B0g7vBmPtovzd3uDE4tVc1ejLYvrd6IEBGnXOT1I6EumsHHkGqarT9KpkLCq1gE%2BRlkMpZ3NxhAbdqTdJYnj9ozonGdNMV8hvnLP%2Ba9R5rOImrSBmIjOuD43zLAxgiEo%2FvdhWiXzQ3u4TE%2BDulS9sZNZyojEpaoAVoRbnw3SAdHYvB4mJyI9X%2BTC26Eipi1Rcqd5hewkjakGhRNDz8MyevM9mQ32gSvBgaVeZ2PULuDMKn20c4GOqUB%2Bg%2Fl%2F00DFdHDDhSj8f43%2FVeTKO8XXmg5Sjby4liGIUwNGjqlsbCI9%2F%2BaVM4K6aeb5kaUJGYN8mD1vUmoDuEmqPcjaEEXwwFFKSsnsbgXPWB1hS2LgcnKt30r8SkRW57wHf%2BP%2BGarwN6ohteN7VrpItg8cB3LI66sq6TNKIJkPs3B6FH72jHDcxK3GXGyOx67YZN5XCajYWn1PPKgZvzHJqU5jbsg&X-Amz-Signature=3b3580821c091331e81c744412a2e4d1aca040fcc8885448455a9743080c6ce8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MNP3WHY%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCl%2FWtNcfxYOm6bhbZHORnJOo2qnx4u7dl%2BhooeKrt8%2BgIgUUlER%2FvFdfya%2F0Vu1mldeJxl2E9UN%2Btsx6CiFApTVAYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOmWIvdo%2BYdCZdlBSrcA2HqVzvk05b6OEZEWLAxYKGYL%2Fo%2Bdb6RhUTUzhJnN2zB%2BDwyQpYBClF1ExTveqg6WbUQ34Xo%2BTwJ12dhfqbnz9R%2FY9pOTjwV%2B8fDg7h25j%2BayBOv5jNKOmvu6nRdQ2jgjMsxSuPLz0KG5dGC7e2iLJlWkEo9XfNCYLWYMUACdqvy4ihvCscPqakUiSbafl%2FF5bMTv2iGzpsJxWaOf5EA6NCysaFkOjFLkMPpzHVfwgMJWJOeTxKuXyzT8XIYzXhIp%2BVf%2BTdxsOCZaF%2FADy29ElB8%2FLUh7G%2BCIFMIDIEygYm%2FVR%2FZ4DB2cOwQ8Z4xh1H628JtaALtF2jtTUAQBfw758k61nsU9rqilpcJIlIpO%2BXGpKlHwSs9SxwHUYgSXWKq%2BmcBjOjM3BMjSsEw4B0g7vBmPtovzd3uDE4tVc1ejLYvrd6IEBGnXOT1I6EumsHHkGqarT9KpkLCq1gE%2BRlkMpZ3NxhAbdqTdJYnj9ozonGdNMV8hvnLP%2Ba9R5rOImrSBmIjOuD43zLAxgiEo%2FvdhWiXzQ3u4TE%2BDulS9sZNZyojEpaoAVoRbnw3SAdHYvB4mJyI9X%2BTC26Eipi1Rcqd5hewkjakGhRNDz8MyevM9mQ32gSvBgaVeZ2PULuDMKn20c4GOqUB%2Bg%2Fl%2F00DFdHDDhSj8f43%2FVeTKO8XXmg5Sjby4liGIUwNGjqlsbCI9%2F%2BaVM4K6aeb5kaUJGYN8mD1vUmoDuEmqPcjaEEXwwFFKSsnsbgXPWB1hS2LgcnKt30r8SkRW57wHf%2BP%2BGarwN6ohteN7VrpItg8cB3LI66sq6TNKIJkPs3B6FH72jHDcxK3GXGyOx67YZN5XCajYWn1PPKgZvzHJqU5jbsg&X-Amz-Signature=de21ffcf71000e1fac8ebcb920464ea6a15c1894b0a3c61094b87ec620ff5f8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









