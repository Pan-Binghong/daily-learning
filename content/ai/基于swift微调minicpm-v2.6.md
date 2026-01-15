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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKA7UFPS%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCtpH6CwkOtkXbfk1eV4%2Fxh6XvkcnSeQvz9sFv%2BKDysPAIhAKAqvfzs6DmC4yNhJCr6YXd2kgA9jEuTwjoAgGAf2A46Kv8DCCsQABoMNjM3NDIzMTgzODA1IgztaZVH3NzfbX40PeAq3APT9MXopF8acaDTKDA7WxRfhnCV0FzUqAmPBRv%2B3Glw2SMaJGfRL12zJck%2B2J0bsEA7%2BrMd6Jg2jpcUvz8J%2F4mSCFQveKp82Q%2FnXOnuxbN%2Fyn4vH0Nv1gbfymqq%2Fwk9P4RYESFe%2FW4A6pyddmzYufLVPBbVnpEaWb2JKTH1nJ%2B%2BHOvArfVsLLcAyVNu83VLEQP0jYQpnZnXNVQoYA5%2FOdCpnirJLxt4%2FHD6Yh7w8k3rfsSTO53hwVrnpmzFwS%2Felr3uPNeNTPvNavENJdw4BPGd5EZQf53rkAcEXfDxBuPjEEnR4e01CgS3i92HEZwb2UYJOBKO%2BRg7VlaePW05qtaDzkFLaP8%2FiSxPmcBmebzkP%2FE1wuj7yw2DVc6%2B78KChHFfIh4HJrCxkKXcUwsGAfVdX55jxuGNw98ZtxqYg%2FPK0XNzJnU3i4cRSothUbo357K28qFyubjQRs7YsfCXrwS2uCAT%2FRTOECPTJW0pGB8c22Ka%2FRuuFzvllL2rB1YpITonGPK1ChgJbv%2BDZQ3L5dU3Ro6G8LzTd8ArhBskhH7v%2Bw08bLT%2BfRKxgs0kGQ6i7ZTviiuzAgcaamlrf6XHw2mJ5bgVhDuzKza7qReE15IdLOIjVxZh68X2wXloMTDmmqHLBjqkARq0V6SVr%2FtzW4M2aXppDUUJi2GSjdqzl%2B8Y0Rb%2BlDDl0FbimO6KXRp7oeG0QGTDc8%2FRaD9OaghOZ0aCFIlYcyjbzcCC5zOUz%2BM4SZg3lij1OzLJN%2FyGpydd%2BmHGsNLLOpRJ%2FdK8EjD4s2HOTVQL0VZErmAJOBRWjCAyq0OKezFqdinmYAgUMtJ6k82VjwkkJaGa4RhkMko6lP1TRmElV6j%2FDdW6&X-Amz-Signature=8f4cf399e334e4a8ea8cd12fd42e308df8a8cca013a35c69e06a97d59f6c0147&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKA7UFPS%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCtpH6CwkOtkXbfk1eV4%2Fxh6XvkcnSeQvz9sFv%2BKDysPAIhAKAqvfzs6DmC4yNhJCr6YXd2kgA9jEuTwjoAgGAf2A46Kv8DCCsQABoMNjM3NDIzMTgzODA1IgztaZVH3NzfbX40PeAq3APT9MXopF8acaDTKDA7WxRfhnCV0FzUqAmPBRv%2B3Glw2SMaJGfRL12zJck%2B2J0bsEA7%2BrMd6Jg2jpcUvz8J%2F4mSCFQveKp82Q%2FnXOnuxbN%2Fyn4vH0Nv1gbfymqq%2Fwk9P4RYESFe%2FW4A6pyddmzYufLVPBbVnpEaWb2JKTH1nJ%2B%2BHOvArfVsLLcAyVNu83VLEQP0jYQpnZnXNVQoYA5%2FOdCpnirJLxt4%2FHD6Yh7w8k3rfsSTO53hwVrnpmzFwS%2Felr3uPNeNTPvNavENJdw4BPGd5EZQf53rkAcEXfDxBuPjEEnR4e01CgS3i92HEZwb2UYJOBKO%2BRg7VlaePW05qtaDzkFLaP8%2FiSxPmcBmebzkP%2FE1wuj7yw2DVc6%2B78KChHFfIh4HJrCxkKXcUwsGAfVdX55jxuGNw98ZtxqYg%2FPK0XNzJnU3i4cRSothUbo357K28qFyubjQRs7YsfCXrwS2uCAT%2FRTOECPTJW0pGB8c22Ka%2FRuuFzvllL2rB1YpITonGPK1ChgJbv%2BDZQ3L5dU3Ro6G8LzTd8ArhBskhH7v%2Bw08bLT%2BfRKxgs0kGQ6i7ZTviiuzAgcaamlrf6XHw2mJ5bgVhDuzKza7qReE15IdLOIjVxZh68X2wXloMTDmmqHLBjqkARq0V6SVr%2FtzW4M2aXppDUUJi2GSjdqzl%2B8Y0Rb%2BlDDl0FbimO6KXRp7oeG0QGTDc8%2FRaD9OaghOZ0aCFIlYcyjbzcCC5zOUz%2BM4SZg3lij1OzLJN%2FyGpydd%2BmHGsNLLOpRJ%2FdK8EjD4s2HOTVQL0VZErmAJOBRWjCAyq0OKezFqdinmYAgUMtJ6k82VjwkkJaGa4RhkMko6lP1TRmElV6j%2FDdW6&X-Amz-Signature=1b21de3f9488e33dfc7097d685437051ff6097ad546e6e3d4642f66761f5bd61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKA7UFPS%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCtpH6CwkOtkXbfk1eV4%2Fxh6XvkcnSeQvz9sFv%2BKDysPAIhAKAqvfzs6DmC4yNhJCr6YXd2kgA9jEuTwjoAgGAf2A46Kv8DCCsQABoMNjM3NDIzMTgzODA1IgztaZVH3NzfbX40PeAq3APT9MXopF8acaDTKDA7WxRfhnCV0FzUqAmPBRv%2B3Glw2SMaJGfRL12zJck%2B2J0bsEA7%2BrMd6Jg2jpcUvz8J%2F4mSCFQveKp82Q%2FnXOnuxbN%2Fyn4vH0Nv1gbfymqq%2Fwk9P4RYESFe%2FW4A6pyddmzYufLVPBbVnpEaWb2JKTH1nJ%2B%2BHOvArfVsLLcAyVNu83VLEQP0jYQpnZnXNVQoYA5%2FOdCpnirJLxt4%2FHD6Yh7w8k3rfsSTO53hwVrnpmzFwS%2Felr3uPNeNTPvNavENJdw4BPGd5EZQf53rkAcEXfDxBuPjEEnR4e01CgS3i92HEZwb2UYJOBKO%2BRg7VlaePW05qtaDzkFLaP8%2FiSxPmcBmebzkP%2FE1wuj7yw2DVc6%2B78KChHFfIh4HJrCxkKXcUwsGAfVdX55jxuGNw98ZtxqYg%2FPK0XNzJnU3i4cRSothUbo357K28qFyubjQRs7YsfCXrwS2uCAT%2FRTOECPTJW0pGB8c22Ka%2FRuuFzvllL2rB1YpITonGPK1ChgJbv%2BDZQ3L5dU3Ro6G8LzTd8ArhBskhH7v%2Bw08bLT%2BfRKxgs0kGQ6i7ZTviiuzAgcaamlrf6XHw2mJ5bgVhDuzKza7qReE15IdLOIjVxZh68X2wXloMTDmmqHLBjqkARq0V6SVr%2FtzW4M2aXppDUUJi2GSjdqzl%2B8Y0Rb%2BlDDl0FbimO6KXRp7oeG0QGTDc8%2FRaD9OaghOZ0aCFIlYcyjbzcCC5zOUz%2BM4SZg3lij1OzLJN%2FyGpydd%2BmHGsNLLOpRJ%2FdK8EjD4s2HOTVQL0VZErmAJOBRWjCAyq0OKezFqdinmYAgUMtJ6k82VjwkkJaGa4RhkMko6lP1TRmElV6j%2FDdW6&X-Amz-Signature=16784da24e54279dc2b722885c85751d3b3dab16058b25fe6ce05e105ffe6b47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

