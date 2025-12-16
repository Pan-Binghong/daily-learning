---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQKUPKB%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZRBtVRn0EimEMPHyymb9%2B1qy6%2BtT7Dv6ADYy2GEdDiAiBlfxDr6Stjbk%2FbumCwOPDzn77jcShApUnW5XPJouzPOCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMLrJA8HOrEFOht1bnKtwDgdYu26j8WGTnL9M2AP1WTojUNRRx3AgJHBIXCeNRjcNEcBJ1xvljZ5fY684QXirs2KiQ2r12Gqrp8wX%2FPeqNb1XIxXerdc8RocNawf%2Foc0%2By%2Bt0ZrME6X6ttIDXZMybkhhfrSxbYVzHp3N%2BH9M3I9xK%2BHSQ%2Fzexn1NglEB%2Beot3bpeljOiptAKrwNMlKXJnep5Zs39h9jWEhvSvcaw1eD6GutRsxcUGX%2BTahZOFpg0Ij4%2FanGmjuuHkzR4CwPffyPHRnSAa34xFvxmytv9OndbEhvOx2fiXCQCp8NtmvXrIv49MgPMkKA4K0Psm8KR4i8BDWW2kwWR69FwKGgkJiFWv0XqVIMDO9cb8Euvu4docZ6hf2e1fQCrL85Ga4ByoH4Fbjucz7MBxPGgRciAQ2TKsamjooWds5mr4SxWaT2FnN%2FYLv6DGSjdMWK9w%2F3PQ7aRCcf8t%2BIauRispJ7SkLl8WJ4sP%2FlYvGv579067EfjsmsVJEux%2FS3xTg3hiLnlB%2FvX6Mv7iM0wzAlG%2BcTuCLiBG1vPmYJmeuaIKZZx1z33po9H32ziCvTiJRsFB%2BGL0c3VyPEF9C3KF%2BKrGjpcVXw1DhcQi%2FeGdfvcu2kH26357et5RMTyTADFXs9egw5oyDygY6pgGfoNCYgQZuWXReXZqCaOBHWdICIqnQSDczSItKeL%2B5hmrxpl46nZ98tLVhjIDsKHGAzDhkqkReqhbGOgXnQgWnYP1kr93FfcpOWcJFNPv63guZYuZraK6yvUSV8dmak5iRdII4dNWgh2KOpmAoRV7Snu0LnGpXUQ%2BnpSNoMkOB%2FT%2BPGXuJS8p0xDcHVwMYYnp6MVP87mQ7xlehiophUnZ%2FWaGowUN1&X-Amz-Signature=fd8b367ca94eaebdf2e2e84abf6a77a4d217ea8d368451e28e1d36512c46d4e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQKUPKB%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZRBtVRn0EimEMPHyymb9%2B1qy6%2BtT7Dv6ADYy2GEdDiAiBlfxDr6Stjbk%2FbumCwOPDzn77jcShApUnW5XPJouzPOCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMLrJA8HOrEFOht1bnKtwDgdYu26j8WGTnL9M2AP1WTojUNRRx3AgJHBIXCeNRjcNEcBJ1xvljZ5fY684QXirs2KiQ2r12Gqrp8wX%2FPeqNb1XIxXerdc8RocNawf%2Foc0%2By%2Bt0ZrME6X6ttIDXZMybkhhfrSxbYVzHp3N%2BH9M3I9xK%2BHSQ%2Fzexn1NglEB%2Beot3bpeljOiptAKrwNMlKXJnep5Zs39h9jWEhvSvcaw1eD6GutRsxcUGX%2BTahZOFpg0Ij4%2FanGmjuuHkzR4CwPffyPHRnSAa34xFvxmytv9OndbEhvOx2fiXCQCp8NtmvXrIv49MgPMkKA4K0Psm8KR4i8BDWW2kwWR69FwKGgkJiFWv0XqVIMDO9cb8Euvu4docZ6hf2e1fQCrL85Ga4ByoH4Fbjucz7MBxPGgRciAQ2TKsamjooWds5mr4SxWaT2FnN%2FYLv6DGSjdMWK9w%2F3PQ7aRCcf8t%2BIauRispJ7SkLl8WJ4sP%2FlYvGv579067EfjsmsVJEux%2FS3xTg3hiLnlB%2FvX6Mv7iM0wzAlG%2BcTuCLiBG1vPmYJmeuaIKZZx1z33po9H32ziCvTiJRsFB%2BGL0c3VyPEF9C3KF%2BKrGjpcVXw1DhcQi%2FeGdfvcu2kH26357et5RMTyTADFXs9egw5oyDygY6pgGfoNCYgQZuWXReXZqCaOBHWdICIqnQSDczSItKeL%2B5hmrxpl46nZ98tLVhjIDsKHGAzDhkqkReqhbGOgXnQgWnYP1kr93FfcpOWcJFNPv63guZYuZraK6yvUSV8dmak5iRdII4dNWgh2KOpmAoRV7Snu0LnGpXUQ%2BnpSNoMkOB%2FT%2BPGXuJS8p0xDcHVwMYYnp6MVP87mQ7xlehiophUnZ%2FWaGowUN1&X-Amz-Signature=c971ec15b544878b2b00ce6c3fdbbce6dd133a80dbfec6bcaf600bd1398dba09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQKUPKB%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZRBtVRn0EimEMPHyymb9%2B1qy6%2BtT7Dv6ADYy2GEdDiAiBlfxDr6Stjbk%2FbumCwOPDzn77jcShApUnW5XPJouzPOCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMLrJA8HOrEFOht1bnKtwDgdYu26j8WGTnL9M2AP1WTojUNRRx3AgJHBIXCeNRjcNEcBJ1xvljZ5fY684QXirs2KiQ2r12Gqrp8wX%2FPeqNb1XIxXerdc8RocNawf%2Foc0%2By%2Bt0ZrME6X6ttIDXZMybkhhfrSxbYVzHp3N%2BH9M3I9xK%2BHSQ%2Fzexn1NglEB%2Beot3bpeljOiptAKrwNMlKXJnep5Zs39h9jWEhvSvcaw1eD6GutRsxcUGX%2BTahZOFpg0Ij4%2FanGmjuuHkzR4CwPffyPHRnSAa34xFvxmytv9OndbEhvOx2fiXCQCp8NtmvXrIv49MgPMkKA4K0Psm8KR4i8BDWW2kwWR69FwKGgkJiFWv0XqVIMDO9cb8Euvu4docZ6hf2e1fQCrL85Ga4ByoH4Fbjucz7MBxPGgRciAQ2TKsamjooWds5mr4SxWaT2FnN%2FYLv6DGSjdMWK9w%2F3PQ7aRCcf8t%2BIauRispJ7SkLl8WJ4sP%2FlYvGv579067EfjsmsVJEux%2FS3xTg3hiLnlB%2FvX6Mv7iM0wzAlG%2BcTuCLiBG1vPmYJmeuaIKZZx1z33po9H32ziCvTiJRsFB%2BGL0c3VyPEF9C3KF%2BKrGjpcVXw1DhcQi%2FeGdfvcu2kH26357et5RMTyTADFXs9egw5oyDygY6pgGfoNCYgQZuWXReXZqCaOBHWdICIqnQSDczSItKeL%2B5hmrxpl46nZ98tLVhjIDsKHGAzDhkqkReqhbGOgXnQgWnYP1kr93FfcpOWcJFNPv63guZYuZraK6yvUSV8dmak5iRdII4dNWgh2KOpmAoRV7Snu0LnGpXUQ%2BnpSNoMkOB%2FT%2BPGXuJS8p0xDcHVwMYYnp6MVP87mQ7xlehiophUnZ%2FWaGowUN1&X-Amz-Signature=846c4a3e36a5f8c784ce36d4ba0002b94046b6d4844272d3161ea662963d5f1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

