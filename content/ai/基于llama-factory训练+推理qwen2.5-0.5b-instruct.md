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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGAWQQ3G%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTuXWSWtCSRwSmu4dIoyaAOhIDcaL1V4mqSQPRwRZOfAiBiqkuQSzagP2ufa%2FcqbpS%2BczH8egQn1HYLRc%2FQVWMEYyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMakjlZrw%2Fvi7mvSTGKtwDWs27W0hyHR%2BB0QBxheUw9QFt2API%2FGWv9WNvP04SaPIHI6GQz0FNL3pP%2Fp3fn%2BJBmyMd6k9iLbTImwxkw2wunAmYk6CQW9%2B5EG5oRPtMgCVeYIQdlqDeX59bI62qZ%2FneVIPQu6uxjVbtm1iH9ncyixO%2BaPiyHXoidl86bYd3BgBbC%2FS7e2KQ5RnWvAYtk78ZxyeYd8IFzipwJn7Lyv07hkh%2BJcVKad3xMjpKq2ghDR91gCLRQq%2Bwvg1hLlMql9mU6V0OBku7lGQopIiEENZlZ2IbtZhQ9sLF1QvJdPiFMGehhjnSumTi29e0P8jmU%2Fm7JHobXt1pbnGbmu2rQhjeJF2k33SXBAQ3goJuIIuozuWGkD9KDYSI7qphMsLNI%2F6O7I7QDgoHU6K3bBkkujdV%2FTejPZmqCgCCeyahtbx74bnumXsQtQ4lN3oDLhbXSbRZTtxHTPRxXh%2F7wEtzZO0896Kix%2Bou%2FM1uMZjpoYxC5W2y60dFmRH4MYcqUjN5omQt%2FeUD9LrR0pL%2FE6%2B2EkK%2FT%2B4KU3DAxgZ2mGeZjzPzXELO5wMHS9S4qcNG9XJqxzXh7Ten5nXJpanNusjWb8SEvqD%2FYll81%2BPSlNU%2BZ9V2sHMLbkNF3WbnU4zJg%2F8wvpmezQY6pgHxJGMwEhIlaDS7ymXh84VE8JrF1Cc4OdBDZr1R3VeyK2Ps1y3oQuELEnnqSlV%2FIlEm9qWwmNSak%2FfcxoA2hnLTzOGW1%2FCgnrQEhe28Hor6xb0awyjHVwX3RRgcAhfmW%2FIGVEmOoVH0AjlZjUkk4Muu4zve38nWPXtUPHXaUid84kVrDySppXhEfFTzoK0NU4opczjf5xTs5kyCBWuDokIChCzXNV%2BL&X-Amz-Signature=efecc6b85add826f6f9ae99b567e086aec38eb59e6b7957ed204d6cc39fbabe5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



