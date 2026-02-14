---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQBLJ4A%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIDl2WhznQRkFPgohLP1ygFf2k9c3XwfgFLK%2Bkv9DZMInAiEAllqtPl18R3oXbanLIuDO8QlSCP%2BhuMUUKL03906Bck4qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdhEY6YsZb%2Fm%2FosnircA%2BmVW5C8P5ej0Y1XOEfa76CCQvng2GmZ5nZpe3lUsIVbo8YTeM0fdV8x8FsYvGt7h7Mr7aay%2F6pw2tV%2FYPyOpqtx439ChV78Kz9zjG7k0jN%2Bd3v%2F3RogKMRFNWRCsvSdh7qlcu29mmUbCxVGycZ23jRCPFlEDRfm5%2BlCkUsdBqbMvI7%2BUrvJxHpCfWy0%2BZaZKoUtdhGjOCa73bc7BrxqXJ8Ie8NXaBVFKnGU4jCnot8x%2BO0S3MH3c9%2Buj2jSMkfbNXX88vqJXXDjKY7%2Bt160oPwmZn176wzRktwCCqmfIrC%2FO4SQHj2GGsNEncYm7rzxzVbVIl7Xt4GEKax%2BoFJoa8CHfvfEzjsRu7vYlP%2BA74VNAmA8ErLs7yGFQNir8PLBPcH2MqmuDWUxGMch4YfPWB07UAIn2%2F7tGV6S97OZi7VbY645mKIPcEQHSF3duQtCGwvUCoNe%2ByuzX1BEXwcLrRft12qYS4NeoIrGgFCJf%2FXvK9EmYOLREM4d7mjxqXfoU7EpKJohE87PKwxtQjmIsaXEliLBtgaw4cqLNaOkgO6iNW7Um4qcOKygQKZFUCoLusZLrugAYRearhX5eCOQS4sNcJRu3s%2FwrI80zcoZbQutXRovRcpNaPurPD3PMO7Av8wGOqUBHOyfnIZHxRrT3T8RIftsDhS7C9yRB8q4Pl3jH7t%2FLuj96JMGTzEeJaHuUAaeP1YejNaEDB07ASgYpXVV05T5gY88H7YyLMwN9fHb4GaxZbql6LxjD%2FGZ4wYKi0QGXJ3aiQY6hibbGZMEBlTplHL4x2wOZLr0j6fUNoWnelBgSBWPMU07TYIDFXuu1NlQVnUuIt7K%2BsKqQyAhIoz0ZHYpIEWoaNCT&X-Amz-Signature=8110a0e79840f5ad8c06336bbcfdd071a1f0e3c33bac2e9680dac3fd912ff88c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQBLJ4A%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIDl2WhznQRkFPgohLP1ygFf2k9c3XwfgFLK%2Bkv9DZMInAiEAllqtPl18R3oXbanLIuDO8QlSCP%2BhuMUUKL03906Bck4qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdhEY6YsZb%2Fm%2FosnircA%2BmVW5C8P5ej0Y1XOEfa76CCQvng2GmZ5nZpe3lUsIVbo8YTeM0fdV8x8FsYvGt7h7Mr7aay%2F6pw2tV%2FYPyOpqtx439ChV78Kz9zjG7k0jN%2Bd3v%2F3RogKMRFNWRCsvSdh7qlcu29mmUbCxVGycZ23jRCPFlEDRfm5%2BlCkUsdBqbMvI7%2BUrvJxHpCfWy0%2BZaZKoUtdhGjOCa73bc7BrxqXJ8Ie8NXaBVFKnGU4jCnot8x%2BO0S3MH3c9%2Buj2jSMkfbNXX88vqJXXDjKY7%2Bt160oPwmZn176wzRktwCCqmfIrC%2FO4SQHj2GGsNEncYm7rzxzVbVIl7Xt4GEKax%2BoFJoa8CHfvfEzjsRu7vYlP%2BA74VNAmA8ErLs7yGFQNir8PLBPcH2MqmuDWUxGMch4YfPWB07UAIn2%2F7tGV6S97OZi7VbY645mKIPcEQHSF3duQtCGwvUCoNe%2ByuzX1BEXwcLrRft12qYS4NeoIrGgFCJf%2FXvK9EmYOLREM4d7mjxqXfoU7EpKJohE87PKwxtQjmIsaXEliLBtgaw4cqLNaOkgO6iNW7Um4qcOKygQKZFUCoLusZLrugAYRearhX5eCOQS4sNcJRu3s%2FwrI80zcoZbQutXRovRcpNaPurPD3PMO7Av8wGOqUBHOyfnIZHxRrT3T8RIftsDhS7C9yRB8q4Pl3jH7t%2FLuj96JMGTzEeJaHuUAaeP1YejNaEDB07ASgYpXVV05T5gY88H7YyLMwN9fHb4GaxZbql6LxjD%2FGZ4wYKi0QGXJ3aiQY6hibbGZMEBlTplHL4x2wOZLr0j6fUNoWnelBgSBWPMU07TYIDFXuu1NlQVnUuIt7K%2BsKqQyAhIoz0ZHYpIEWoaNCT&X-Amz-Signature=e9e5380dc73ba3be8fa5e9edc2f622d5034c582714e8db203967ee95549094eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



