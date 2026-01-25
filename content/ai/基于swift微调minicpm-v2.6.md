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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGF3YNXG%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIEy7WHZ829rK%2Bgjoa5RMi0SlU%2Fo3UVnAU5Jh2U26MMWNAiEA2mJRcLv8458ZADxUEMfWWG%2Bk8I24pAeSfLBj9%2FOw720q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDGHE8XB7%2Ffm0%2F6YQ7ircA4zf%2FVmozMz8NNRIc1kRjgEMjJ5HAQi4Lv2yo0soDJ6VBrsr6StcZofdqHKNRcfmFshpAh8kbEp5gSZU5wz%2BB5PPLMXrYTWsmjuiSTNI3VUEEuBY9G2Cja1797Md2FzKDXOp10bzzVdg3m5J%2FHGXTsvTj%2B%2F7L2IwLcUaJ4d5V3RnqF9GLXl80eaWFp6TR28breWvwSlucvTmcfp5r6tu3K2vRh22IMH6Zi7jUDyioQRX83OXiEFSH9TVaj3vesl4fkGeBBXhpynPEvs6vPSJt0CHGZvv2EvHga1ff1vzWvYLOYdZO%2FDYvX%2BilRUkb6DUH5ODcsB2vYN%2FtDS2orstMST%2F8jnro5NBxk5NFnCMBd0KQHBCoYm1EZOaGy9Wx3WJmD3tOz44y2%2FsHIlf9IGNxNRIO8BhCHuzNkLNaBcktOk2EW5WWYapLrJ%2F%2BeT8hNvgqAjQQLTGSkgNJ9iUcgTJiWgMzNUjtQrv%2Fvw80uC3dqIYOy%2F5FepHgz5O1dD%2F3smaiUSKv9jiej5SLQD%2BhbmUHcrtVaM2hA2O2O3x2MuFRwthgIc%2FldLZd5KgMiyGiUZkobHSf2mLVt3KITRqvE%2FM7raXSRCl63%2Bvr7bhfCuCXAz8cGg82biSPePX2Qe6MPCF1ssGOqUBZ9ZZ7SY0a0ka8lemuGhy5mUgWxATp1xz1YzGXNp%2F1k4zCCsPM28Q3yZLmk4OJ7IuL%2B4Bv5yDx3JLDwYr01mZLc1X7sr%2FnWO2tS0brPrQlK%2FuqF%2FJhUtQcUuVwmrcKrBqHbZSmFLIu5iLDvVaqVly9QA0IBQwTFJdFwx6IPMC6EkXY1aSoqn71JfUEwd3nAdytFkA5rNVn%2BQ7RumGNBPIwKyIVFkG&X-Amz-Signature=580cacc021577aca04756d5e9eedd201d015196e0af57a8869d8ab7a751d28df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGF3YNXG%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIEy7WHZ829rK%2Bgjoa5RMi0SlU%2Fo3UVnAU5Jh2U26MMWNAiEA2mJRcLv8458ZADxUEMfWWG%2Bk8I24pAeSfLBj9%2FOw720q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDGHE8XB7%2Ffm0%2F6YQ7ircA4zf%2FVmozMz8NNRIc1kRjgEMjJ5HAQi4Lv2yo0soDJ6VBrsr6StcZofdqHKNRcfmFshpAh8kbEp5gSZU5wz%2BB5PPLMXrYTWsmjuiSTNI3VUEEuBY9G2Cja1797Md2FzKDXOp10bzzVdg3m5J%2FHGXTsvTj%2B%2F7L2IwLcUaJ4d5V3RnqF9GLXl80eaWFp6TR28breWvwSlucvTmcfp5r6tu3K2vRh22IMH6Zi7jUDyioQRX83OXiEFSH9TVaj3vesl4fkGeBBXhpynPEvs6vPSJt0CHGZvv2EvHga1ff1vzWvYLOYdZO%2FDYvX%2BilRUkb6DUH5ODcsB2vYN%2FtDS2orstMST%2F8jnro5NBxk5NFnCMBd0KQHBCoYm1EZOaGy9Wx3WJmD3tOz44y2%2FsHIlf9IGNxNRIO8BhCHuzNkLNaBcktOk2EW5WWYapLrJ%2F%2BeT8hNvgqAjQQLTGSkgNJ9iUcgTJiWgMzNUjtQrv%2Fvw80uC3dqIYOy%2F5FepHgz5O1dD%2F3smaiUSKv9jiej5SLQD%2BhbmUHcrtVaM2hA2O2O3x2MuFRwthgIc%2FldLZd5KgMiyGiUZkobHSf2mLVt3KITRqvE%2FM7raXSRCl63%2Bvr7bhfCuCXAz8cGg82biSPePX2Qe6MPCF1ssGOqUBZ9ZZ7SY0a0ka8lemuGhy5mUgWxATp1xz1YzGXNp%2F1k4zCCsPM28Q3yZLmk4OJ7IuL%2B4Bv5yDx3JLDwYr01mZLc1X7sr%2FnWO2tS0brPrQlK%2FuqF%2FJhUtQcUuVwmrcKrBqHbZSmFLIu5iLDvVaqVly9QA0IBQwTFJdFwx6IPMC6EkXY1aSoqn71JfUEwd3nAdytFkA5rNVn%2BQ7RumGNBPIwKyIVFkG&X-Amz-Signature=0099e5b4cdd607a88c5a0628935e0b79930a16d7c12b759d990590f9a97ad88c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGF3YNXG%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIEy7WHZ829rK%2Bgjoa5RMi0SlU%2Fo3UVnAU5Jh2U26MMWNAiEA2mJRcLv8458ZADxUEMfWWG%2Bk8I24pAeSfLBj9%2FOw720q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDGHE8XB7%2Ffm0%2F6YQ7ircA4zf%2FVmozMz8NNRIc1kRjgEMjJ5HAQi4Lv2yo0soDJ6VBrsr6StcZofdqHKNRcfmFshpAh8kbEp5gSZU5wz%2BB5PPLMXrYTWsmjuiSTNI3VUEEuBY9G2Cja1797Md2FzKDXOp10bzzVdg3m5J%2FHGXTsvTj%2B%2F7L2IwLcUaJ4d5V3RnqF9GLXl80eaWFp6TR28breWvwSlucvTmcfp5r6tu3K2vRh22IMH6Zi7jUDyioQRX83OXiEFSH9TVaj3vesl4fkGeBBXhpynPEvs6vPSJt0CHGZvv2EvHga1ff1vzWvYLOYdZO%2FDYvX%2BilRUkb6DUH5ODcsB2vYN%2FtDS2orstMST%2F8jnro5NBxk5NFnCMBd0KQHBCoYm1EZOaGy9Wx3WJmD3tOz44y2%2FsHIlf9IGNxNRIO8BhCHuzNkLNaBcktOk2EW5WWYapLrJ%2F%2BeT8hNvgqAjQQLTGSkgNJ9iUcgTJiWgMzNUjtQrv%2Fvw80uC3dqIYOy%2F5FepHgz5O1dD%2F3smaiUSKv9jiej5SLQD%2BhbmUHcrtVaM2hA2O2O3x2MuFRwthgIc%2FldLZd5KgMiyGiUZkobHSf2mLVt3KITRqvE%2FM7raXSRCl63%2Bvr7bhfCuCXAz8cGg82biSPePX2Qe6MPCF1ssGOqUBZ9ZZ7SY0a0ka8lemuGhy5mUgWxATp1xz1YzGXNp%2F1k4zCCsPM28Q3yZLmk4OJ7IuL%2B4Bv5yDx3JLDwYr01mZLc1X7sr%2FnWO2tS0brPrQlK%2FuqF%2FJhUtQcUuVwmrcKrBqHbZSmFLIu5iLDvVaqVly9QA0IBQwTFJdFwx6IPMC6EkXY1aSoqn71JfUEwd3nAdytFkA5rNVn%2BQ7RumGNBPIwKyIVFkG&X-Amz-Signature=5b6472c11099717d582829a0f5299783bd494254bd9dd3d6e4453ac0ed029924&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

