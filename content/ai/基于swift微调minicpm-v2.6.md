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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDL7UN6S%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIGXXv07jFo01mHFI4sssHKkAiv9x56ydz0jERFbFK4R9AiEAuss62qLvBZdoPDlABd1gBcK%2BRCPWypWnapofddM2s90qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLelEjYDNepAqi%2B1pSrcA2u%2BLFJpMYiWAaT6sskWNJAMokkf0hH6TDqEs6SWIXgL%2F%2BN04xGtINWjcl42rYx8g%2Ftxytgmpvi6oeEHs84HMgCRLI1O9y0ze3wI5Fzo4am7Hn9DVAoQ9HvUXMQ1uGbVGqwFFEueH7TJtVRN22iPMmuYs%2BTiSHeQa3R7wYUlFgPStks%2F0vDyULJL6hjUvJ1XjtxyTWgRfXkKdrktc3VzvQyfk5LHRgdV1WAhDeZfcC6R0o0CUlOVp0U9UqK6SbCiZexeTIPbCAaU1eWCv1tDVSuECBV0LkCmHZYsWsVMi9awimlsIF0HkAZUZP1ZHZ%2BHLuwnIZYPRrZsN5MhsSPfgU%2B%2FoCwkYV4QnEBTzfzhizHVD7BmAl0oxBba%2FNlUARdBtDz%2Bi00Fd7eY2pMIsSQrPrrbpDoDQYgpK%2BcDCkrHoeom7l%2FZXSNWmG4%2FZ%2B9yaR2QHOwpGiT0BvzUTo95f8vtbsMxg4i4pAcN1%2BlLSgCtloFQCUnoOtNvAgOBiFAp7VOxL9jYdKJ5yWkuTRcC5012g921t6PTmCqKXjH8MFZ9DtQOFho5Kp7ZGY%2BxIVBIYGO%2Bo%2Bjo0NticAfhveZN7BTkyMsIT%2F5YGmYvS79oIMQ292ZjK0Ti0%2FrBMNVbJpfRMO3mlssGOqUB6MkSqwvL8FnjL%2BucjPaigCHbHPacKH23BHdDKoBiGUIU1O2m0%2Bx%2FgQrpAFOYTaiizQB4hvAoCmLGLaSsjexHoJNfPy9t5mZqzQeIwd3d8EIwIHeGs3%2BSaEtPJRw3t6HPbUuvbk9xSol4Ap33QPqXg3jMnmBn4WwhcOqTJChGpzTICk90qLJimbo04THpx6xJXzZbf1EydefBCJ8NIdUEG6hVjUzZ&X-Amz-Signature=de68a3762c5f76d6bd9380fc588492bfcd9a429f9f421a5296e396ae5fe8c07d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDL7UN6S%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIGXXv07jFo01mHFI4sssHKkAiv9x56ydz0jERFbFK4R9AiEAuss62qLvBZdoPDlABd1gBcK%2BRCPWypWnapofddM2s90qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLelEjYDNepAqi%2B1pSrcA2u%2BLFJpMYiWAaT6sskWNJAMokkf0hH6TDqEs6SWIXgL%2F%2BN04xGtINWjcl42rYx8g%2Ftxytgmpvi6oeEHs84HMgCRLI1O9y0ze3wI5Fzo4am7Hn9DVAoQ9HvUXMQ1uGbVGqwFFEueH7TJtVRN22iPMmuYs%2BTiSHeQa3R7wYUlFgPStks%2F0vDyULJL6hjUvJ1XjtxyTWgRfXkKdrktc3VzvQyfk5LHRgdV1WAhDeZfcC6R0o0CUlOVp0U9UqK6SbCiZexeTIPbCAaU1eWCv1tDVSuECBV0LkCmHZYsWsVMi9awimlsIF0HkAZUZP1ZHZ%2BHLuwnIZYPRrZsN5MhsSPfgU%2B%2FoCwkYV4QnEBTzfzhizHVD7BmAl0oxBba%2FNlUARdBtDz%2Bi00Fd7eY2pMIsSQrPrrbpDoDQYgpK%2BcDCkrHoeom7l%2FZXSNWmG4%2FZ%2B9yaR2QHOwpGiT0BvzUTo95f8vtbsMxg4i4pAcN1%2BlLSgCtloFQCUnoOtNvAgOBiFAp7VOxL9jYdKJ5yWkuTRcC5012g921t6PTmCqKXjH8MFZ9DtQOFho5Kp7ZGY%2BxIVBIYGO%2Bo%2Bjo0NticAfhveZN7BTkyMsIT%2F5YGmYvS79oIMQ292ZjK0Ti0%2FrBMNVbJpfRMO3mlssGOqUB6MkSqwvL8FnjL%2BucjPaigCHbHPacKH23BHdDKoBiGUIU1O2m0%2Bx%2FgQrpAFOYTaiizQB4hvAoCmLGLaSsjexHoJNfPy9t5mZqzQeIwd3d8EIwIHeGs3%2BSaEtPJRw3t6HPbUuvbk9xSol4Ap33QPqXg3jMnmBn4WwhcOqTJChGpzTICk90qLJimbo04THpx6xJXzZbf1EydefBCJ8NIdUEG6hVjUzZ&X-Amz-Signature=ee1d5658de60e2030f2e2c02763d3b9c45f1d9cc657d2642d35260793c478b65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDL7UN6S%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIGXXv07jFo01mHFI4sssHKkAiv9x56ydz0jERFbFK4R9AiEAuss62qLvBZdoPDlABd1gBcK%2BRCPWypWnapofddM2s90qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLelEjYDNepAqi%2B1pSrcA2u%2BLFJpMYiWAaT6sskWNJAMokkf0hH6TDqEs6SWIXgL%2F%2BN04xGtINWjcl42rYx8g%2Ftxytgmpvi6oeEHs84HMgCRLI1O9y0ze3wI5Fzo4am7Hn9DVAoQ9HvUXMQ1uGbVGqwFFEueH7TJtVRN22iPMmuYs%2BTiSHeQa3R7wYUlFgPStks%2F0vDyULJL6hjUvJ1XjtxyTWgRfXkKdrktc3VzvQyfk5LHRgdV1WAhDeZfcC6R0o0CUlOVp0U9UqK6SbCiZexeTIPbCAaU1eWCv1tDVSuECBV0LkCmHZYsWsVMi9awimlsIF0HkAZUZP1ZHZ%2BHLuwnIZYPRrZsN5MhsSPfgU%2B%2FoCwkYV4QnEBTzfzhizHVD7BmAl0oxBba%2FNlUARdBtDz%2Bi00Fd7eY2pMIsSQrPrrbpDoDQYgpK%2BcDCkrHoeom7l%2FZXSNWmG4%2FZ%2B9yaR2QHOwpGiT0BvzUTo95f8vtbsMxg4i4pAcN1%2BlLSgCtloFQCUnoOtNvAgOBiFAp7VOxL9jYdKJ5yWkuTRcC5012g921t6PTmCqKXjH8MFZ9DtQOFho5Kp7ZGY%2BxIVBIYGO%2Bo%2Bjo0NticAfhveZN7BTkyMsIT%2F5YGmYvS79oIMQ292ZjK0Ti0%2FrBMNVbJpfRMO3mlssGOqUB6MkSqwvL8FnjL%2BucjPaigCHbHPacKH23BHdDKoBiGUIU1O2m0%2Bx%2FgQrpAFOYTaiizQB4hvAoCmLGLaSsjexHoJNfPy9t5mZqzQeIwd3d8EIwIHeGs3%2BSaEtPJRw3t6HPbUuvbk9xSol4Ap33QPqXg3jMnmBn4WwhcOqTJChGpzTICk90qLJimbo04THpx6xJXzZbf1EydefBCJ8NIdUEG6hVjUzZ&X-Amz-Signature=f22c14a95fbda9274cf8e769afaff106e77ffd2e0187135963e26c73c6b9e47a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

