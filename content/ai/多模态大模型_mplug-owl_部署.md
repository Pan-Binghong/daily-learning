---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JS3XCWD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTB5a4BJNJPIVQv5yLTbSPKs%2BvqlpJzTpCdhO25x0K9wIgCCU7smfRXW%2By2WN4TeIScvYMuIX%2B8zYVb7dZ5JmGjVYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJytE3tMyyI6hq6oNircA%2FQoDPW7uHNBUakv4FvwGazocHjzw9UjpQcDeU1fIvbEHLAAw%2FneUKf9LEppb6CAtuUdDdaKwdSMWQGlhRV1emRYk3L7xX9%2FZ4G8pwP0xzlT5NLAA5j6%2FPhht8F07VDvnVp12pnG5N5bpzBfv9WliWWxj6vmNC1hD9fqixOgH%2BsG9CArOXgJ2RnfM7FVBYkkJxaw0Z396J5kWtIDLSEqeAiCAgY%2FXjptlQAmwmL3O1RfUUjahVTyZffBq0GoV1iqy1aMEYkngKQg2HBMn6xSIrZDMaKBb9ppPV%2FVQPSbNJCK2lWdqJfnMDpxxpeFJrSiB3uvrsLzTxodfRqZrzinrngfh7FPdvbcfpFD0Twt5Or08rFemOoT5mBUhQeuzB6ZyZ1IsSCfJPt4HEHQjvBQ8%2FgllhgVy1pXkOO2C4zBx%2FoTGPvsI4nWiPBtbbVemVmZ0q31TmB%2BowTgn7gRV6cV6QzNJeoEFjpb5FnMf6AXl9HGG9op0sPs8MIl4EniOM4FbWyeEVtwkmyjlompUQVkJPWB1AaUEpKqVl3PvfbAD7cyNtdLMP2rXb4kv5EvAfAZUvihDPKbP2mqngyJ5nFOoEHnU%2FUKLoCktEpSh%2FFWEqKasagr7FKlNQKnxGGjMKryr8gGOqUB7eW08Vjm7HlOwNEXqyV3OZYJwrYlUBl%2F9%2BPpFkEZjjZPQOOQMID%2BLLQbbbkJL4cNtjUHA3R%2BiyWi9tKr%2FS%2FK2UzQzR7tiPd%2FZY8Q84GF%2B82ZA8I6tJKKPsDy3rYGnXLTtTWZU8VX3LkP4%2Bw%2FOWEnz49K3%2FZA8ifPDo29kswUELAFpEkWd%2BzrFh%2FRUSI0Hj0n6rLXCsffOO6HmITzfOeN%2F1dSMLjB&X-Amz-Signature=f8812f25cf020b3e8a987c89d5ace360fe1f1ba7d354a1e46e42095b61fd9f91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JS3XCWD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTB5a4BJNJPIVQv5yLTbSPKs%2BvqlpJzTpCdhO25x0K9wIgCCU7smfRXW%2By2WN4TeIScvYMuIX%2B8zYVb7dZ5JmGjVYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJytE3tMyyI6hq6oNircA%2FQoDPW7uHNBUakv4FvwGazocHjzw9UjpQcDeU1fIvbEHLAAw%2FneUKf9LEppb6CAtuUdDdaKwdSMWQGlhRV1emRYk3L7xX9%2FZ4G8pwP0xzlT5NLAA5j6%2FPhht8F07VDvnVp12pnG5N5bpzBfv9WliWWxj6vmNC1hD9fqixOgH%2BsG9CArOXgJ2RnfM7FVBYkkJxaw0Z396J5kWtIDLSEqeAiCAgY%2FXjptlQAmwmL3O1RfUUjahVTyZffBq0GoV1iqy1aMEYkngKQg2HBMn6xSIrZDMaKBb9ppPV%2FVQPSbNJCK2lWdqJfnMDpxxpeFJrSiB3uvrsLzTxodfRqZrzinrngfh7FPdvbcfpFD0Twt5Or08rFemOoT5mBUhQeuzB6ZyZ1IsSCfJPt4HEHQjvBQ8%2FgllhgVy1pXkOO2C4zBx%2FoTGPvsI4nWiPBtbbVemVmZ0q31TmB%2BowTgn7gRV6cV6QzNJeoEFjpb5FnMf6AXl9HGG9op0sPs8MIl4EniOM4FbWyeEVtwkmyjlompUQVkJPWB1AaUEpKqVl3PvfbAD7cyNtdLMP2rXb4kv5EvAfAZUvihDPKbP2mqngyJ5nFOoEHnU%2FUKLoCktEpSh%2FFWEqKasagr7FKlNQKnxGGjMKryr8gGOqUB7eW08Vjm7HlOwNEXqyV3OZYJwrYlUBl%2F9%2BPpFkEZjjZPQOOQMID%2BLLQbbbkJL4cNtjUHA3R%2BiyWi9tKr%2FS%2FK2UzQzR7tiPd%2FZY8Q84GF%2B82ZA8I6tJKKPsDy3rYGnXLTtTWZU8VX3LkP4%2Bw%2FOWEnz49K3%2FZA8ifPDo29kswUELAFpEkWd%2BzrFh%2FRUSI0Hj0n6rLXCsffOO6HmITzfOeN%2F1dSMLjB&X-Amz-Signature=350ef472d664583b8cb5e83a046a61f7394cd1e90717f1f025dc74a33570049d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

