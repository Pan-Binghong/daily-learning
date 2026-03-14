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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QILDG555%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyzykx4zm7KwbylcyKFPawH6paTfWWAZX0sI4C5hwXEwIhAPQf3W73OfeX7XQclIkoI7nv66fxj9H%2FGzGZP0Tjd0jQKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSYfPrmtjqeMydOhYq3AMWrLjTupPduTQiUtuIio1j2pUXhOfeicWpAlxzTxUsv4ktw26MhfcbNLJVa4%2Flioxvej86sN2JLcKcywWcQkAq%2FVuOkc1T0ikT512lJvEZEPE4SKuA0cxMWl2rijTt%2FMVlkWTcrqMJG%2Beudqd1OHKhc13KNakNmh5Su4FGVk5%2BpnEzGE6K%2FpIozkBspWE4ePUrirQKyyxa%2BSjaxtX%2FlBFt4k7ywD224BwTNVjQP4q8729gDlG%2BNoAieTbWxqMbezkebTyz4TB0%2FEhObDshdvAB1WpitOe%2F8%2Bzm%2FzjzDf35L%2FAhuIPISgpce7xA%2BSKitLfa3RKrJF7hzN5dia080eGfAdUeWYfdA4tq%2BbC9N3T9hD3iWY1GjbvX1Gv4cJn9S4UmnalO0QFD%2Fewi3b3J2%2F%2Brygt5Uw7TJ5IUb6qkNVdHKx3os4avWS6T6O0UJ2oHBVGLnb51MuOKNqXO0ietQ5c0NakxF3oJHoiHuEmKP62kvJaOkmuufxlDJo4UD1EBYkJ8hB%2BTj3riUiO4OOSa40TQ11umfi%2B%2BluzxWD9Mr%2F2%2BICuCPFsEypaw8Y5db8M4vcziJSX0X4n6Z4%2FxkNNsHdpceKXEL5Ssz7BUDKFTQSLR9Yxs1TRatNdo7nG0LzCDg9PNBjqkAXkOqAmxPNDZ7cg38pqGDXgx7zJWgrVDAJTCOqa6BXhKmuaTgCoar8d5QIQB3aDC%2FdOGbWK%2FU%2BJlF96jKO8ubDvCEnLq2TlCV%2FuoLGR7Z0754Gl%2BfaYdRCJR89Yyu4iMrFPrciv742znkkV7AZEM%2Ff2ay%2F4zurK2tnklMjMJz%2BGgK8GP2cPspMxm%2FMfAO8E2%2Fzw1SgF0tPfSh2ON5k%2Bt1DzJDGPS&X-Amz-Signature=e550bae79903dc25d90c06127dce7c8bb78215882049415aacc8c050c0605e71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QILDG555%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyzykx4zm7KwbylcyKFPawH6paTfWWAZX0sI4C5hwXEwIhAPQf3W73OfeX7XQclIkoI7nv66fxj9H%2FGzGZP0Tjd0jQKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSYfPrmtjqeMydOhYq3AMWrLjTupPduTQiUtuIio1j2pUXhOfeicWpAlxzTxUsv4ktw26MhfcbNLJVa4%2Flioxvej86sN2JLcKcywWcQkAq%2FVuOkc1T0ikT512lJvEZEPE4SKuA0cxMWl2rijTt%2FMVlkWTcrqMJG%2Beudqd1OHKhc13KNakNmh5Su4FGVk5%2BpnEzGE6K%2FpIozkBspWE4ePUrirQKyyxa%2BSjaxtX%2FlBFt4k7ywD224BwTNVjQP4q8729gDlG%2BNoAieTbWxqMbezkebTyz4TB0%2FEhObDshdvAB1WpitOe%2F8%2Bzm%2FzjzDf35L%2FAhuIPISgpce7xA%2BSKitLfa3RKrJF7hzN5dia080eGfAdUeWYfdA4tq%2BbC9N3T9hD3iWY1GjbvX1Gv4cJn9S4UmnalO0QFD%2Fewi3b3J2%2F%2Brygt5Uw7TJ5IUb6qkNVdHKx3os4avWS6T6O0UJ2oHBVGLnb51MuOKNqXO0ietQ5c0NakxF3oJHoiHuEmKP62kvJaOkmuufxlDJo4UD1EBYkJ8hB%2BTj3riUiO4OOSa40TQ11umfi%2B%2BluzxWD9Mr%2F2%2BICuCPFsEypaw8Y5db8M4vcziJSX0X4n6Z4%2FxkNNsHdpceKXEL5Ssz7BUDKFTQSLR9Yxs1TRatNdo7nG0LzCDg9PNBjqkAXkOqAmxPNDZ7cg38pqGDXgx7zJWgrVDAJTCOqa6BXhKmuaTgCoar8d5QIQB3aDC%2FdOGbWK%2FU%2BJlF96jKO8ubDvCEnLq2TlCV%2FuoLGR7Z0754Gl%2BfaYdRCJR89Yyu4iMrFPrciv742znkkV7AZEM%2Ff2ay%2F4zurK2tnklMjMJz%2BGgK8GP2cPspMxm%2FMfAO8E2%2Fzw1SgF0tPfSh2ON5k%2Bt1DzJDGPS&X-Amz-Signature=ea4b869d2fa5f7cb81b8da586061014e67ec9c9ec2ec0e986159cee9b3773f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QILDG555%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyzykx4zm7KwbylcyKFPawH6paTfWWAZX0sI4C5hwXEwIhAPQf3W73OfeX7XQclIkoI7nv66fxj9H%2FGzGZP0Tjd0jQKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSYfPrmtjqeMydOhYq3AMWrLjTupPduTQiUtuIio1j2pUXhOfeicWpAlxzTxUsv4ktw26MhfcbNLJVa4%2Flioxvej86sN2JLcKcywWcQkAq%2FVuOkc1T0ikT512lJvEZEPE4SKuA0cxMWl2rijTt%2FMVlkWTcrqMJG%2Beudqd1OHKhc13KNakNmh5Su4FGVk5%2BpnEzGE6K%2FpIozkBspWE4ePUrirQKyyxa%2BSjaxtX%2FlBFt4k7ywD224BwTNVjQP4q8729gDlG%2BNoAieTbWxqMbezkebTyz4TB0%2FEhObDshdvAB1WpitOe%2F8%2Bzm%2FzjzDf35L%2FAhuIPISgpce7xA%2BSKitLfa3RKrJF7hzN5dia080eGfAdUeWYfdA4tq%2BbC9N3T9hD3iWY1GjbvX1Gv4cJn9S4UmnalO0QFD%2Fewi3b3J2%2F%2Brygt5Uw7TJ5IUb6qkNVdHKx3os4avWS6T6O0UJ2oHBVGLnb51MuOKNqXO0ietQ5c0NakxF3oJHoiHuEmKP62kvJaOkmuufxlDJo4UD1EBYkJ8hB%2BTj3riUiO4OOSa40TQ11umfi%2B%2BluzxWD9Mr%2F2%2BICuCPFsEypaw8Y5db8M4vcziJSX0X4n6Z4%2FxkNNsHdpceKXEL5Ssz7BUDKFTQSLR9Yxs1TRatNdo7nG0LzCDg9PNBjqkAXkOqAmxPNDZ7cg38pqGDXgx7zJWgrVDAJTCOqa6BXhKmuaTgCoar8d5QIQB3aDC%2FdOGbWK%2FU%2BJlF96jKO8ubDvCEnLq2TlCV%2FuoLGR7Z0754Gl%2BfaYdRCJR89Yyu4iMrFPrciv742znkkV7AZEM%2Ff2ay%2F4zurK2tnklMjMJz%2BGgK8GP2cPspMxm%2FMfAO8E2%2Fzw1SgF0tPfSh2ON5k%2Bt1DzJDGPS&X-Amz-Signature=2a1c64f66d9c659beef5850479303aa74e34636aace2abe8ce87f675ba607626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

