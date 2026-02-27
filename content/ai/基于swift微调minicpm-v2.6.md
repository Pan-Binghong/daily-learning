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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOWGGGVW%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGhbs14lV2bW4%2BY4ICy8C7CJKu1KO8mnPYLWvoqqBWBmAiB9WScvALsaoqfv4HPz761M4fiVWd%2B3Ph8d3dQCLHWpuir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzran%2FS4px5PQVxaUKtwDBeEo7mybJdDT6FVaUds7At7cqrcihBSBbHDeKBEEM24v4XlNqSC2lpfGhzSLCvGwCl5ljSWpwyBMNYvDXnbRGC%2Bb8uhe34aMcKOZLZZJ7rWG%2Fvnp5kAz3ZDc4MO%2BnLPiXCRPHjL2uSmNgLdQaHoVNXierxTqW6mxtKRgvUykxBGV3cca%2FtcjdiF7xVjyLgWn5m4G1FBI0K%2FDW4UX6u9MO5inH63XvYD3PV%2Bwbd1knuP09jOrT1ifN0s8RA%2FdPPWi0nv128ef%2F4GUGiUunttxplwT6Q1og%2Fbon0qybf1FQpGGpt7XzYblsFHmzcQITA%2FzLoAqjRo%2FSs0kA%2BDRcoSmfxZ36C7GAla4Ixfcttxj1eY82uUns9aazVdtzv3PNEifeaLHDPQ61wL35z%2FVeyhtZPL35jP5c43QVAmKXwGkpLGyGbIRxStWQanhldUwSnN8THVe1ZVwBHIDuO9Y6qPf%2BsuF%2BFQ%2Ba41xrFZCSpriAvBQxwNI5RqCSOfTsyJmwArtrRs2BkvWgX2iniVC%2BrRpQZIyozGQAC%2F%2BhF%2F%2FcyayuLwBsMdYLiAEF06aY4ZACA4KQq4VUW%2FDXuvbYoxKfJl6gsdBl5%2BhcICgckqmjcD7o%2BG80kUnxVqroGLzjREw4IaEzQY6pgF8tVHUeUn%2BqFZVvAFhgUfRf3%2BYZwouPgpt36JCp35pcLmsUzRHstam0FmNW5hBYSJmW6%2FI%2BMcS%2FWz2vCbXlIEJiSU%2FubzGEpncsBdbU%2BI5wFEAgnmqziIakYyGN3pWFoFjRz3LfY%2B2iPaYXFpGHw1bqhuVWNNz%2FDm60qsh%2BswPqI9n3jUwep56tO6KvoLSKe%2Flac8bygj0sEQqWB4fzdwYwKd4v2Xg&X-Amz-Signature=e71ca820cca281caf8cd207d32ef21a6581a2c408486b2fece3a49c3f8b4c9b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOWGGGVW%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGhbs14lV2bW4%2BY4ICy8C7CJKu1KO8mnPYLWvoqqBWBmAiB9WScvALsaoqfv4HPz761M4fiVWd%2B3Ph8d3dQCLHWpuir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzran%2FS4px5PQVxaUKtwDBeEo7mybJdDT6FVaUds7At7cqrcihBSBbHDeKBEEM24v4XlNqSC2lpfGhzSLCvGwCl5ljSWpwyBMNYvDXnbRGC%2Bb8uhe34aMcKOZLZZJ7rWG%2Fvnp5kAz3ZDc4MO%2BnLPiXCRPHjL2uSmNgLdQaHoVNXierxTqW6mxtKRgvUykxBGV3cca%2FtcjdiF7xVjyLgWn5m4G1FBI0K%2FDW4UX6u9MO5inH63XvYD3PV%2Bwbd1knuP09jOrT1ifN0s8RA%2FdPPWi0nv128ef%2F4GUGiUunttxplwT6Q1og%2Fbon0qybf1FQpGGpt7XzYblsFHmzcQITA%2FzLoAqjRo%2FSs0kA%2BDRcoSmfxZ36C7GAla4Ixfcttxj1eY82uUns9aazVdtzv3PNEifeaLHDPQ61wL35z%2FVeyhtZPL35jP5c43QVAmKXwGkpLGyGbIRxStWQanhldUwSnN8THVe1ZVwBHIDuO9Y6qPf%2BsuF%2BFQ%2Ba41xrFZCSpriAvBQxwNI5RqCSOfTsyJmwArtrRs2BkvWgX2iniVC%2BrRpQZIyozGQAC%2F%2BhF%2F%2FcyayuLwBsMdYLiAEF06aY4ZACA4KQq4VUW%2FDXuvbYoxKfJl6gsdBl5%2BhcICgckqmjcD7o%2BG80kUnxVqroGLzjREw4IaEzQY6pgF8tVHUeUn%2BqFZVvAFhgUfRf3%2BYZwouPgpt36JCp35pcLmsUzRHstam0FmNW5hBYSJmW6%2FI%2BMcS%2FWz2vCbXlIEJiSU%2FubzGEpncsBdbU%2BI5wFEAgnmqziIakYyGN3pWFoFjRz3LfY%2B2iPaYXFpGHw1bqhuVWNNz%2FDm60qsh%2BswPqI9n3jUwep56tO6KvoLSKe%2Flac8bygj0sEQqWB4fzdwYwKd4v2Xg&X-Amz-Signature=adce6df38d5e0e8e2b60f8805dd5e33cea9b6ce9a82684ac602c685b5cb2eb34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOWGGGVW%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGhbs14lV2bW4%2BY4ICy8C7CJKu1KO8mnPYLWvoqqBWBmAiB9WScvALsaoqfv4HPz761M4fiVWd%2B3Ph8d3dQCLHWpuir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzran%2FS4px5PQVxaUKtwDBeEo7mybJdDT6FVaUds7At7cqrcihBSBbHDeKBEEM24v4XlNqSC2lpfGhzSLCvGwCl5ljSWpwyBMNYvDXnbRGC%2Bb8uhe34aMcKOZLZZJ7rWG%2Fvnp5kAz3ZDc4MO%2BnLPiXCRPHjL2uSmNgLdQaHoVNXierxTqW6mxtKRgvUykxBGV3cca%2FtcjdiF7xVjyLgWn5m4G1FBI0K%2FDW4UX6u9MO5inH63XvYD3PV%2Bwbd1knuP09jOrT1ifN0s8RA%2FdPPWi0nv128ef%2F4GUGiUunttxplwT6Q1og%2Fbon0qybf1FQpGGpt7XzYblsFHmzcQITA%2FzLoAqjRo%2FSs0kA%2BDRcoSmfxZ36C7GAla4Ixfcttxj1eY82uUns9aazVdtzv3PNEifeaLHDPQ61wL35z%2FVeyhtZPL35jP5c43QVAmKXwGkpLGyGbIRxStWQanhldUwSnN8THVe1ZVwBHIDuO9Y6qPf%2BsuF%2BFQ%2Ba41xrFZCSpriAvBQxwNI5RqCSOfTsyJmwArtrRs2BkvWgX2iniVC%2BrRpQZIyozGQAC%2F%2BhF%2F%2FcyayuLwBsMdYLiAEF06aY4ZACA4KQq4VUW%2FDXuvbYoxKfJl6gsdBl5%2BhcICgckqmjcD7o%2BG80kUnxVqroGLzjREw4IaEzQY6pgF8tVHUeUn%2BqFZVvAFhgUfRf3%2BYZwouPgpt36JCp35pcLmsUzRHstam0FmNW5hBYSJmW6%2FI%2BMcS%2FWz2vCbXlIEJiSU%2FubzGEpncsBdbU%2BI5wFEAgnmqziIakYyGN3pWFoFjRz3LfY%2B2iPaYXFpGHw1bqhuVWNNz%2FDm60qsh%2BswPqI9n3jUwep56tO6KvoLSKe%2Flac8bygj0sEQqWB4fzdwYwKd4v2Xg&X-Amz-Signature=156628008fcbd38685bb132f6994b2e42913eaef829ac36649b2c0b515473460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

