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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHVV26IS%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9AYiWv0lWIj6p2VlmxjbulD%2BUMAN587nO0jKWX0LkVAiACGiqCYP2aNeXt14pUtQN9nAhZRtw5BpvW6B%2FczkB%2FGiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAu5AYMPE%2FHACcxiKtwDzjd3xwdC5ROQHl8HbsTI%2BXaT3fKAX04tIbM75vMNQoUIGkvs3zHjs19dTyJ23r%2BABbGww0y8nRgfka6OY4%2F9a4S9xOhIDqCJCzSHKy6wWd66Sw2NGOJjH8hfsEXWEpSc%2F6YYyFy%2FSeabkFddr8V1d0WOeWe6d%2B6IXns0hVkeOMYwYD2Fh2rkwz89%2Bq%2F4l1jUXh7I79pJQTfm4p%2BWGczxJwkOmJydardgV4BPtKfpyWdgwRNS02DhyASduzlH%2Fgy5oyoS4DvSdgPDDJTee0n8yYTb771qayJ8kvFY9RpjbOvBy3kxo4R0EOIK2EJaqBiDGJ%2ByYG9OkCNvBQzyksoAUlNv7%2FhCzRuvkcJPlcHP8FXMtoUk%2Bv%2FElI3qmGqlFmgFbbXjdE9Ho42semZL5iDrP9eShkT5p3TJQ1Ym3xabOJKE69fpV6uNSUVhOTr4M5Sy%2BmEeihrZVmO4%2BKmEF0tBYnrZ4RDaInEilBtWDf1UKGUC7sb7D2%2FWywh6j%2BVqUybHnpU4ASy5m8XMCpJgp2wlSCDVa%2B8Ru0NHmtNsfsBOYkaqo2hB662Rm79EwL8RsxE6zZSx2WC8a3g4kqy3bISTSVet7L1Hh7iWumyNMY6K9PYIzkPTFcshJJD9Gf4w4vCvyAY6pgE5Mg5m0MVegOmkPyb83WAKq9NxiybEj%2B8xnAmPwh3BYHitxCZJFV6e343mXcNbI31xSeXmPu6SkTyi3JfYkHa12NGT5T6dptpUtA%2FWxftHDBNn83Yn4uihwcXu%2BVwZzl9TpF1ec2z3ldCMUf0KufVQLyBU2V6yzlfduiKn4SU4lgtq5b9TwSuwqnk3alX6V8vssn39LBQVOzT1P4QBd2ol8xr1jCF4&X-Amz-Signature=8433b3b57cb9e3e3d72cfe35cb771fbacc7d3d709575c90f48fcc6b227589e51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHVV26IS%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9AYiWv0lWIj6p2VlmxjbulD%2BUMAN587nO0jKWX0LkVAiACGiqCYP2aNeXt14pUtQN9nAhZRtw5BpvW6B%2FczkB%2FGiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAu5AYMPE%2FHACcxiKtwDzjd3xwdC5ROQHl8HbsTI%2BXaT3fKAX04tIbM75vMNQoUIGkvs3zHjs19dTyJ23r%2BABbGww0y8nRgfka6OY4%2F9a4S9xOhIDqCJCzSHKy6wWd66Sw2NGOJjH8hfsEXWEpSc%2F6YYyFy%2FSeabkFddr8V1d0WOeWe6d%2B6IXns0hVkeOMYwYD2Fh2rkwz89%2Bq%2F4l1jUXh7I79pJQTfm4p%2BWGczxJwkOmJydardgV4BPtKfpyWdgwRNS02DhyASduzlH%2Fgy5oyoS4DvSdgPDDJTee0n8yYTb771qayJ8kvFY9RpjbOvBy3kxo4R0EOIK2EJaqBiDGJ%2ByYG9OkCNvBQzyksoAUlNv7%2FhCzRuvkcJPlcHP8FXMtoUk%2Bv%2FElI3qmGqlFmgFbbXjdE9Ho42semZL5iDrP9eShkT5p3TJQ1Ym3xabOJKE69fpV6uNSUVhOTr4M5Sy%2BmEeihrZVmO4%2BKmEF0tBYnrZ4RDaInEilBtWDf1UKGUC7sb7D2%2FWywh6j%2BVqUybHnpU4ASy5m8XMCpJgp2wlSCDVa%2B8Ru0NHmtNsfsBOYkaqo2hB662Rm79EwL8RsxE6zZSx2WC8a3g4kqy3bISTSVet7L1Hh7iWumyNMY6K9PYIzkPTFcshJJD9Gf4w4vCvyAY6pgE5Mg5m0MVegOmkPyb83WAKq9NxiybEj%2B8xnAmPwh3BYHitxCZJFV6e343mXcNbI31xSeXmPu6SkTyi3JfYkHa12NGT5T6dptpUtA%2FWxftHDBNn83Yn4uihwcXu%2BVwZzl9TpF1ec2z3ldCMUf0KufVQLyBU2V6yzlfduiKn4SU4lgtq5b9TwSuwqnk3alX6V8vssn39LBQVOzT1P4QBd2ol8xr1jCF4&X-Amz-Signature=e33ec36e49bea9082e29dd62331375c00391f2163a1759fbf2c9ff214b5b8fc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHVV26IS%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9AYiWv0lWIj6p2VlmxjbulD%2BUMAN587nO0jKWX0LkVAiACGiqCYP2aNeXt14pUtQN9nAhZRtw5BpvW6B%2FczkB%2FGiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAu5AYMPE%2FHACcxiKtwDzjd3xwdC5ROQHl8HbsTI%2BXaT3fKAX04tIbM75vMNQoUIGkvs3zHjs19dTyJ23r%2BABbGww0y8nRgfka6OY4%2F9a4S9xOhIDqCJCzSHKy6wWd66Sw2NGOJjH8hfsEXWEpSc%2F6YYyFy%2FSeabkFddr8V1d0WOeWe6d%2B6IXns0hVkeOMYwYD2Fh2rkwz89%2Bq%2F4l1jUXh7I79pJQTfm4p%2BWGczxJwkOmJydardgV4BPtKfpyWdgwRNS02DhyASduzlH%2Fgy5oyoS4DvSdgPDDJTee0n8yYTb771qayJ8kvFY9RpjbOvBy3kxo4R0EOIK2EJaqBiDGJ%2ByYG9OkCNvBQzyksoAUlNv7%2FhCzRuvkcJPlcHP8FXMtoUk%2Bv%2FElI3qmGqlFmgFbbXjdE9Ho42semZL5iDrP9eShkT5p3TJQ1Ym3xabOJKE69fpV6uNSUVhOTr4M5Sy%2BmEeihrZVmO4%2BKmEF0tBYnrZ4RDaInEilBtWDf1UKGUC7sb7D2%2FWywh6j%2BVqUybHnpU4ASy5m8XMCpJgp2wlSCDVa%2B8Ru0NHmtNsfsBOYkaqo2hB662Rm79EwL8RsxE6zZSx2WC8a3g4kqy3bISTSVet7L1Hh7iWumyNMY6K9PYIzkPTFcshJJD9Gf4w4vCvyAY6pgE5Mg5m0MVegOmkPyb83WAKq9NxiybEj%2B8xnAmPwh3BYHitxCZJFV6e343mXcNbI31xSeXmPu6SkTyi3JfYkHa12NGT5T6dptpUtA%2FWxftHDBNn83Yn4uihwcXu%2BVwZzl9TpF1ec2z3ldCMUf0KufVQLyBU2V6yzlfduiKn4SU4lgtq5b9TwSuwqnk3alX6V8vssn39LBQVOzT1P4QBd2ol8xr1jCF4&X-Amz-Signature=d4d4e200e48d1638787f3accdcf1534e27702df9f7d72dce8b85e8374005935c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

