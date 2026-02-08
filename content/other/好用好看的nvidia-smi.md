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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7U2TK3Q%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx7zkxu3E8IjQye2b7X4kW%2FU5KN%2BrUzQ2vEHb7g5DpxgIhAPkACxaywt99LXFDGCI%2Fx7v01v1FF%2BlvMjignckcw%2FUeKv8DCG0QABoMNjM3NDIzMTgzODA1IgzjtV8V8ChtowOFzFcq3APm%2FI8mtUfLlqETq0A3t%2FCj0F92SX8bp9Vb8zk6zaGL6QdKJt2ubFkqSbfRimSY4%2Bpmq4JGV2QNPO6Q7Ipdv8IkkXCFxeCAHyPyA%2BRtTNZhp2pHZDZH%2B4EFjP%2Bo33wT5vHj76zL5YF3izdLBhHJbBEV4dDsv83SREdS8gcnAI8C8UkwQZ1Bk%2B2h%2BVVID594YXtdKUS%2BGDsfMhLA99hdFkgexRsbRHtqssD3tOiBYWaKpiNvt%2FuH1VJOUXxKBT2W7Y3BduEDNItsmB2fLV29q5iddnZphK%2FeYLMBmZZrskmFybTARqzUdUonFOVPJeyGceLRd2mCr5%2FePuzXomWVKtnln%2Fxfxe2Y5OxRMZzI49mbG3QZQRBq27%2B512C%2FRMykAbJUQdoD80zu09T54a2a%2BbpDuUG9caNh0wQxZRN2rvOp8eYQOw1KG7DbuSf%2F9eiJe2Q0d1%2B5oBnTz4VYpqB1pMWbBv2YLceRmIH1fkuQf7nfuuaYydblCkyw3XdQvwdgoSeQiCGH1ITE9U0UJHYcCn2WJtHLW7GFgwDo5BSIzIOyeMAif7cZUvHKNkL%2BSHWWJZ405b8gXrO4oQ1KKWRKILz9DkO9uVJEo2HjfMcg5pexJ5mbzpVgcFaKatWRLjDTi6DMBjqkAcgmJkkJWyECASSfN66cr91E2YNXNtYFXGFb4ZAwTYR780YLn3vs3SoUR9x5vYFzs4TL0Uu5ILAH1uXnPdc16re5agZ8htnSnkGYGuFHg6bvSxNOfiyvbSMJOgot60MEPdjUf03PS%2FeZZSyI5aAwK9FII8kfrAEcH%2BCMrY15wY5tWwKtiVYa3xegqd0e%2BH%2B14ACcT0tnmrTTB6WN0m1FRH3boivB&X-Amz-Signature=7f8bda154ed91f0da8f72262e53e678850f7231a43f449a416db229bea20cec6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7U2TK3Q%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx7zkxu3E8IjQye2b7X4kW%2FU5KN%2BrUzQ2vEHb7g5DpxgIhAPkACxaywt99LXFDGCI%2Fx7v01v1FF%2BlvMjignckcw%2FUeKv8DCG0QABoMNjM3NDIzMTgzODA1IgzjtV8V8ChtowOFzFcq3APm%2FI8mtUfLlqETq0A3t%2FCj0F92SX8bp9Vb8zk6zaGL6QdKJt2ubFkqSbfRimSY4%2Bpmq4JGV2QNPO6Q7Ipdv8IkkXCFxeCAHyPyA%2BRtTNZhp2pHZDZH%2B4EFjP%2Bo33wT5vHj76zL5YF3izdLBhHJbBEV4dDsv83SREdS8gcnAI8C8UkwQZ1Bk%2B2h%2BVVID594YXtdKUS%2BGDsfMhLA99hdFkgexRsbRHtqssD3tOiBYWaKpiNvt%2FuH1VJOUXxKBT2W7Y3BduEDNItsmB2fLV29q5iddnZphK%2FeYLMBmZZrskmFybTARqzUdUonFOVPJeyGceLRd2mCr5%2FePuzXomWVKtnln%2Fxfxe2Y5OxRMZzI49mbG3QZQRBq27%2B512C%2FRMykAbJUQdoD80zu09T54a2a%2BbpDuUG9caNh0wQxZRN2rvOp8eYQOw1KG7DbuSf%2F9eiJe2Q0d1%2B5oBnTz4VYpqB1pMWbBv2YLceRmIH1fkuQf7nfuuaYydblCkyw3XdQvwdgoSeQiCGH1ITE9U0UJHYcCn2WJtHLW7GFgwDo5BSIzIOyeMAif7cZUvHKNkL%2BSHWWJZ405b8gXrO4oQ1KKWRKILz9DkO9uVJEo2HjfMcg5pexJ5mbzpVgcFaKatWRLjDTi6DMBjqkAcgmJkkJWyECASSfN66cr91E2YNXNtYFXGFb4ZAwTYR780YLn3vs3SoUR9x5vYFzs4TL0Uu5ILAH1uXnPdc16re5agZ8htnSnkGYGuFHg6bvSxNOfiyvbSMJOgot60MEPdjUf03PS%2FeZZSyI5aAwK9FII8kfrAEcH%2BCMrY15wY5tWwKtiVYa3xegqd0e%2BH%2B14ACcT0tnmrTTB6WN0m1FRH3boivB&X-Amz-Signature=0bc01a1bddbd5bd22b93f87e3768d1fee80c22bc976169c8442f60a8a9bd93aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









