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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEN2IRRI%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3RvjDHE1SU%2BhVMfY4hmgbakYQH0TVHuGwOdQBGuWrDAiACUs5JF22EuN1q0t8fwqT0PyTrVtMYucQfxf%2BA%2FmDSqCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGvQkg6Tx4zPqkrYIKtwDa8YO0YxchJfbp%2F%2BcVB7ljKrQtSmKwGm3htqI84s3XOwfYyOH0jaVlJpihF0%2F%2BiD0M0rJWatH6j2OBzkGGL7Uz%2FkoIgTSaQS%2B5yIqhIl4X6uMPu29S6TwRdGmEfhJfwvGoxAUEhBYxf0zhlpG36GoMIQuugHp%2FGJ%2BA3d7BY2XOtwWtIovPNh8SnkO5uozb38N6MvqU%2FhXRnC0z8hx0OQCLD2lB117APLRp9FSIsK7CvxqQGS3BYOVOxXfjfuj3RczNa6oXtpLvWwf2VHCSGRTcXrEBA2WJ4gKTKLJdE5k5aMtAYYWvRdk0gBGzzc5VVutcAoyzT3%2BiHGWSD55%2FW0sZikrZTdzXRug9hRHxprD%2Fmdz2jIx3RTLlfFbFN9w907h%2FJtgxShOA%2BPikYCmI%2F9BgrasNSY%2FO4putlhGpycEbpA0dGy7FBXeL4uqJM4vTKy7XXGIylayGnzlkPDNymYbBVz%2B%2BsBXpcFfMCiwdfGuYOo2X2CDgiljv%2Fqiir1rItktj469vtdS%2FQZ6Th9sgK29kGfaNY34N4nFUkMtv6cBw3ABqY8UlSQBEHr64JUrN2CXT1oGFPHfFz002XXTPCF%2FRK3WjniK4Woz7SV8LCsmMh8U6tb9yYqJXxYyKd8wjuKSygY6pgHBv%2BuexZoB%2F%2FIUjMDi6I%2FTwhKdmXT146V4L1j4TH6c6WVKysljOhEzYrh4TnG0t0WrCQZfTdpihWDBfcK23f4N%2FjNNeUBNzl2YcMWIXZCd0gHHfI4vSU6zUoq55VD%2FtczEjlBbILUQ708tAg8v34dqPtgwO8ED%2Ba92zzyg96YHU5WVdSz3jvpdoKUioCS86RhMzJ2XoQtFugUEEdFvWp38IoZFzi9r&X-Amz-Signature=4a82b1fb6902e2afa83e6540e2fb3aa071713d28102dd7c64d46b31add923d51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEN2IRRI%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3RvjDHE1SU%2BhVMfY4hmgbakYQH0TVHuGwOdQBGuWrDAiACUs5JF22EuN1q0t8fwqT0PyTrVtMYucQfxf%2BA%2FmDSqCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGvQkg6Tx4zPqkrYIKtwDa8YO0YxchJfbp%2F%2BcVB7ljKrQtSmKwGm3htqI84s3XOwfYyOH0jaVlJpihF0%2F%2BiD0M0rJWatH6j2OBzkGGL7Uz%2FkoIgTSaQS%2B5yIqhIl4X6uMPu29S6TwRdGmEfhJfwvGoxAUEhBYxf0zhlpG36GoMIQuugHp%2FGJ%2BA3d7BY2XOtwWtIovPNh8SnkO5uozb38N6MvqU%2FhXRnC0z8hx0OQCLD2lB117APLRp9FSIsK7CvxqQGS3BYOVOxXfjfuj3RczNa6oXtpLvWwf2VHCSGRTcXrEBA2WJ4gKTKLJdE5k5aMtAYYWvRdk0gBGzzc5VVutcAoyzT3%2BiHGWSD55%2FW0sZikrZTdzXRug9hRHxprD%2Fmdz2jIx3RTLlfFbFN9w907h%2FJtgxShOA%2BPikYCmI%2F9BgrasNSY%2FO4putlhGpycEbpA0dGy7FBXeL4uqJM4vTKy7XXGIylayGnzlkPDNymYbBVz%2B%2BsBXpcFfMCiwdfGuYOo2X2CDgiljv%2Fqiir1rItktj469vtdS%2FQZ6Th9sgK29kGfaNY34N4nFUkMtv6cBw3ABqY8UlSQBEHr64JUrN2CXT1oGFPHfFz002XXTPCF%2FRK3WjniK4Woz7SV8LCsmMh8U6tb9yYqJXxYyKd8wjuKSygY6pgHBv%2BuexZoB%2F%2FIUjMDi6I%2FTwhKdmXT146V4L1j4TH6c6WVKysljOhEzYrh4TnG0t0WrCQZfTdpihWDBfcK23f4N%2FjNNeUBNzl2YcMWIXZCd0gHHfI4vSU6zUoq55VD%2FtczEjlBbILUQ708tAg8v34dqPtgwO8ED%2Ba92zzyg96YHU5WVdSz3jvpdoKUioCS86RhMzJ2XoQtFugUEEdFvWp38IoZFzi9r&X-Amz-Signature=d4dcbc87ddff28c5b0b8c53389d16822a44969f2c92ef155a1382ae3d2cd0dfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEN2IRRI%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3RvjDHE1SU%2BhVMfY4hmgbakYQH0TVHuGwOdQBGuWrDAiACUs5JF22EuN1q0t8fwqT0PyTrVtMYucQfxf%2BA%2FmDSqCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGvQkg6Tx4zPqkrYIKtwDa8YO0YxchJfbp%2F%2BcVB7ljKrQtSmKwGm3htqI84s3XOwfYyOH0jaVlJpihF0%2F%2BiD0M0rJWatH6j2OBzkGGL7Uz%2FkoIgTSaQS%2B5yIqhIl4X6uMPu29S6TwRdGmEfhJfwvGoxAUEhBYxf0zhlpG36GoMIQuugHp%2FGJ%2BA3d7BY2XOtwWtIovPNh8SnkO5uozb38N6MvqU%2FhXRnC0z8hx0OQCLD2lB117APLRp9FSIsK7CvxqQGS3BYOVOxXfjfuj3RczNa6oXtpLvWwf2VHCSGRTcXrEBA2WJ4gKTKLJdE5k5aMtAYYWvRdk0gBGzzc5VVutcAoyzT3%2BiHGWSD55%2FW0sZikrZTdzXRug9hRHxprD%2Fmdz2jIx3RTLlfFbFN9w907h%2FJtgxShOA%2BPikYCmI%2F9BgrasNSY%2FO4putlhGpycEbpA0dGy7FBXeL4uqJM4vTKy7XXGIylayGnzlkPDNymYbBVz%2B%2BsBXpcFfMCiwdfGuYOo2X2CDgiljv%2Fqiir1rItktj469vtdS%2FQZ6Th9sgK29kGfaNY34N4nFUkMtv6cBw3ABqY8UlSQBEHr64JUrN2CXT1oGFPHfFz002XXTPCF%2FRK3WjniK4Woz7SV8LCsmMh8U6tb9yYqJXxYyKd8wjuKSygY6pgHBv%2BuexZoB%2F%2FIUjMDi6I%2FTwhKdmXT146V4L1j4TH6c6WVKysljOhEzYrh4TnG0t0WrCQZfTdpihWDBfcK23f4N%2FjNNeUBNzl2YcMWIXZCd0gHHfI4vSU6zUoq55VD%2FtczEjlBbILUQ708tAg8v34dqPtgwO8ED%2Ba92zzyg96YHU5WVdSz3jvpdoKUioCS86RhMzJ2XoQtFugUEEdFvWp38IoZFzi9r&X-Amz-Signature=80c82d36aa98b7ceae261780fb4504345de439e3bffd01cd1e99f05112b202f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

