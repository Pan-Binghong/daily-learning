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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQKUPKB%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZRBtVRn0EimEMPHyymb9%2B1qy6%2BtT7Dv6ADYy2GEdDiAiBlfxDr6Stjbk%2FbumCwOPDzn77jcShApUnW5XPJouzPOCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMLrJA8HOrEFOht1bnKtwDgdYu26j8WGTnL9M2AP1WTojUNRRx3AgJHBIXCeNRjcNEcBJ1xvljZ5fY684QXirs2KiQ2r12Gqrp8wX%2FPeqNb1XIxXerdc8RocNawf%2Foc0%2By%2Bt0ZrME6X6ttIDXZMybkhhfrSxbYVzHp3N%2BH9M3I9xK%2BHSQ%2Fzexn1NglEB%2Beot3bpeljOiptAKrwNMlKXJnep5Zs39h9jWEhvSvcaw1eD6GutRsxcUGX%2BTahZOFpg0Ij4%2FanGmjuuHkzR4CwPffyPHRnSAa34xFvxmytv9OndbEhvOx2fiXCQCp8NtmvXrIv49MgPMkKA4K0Psm8KR4i8BDWW2kwWR69FwKGgkJiFWv0XqVIMDO9cb8Euvu4docZ6hf2e1fQCrL85Ga4ByoH4Fbjucz7MBxPGgRciAQ2TKsamjooWds5mr4SxWaT2FnN%2FYLv6DGSjdMWK9w%2F3PQ7aRCcf8t%2BIauRispJ7SkLl8WJ4sP%2FlYvGv579067EfjsmsVJEux%2FS3xTg3hiLnlB%2FvX6Mv7iM0wzAlG%2BcTuCLiBG1vPmYJmeuaIKZZx1z33po9H32ziCvTiJRsFB%2BGL0c3VyPEF9C3KF%2BKrGjpcVXw1DhcQi%2FeGdfvcu2kH26357et5RMTyTADFXs9egw5oyDygY6pgGfoNCYgQZuWXReXZqCaOBHWdICIqnQSDczSItKeL%2B5hmrxpl46nZ98tLVhjIDsKHGAzDhkqkReqhbGOgXnQgWnYP1kr93FfcpOWcJFNPv63guZYuZraK6yvUSV8dmak5iRdII4dNWgh2KOpmAoRV7Snu0LnGpXUQ%2BnpSNoMkOB%2FT%2BPGXuJS8p0xDcHVwMYYnp6MVP87mQ7xlehiophUnZ%2FWaGowUN1&X-Amz-Signature=07c11a9614a0d0c700ea70b10bca6b642c1ce2c15ba6afe115c4a235a015c6a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQKUPKB%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZRBtVRn0EimEMPHyymb9%2B1qy6%2BtT7Dv6ADYy2GEdDiAiBlfxDr6Stjbk%2FbumCwOPDzn77jcShApUnW5XPJouzPOCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMLrJA8HOrEFOht1bnKtwDgdYu26j8WGTnL9M2AP1WTojUNRRx3AgJHBIXCeNRjcNEcBJ1xvljZ5fY684QXirs2KiQ2r12Gqrp8wX%2FPeqNb1XIxXerdc8RocNawf%2Foc0%2By%2Bt0ZrME6X6ttIDXZMybkhhfrSxbYVzHp3N%2BH9M3I9xK%2BHSQ%2Fzexn1NglEB%2Beot3bpeljOiptAKrwNMlKXJnep5Zs39h9jWEhvSvcaw1eD6GutRsxcUGX%2BTahZOFpg0Ij4%2FanGmjuuHkzR4CwPffyPHRnSAa34xFvxmytv9OndbEhvOx2fiXCQCp8NtmvXrIv49MgPMkKA4K0Psm8KR4i8BDWW2kwWR69FwKGgkJiFWv0XqVIMDO9cb8Euvu4docZ6hf2e1fQCrL85Ga4ByoH4Fbjucz7MBxPGgRciAQ2TKsamjooWds5mr4SxWaT2FnN%2FYLv6DGSjdMWK9w%2F3PQ7aRCcf8t%2BIauRispJ7SkLl8WJ4sP%2FlYvGv579067EfjsmsVJEux%2FS3xTg3hiLnlB%2FvX6Mv7iM0wzAlG%2BcTuCLiBG1vPmYJmeuaIKZZx1z33po9H32ziCvTiJRsFB%2BGL0c3VyPEF9C3KF%2BKrGjpcVXw1DhcQi%2FeGdfvcu2kH26357et5RMTyTADFXs9egw5oyDygY6pgGfoNCYgQZuWXReXZqCaOBHWdICIqnQSDczSItKeL%2B5hmrxpl46nZ98tLVhjIDsKHGAzDhkqkReqhbGOgXnQgWnYP1kr93FfcpOWcJFNPv63guZYuZraK6yvUSV8dmak5iRdII4dNWgh2KOpmAoRV7Snu0LnGpXUQ%2BnpSNoMkOB%2FT%2BPGXuJS8p0xDcHVwMYYnp6MVP87mQ7xlehiophUnZ%2FWaGowUN1&X-Amz-Signature=ff5f11a1ec4d9627c750f4db0898af06a878989d1a4312dda14970ce56a831bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









