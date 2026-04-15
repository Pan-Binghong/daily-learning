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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O6AFONT%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbgEtgtasfWmb4ulYU7LCCe7wBLtvR9YmE19Ykx%2BONMAIgeSJzx9DiNGev69uIN%2BfIyEO3tMWZbOCfN6eojmuSrT8qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkLcXS8uTCuGDGAoircAyw39setECN8n34f36dZyhbxTVodGXNHM67UX%2Be2HsNs%2Bh0K2aOqzrVfUqgPA%2BzYmCikqxlOMViqRkXwLG92uk9Fh%2BV0fOOWFGL8dpaRCgmtYZ%2BctPeXCmZ6N3DRxRpnkQa%2FDSiOtLwKPz31AwQj0NguaY89pebmPHPna0Xkw%2B2MtJ30FksbL2uI6z%2FXRCDCAvdE1FWO2ZnryWc2oIDJFOK9JuwpJ0WdeNfQ2c2r01lwrriIEFMLkmofudIgBfdbYmgSD03lb5SK1Zw6PpahSoSX3E%2FJRehiCg5JAdVo3ftOGmEKAdFNUbByK9pOv7VWbS3c63i1tgOQ0futZJQ5Ue87SE04iKgewhT0P7sE5iBrba7EXr6EzsK5quCuOBmLS1ulw1uHV25ZlhuRgwhWdZx38rpa%2Bq%2BdJ8wwc%2B2lbem05bG3z9i1S5uihYPr4taF4%2Bxro7wIcYV4bg295i73KAMDeQCWGUuVP7x0fa0vVXtVxMqj%2BHpsi667w%2BaxgmEhIQb2SA12nalK7JaFhzc%2FGWwxVe7yWK88xj%2F8LEMo9%2BOBbM9DpMFhEyrZgmRIRxvmevqFLAfNbaUfxf6951ze4vvQ4Dz0XjbljQE8TkgXrjZQUX%2FdG%2BxFVBXxPCAZMImT%2FM4GOqUBOO%2FfzQQw0r5y6zQN9tkWgU3wFKLcVKJsfsY3%2F8xbCbPYfPT%2F3EYb00z6D5ykirjflQ7uOcbO5uL7r3SXVrqncPRQHKykHLDxAYMDxu2%2FEOvf8FffaH8Vh6JyuiisqxQnedswKQDdrf8TyCszV29C324MjSP6ERjC%2FXOWsAfuroGyy4%2FqGr%2FzB6%2BVSK7kl80jyuTyeInKAlHK5vjbk7chAjmVr2rh&X-Amz-Signature=2e61a29c739b4c809231eec09fe381e81322190256cec7929d77ce69485d6537&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O6AFONT%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbgEtgtasfWmb4ulYU7LCCe7wBLtvR9YmE19Ykx%2BONMAIgeSJzx9DiNGev69uIN%2BfIyEO3tMWZbOCfN6eojmuSrT8qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkLcXS8uTCuGDGAoircAyw39setECN8n34f36dZyhbxTVodGXNHM67UX%2Be2HsNs%2Bh0K2aOqzrVfUqgPA%2BzYmCikqxlOMViqRkXwLG92uk9Fh%2BV0fOOWFGL8dpaRCgmtYZ%2BctPeXCmZ6N3DRxRpnkQa%2FDSiOtLwKPz31AwQj0NguaY89pebmPHPna0Xkw%2B2MtJ30FksbL2uI6z%2FXRCDCAvdE1FWO2ZnryWc2oIDJFOK9JuwpJ0WdeNfQ2c2r01lwrriIEFMLkmofudIgBfdbYmgSD03lb5SK1Zw6PpahSoSX3E%2FJRehiCg5JAdVo3ftOGmEKAdFNUbByK9pOv7VWbS3c63i1tgOQ0futZJQ5Ue87SE04iKgewhT0P7sE5iBrba7EXr6EzsK5quCuOBmLS1ulw1uHV25ZlhuRgwhWdZx38rpa%2Bq%2BdJ8wwc%2B2lbem05bG3z9i1S5uihYPr4taF4%2Bxro7wIcYV4bg295i73KAMDeQCWGUuVP7x0fa0vVXtVxMqj%2BHpsi667w%2BaxgmEhIQb2SA12nalK7JaFhzc%2FGWwxVe7yWK88xj%2F8LEMo9%2BOBbM9DpMFhEyrZgmRIRxvmevqFLAfNbaUfxf6951ze4vvQ4Dz0XjbljQE8TkgXrjZQUX%2FdG%2BxFVBXxPCAZMImT%2FM4GOqUBOO%2FfzQQw0r5y6zQN9tkWgU3wFKLcVKJsfsY3%2F8xbCbPYfPT%2F3EYb00z6D5ykirjflQ7uOcbO5uL7r3SXVrqncPRQHKykHLDxAYMDxu2%2FEOvf8FffaH8Vh6JyuiisqxQnedswKQDdrf8TyCszV29C324MjSP6ERjC%2FXOWsAfuroGyy4%2FqGr%2FzB6%2BVSK7kl80jyuTyeInKAlHK5vjbk7chAjmVr2rh&X-Amz-Signature=057a15158d4a66aee0c587b87884307fe6b36e651818b8d13bc5b8c9f0971052&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O6AFONT%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbgEtgtasfWmb4ulYU7LCCe7wBLtvR9YmE19Ykx%2BONMAIgeSJzx9DiNGev69uIN%2BfIyEO3tMWZbOCfN6eojmuSrT8qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkLcXS8uTCuGDGAoircAyw39setECN8n34f36dZyhbxTVodGXNHM67UX%2Be2HsNs%2Bh0K2aOqzrVfUqgPA%2BzYmCikqxlOMViqRkXwLG92uk9Fh%2BV0fOOWFGL8dpaRCgmtYZ%2BctPeXCmZ6N3DRxRpnkQa%2FDSiOtLwKPz31AwQj0NguaY89pebmPHPna0Xkw%2B2MtJ30FksbL2uI6z%2FXRCDCAvdE1FWO2ZnryWc2oIDJFOK9JuwpJ0WdeNfQ2c2r01lwrriIEFMLkmofudIgBfdbYmgSD03lb5SK1Zw6PpahSoSX3E%2FJRehiCg5JAdVo3ftOGmEKAdFNUbByK9pOv7VWbS3c63i1tgOQ0futZJQ5Ue87SE04iKgewhT0P7sE5iBrba7EXr6EzsK5quCuOBmLS1ulw1uHV25ZlhuRgwhWdZx38rpa%2Bq%2BdJ8wwc%2B2lbem05bG3z9i1S5uihYPr4taF4%2Bxro7wIcYV4bg295i73KAMDeQCWGUuVP7x0fa0vVXtVxMqj%2BHpsi667w%2BaxgmEhIQb2SA12nalK7JaFhzc%2FGWwxVe7yWK88xj%2F8LEMo9%2BOBbM9DpMFhEyrZgmRIRxvmevqFLAfNbaUfxf6951ze4vvQ4Dz0XjbljQE8TkgXrjZQUX%2FdG%2BxFVBXxPCAZMImT%2FM4GOqUBOO%2FfzQQw0r5y6zQN9tkWgU3wFKLcVKJsfsY3%2F8xbCbPYfPT%2F3EYb00z6D5ykirjflQ7uOcbO5uL7r3SXVrqncPRQHKykHLDxAYMDxu2%2FEOvf8FffaH8Vh6JyuiisqxQnedswKQDdrf8TyCszV29C324MjSP6ERjC%2FXOWsAfuroGyy4%2FqGr%2FzB6%2BVSK7kl80jyuTyeInKAlHK5vjbk7chAjmVr2rh&X-Amz-Signature=b9dc53d2fe02bd70dbe2171aeb5715fa4f6b615c202215a0b7d87f66a3e21f5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

