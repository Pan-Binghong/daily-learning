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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TYFZ2KT%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICeSXjlpB%2B%2B1G4uAZf%2FL0qRQ8THGR2AeqyQIR7Ufzb60AiEAkyX66uQeAYeIb1uwKNhacT8nzjGxIHxJCuHd%2FJOaecgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDPGxaFACJv2M3FtR6CrcA%2FX67P%2BlxrJEEsv2zn3oHAPehWS5RxirYfvc%2BS78nZRRN5GPi%2F%2Fs7cohxnNDTOFu2iX8nOAEns71lwD3RbwZ2%2BqENVygB8AAqV0BhjRW%2FKsa3%2B%2FPF180cqRauJl97Y7%2BzhwfGH4qUWkMFcnNYsL9EnI9Css45fISqYH3u6K%2BRxTsjajeELwBY%2BeO1vMXCs0IOKtjQxhc0BC2StSslOfxJieGtcMe2weGHT3zYMzp9imgwxZVJf7vzRx%2Bo%2F0%2BqGYNQQtRP%2BVLQLdvGKKyVLHQeKAC0%2BzZLLDasUrDj4jKJNzXp96dPPIAGKam7TFHa9vASsy0l3hKTXi2v1t23MIV9KrnP71Ec8cOQY9gtcYKqifE7M6zpAqsphEeIb2pllG7%2FaS%2BsCpzdcyndSO%2F4pd%2FEzPAdM0BHx5pIpv8c8aDjbVl3xeUwByR5R1%2BFK8xyE3U5qFH%2BqJTltp%2BgzU%2FNPmuOzcEKsSVoXa9sQfH3jaDvg0ybwTcAqIPmHVcRco8z77x%2FfhbgNQJ%2BfaUjJ7m2qHBrPpTw7FPUHmKaoIbmZPxl0rnB5F5uKi7gmQdWXHRz%2FeAp%2FAFAFHCh1iDBYKPqYMF5TWjDjzDUL4ezn%2FA8Z8iKFZzzkYnOvLRHKWbVl3JMIrApssGOqUBM09wHUqglSWJVcZdHl9qmAKpNs3VcSJjyp1pelR2VB5u%2BuGCkMCCO%2F8JXkFulqV3pc5MchY1EcNJl1rEO67sTBepsG3%2FhaWdldlsKZ2MMXe0YmZceNs2m09UV6sMT3oRFiWuHT3qNt0BYcAuqqI7ER7OXDDMieStHn8%2F%2BViaVlYQ15WGqVJD%2BIs6Y%2BFcA4JRwebKWMp8Xh2eUPwrjPcd4rH%2Bp4Co&X-Amz-Signature=e572dcac38ef5b090b0dac9da8640670d52a59c6e47409fa499dad7cd749f3db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TYFZ2KT%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICeSXjlpB%2B%2B1G4uAZf%2FL0qRQ8THGR2AeqyQIR7Ufzb60AiEAkyX66uQeAYeIb1uwKNhacT8nzjGxIHxJCuHd%2FJOaecgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDPGxaFACJv2M3FtR6CrcA%2FX67P%2BlxrJEEsv2zn3oHAPehWS5RxirYfvc%2BS78nZRRN5GPi%2F%2Fs7cohxnNDTOFu2iX8nOAEns71lwD3RbwZ2%2BqENVygB8AAqV0BhjRW%2FKsa3%2B%2FPF180cqRauJl97Y7%2BzhwfGH4qUWkMFcnNYsL9EnI9Css45fISqYH3u6K%2BRxTsjajeELwBY%2BeO1vMXCs0IOKtjQxhc0BC2StSslOfxJieGtcMe2weGHT3zYMzp9imgwxZVJf7vzRx%2Bo%2F0%2BqGYNQQtRP%2BVLQLdvGKKyVLHQeKAC0%2BzZLLDasUrDj4jKJNzXp96dPPIAGKam7TFHa9vASsy0l3hKTXi2v1t23MIV9KrnP71Ec8cOQY9gtcYKqifE7M6zpAqsphEeIb2pllG7%2FaS%2BsCpzdcyndSO%2F4pd%2FEzPAdM0BHx5pIpv8c8aDjbVl3xeUwByR5R1%2BFK8xyE3U5qFH%2BqJTltp%2BgzU%2FNPmuOzcEKsSVoXa9sQfH3jaDvg0ybwTcAqIPmHVcRco8z77x%2FfhbgNQJ%2BfaUjJ7m2qHBrPpTw7FPUHmKaoIbmZPxl0rnB5F5uKi7gmQdWXHRz%2FeAp%2FAFAFHCh1iDBYKPqYMF5TWjDjzDUL4ezn%2FA8Z8iKFZzzkYnOvLRHKWbVl3JMIrApssGOqUBM09wHUqglSWJVcZdHl9qmAKpNs3VcSJjyp1pelR2VB5u%2BuGCkMCCO%2F8JXkFulqV3pc5MchY1EcNJl1rEO67sTBepsG3%2FhaWdldlsKZ2MMXe0YmZceNs2m09UV6sMT3oRFiWuHT3qNt0BYcAuqqI7ER7OXDDMieStHn8%2F%2BViaVlYQ15WGqVJD%2BIs6Y%2BFcA4JRwebKWMp8Xh2eUPwrjPcd4rH%2Bp4Co&X-Amz-Signature=d81c98b908e730347c1d76096cf39891aa533cc4a7ce88518a8d52b8ced044c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TYFZ2KT%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICeSXjlpB%2B%2B1G4uAZf%2FL0qRQ8THGR2AeqyQIR7Ufzb60AiEAkyX66uQeAYeIb1uwKNhacT8nzjGxIHxJCuHd%2FJOaecgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDPGxaFACJv2M3FtR6CrcA%2FX67P%2BlxrJEEsv2zn3oHAPehWS5RxirYfvc%2BS78nZRRN5GPi%2F%2Fs7cohxnNDTOFu2iX8nOAEns71lwD3RbwZ2%2BqENVygB8AAqV0BhjRW%2FKsa3%2B%2FPF180cqRauJl97Y7%2BzhwfGH4qUWkMFcnNYsL9EnI9Css45fISqYH3u6K%2BRxTsjajeELwBY%2BeO1vMXCs0IOKtjQxhc0BC2StSslOfxJieGtcMe2weGHT3zYMzp9imgwxZVJf7vzRx%2Bo%2F0%2BqGYNQQtRP%2BVLQLdvGKKyVLHQeKAC0%2BzZLLDasUrDj4jKJNzXp96dPPIAGKam7TFHa9vASsy0l3hKTXi2v1t23MIV9KrnP71Ec8cOQY9gtcYKqifE7M6zpAqsphEeIb2pllG7%2FaS%2BsCpzdcyndSO%2F4pd%2FEzPAdM0BHx5pIpv8c8aDjbVl3xeUwByR5R1%2BFK8xyE3U5qFH%2BqJTltp%2BgzU%2FNPmuOzcEKsSVoXa9sQfH3jaDvg0ybwTcAqIPmHVcRco8z77x%2FfhbgNQJ%2BfaUjJ7m2qHBrPpTw7FPUHmKaoIbmZPxl0rnB5F5uKi7gmQdWXHRz%2FeAp%2FAFAFHCh1iDBYKPqYMF5TWjDjzDUL4ezn%2FA8Z8iKFZzzkYnOvLRHKWbVl3JMIrApssGOqUBM09wHUqglSWJVcZdHl9qmAKpNs3VcSJjyp1pelR2VB5u%2BuGCkMCCO%2F8JXkFulqV3pc5MchY1EcNJl1rEO67sTBepsG3%2FhaWdldlsKZ2MMXe0YmZceNs2m09UV6sMT3oRFiWuHT3qNt0BYcAuqqI7ER7OXDDMieStHn8%2F%2BViaVlYQ15WGqVJD%2BIs6Y%2BFcA4JRwebKWMp8Xh2eUPwrjPcd4rH%2Bp4Co&X-Amz-Signature=3a96506d0b634a6976c37aad998d9701e05ca01a1be83bd58311237dd5dd5f71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

