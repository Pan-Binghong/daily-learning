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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBG5RZSR%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD1dKgcukT6JZv%2FDXPixREOXWat%2BUVOvWt787cipcnTaAIhALhpqmDxCoB7yWTihnj0XEGAvyTVFlyfJHEsUK%2FLbo7hKv8DCBQQABoMNjM3NDIzMTgzODA1Igw%2FqNTNiLPoI17XdD4q3ANuFaG9QqVMl4ZQatH%2B1UxYl44CcSvGQWTSOU%2Bcv0G87WSDzSI1aE4ZOsHFzpwj7ATpu1lDEtmEw%2FLJkuAK3Tx%2FZrmlWK%2F4Gi8rD52mHfYTVCfDC3MAqjxcsPWKStBZbaGnFIde7SDuvsRl792U1CHNP35hs9lsxKAXI1UE72uA5EW7Qv5ER2XqltUzVAEjDueYultgLmtr%2FueAzWnhXrD5Fz0TWmo873QeQznDCY1S0XrmUAY3S9Lafu%2FqxsHqNyB0FrqH0dyaVs93lDbYHOKQlnrywbCNQ2Hp5OS6vH3ceJpma4CHV8y0c7PgujdQRYMUZYMOFiibll6bSG1wty5VPzuYBw%2BZdxMqnJRJWErb2%2BtcoEZXtUydbf4Z0%2BtcCsfoiTf9NaemLojisNTPzJpmE00AFw00VnqzstmyLW3rLT1dabTOAw%2Fi9IjdFWta2yMPd9n5gPO%2BbuB92961z%2FFJQsVmJIxYVx6me7A6wQbEUYJFk8p7pQ23oGvr1OCakAarXe%2F2X4r%2FjAn3Qp3iTPKEo6DlSOs9d8AjzY2pw4jhY3RUveV3pfm98JCkd479ggam0nUz%2BNJAtBoGuGf81MW7JdRpqmr2kC8MGUM%2FxursJmQsa%2BxuE8E6eqJeOTDIvcrIBjqkAeuRMZ%2FdUy7DkyJUpHYmgFNmAzsoqzEGIBHMHw7x5xJ8EGqgSHknvHLljxKt2LvrxH8ZL54NlHx3lUGZlcVLIkd6t5dZi4UHxUO07X%2BnSEGtsNOeo%2Bdnek%2BHqEyWZP0GX%2BN04psp3U4wto5fgMonwzRuCgBXru9Mr4lkGzVSPlWuCRNV7d%2BBUYCK6hVcLcfLMT7SgCYgmtLE1viA6rxYhjuwXShA&X-Amz-Signature=270737ee25b8c7472de60587423f5771a5ab93f62f588baa9df312521d36b910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBG5RZSR%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD1dKgcukT6JZv%2FDXPixREOXWat%2BUVOvWt787cipcnTaAIhALhpqmDxCoB7yWTihnj0XEGAvyTVFlyfJHEsUK%2FLbo7hKv8DCBQQABoMNjM3NDIzMTgzODA1Igw%2FqNTNiLPoI17XdD4q3ANuFaG9QqVMl4ZQatH%2B1UxYl44CcSvGQWTSOU%2Bcv0G87WSDzSI1aE4ZOsHFzpwj7ATpu1lDEtmEw%2FLJkuAK3Tx%2FZrmlWK%2F4Gi8rD52mHfYTVCfDC3MAqjxcsPWKStBZbaGnFIde7SDuvsRl792U1CHNP35hs9lsxKAXI1UE72uA5EW7Qv5ER2XqltUzVAEjDueYultgLmtr%2FueAzWnhXrD5Fz0TWmo873QeQznDCY1S0XrmUAY3S9Lafu%2FqxsHqNyB0FrqH0dyaVs93lDbYHOKQlnrywbCNQ2Hp5OS6vH3ceJpma4CHV8y0c7PgujdQRYMUZYMOFiibll6bSG1wty5VPzuYBw%2BZdxMqnJRJWErb2%2BtcoEZXtUydbf4Z0%2BtcCsfoiTf9NaemLojisNTPzJpmE00AFw00VnqzstmyLW3rLT1dabTOAw%2Fi9IjdFWta2yMPd9n5gPO%2BbuB92961z%2FFJQsVmJIxYVx6me7A6wQbEUYJFk8p7pQ23oGvr1OCakAarXe%2F2X4r%2FjAn3Qp3iTPKEo6DlSOs9d8AjzY2pw4jhY3RUveV3pfm98JCkd479ggam0nUz%2BNJAtBoGuGf81MW7JdRpqmr2kC8MGUM%2FxursJmQsa%2BxuE8E6eqJeOTDIvcrIBjqkAeuRMZ%2FdUy7DkyJUpHYmgFNmAzsoqzEGIBHMHw7x5xJ8EGqgSHknvHLljxKt2LvrxH8ZL54NlHx3lUGZlcVLIkd6t5dZi4UHxUO07X%2BnSEGtsNOeo%2Bdnek%2BHqEyWZP0GX%2BN04psp3U4wto5fgMonwzRuCgBXru9Mr4lkGzVSPlWuCRNV7d%2BBUYCK6hVcLcfLMT7SgCYgmtLE1viA6rxYhjuwXShA&X-Amz-Signature=00ca9ad90840de63325fce20d7505f39d1457f09d34816dba618ad2da0c6d1ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









