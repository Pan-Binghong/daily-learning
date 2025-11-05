---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AV2LOTW%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDe6g1udrWwybksjbnD018u0w4d7fNtOeyV3wtLGisQAiBz4EYcybuHJxBm9ZYqZzb3ftk7DHBVEEaglmTgSlTHoiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCDmfkwAdUKRnVvUdKtwD6s9TE0le%2Bnu8aIVeh0Yb1Slmzme%2BU4XCV2WiEYZ6Ge1pFcZ2%2Fmcg2rKV1p2jtwf3w01rt48mjpoPscTrE0IFFeHKqx6e1N4nfbMbIVixiWtq%2Fwzh%2FZvWuBidosIXtXA6UPm%2BVdr10xtlH0EC3j1u5n1L%2B3HJ%2BgYruqduJAMT5zhhw87QBr%2FUu4Ok9eR4%2BR4WlILya5ZRf77wfFyvRNx7FmCwkpkq22W7eCeGcHMVHGKOwmeg0YseKfQ6jGVLruUsAdrdos1WJx%2BIjFEXCRWu9yO2D76cbyKjK23jxFFCIjHEzCBlaoxU4P6yWqcVvzXlAmbOdlOg3YJVmYMHRvqvRMVPK4mE5e3DXRBqZbMcDVnSPHRqt8nFmNy77LSab7ptSnMP7hYcyycYO3uGY3%2B2XEwwEiBiBVt0owJ5HgrndO1fGMldhS9vdSzjDDzMiu8OA54ydmuyUWyGRA%2F4MOEWXdBL2XJILqqTRPAwkkZd2BoAZq47olFoHzf1f6Tdx6i4Rv9r71XkieSTEqOsyG4%2B8RLj%2F4NbRBqTceBMO%2BDs33iFbl4m9pS4I0jqZOxihYcWy1NAr0WcLWGm99l%2BqWWRUQy1rFIiUeojrnl9qSQJz0%2BBWOrU7VeObLsaJz8wiaOsyAY6pgHGBJqrccudoezesWNXsxpbTph%2Fm%2Bm3j8FQZ3bvYbHzKnTtlg1AQxWUZhci2aKTFnTsO7QKxS0zyCNsORMO47QYu7BhGNvvOZmoO0IEpYJ2plTQMFkARrcOLMEiueqav0ANny23iZ9s9QLudz1iBr7jLGNRIKBHujs1rh4H66itBtJvtKsEHT%2B5bve26Tj%2BupdMTF3Sx5t3H6rAfciPE%2FPYUOU2IzNm&X-Amz-Signature=3eb1b0777f6612bd7d8c21756a031fdf863cd5808ed3dd7738bc3ad7a1b9c6d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AV2LOTW%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDe6g1udrWwybksjbnD018u0w4d7fNtOeyV3wtLGisQAiBz4EYcybuHJxBm9ZYqZzb3ftk7DHBVEEaglmTgSlTHoiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCDmfkwAdUKRnVvUdKtwD6s9TE0le%2Bnu8aIVeh0Yb1Slmzme%2BU4XCV2WiEYZ6Ge1pFcZ2%2Fmcg2rKV1p2jtwf3w01rt48mjpoPscTrE0IFFeHKqx6e1N4nfbMbIVixiWtq%2Fwzh%2FZvWuBidosIXtXA6UPm%2BVdr10xtlH0EC3j1u5n1L%2B3HJ%2BgYruqduJAMT5zhhw87QBr%2FUu4Ok9eR4%2BR4WlILya5ZRf77wfFyvRNx7FmCwkpkq22W7eCeGcHMVHGKOwmeg0YseKfQ6jGVLruUsAdrdos1WJx%2BIjFEXCRWu9yO2D76cbyKjK23jxFFCIjHEzCBlaoxU4P6yWqcVvzXlAmbOdlOg3YJVmYMHRvqvRMVPK4mE5e3DXRBqZbMcDVnSPHRqt8nFmNy77LSab7ptSnMP7hYcyycYO3uGY3%2B2XEwwEiBiBVt0owJ5HgrndO1fGMldhS9vdSzjDDzMiu8OA54ydmuyUWyGRA%2F4MOEWXdBL2XJILqqTRPAwkkZd2BoAZq47olFoHzf1f6Tdx6i4Rv9r71XkieSTEqOsyG4%2B8RLj%2F4NbRBqTceBMO%2BDs33iFbl4m9pS4I0jqZOxihYcWy1NAr0WcLWGm99l%2BqWWRUQy1rFIiUeojrnl9qSQJz0%2BBWOrU7VeObLsaJz8wiaOsyAY6pgHGBJqrccudoezesWNXsxpbTph%2Fm%2Bm3j8FQZ3bvYbHzKnTtlg1AQxWUZhci2aKTFnTsO7QKxS0zyCNsORMO47QYu7BhGNvvOZmoO0IEpYJ2plTQMFkARrcOLMEiueqav0ANny23iZ9s9QLudz1iBr7jLGNRIKBHujs1rh4H66itBtJvtKsEHT%2B5bve26Tj%2BupdMTF3Sx5t3H6rAfciPE%2FPYUOU2IzNm&X-Amz-Signature=aa74cf2cf07e7ab763e620c99fccd679e0ecb89abc3b720e863df3256614d0f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AV2LOTW%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDe6g1udrWwybksjbnD018u0w4d7fNtOeyV3wtLGisQAiBz4EYcybuHJxBm9ZYqZzb3ftk7DHBVEEaglmTgSlTHoiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCDmfkwAdUKRnVvUdKtwD6s9TE0le%2Bnu8aIVeh0Yb1Slmzme%2BU4XCV2WiEYZ6Ge1pFcZ2%2Fmcg2rKV1p2jtwf3w01rt48mjpoPscTrE0IFFeHKqx6e1N4nfbMbIVixiWtq%2Fwzh%2FZvWuBidosIXtXA6UPm%2BVdr10xtlH0EC3j1u5n1L%2B3HJ%2BgYruqduJAMT5zhhw87QBr%2FUu4Ok9eR4%2BR4WlILya5ZRf77wfFyvRNx7FmCwkpkq22W7eCeGcHMVHGKOwmeg0YseKfQ6jGVLruUsAdrdos1WJx%2BIjFEXCRWu9yO2D76cbyKjK23jxFFCIjHEzCBlaoxU4P6yWqcVvzXlAmbOdlOg3YJVmYMHRvqvRMVPK4mE5e3DXRBqZbMcDVnSPHRqt8nFmNy77LSab7ptSnMP7hYcyycYO3uGY3%2B2XEwwEiBiBVt0owJ5HgrndO1fGMldhS9vdSzjDDzMiu8OA54ydmuyUWyGRA%2F4MOEWXdBL2XJILqqTRPAwkkZd2BoAZq47olFoHzf1f6Tdx6i4Rv9r71XkieSTEqOsyG4%2B8RLj%2F4NbRBqTceBMO%2BDs33iFbl4m9pS4I0jqZOxihYcWy1NAr0WcLWGm99l%2BqWWRUQy1rFIiUeojrnl9qSQJz0%2BBWOrU7VeObLsaJz8wiaOsyAY6pgHGBJqrccudoezesWNXsxpbTph%2Fm%2Bm3j8FQZ3bvYbHzKnTtlg1AQxWUZhci2aKTFnTsO7QKxS0zyCNsORMO47QYu7BhGNvvOZmoO0IEpYJ2plTQMFkARrcOLMEiueqav0ANny23iZ9s9QLudz1iBr7jLGNRIKBHujs1rh4H66itBtJvtKsEHT%2B5bve26Tj%2BupdMTF3Sx5t3H6rAfciPE%2FPYUOU2IzNm&X-Amz-Signature=03faae7f932c1171786f16de6e7ac1404484ab96738c98817b1a6d85c8097c0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

