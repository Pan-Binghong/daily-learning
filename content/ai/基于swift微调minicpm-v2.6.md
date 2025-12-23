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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZXDVL73%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIGGldXq7dKLlq1EU46mfZ%2B6kVfrf1kjXibFFlwol6m8eAiEAokZQWwjE54s8nztcIfPxDy6TZlc7EOMs6wtB%2FQ%2FEZqIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDMW0mdEM1%2FD5beovHyrcA91LO5swBZT%2FTR98q%2BbHAd%2F7a0bsHBSa7TyOhMMJUAN7SCyjudnBaED86QaEmeeqDC%2BaRjte6yzreIjaRn52aVUemMxRrFUlt%2BpxT9xG1V6%2FMD79jK%2BrtdcyplSxfF8B5J7xrm82%2BRLsefCmATl1qyCcxyOqZNlhAwFxCvo6xJOhyKJ%2FKlimKHSP9J%2FQ%2FxMbMRve8M73L3uH3iTvwNJr%2BVPWQA6TIZLw%2FYcyF3s7fbunT6NcFF3o%2BOlPQsv0ctzVT7r9MD9O4MZs8Z5IC4vPcW%2FnW%2Bs3tiT4w1pS46gHjqRW4XWuOP31h9TRxLjBM7oKMKumJz%2FuPy9vu2WpoPgOkG0vDyQAmmAykLHNntPAZJQxdU1Svx5jQuZnp8hcWQbXYcdaVC5q%2Blf650IW9sS0HZxRzNLNrAzSjtfRdc8AahDpOEi8aQN0%2FyFFP7swCbvQK9YcjdBVLJpgehhSpp7Z%2BzQT6RBy8oHjBQLYIobmE6iO7Jw%2BVQUxv7cb6jZpJozk5AhiYFbOdZawuguvumJ2WLzV0l9x1up2sedbx5PR0o3nFZvoAAl5EGygODy7Pmrs67ieUr9nI4IVRD%2FGH%2Fagoj4XdVcR7TFG8Xw9SGd00GqMn17K4kma4%2F%2FJZUcNMNH7p8oGOqUBey3dyTFnd%2FZ6NliParfKIh3nQMlDZ%2FifP8AUyfOBmGv5b1bFbaE8u3DaGR4Is9a8oOysb%2FyzQPQGVyFz3wqqgAQs4BNTMNHLzPqm9vxDorcY%2BrStzqXhK2H8k8t0Y6uQL8q9NpuGDQPR9sJA0UQMjef18OVyb1xaOXtlahF%2B80i0hRn8rFDu7mFiZCYOZOyZHzE7q%2FSiGLO5LAWxyDvxaZE2Ov1%2F&X-Amz-Signature=31ffd2d364e72bea5b883c99d8e3904da3d33bfc76c5211a9e5dcd87eae5748b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZXDVL73%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIGGldXq7dKLlq1EU46mfZ%2B6kVfrf1kjXibFFlwol6m8eAiEAokZQWwjE54s8nztcIfPxDy6TZlc7EOMs6wtB%2FQ%2FEZqIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDMW0mdEM1%2FD5beovHyrcA91LO5swBZT%2FTR98q%2BbHAd%2F7a0bsHBSa7TyOhMMJUAN7SCyjudnBaED86QaEmeeqDC%2BaRjte6yzreIjaRn52aVUemMxRrFUlt%2BpxT9xG1V6%2FMD79jK%2BrtdcyplSxfF8B5J7xrm82%2BRLsefCmATl1qyCcxyOqZNlhAwFxCvo6xJOhyKJ%2FKlimKHSP9J%2FQ%2FxMbMRve8M73L3uH3iTvwNJr%2BVPWQA6TIZLw%2FYcyF3s7fbunT6NcFF3o%2BOlPQsv0ctzVT7r9MD9O4MZs8Z5IC4vPcW%2FnW%2Bs3tiT4w1pS46gHjqRW4XWuOP31h9TRxLjBM7oKMKumJz%2FuPy9vu2WpoPgOkG0vDyQAmmAykLHNntPAZJQxdU1Svx5jQuZnp8hcWQbXYcdaVC5q%2Blf650IW9sS0HZxRzNLNrAzSjtfRdc8AahDpOEi8aQN0%2FyFFP7swCbvQK9YcjdBVLJpgehhSpp7Z%2BzQT6RBy8oHjBQLYIobmE6iO7Jw%2BVQUxv7cb6jZpJozk5AhiYFbOdZawuguvumJ2WLzV0l9x1up2sedbx5PR0o3nFZvoAAl5EGygODy7Pmrs67ieUr9nI4IVRD%2FGH%2Fagoj4XdVcR7TFG8Xw9SGd00GqMn17K4kma4%2F%2FJZUcNMNH7p8oGOqUBey3dyTFnd%2FZ6NliParfKIh3nQMlDZ%2FifP8AUyfOBmGv5b1bFbaE8u3DaGR4Is9a8oOysb%2FyzQPQGVyFz3wqqgAQs4BNTMNHLzPqm9vxDorcY%2BrStzqXhK2H8k8t0Y6uQL8q9NpuGDQPR9sJA0UQMjef18OVyb1xaOXtlahF%2B80i0hRn8rFDu7mFiZCYOZOyZHzE7q%2FSiGLO5LAWxyDvxaZE2Ov1%2F&X-Amz-Signature=14cdf1346e38e18d74069ac04da974038527b678b6756c9fceb63156e517cceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZXDVL73%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIGGldXq7dKLlq1EU46mfZ%2B6kVfrf1kjXibFFlwol6m8eAiEAokZQWwjE54s8nztcIfPxDy6TZlc7EOMs6wtB%2FQ%2FEZqIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDMW0mdEM1%2FD5beovHyrcA91LO5swBZT%2FTR98q%2BbHAd%2F7a0bsHBSa7TyOhMMJUAN7SCyjudnBaED86QaEmeeqDC%2BaRjte6yzreIjaRn52aVUemMxRrFUlt%2BpxT9xG1V6%2FMD79jK%2BrtdcyplSxfF8B5J7xrm82%2BRLsefCmATl1qyCcxyOqZNlhAwFxCvo6xJOhyKJ%2FKlimKHSP9J%2FQ%2FxMbMRve8M73L3uH3iTvwNJr%2BVPWQA6TIZLw%2FYcyF3s7fbunT6NcFF3o%2BOlPQsv0ctzVT7r9MD9O4MZs8Z5IC4vPcW%2FnW%2Bs3tiT4w1pS46gHjqRW4XWuOP31h9TRxLjBM7oKMKumJz%2FuPy9vu2WpoPgOkG0vDyQAmmAykLHNntPAZJQxdU1Svx5jQuZnp8hcWQbXYcdaVC5q%2Blf650IW9sS0HZxRzNLNrAzSjtfRdc8AahDpOEi8aQN0%2FyFFP7swCbvQK9YcjdBVLJpgehhSpp7Z%2BzQT6RBy8oHjBQLYIobmE6iO7Jw%2BVQUxv7cb6jZpJozk5AhiYFbOdZawuguvumJ2WLzV0l9x1up2sedbx5PR0o3nFZvoAAl5EGygODy7Pmrs67ieUr9nI4IVRD%2FGH%2Fagoj4XdVcR7TFG8Xw9SGd00GqMn17K4kma4%2F%2FJZUcNMNH7p8oGOqUBey3dyTFnd%2FZ6NliParfKIh3nQMlDZ%2FifP8AUyfOBmGv5b1bFbaE8u3DaGR4Is9a8oOysb%2FyzQPQGVyFz3wqqgAQs4BNTMNHLzPqm9vxDorcY%2BrStzqXhK2H8k8t0Y6uQL8q9NpuGDQPR9sJA0UQMjef18OVyb1xaOXtlahF%2B80i0hRn8rFDu7mFiZCYOZOyZHzE7q%2FSiGLO5LAWxyDvxaZE2Ov1%2F&X-Amz-Signature=2f3198d77e2dcaaa81870a4d66fcb5981882214742778bb050800ae0e411c388&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

