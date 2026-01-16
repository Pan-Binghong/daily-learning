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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3Y7UZRK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQC4CH6inC3zp9MsGDsIHY2XJQLyA8TDiqJFSfwYT%2BEb6QIgOAAlME%2Fcyu6CEPjAFCSD4BEYghK7wAjd%2BL2s%2Bbh24skq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDIuJNG2JdW%2Bm6kzybyrcAxFD2kZCbWoNRH%2FLzfZU8mqrEX%2Fd6GJ03kvic3vozyGM8uGw%2FnITl16pPmtEJU78RrxpxUvE3zxL5myFYGoC5NpcFSyIZn8qyv6HQXQwpYj%2BipjrMgIOkkueI1SPULhfk%2FXDATndVstGkhTx9UyfKMd9ZcC0O8qfRNfv8Lpgtrt%2BXZnW1T8laZ9%2FM5npBUsxDxekF2OkD1W1zjoLD4esaTNx6fkd%2FVLIVQM0FEe2zfBbUesoKq1fIfxltAF46EUsRvAEZtxMWFTIqrIe9T3BHlbLRvwTq%2FvLgkHUyZ0JaNpFOMp85SmKzUaX89t5Aa5kvFGTPKp6JVWiVyn%2BeTM4GcRk31pLLrxxEDfP8Ifzb2hFZDSpA2ZmzyawqoPtEu88zHHKUrQrn3PYajY88lFk4FGBsU10Orh9xaAvgpUIkBu50LD6aepPPj%2BuKu2RUSyWgaDU5vN9C%2Fy5jrzOovx260Vz2qk8j2DFILyDMsQM0MiJ2UkVjkdtof7%2BJKrWSjLvVlke4dvQ0sXmLnZXnfXkAn3Gn0krR3%2BwoGCFc%2BsAIkTx4RPuzr9gr06u3bJUt6CEr9bQGSi%2BLvFeYBtoBp5fIhv8PIqDFbSh%2FymDNRW2pl9uYEYYW08Tq2Lws4QEMM%2B%2FpssGOqUBHGea0K7Rh2wtcjk%2F%2Bs2d0A1UW8CkR6vSgIa0iGSPoLdEengjkTVMi5nJmPAsPy0uuN8M4389s64ww4V06mkFzgcV6r%2Fubif%2FgyowXtpFK2lp%2BShBuVNiLlL0nSe9GmXHbYhW95ajUp%2B0ZKl2mpA%2FJXF1xodLCxnlntTMha%2FaGHHvLoJkZtYfp4os43DIYEaKsjz2lFh9XPm1nkNzzdv%2FP6qZi5sK&X-Amz-Signature=fc376cec4d05a7b5f47f47385bd924b781ab705676250d365a58e54c75500891&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3Y7UZRK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQC4CH6inC3zp9MsGDsIHY2XJQLyA8TDiqJFSfwYT%2BEb6QIgOAAlME%2Fcyu6CEPjAFCSD4BEYghK7wAjd%2BL2s%2Bbh24skq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDIuJNG2JdW%2Bm6kzybyrcAxFD2kZCbWoNRH%2FLzfZU8mqrEX%2Fd6GJ03kvic3vozyGM8uGw%2FnITl16pPmtEJU78RrxpxUvE3zxL5myFYGoC5NpcFSyIZn8qyv6HQXQwpYj%2BipjrMgIOkkueI1SPULhfk%2FXDATndVstGkhTx9UyfKMd9ZcC0O8qfRNfv8Lpgtrt%2BXZnW1T8laZ9%2FM5npBUsxDxekF2OkD1W1zjoLD4esaTNx6fkd%2FVLIVQM0FEe2zfBbUesoKq1fIfxltAF46EUsRvAEZtxMWFTIqrIe9T3BHlbLRvwTq%2FvLgkHUyZ0JaNpFOMp85SmKzUaX89t5Aa5kvFGTPKp6JVWiVyn%2BeTM4GcRk31pLLrxxEDfP8Ifzb2hFZDSpA2ZmzyawqoPtEu88zHHKUrQrn3PYajY88lFk4FGBsU10Orh9xaAvgpUIkBu50LD6aepPPj%2BuKu2RUSyWgaDU5vN9C%2Fy5jrzOovx260Vz2qk8j2DFILyDMsQM0MiJ2UkVjkdtof7%2BJKrWSjLvVlke4dvQ0sXmLnZXnfXkAn3Gn0krR3%2BwoGCFc%2BsAIkTx4RPuzr9gr06u3bJUt6CEr9bQGSi%2BLvFeYBtoBp5fIhv8PIqDFbSh%2FymDNRW2pl9uYEYYW08Tq2Lws4QEMM%2B%2FpssGOqUBHGea0K7Rh2wtcjk%2F%2Bs2d0A1UW8CkR6vSgIa0iGSPoLdEengjkTVMi5nJmPAsPy0uuN8M4389s64ww4V06mkFzgcV6r%2Fubif%2FgyowXtpFK2lp%2BShBuVNiLlL0nSe9GmXHbYhW95ajUp%2B0ZKl2mpA%2FJXF1xodLCxnlntTMha%2FaGHHvLoJkZtYfp4os43DIYEaKsjz2lFh9XPm1nkNzzdv%2FP6qZi5sK&X-Amz-Signature=4955c0faa8bc432f462cb86de8a7000effebd1678b6738c1c007826a67cfc39f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









