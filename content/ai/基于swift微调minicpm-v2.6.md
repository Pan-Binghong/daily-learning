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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QA7W6RX%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCiWkJ64DuL8R2mT6lrxlfCFl3C3E2GB0S4IXpXNmetVQIhAPljgH%2BxRFwYV7WwOI0v39Y9SUoWwnm1xU6NVwbSHJ1UKv8DCFIQABoMNjM3NDIzMTgzODA1IgzCeqsa5z4pJiW0rakq3AM0%2FERIT5SEWjJKVtFyW6qQjZXmr64Ld10L%2FDK79abgdFnbDB34HgrLAxyuhfHDx9AX2F4swhPZpz5bd2ChUXXImGFgNbFKkB41PneXkBs8L%2BlCsb1I%2FTi2BEmNTT5wKdo%2FfcWk4ZmJvd0IinkYrhBBrxCaUzR3d3MX0IZWv%2BekMSO%2F8uH6G3YkY8x3Ql1RIZeR7m5CWSOkIue0vQxjry9QqmgIRI%2FMuu3uj5sv2t6ti6m8ifwOzB1EM7OLufnj%2FX9VltjyoQ71cOkrSUVrn%2B6An02eqOaGfPXYncP0yYl8S3V4yZMn%2FFz%2FTdfa0cJCSRvyWyPbU5U7K%2FuIaX9GuOeFPuS%2Bq0otCyPnYK7NXSTrqa7tQZMrwljs3PDQ6K0y0WmpO3Y3TWeYTpglIHWkAjQyTDpc%2F1cew9fzaF5awkYJfUwow0K96zpuluio2kW%2FVs4TmwvjYIQT9KGYO%2FCcznnRIBq5ByQFUrlFtqCVsE2XIuMozilrhqxElyV%2Bt%2Fz5EiNqSaa4sR%2Bi7Ui2wJOeYvWl8lXcTOIhKihzMrSnw7akfRHq8dnOGOVQGJh1YujORQVNIxn8yS2Jfo2eSv73zOjgst3JcsKQN0FO%2FygJBBUz8kz8nwOZGhx6HlpTVDC28sLNBjqkAV8XrIdan5FsPbDvdD77TyNR2bygAp%2BeW7JCuEa23kwTcJMsBiPbwE%2FhY985kHB%2BK8PggzPHtIHBhLdHzcFtAd7w6lnQumPcIcEYBAiAccFGTyXS%2B3%2B0STs0EoZ%2BuUAsSYLhKQ3Tm7YpxDyCoWVPDf%2FfNNueXi4ojjkkfHbu2s93jo%2FOJ3%2Fb1rHb7hw526dNAead9YNTXwihIK%2BQBA9WpOZB5zfI&X-Amz-Signature=9046d72b88ed814d81dd0501624c0aa5c417dec9831547a8e48f6114430bc8a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QA7W6RX%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCiWkJ64DuL8R2mT6lrxlfCFl3C3E2GB0S4IXpXNmetVQIhAPljgH%2BxRFwYV7WwOI0v39Y9SUoWwnm1xU6NVwbSHJ1UKv8DCFIQABoMNjM3NDIzMTgzODA1IgzCeqsa5z4pJiW0rakq3AM0%2FERIT5SEWjJKVtFyW6qQjZXmr64Ld10L%2FDK79abgdFnbDB34HgrLAxyuhfHDx9AX2F4swhPZpz5bd2ChUXXImGFgNbFKkB41PneXkBs8L%2BlCsb1I%2FTi2BEmNTT5wKdo%2FfcWk4ZmJvd0IinkYrhBBrxCaUzR3d3MX0IZWv%2BekMSO%2F8uH6G3YkY8x3Ql1RIZeR7m5CWSOkIue0vQxjry9QqmgIRI%2FMuu3uj5sv2t6ti6m8ifwOzB1EM7OLufnj%2FX9VltjyoQ71cOkrSUVrn%2B6An02eqOaGfPXYncP0yYl8S3V4yZMn%2FFz%2FTdfa0cJCSRvyWyPbU5U7K%2FuIaX9GuOeFPuS%2Bq0otCyPnYK7NXSTrqa7tQZMrwljs3PDQ6K0y0WmpO3Y3TWeYTpglIHWkAjQyTDpc%2F1cew9fzaF5awkYJfUwow0K96zpuluio2kW%2FVs4TmwvjYIQT9KGYO%2FCcznnRIBq5ByQFUrlFtqCVsE2XIuMozilrhqxElyV%2Bt%2Fz5EiNqSaa4sR%2Bi7Ui2wJOeYvWl8lXcTOIhKihzMrSnw7akfRHq8dnOGOVQGJh1YujORQVNIxn8yS2Jfo2eSv73zOjgst3JcsKQN0FO%2FygJBBUz8kz8nwOZGhx6HlpTVDC28sLNBjqkAV8XrIdan5FsPbDvdD77TyNR2bygAp%2BeW7JCuEa23kwTcJMsBiPbwE%2FhY985kHB%2BK8PggzPHtIHBhLdHzcFtAd7w6lnQumPcIcEYBAiAccFGTyXS%2B3%2B0STs0EoZ%2BuUAsSYLhKQ3Tm7YpxDyCoWVPDf%2FfNNueXi4ojjkkfHbu2s93jo%2FOJ3%2Fb1rHb7hw526dNAead9YNTXwihIK%2BQBA9WpOZB5zfI&X-Amz-Signature=b494ec424aaee0a60102ca490fa3f52dcf0943a2d4a34fc116ddb043812f24b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QA7W6RX%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCiWkJ64DuL8R2mT6lrxlfCFl3C3E2GB0S4IXpXNmetVQIhAPljgH%2BxRFwYV7WwOI0v39Y9SUoWwnm1xU6NVwbSHJ1UKv8DCFIQABoMNjM3NDIzMTgzODA1IgzCeqsa5z4pJiW0rakq3AM0%2FERIT5SEWjJKVtFyW6qQjZXmr64Ld10L%2FDK79abgdFnbDB34HgrLAxyuhfHDx9AX2F4swhPZpz5bd2ChUXXImGFgNbFKkB41PneXkBs8L%2BlCsb1I%2FTi2BEmNTT5wKdo%2FfcWk4ZmJvd0IinkYrhBBrxCaUzR3d3MX0IZWv%2BekMSO%2F8uH6G3YkY8x3Ql1RIZeR7m5CWSOkIue0vQxjry9QqmgIRI%2FMuu3uj5sv2t6ti6m8ifwOzB1EM7OLufnj%2FX9VltjyoQ71cOkrSUVrn%2B6An02eqOaGfPXYncP0yYl8S3V4yZMn%2FFz%2FTdfa0cJCSRvyWyPbU5U7K%2FuIaX9GuOeFPuS%2Bq0otCyPnYK7NXSTrqa7tQZMrwljs3PDQ6K0y0WmpO3Y3TWeYTpglIHWkAjQyTDpc%2F1cew9fzaF5awkYJfUwow0K96zpuluio2kW%2FVs4TmwvjYIQT9KGYO%2FCcznnRIBq5ByQFUrlFtqCVsE2XIuMozilrhqxElyV%2Bt%2Fz5EiNqSaa4sR%2Bi7Ui2wJOeYvWl8lXcTOIhKihzMrSnw7akfRHq8dnOGOVQGJh1YujORQVNIxn8yS2Jfo2eSv73zOjgst3JcsKQN0FO%2FygJBBUz8kz8nwOZGhx6HlpTVDC28sLNBjqkAV8XrIdan5FsPbDvdD77TyNR2bygAp%2BeW7JCuEa23kwTcJMsBiPbwE%2FhY985kHB%2BK8PggzPHtIHBhLdHzcFtAd7w6lnQumPcIcEYBAiAccFGTyXS%2B3%2B0STs0EoZ%2BuUAsSYLhKQ3Tm7YpxDyCoWVPDf%2FfNNueXi4ojjkkfHbu2s93jo%2FOJ3%2Fb1rHb7hw526dNAead9YNTXwihIK%2BQBA9WpOZB5zfI&X-Amz-Signature=9e52e0edc190b149e1120f1e876a6320a489d6be22a01abbd7946a694e18cea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

