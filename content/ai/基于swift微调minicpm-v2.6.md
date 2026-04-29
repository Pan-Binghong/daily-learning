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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBI2IJC4%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQD4Q%2FvWXmNHgiNBDouyXbpXiu3kMd1YZrcSQoAECNwwtAIhAN49W9DwdOpRlANpV%2FLGvebgsmHfDMipSVxfjYJc70nxKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycTabSLNtyLxIpE1Yq3AO9apCApFVS3K46pkDqCsbHHVVWSVzvBl6dWrSHLeryEf%2BBVja0G2zqkYHy1UrrB4PEp2qHd9cnnqsSs2cZUkwGEJ%2F%2FPeRfMhR%2BUv2snp2yPEaq5Ei8NpW488UxH32EAotYyIMNrT2qHliRtKw35hgw5CdnCJBw%2BBaWmTmnRKiAzL88U1jc60Nt8xqNlZkLbbO4eEJrMotq2kNyWQZSDwr%2Be6QYJdhuUDCbjlltiBwsdo2GXsnPn%2FX2OgUC8ic9yUIBIZkRRO5r07o7YT5u91ogRLxtmJ6X0aeEfJ7LN2Rv%2BBsLZyOBwqXsRZWl%2BVhBK%2Bkawo2mVpLWDz2AklB6pWawuC8P%2BpzbPWE9RxZQWKDaoVZ3WhgOZxR0bDyPZ0ffSRrgRy7sSctNyilJAwHS7vx5eYL0LYrJ6dmtVslNczVyP6h25yU%2BDH%2FX27%2Fh3Z%2FWjqZjXn92Jv21f%2B402uTVKhXUmnioYk1hg5gNseNtZJ68R%2Fj0TP2jhvL3vE%2FUUbvJagUjRJnkbc2Jo0kI5S23KUeubWaYLoAkDcJgOSIOUrXEx0l1XhWmY8dp3b7mvKrvENoDHHrqnUgQQ5odovwxoOgDKMzUwrScMgGwoeTjahQgSgCBKAZ2EGBa75AVcjDDkcbPBjqkAWkD38oJvlu7yUlFRIaSx%2FFTaKvgmtGdYtbdIvMoBRdSWblz38GSf%2F%2BZxdcH2FTxSxVIjdPLAHFB5D55U%2BrCHUfsxGBMlcXAC8x2yMkIZsCHdLGH4mCV9X36UvCpSqPirYPi7bK8Fc0CMQ81J%2Fc3Yp%2B9T%2F7SGrOKVrZdL4jn%2FWdowVGWAlsZpM%2Fq%2Bu7%2FRUvElbVWWCsXQb7kU7JyewkE80%2FxoVMB&X-Amz-Signature=c3a7369214664567ce7f9e3e9b167aabac1d470a17a9b3291dc27f204c4c54b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBI2IJC4%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQD4Q%2FvWXmNHgiNBDouyXbpXiu3kMd1YZrcSQoAECNwwtAIhAN49W9DwdOpRlANpV%2FLGvebgsmHfDMipSVxfjYJc70nxKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycTabSLNtyLxIpE1Yq3AO9apCApFVS3K46pkDqCsbHHVVWSVzvBl6dWrSHLeryEf%2BBVja0G2zqkYHy1UrrB4PEp2qHd9cnnqsSs2cZUkwGEJ%2F%2FPeRfMhR%2BUv2snp2yPEaq5Ei8NpW488UxH32EAotYyIMNrT2qHliRtKw35hgw5CdnCJBw%2BBaWmTmnRKiAzL88U1jc60Nt8xqNlZkLbbO4eEJrMotq2kNyWQZSDwr%2Be6QYJdhuUDCbjlltiBwsdo2GXsnPn%2FX2OgUC8ic9yUIBIZkRRO5r07o7YT5u91ogRLxtmJ6X0aeEfJ7LN2Rv%2BBsLZyOBwqXsRZWl%2BVhBK%2Bkawo2mVpLWDz2AklB6pWawuC8P%2BpzbPWE9RxZQWKDaoVZ3WhgOZxR0bDyPZ0ffSRrgRy7sSctNyilJAwHS7vx5eYL0LYrJ6dmtVslNczVyP6h25yU%2BDH%2FX27%2Fh3Z%2FWjqZjXn92Jv21f%2B402uTVKhXUmnioYk1hg5gNseNtZJ68R%2Fj0TP2jhvL3vE%2FUUbvJagUjRJnkbc2Jo0kI5S23KUeubWaYLoAkDcJgOSIOUrXEx0l1XhWmY8dp3b7mvKrvENoDHHrqnUgQQ5odovwxoOgDKMzUwrScMgGwoeTjahQgSgCBKAZ2EGBa75AVcjDDkcbPBjqkAWkD38oJvlu7yUlFRIaSx%2FFTaKvgmtGdYtbdIvMoBRdSWblz38GSf%2F%2BZxdcH2FTxSxVIjdPLAHFB5D55U%2BrCHUfsxGBMlcXAC8x2yMkIZsCHdLGH4mCV9X36UvCpSqPirYPi7bK8Fc0CMQ81J%2Fc3Yp%2B9T%2F7SGrOKVrZdL4jn%2FWdowVGWAlsZpM%2Fq%2Bu7%2FRUvElbVWWCsXQb7kU7JyewkE80%2FxoVMB&X-Amz-Signature=fb0873d0c217340b66cacb98dd5959f7ab06ad89e48729e587d800ee27d56bc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBI2IJC4%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQD4Q%2FvWXmNHgiNBDouyXbpXiu3kMd1YZrcSQoAECNwwtAIhAN49W9DwdOpRlANpV%2FLGvebgsmHfDMipSVxfjYJc70nxKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycTabSLNtyLxIpE1Yq3AO9apCApFVS3K46pkDqCsbHHVVWSVzvBl6dWrSHLeryEf%2BBVja0G2zqkYHy1UrrB4PEp2qHd9cnnqsSs2cZUkwGEJ%2F%2FPeRfMhR%2BUv2snp2yPEaq5Ei8NpW488UxH32EAotYyIMNrT2qHliRtKw35hgw5CdnCJBw%2BBaWmTmnRKiAzL88U1jc60Nt8xqNlZkLbbO4eEJrMotq2kNyWQZSDwr%2Be6QYJdhuUDCbjlltiBwsdo2GXsnPn%2FX2OgUC8ic9yUIBIZkRRO5r07o7YT5u91ogRLxtmJ6X0aeEfJ7LN2Rv%2BBsLZyOBwqXsRZWl%2BVhBK%2Bkawo2mVpLWDz2AklB6pWawuC8P%2BpzbPWE9RxZQWKDaoVZ3WhgOZxR0bDyPZ0ffSRrgRy7sSctNyilJAwHS7vx5eYL0LYrJ6dmtVslNczVyP6h25yU%2BDH%2FX27%2Fh3Z%2FWjqZjXn92Jv21f%2B402uTVKhXUmnioYk1hg5gNseNtZJ68R%2Fj0TP2jhvL3vE%2FUUbvJagUjRJnkbc2Jo0kI5S23KUeubWaYLoAkDcJgOSIOUrXEx0l1XhWmY8dp3b7mvKrvENoDHHrqnUgQQ5odovwxoOgDKMzUwrScMgGwoeTjahQgSgCBKAZ2EGBa75AVcjDDkcbPBjqkAWkD38oJvlu7yUlFRIaSx%2FFTaKvgmtGdYtbdIvMoBRdSWblz38GSf%2F%2BZxdcH2FTxSxVIjdPLAHFB5D55U%2BrCHUfsxGBMlcXAC8x2yMkIZsCHdLGH4mCV9X36UvCpSqPirYPi7bK8Fc0CMQ81J%2Fc3Yp%2B9T%2F7SGrOKVrZdL4jn%2FWdowVGWAlsZpM%2Fq%2Bu7%2FRUvElbVWWCsXQb7kU7JyewkE80%2FxoVMB&X-Amz-Signature=da956cb2583abe5a0bb0ee8592349741b7b9071826e0688f4d54c917dc28b7a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

