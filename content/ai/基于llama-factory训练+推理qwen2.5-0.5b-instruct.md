---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZA3GRW3V%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGiNGMHiWeFipGTK9h%2FSywA0WqYnoL2W2MiSq1Ua3BPOAiAJKAO2kJ%2F5sJ%2BEmRJXR6Dipe6Kf%2BU2Y0DEpgDbD2rzUiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQQBl6XeqgNttYp8VKtwDeHhs7WZVDxwd75GKBkkDGc%2BwbDQA3Tfnyaa0q7QdKn89lqKoOC7eMp0mbUcSz3%2BP61OgwW8RF53kiRA99T%2BS5vnmokXUUWPBqF%2FcclhQIC%2FOSn6EN1m9KqJSehE6YhM4XHhYPQ1gy2lnGjnKgNAFB00%2By1gHUxmKFdWGs%2F1Fx4vZJOoSrwsZ%2BtCPWvK9LZt21RchMyqelToR6%2FFl0vGenN%2FeA6N%2BzpHwgDDt1Z5ORe%2BXzIr%2BPVcDbTDjDZ3B%2BWNdtCR6BTkZ0jzqbJRwyU5RJxi%2FKz47N87sVHtZwCzYcOcNcaSoIAS5yfKATDs8iEogXNQfReWOCALnGbsVWy4vI05mEGZVAZ29tVUrZYPiaBz0fEXAXoLJwC0zDQENBZh4DtKlp64eEper9kOEN5tpgCoPe2XTfBUaN5yFKGoiYP6q%2FR1wBiosX4gyaYyE%2FewnwLhzsNAdXyU3DcAdmzvsqnUI%2FXvkbJ4aFrPXblJMx41pSy%2BVktZ8wdg7yXyda38nKZv42dk8hsb6RR1%2Fpnwb9WB7h6EIhJW%2BM0xudQha2H8E7F0E4w2rp%2BWzzS%2Bt%2FzpP66eW1V%2BlG8EfNmnpnoQ1d2hbifl8jl7dn567JbPgbMO1RsOZ2k6hgwSevoww1eDkyAY6pgEETwj%2F7CMjz9xOMVir8pbREk90suGJRVfd1dz%2F%2FVEJomqmZZyrCaXj7zlNbyZBIgdIQl9Py1gTHdhTvCpgV92l%2BNbm%2FgT3K7Cv4S1U5fTI%2BjR6WQaMC9a4JeJjR6IKTA0KreeFkApLWSp1VzwU1TT8nu0yb66LZigPZb0zIJMZi1OUrV6pTZ%2BdP1HH4z03rJ4Ow2RlYTIL4yKcLHDTwvuMGZrk9mGl&X-Amz-Signature=51e2627311b3b02b63cce53534615f4903dcbf712c6b79c991c8e684010ca802&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前置条件: 环境，模型

- 模型路径 : /root/autodl-tmp/xinference/modelscope/hub/qwen/Qwen2___5-0___5B-Instruct
- 微调完成 : /root/saves/Qwen2-0.5B-Chat/lora/train_2024-10-10-19-48-53/checkpoint-62
- 融合完成 : /root/LLaMA-Factory/models/qwen2.5
## 数据

## 训练

## 推理

## Reference

> https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

> https://llamafactory.readthedocs.io/zh-cn/latest/index.html

> https://inference.readthedocs.io/zh-cn/latest/



