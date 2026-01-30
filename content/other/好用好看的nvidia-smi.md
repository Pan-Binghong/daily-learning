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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5LVK4IB%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZHPLGLaVy%2BA8npEPyVTuLJDdq2SdEW6tDI%2FoxYw5kdwIgadRNaP0JqMuQwyvL7a%2BzQdwNG9aN%2Fr03xISJWVq89aAqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW04B0i%2Bkr%2F6kmpSrcA1tRmhOB4MwgiA4%2BrXZJ10gknrHID1Wqv%2FmQlfnk%2FYdhc2cmG8Qgdz1bIdsSYPNgVccUjBBJneEL0A1vvX5LB%2B0COZBIUo1JVLuU2ockr1VopEOuozqrT3jx6babylw5pBRNvM%2Fsjfy%2FNtEbCCF1OB9EdxZrTxyUZ6Ztokrp4d1wLCXUySiIY9CCMkyoTfdt9ZRKSfwnmeRyY9DzorliR9Ue2ARPp7HaNgCjIQzQAIVpUQQ9Nax2%2FBGTmpUp8ohy235uo20Y2p8PnT63dTlQb3O01qeiSdUhgDWlr87zUUBTTZFU7EclqDg1ufMHhyQaosohICPp3M8mZCEgnFbsHg1OGqafbvg2vJfSewl%2BRDp2tBPD8z7BMyikeVU3mGs3Tw3iCPU4tjGtkjxedF3DYXaziTYFqftA%2FwH7lp0%2FZPfYYt3TQ011Bnsj0SznNbH%2Bl1Bt%2FkZvhG17Um39DLAqLzq2yJrMNlgiV4rwjQa8wA6cLlFlOWOiLHA%2BizYRfKuZCzQMlc9WMhhi6eBXQ88A8FmEViV5kuTEQXtKnQV8IcapEgj0pVOp8%2FpZzv9%2F4wVk%2FMKjje1KIW0Q2cgUze6BiBkg%2FuJuKIQCVTQ0YZevJEN%2Fjt2DPo%2Fcr9%2BkWxVTMPnI8MsGOqUBTrEcJ4EcrTvNkISZmwpOsAnU8XsEhlN66xkvc79Ua3A2ip9iowtyc0pTjFTJXTzFT%2B8csqwbRQibOmEJawVV3uzpWKzrBdxj6NcleNquzeVrVeHpOSinIFzMGyOMx8Kbg%2BWFnnhtMHJz5dJs2PrII8BeUPMzA51PsCxNeZdFkHNirHVASizXJzoxZL2231ztk%2B2gEJ6lFqCBocKvgTqlABPTK486&X-Amz-Signature=0788a0cbf3c44e41f45f395c0e4bd3972e76557aac4e393ea978140a2a034817&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5LVK4IB%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZHPLGLaVy%2BA8npEPyVTuLJDdq2SdEW6tDI%2FoxYw5kdwIgadRNaP0JqMuQwyvL7a%2BzQdwNG9aN%2Fr03xISJWVq89aAqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW04B0i%2Bkr%2F6kmpSrcA1tRmhOB4MwgiA4%2BrXZJ10gknrHID1Wqv%2FmQlfnk%2FYdhc2cmG8Qgdz1bIdsSYPNgVccUjBBJneEL0A1vvX5LB%2B0COZBIUo1JVLuU2ockr1VopEOuozqrT3jx6babylw5pBRNvM%2Fsjfy%2FNtEbCCF1OB9EdxZrTxyUZ6Ztokrp4d1wLCXUySiIY9CCMkyoTfdt9ZRKSfwnmeRyY9DzorliR9Ue2ARPp7HaNgCjIQzQAIVpUQQ9Nax2%2FBGTmpUp8ohy235uo20Y2p8PnT63dTlQb3O01qeiSdUhgDWlr87zUUBTTZFU7EclqDg1ufMHhyQaosohICPp3M8mZCEgnFbsHg1OGqafbvg2vJfSewl%2BRDp2tBPD8z7BMyikeVU3mGs3Tw3iCPU4tjGtkjxedF3DYXaziTYFqftA%2FwH7lp0%2FZPfYYt3TQ011Bnsj0SznNbH%2Bl1Bt%2FkZvhG17Um39DLAqLzq2yJrMNlgiV4rwjQa8wA6cLlFlOWOiLHA%2BizYRfKuZCzQMlc9WMhhi6eBXQ88A8FmEViV5kuTEQXtKnQV8IcapEgj0pVOp8%2FpZzv9%2F4wVk%2FMKjje1KIW0Q2cgUze6BiBkg%2FuJuKIQCVTQ0YZevJEN%2Fjt2DPo%2Fcr9%2BkWxVTMPnI8MsGOqUBTrEcJ4EcrTvNkISZmwpOsAnU8XsEhlN66xkvc79Ua3A2ip9iowtyc0pTjFTJXTzFT%2B8csqwbRQibOmEJawVV3uzpWKzrBdxj6NcleNquzeVrVeHpOSinIFzMGyOMx8Kbg%2BWFnnhtMHJz5dJs2PrII8BeUPMzA51PsCxNeZdFkHNirHVASizXJzoxZL2231ztk%2B2gEJ6lFqCBocKvgTqlABPTK486&X-Amz-Signature=7b6f02d110ead05381ccb973f0d22149b2cee1b0411ec8931340323ad4236d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









