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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOJ4UFCP%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIC84BQzlDIkxNYbhyjuzoLpEUpQ4SP3jV%2B91Lh%2BiB4m5AiBdOdLONP6VUtPIdRIDlbHWzx2FJsIED2wkjW%2FCaToMHiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpU93qF%2B%2BAQnPTltwKtwDXiMn3JIe2Ym%2B3AWSB9mYL1fpz%2B09CqTkVF9XCTuqTIsdZQRaCYimjZAAGpi6uORTzs051aOFKZvx1Yappxbqa7iLOW%2F2CLlU9pfgYoHh2LOx0sfYE%2BfXoe3Ot63cmBIGxw4f2E4JXco%2BbkZ4S4YtqIts6ZuvlDAwFuXvoQNhWVekc1g3Zh2VWq4FGq858XkMNzBdbZsn9%2BnuQnGFAyTdBTYolFQL8VQVb9aumuvYFpfTnU9zaE3ZoTsdjZy4oXtyyEBecEa1lCiQ1iU42XycBRs6mvKW3mdd9eI2DU579oMizfdV4YyCWo3rUtvRmGJDPHZjdqr2Kryq4NAl9bJOWHjeUdzW8kAA9%2BV685ThZ4%2BeSRUxlzHjfLiPku%2FqUM2pPUxb3dQxNgEj3siHi%2BTEuE1VikV32K7MCvV57OWY0seEHQSZibvtXQGGiAJdzv94EIhFyPt3SrXTlquZGHbjY3x7BqT22jLxeMPQnsic0xT4ttbawrhAxMpLtvlZKRr3gVmW%2FrdYO%2FSZNdbNxOFod0ZRNtl8kO9jv8E9xX3OrY1fVJb9zQCv9h%2FlXIG9v%2BpVdMlTL%2BJ4a771Lk%2F%2B9KmeA8GpK8fxtj23y0T%2Fu%2FMuAZH7Rq4r5vhzwu8poY8wp%2Br5yAY6pgEY9OJuzMPpKjZqViP5n%2BnbYc9sRVsdFbOPYuAjwpOv7h6XCnqcI9gGH0f9Gs%2FMgu%2FBf4AHrXuvH3cMAm5fJBybJ4xSXRmlKAAowFqULjBPndYIwyFsCQW4qV%2B57HUNzxDzDtkgsWqkKCcRSLv%2FVOt8voUscO2ikqK5naefZrv6hvTXoYb%2FDLZu5fGkvB5phzULp8d1J%2B64ZJcBIC3pXJBlbMNUv%2B6z&X-Amz-Signature=0e3f971407f922aabda1ba21feee7e006f1621c849ad0c10f404f9f75429be69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOJ4UFCP%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIC84BQzlDIkxNYbhyjuzoLpEUpQ4SP3jV%2B91Lh%2BiB4m5AiBdOdLONP6VUtPIdRIDlbHWzx2FJsIED2wkjW%2FCaToMHiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpU93qF%2B%2BAQnPTltwKtwDXiMn3JIe2Ym%2B3AWSB9mYL1fpz%2B09CqTkVF9XCTuqTIsdZQRaCYimjZAAGpi6uORTzs051aOFKZvx1Yappxbqa7iLOW%2F2CLlU9pfgYoHh2LOx0sfYE%2BfXoe3Ot63cmBIGxw4f2E4JXco%2BbkZ4S4YtqIts6ZuvlDAwFuXvoQNhWVekc1g3Zh2VWq4FGq858XkMNzBdbZsn9%2BnuQnGFAyTdBTYolFQL8VQVb9aumuvYFpfTnU9zaE3ZoTsdjZy4oXtyyEBecEa1lCiQ1iU42XycBRs6mvKW3mdd9eI2DU579oMizfdV4YyCWo3rUtvRmGJDPHZjdqr2Kryq4NAl9bJOWHjeUdzW8kAA9%2BV685ThZ4%2BeSRUxlzHjfLiPku%2FqUM2pPUxb3dQxNgEj3siHi%2BTEuE1VikV32K7MCvV57OWY0seEHQSZibvtXQGGiAJdzv94EIhFyPt3SrXTlquZGHbjY3x7BqT22jLxeMPQnsic0xT4ttbawrhAxMpLtvlZKRr3gVmW%2FrdYO%2FSZNdbNxOFod0ZRNtl8kO9jv8E9xX3OrY1fVJb9zQCv9h%2FlXIG9v%2BpVdMlTL%2BJ4a771Lk%2F%2B9KmeA8GpK8fxtj23y0T%2Fu%2FMuAZH7Rq4r5vhzwu8poY8wp%2Br5yAY6pgEY9OJuzMPpKjZqViP5n%2BnbYc9sRVsdFbOPYuAjwpOv7h6XCnqcI9gGH0f9Gs%2FMgu%2FBf4AHrXuvH3cMAm5fJBybJ4xSXRmlKAAowFqULjBPndYIwyFsCQW4qV%2B57HUNzxDzDtkgsWqkKCcRSLv%2FVOt8voUscO2ikqK5naefZrv6hvTXoYb%2FDLZu5fGkvB5phzULp8d1J%2B64ZJcBIC3pXJBlbMNUv%2B6z&X-Amz-Signature=2e4ba1bf7f5e002ce40a1088e8b9cca318cdc9c6dcf6402b1ba0ab79bfbbc9d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOJ4UFCP%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIC84BQzlDIkxNYbhyjuzoLpEUpQ4SP3jV%2B91Lh%2BiB4m5AiBdOdLONP6VUtPIdRIDlbHWzx2FJsIED2wkjW%2FCaToMHiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpU93qF%2B%2BAQnPTltwKtwDXiMn3JIe2Ym%2B3AWSB9mYL1fpz%2B09CqTkVF9XCTuqTIsdZQRaCYimjZAAGpi6uORTzs051aOFKZvx1Yappxbqa7iLOW%2F2CLlU9pfgYoHh2LOx0sfYE%2BfXoe3Ot63cmBIGxw4f2E4JXco%2BbkZ4S4YtqIts6ZuvlDAwFuXvoQNhWVekc1g3Zh2VWq4FGq858XkMNzBdbZsn9%2BnuQnGFAyTdBTYolFQL8VQVb9aumuvYFpfTnU9zaE3ZoTsdjZy4oXtyyEBecEa1lCiQ1iU42XycBRs6mvKW3mdd9eI2DU579oMizfdV4YyCWo3rUtvRmGJDPHZjdqr2Kryq4NAl9bJOWHjeUdzW8kAA9%2BV685ThZ4%2BeSRUxlzHjfLiPku%2FqUM2pPUxb3dQxNgEj3siHi%2BTEuE1VikV32K7MCvV57OWY0seEHQSZibvtXQGGiAJdzv94EIhFyPt3SrXTlquZGHbjY3x7BqT22jLxeMPQnsic0xT4ttbawrhAxMpLtvlZKRr3gVmW%2FrdYO%2FSZNdbNxOFod0ZRNtl8kO9jv8E9xX3OrY1fVJb9zQCv9h%2FlXIG9v%2BpVdMlTL%2BJ4a771Lk%2F%2B9KmeA8GpK8fxtj23y0T%2Fu%2FMuAZH7Rq4r5vhzwu8poY8wp%2Br5yAY6pgEY9OJuzMPpKjZqViP5n%2BnbYc9sRVsdFbOPYuAjwpOv7h6XCnqcI9gGH0f9Gs%2FMgu%2FBf4AHrXuvH3cMAm5fJBybJ4xSXRmlKAAowFqULjBPndYIwyFsCQW4qV%2B57HUNzxDzDtkgsWqkKCcRSLv%2FVOt8voUscO2ikqK5naefZrv6hvTXoYb%2FDLZu5fGkvB5phzULp8d1J%2B64ZJcBIC3pXJBlbMNUv%2B6z&X-Amz-Signature=947aa49f7ef35914e48b4ece938721a3efb65581b5ea8ed433f42b8348660fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

