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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XX6QLLB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEHZ%2FhPS66Gah6zqZyl13VFY5%2BH9RMmUmbwc3PrTzgYAiEA%2F01Y23Jf9bEmdUO%2BtZFS3iI9KynRObImWrT5algAJxkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgKo%2BmhKNSTOkRjCCrcA3hZZMKZVTuc5Y2gi91Zsd1O3xXJCU5YxcVilsDpn%2FTR80tgalAcSI8uTjSlagyoHEGZBxAA7bNeScYP8XnfBJE6rF89DGCOszAenXqkWVMrvzPSdx7KA57HURDjORR1Y8UTBDavcwNS7U%2FoPOlX2RHlY1Q9Ps3%2BJppULzKb3Xouta%2FoHP2b6pl5z%2BDCaUi%2FwxJnl711j8OeFXlbVlZiwRdOYc3WyvuiyJgxGQt3dPGVu%2FBYTrqsH5KEBkMjv8pINtCiM8wRtao7XL83nKu9GbMy89A5vIQL9cm3BswzOLHuR7ZcSYRNG3WcVxww4PatQSbufdEQIWGC3mgsgeJT6wH4ruZQVWHeMmBm9Hob%2BB4lNKEEzhgyz%2FHHyVJyGste%2FKbMEsIECgspVUQxOWpWTfC%2FucAunPijdRTFJ1gsUNAFh2jWg2XIheo%2BVyH5qCgz2nY6y4H6EiPUv1At%2BAt%2BlM1OxLN5t8KfcYjljcuL6Wx1AhzhriDdb5wzE%2BcsLGetua48aPG%2FsN%2F4A4HOLA3QX%2F3hvdzCPkXHSydmWbeBv1CV4tlbucnbN8zu51X4NBlgqPcE4oPFWcHEUgEE0f6Jjk%2B3XyR5wDVilAayQUCYsTaxMDspkYtb%2BgvFEBpPMOXd9s4GOqUBVhd143DpNNsyzmPyu6I0JOlB0Y1kxwLGCaRIj0uYXVBEkzDzxD6nsLrvOlD8X%2BbLL3WcqFUgou6BNWFH5Po7xA%2F61sOMg2RIpsdmeBiAtF3vsvd9Q3ZtAwW6B%2BpJuAcR4vgCPl2gWfon%2Bfrw856GscBMoVe8uIvSAZ1ZakeCvteuyrs1nSoMcPBAoLfFmwm0aLnAq6tlOfW01ETdBmIQbnJ8IlZb&X-Amz-Signature=3e5bd5cc905b80c8e7a12377caf5e84ac4614e215f8f9e2801754100b672f0c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XX6QLLB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEHZ%2FhPS66Gah6zqZyl13VFY5%2BH9RMmUmbwc3PrTzgYAiEA%2F01Y23Jf9bEmdUO%2BtZFS3iI9KynRObImWrT5algAJxkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgKo%2BmhKNSTOkRjCCrcA3hZZMKZVTuc5Y2gi91Zsd1O3xXJCU5YxcVilsDpn%2FTR80tgalAcSI8uTjSlagyoHEGZBxAA7bNeScYP8XnfBJE6rF89DGCOszAenXqkWVMrvzPSdx7KA57HURDjORR1Y8UTBDavcwNS7U%2FoPOlX2RHlY1Q9Ps3%2BJppULzKb3Xouta%2FoHP2b6pl5z%2BDCaUi%2FwxJnl711j8OeFXlbVlZiwRdOYc3WyvuiyJgxGQt3dPGVu%2FBYTrqsH5KEBkMjv8pINtCiM8wRtao7XL83nKu9GbMy89A5vIQL9cm3BswzOLHuR7ZcSYRNG3WcVxww4PatQSbufdEQIWGC3mgsgeJT6wH4ruZQVWHeMmBm9Hob%2BB4lNKEEzhgyz%2FHHyVJyGste%2FKbMEsIECgspVUQxOWpWTfC%2FucAunPijdRTFJ1gsUNAFh2jWg2XIheo%2BVyH5qCgz2nY6y4H6EiPUv1At%2BAt%2BlM1OxLN5t8KfcYjljcuL6Wx1AhzhriDdb5wzE%2BcsLGetua48aPG%2FsN%2F4A4HOLA3QX%2F3hvdzCPkXHSydmWbeBv1CV4tlbucnbN8zu51X4NBlgqPcE4oPFWcHEUgEE0f6Jjk%2B3XyR5wDVilAayQUCYsTaxMDspkYtb%2BgvFEBpPMOXd9s4GOqUBVhd143DpNNsyzmPyu6I0JOlB0Y1kxwLGCaRIj0uYXVBEkzDzxD6nsLrvOlD8X%2BbLL3WcqFUgou6BNWFH5Po7xA%2F61sOMg2RIpsdmeBiAtF3vsvd9Q3ZtAwW6B%2BpJuAcR4vgCPl2gWfon%2Bfrw856GscBMoVe8uIvSAZ1ZakeCvteuyrs1nSoMcPBAoLfFmwm0aLnAq6tlOfW01ETdBmIQbnJ8IlZb&X-Amz-Signature=3bc3aaeb134d3b1e58d25d07440cbb4ad31f37b0f324306e1ad2cf93e26f1f0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









