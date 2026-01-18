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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTA6JOL%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBG1Lpz%2F7Qqwu0GHYAgXzCot7njGZMX0CQb%2FrdtrYBTgAiEAh9dDa%2B8JZICrpKIzCGoZKh860ZvDmoJds5fxd28hQNwq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIsfRuRJ1gcxI618UCrcA8H3A1TgQvMfIKx36zBH5aSvxxH79YGOqsnosKcshaDhOSvl5KeZtTEU4ciY7sTZg%2B%2BKwDDyTQHRENKcTxObueh%2B4smTsKtxUKVPAtalGUJZ047sF3xTxvtfIIDCWsTUISGlmJe0UEQlSqQVkp5Zv4%2Fl14xz5tlTLX3AqYeqHVdkcO%2FnnP3Kka8QlZ7%2FzAJSTOyGLeV%2FBjIrv%2BUDolRaS8%2FXjjNs%2F1tCRbz6Y52DyJ4vFTXMOAVvR2jht8Q9m0vt8upJkYVRPYhoPNUpVVRhTiNKEuGRpoCfFqlwI%2Fi8rKzQZWvTJtQE%2FzhOZFvgZcVviMlgh5WuopGrIgbkj5LAmuyO%2B9e%2BQmR9pBwLuFgeHpCj5bMQSYCN3OgPGWE5SKUky7HJXU1yjKriym7djbTKwfc0QgOKl%2FQrJAvYynKzii9IamRd8hekR3BstqfjTJG6z2Ow1Yjik%2FMcbFuIwZBby7Bz1AgChdrZ4zYczq0xeP4rbDhbyzZ%2BiZZmE4%2FYLdTfJQry5Ww1N2TbX1fm4ewNWquWjfrGaVeg5vbO%2Bm4P11CAENT8L%2FnNxq5kI3NMjog0cVLoLr7ZsfhhHAjmEcn9i5A9bXvGqa%2BiqVuhaxymUgNlO%2BB1nwb818QpoCyFMKGCscsGOqUBTQe6fOL8bk%2B0KvoMgOOcZMslp02Lnbbebc%2FJ5lXKf%2Fk0PoSZjco2EZAaj%2BjMs2eJxErUxIBdLHGUjoVOYwv9tqv2dvkXkogwISDQ1iqivqjjAp0eVXydMlxexloqTmyJ7TBVpSZ2K0L1ZRnDO0YdEdj%2FqdHVit6f1HNR%2BsC4CoJSMFWR%2Fi%2BoEzno%2FOMbkiNarWuR53AvWB0y2U9v3ZituyHMxAUY&X-Amz-Signature=cd084ade7dfaf417259cc962ed9321bde58c5a9acbeaee69f2da3752cebf96df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTA6JOL%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBG1Lpz%2F7Qqwu0GHYAgXzCot7njGZMX0CQb%2FrdtrYBTgAiEAh9dDa%2B8JZICrpKIzCGoZKh860ZvDmoJds5fxd28hQNwq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIsfRuRJ1gcxI618UCrcA8H3A1TgQvMfIKx36zBH5aSvxxH79YGOqsnosKcshaDhOSvl5KeZtTEU4ciY7sTZg%2B%2BKwDDyTQHRENKcTxObueh%2B4smTsKtxUKVPAtalGUJZ047sF3xTxvtfIIDCWsTUISGlmJe0UEQlSqQVkp5Zv4%2Fl14xz5tlTLX3AqYeqHVdkcO%2FnnP3Kka8QlZ7%2FzAJSTOyGLeV%2FBjIrv%2BUDolRaS8%2FXjjNs%2F1tCRbz6Y52DyJ4vFTXMOAVvR2jht8Q9m0vt8upJkYVRPYhoPNUpVVRhTiNKEuGRpoCfFqlwI%2Fi8rKzQZWvTJtQE%2FzhOZFvgZcVviMlgh5WuopGrIgbkj5LAmuyO%2B9e%2BQmR9pBwLuFgeHpCj5bMQSYCN3OgPGWE5SKUky7HJXU1yjKriym7djbTKwfc0QgOKl%2FQrJAvYynKzii9IamRd8hekR3BstqfjTJG6z2Ow1Yjik%2FMcbFuIwZBby7Bz1AgChdrZ4zYczq0xeP4rbDhbyzZ%2BiZZmE4%2FYLdTfJQry5Ww1N2TbX1fm4ewNWquWjfrGaVeg5vbO%2Bm4P11CAENT8L%2FnNxq5kI3NMjog0cVLoLr7ZsfhhHAjmEcn9i5A9bXvGqa%2BiqVuhaxymUgNlO%2BB1nwb818QpoCyFMKGCscsGOqUBTQe6fOL8bk%2B0KvoMgOOcZMslp02Lnbbebc%2FJ5lXKf%2Fk0PoSZjco2EZAaj%2BjMs2eJxErUxIBdLHGUjoVOYwv9tqv2dvkXkogwISDQ1iqivqjjAp0eVXydMlxexloqTmyJ7TBVpSZ2K0L1ZRnDO0YdEdj%2FqdHVit6f1HNR%2BsC4CoJSMFWR%2Fi%2BoEzno%2FOMbkiNarWuR53AvWB0y2U9v3ZituyHMxAUY&X-Amz-Signature=1279a5ff545430b0b6463ab67cbd33685a9f5c01e6dfc0cdbfae6719606b80c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTA6JOL%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBG1Lpz%2F7Qqwu0GHYAgXzCot7njGZMX0CQb%2FrdtrYBTgAiEAh9dDa%2B8JZICrpKIzCGoZKh860ZvDmoJds5fxd28hQNwq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIsfRuRJ1gcxI618UCrcA8H3A1TgQvMfIKx36zBH5aSvxxH79YGOqsnosKcshaDhOSvl5KeZtTEU4ciY7sTZg%2B%2BKwDDyTQHRENKcTxObueh%2B4smTsKtxUKVPAtalGUJZ047sF3xTxvtfIIDCWsTUISGlmJe0UEQlSqQVkp5Zv4%2Fl14xz5tlTLX3AqYeqHVdkcO%2FnnP3Kka8QlZ7%2FzAJSTOyGLeV%2FBjIrv%2BUDolRaS8%2FXjjNs%2F1tCRbz6Y52DyJ4vFTXMOAVvR2jht8Q9m0vt8upJkYVRPYhoPNUpVVRhTiNKEuGRpoCfFqlwI%2Fi8rKzQZWvTJtQE%2FzhOZFvgZcVviMlgh5WuopGrIgbkj5LAmuyO%2B9e%2BQmR9pBwLuFgeHpCj5bMQSYCN3OgPGWE5SKUky7HJXU1yjKriym7djbTKwfc0QgOKl%2FQrJAvYynKzii9IamRd8hekR3BstqfjTJG6z2Ow1Yjik%2FMcbFuIwZBby7Bz1AgChdrZ4zYczq0xeP4rbDhbyzZ%2BiZZmE4%2FYLdTfJQry5Ww1N2TbX1fm4ewNWquWjfrGaVeg5vbO%2Bm4P11CAENT8L%2FnNxq5kI3NMjog0cVLoLr7ZsfhhHAjmEcn9i5A9bXvGqa%2BiqVuhaxymUgNlO%2BB1nwb818QpoCyFMKGCscsGOqUBTQe6fOL8bk%2B0KvoMgOOcZMslp02Lnbbebc%2FJ5lXKf%2Fk0PoSZjco2EZAaj%2BjMs2eJxErUxIBdLHGUjoVOYwv9tqv2dvkXkogwISDQ1iqivqjjAp0eVXydMlxexloqTmyJ7TBVpSZ2K0L1ZRnDO0YdEdj%2FqdHVit6f1HNR%2BsC4CoJSMFWR%2Fi%2BoEzno%2FOMbkiNarWuR53AvWB0y2U9v3ZituyHMxAUY&X-Amz-Signature=3a71d632df29596b173c3118382382ec0d6a644237d155c33beee917eb021d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

