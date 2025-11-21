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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P7VWGOV%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDvMnjgLF1lRfdx2jtWmwAMI5Rt%2FiAHD8rHRPtKq9IJbwIgXkGhQqEtWvyjtv3jFKlRSonXU7JgxfZJFWaTflcuWboq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDCjN8Za%2By9FWsWnOiCrcA3FPWKkLfnXzBtP1LY2Oi%2Bo3%2BJbeILMPYs2lKePZkLU6A3LyV8IiM3o2RAtVScm49XzUKjgLWZ%2FO27J2QL0QP8JbeWBknHT3ewGlwjL4Ea2AYyen9xBLNXANpkKfbOCF3VBSRJYl8N0h7B4BgvU1LxPH5kI7SdV2xtJOZsKj7mssijBulFhK11lPrskwhm5%2FQreYxJ%2Bhp6DGT9rc7l1ky3Qbb%2BQmcd3TQmnpbMEZODODcvG63dUklKMtCUYXjpFJJGTCOPRkVZ3SHHIivSUlvTxcRyzlbTeThek8ApXkhSCDdigvZjP9Eo7XND59ZtcU6oqQ%2F819c%2Fuje9wHHeF6UGJKU3yJC4SLSQdaz%2BTT7Lb1WOSAAXftUhTuQYAE0CnDG5PWZmnL8U6UU%2BemKfgJLgisnQjY87UlCPDweOvbjM2I3BEJFQYVYOQv6ByBo8eQiWo4QmPUwR9rQzDBRz9Km7Q%2BmiD53ThT2x45hXzt7tjnO0pHjWsa1ywwFrJYaf7Af6%2FHyKMroBcxt9eFnULm3Jrt2KHM0aBEveTCNhEL7esq7BsUw62vPf9XURHH%2BZOM%2FwAaoRPgWPxtcN%2BIrhSSNrz2rb7lO3sprckZtaan8NHGhfn8YPkfENwQeXpVMOae%2F8gGOqUBuIOYVSUjKPFIdYIMYx%2F%2FQ7drb%2FMltxUS2xsp1eCvxmKcPI3zMT4tLCMjmpAuod8QeCGiHWI6LU86M9aYUs5epXtj%2B%2BXwRef2BJkkchIeVCviuhzppuKVHOrsCxmSePQsO33QA0%2Fdfs0FlZkNS7NsshnRw0FNRxuNrVkts%2BV3zg9grRVfYYPL4wvuGiSVYTjVV5kmeFVU1IqMSrZ7xCygy6U9WtAX&X-Amz-Signature=478f50fecb1fb990af8cb5c26a4db1adab67fb33a18bbd33b98fdedd0aa5df7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P7VWGOV%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDvMnjgLF1lRfdx2jtWmwAMI5Rt%2FiAHD8rHRPtKq9IJbwIgXkGhQqEtWvyjtv3jFKlRSonXU7JgxfZJFWaTflcuWboq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDCjN8Za%2By9FWsWnOiCrcA3FPWKkLfnXzBtP1LY2Oi%2Bo3%2BJbeILMPYs2lKePZkLU6A3LyV8IiM3o2RAtVScm49XzUKjgLWZ%2FO27J2QL0QP8JbeWBknHT3ewGlwjL4Ea2AYyen9xBLNXANpkKfbOCF3VBSRJYl8N0h7B4BgvU1LxPH5kI7SdV2xtJOZsKj7mssijBulFhK11lPrskwhm5%2FQreYxJ%2Bhp6DGT9rc7l1ky3Qbb%2BQmcd3TQmnpbMEZODODcvG63dUklKMtCUYXjpFJJGTCOPRkVZ3SHHIivSUlvTxcRyzlbTeThek8ApXkhSCDdigvZjP9Eo7XND59ZtcU6oqQ%2F819c%2Fuje9wHHeF6UGJKU3yJC4SLSQdaz%2BTT7Lb1WOSAAXftUhTuQYAE0CnDG5PWZmnL8U6UU%2BemKfgJLgisnQjY87UlCPDweOvbjM2I3BEJFQYVYOQv6ByBo8eQiWo4QmPUwR9rQzDBRz9Km7Q%2BmiD53ThT2x45hXzt7tjnO0pHjWsa1ywwFrJYaf7Af6%2FHyKMroBcxt9eFnULm3Jrt2KHM0aBEveTCNhEL7esq7BsUw62vPf9XURHH%2BZOM%2FwAaoRPgWPxtcN%2BIrhSSNrz2rb7lO3sprckZtaan8NHGhfn8YPkfENwQeXpVMOae%2F8gGOqUBuIOYVSUjKPFIdYIMYx%2F%2FQ7drb%2FMltxUS2xsp1eCvxmKcPI3zMT4tLCMjmpAuod8QeCGiHWI6LU86M9aYUs5epXtj%2B%2BXwRef2BJkkchIeVCviuhzppuKVHOrsCxmSePQsO33QA0%2Fdfs0FlZkNS7NsshnRw0FNRxuNrVkts%2BV3zg9grRVfYYPL4wvuGiSVYTjVV5kmeFVU1IqMSrZ7xCygy6U9WtAX&X-Amz-Signature=b87c1f241bdcb1a733fecf9c54952255bdd7141cd913d8612e19bf7698802b8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









