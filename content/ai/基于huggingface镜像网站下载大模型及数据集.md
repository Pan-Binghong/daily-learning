---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTVAENG3%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBkYxv25MlOcNaRwk6vX%2F1vaQ3KOra7Y80n6CFOKHmeAiAmagl1juH1LJiHhGUUrGa2Ln9RocOxBRp%2Fs7N74rONCCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMV2TW1kCmvN%2FzjbIFKtwDrb04y%2BBj29tKfOu8O86OFGLcfXXda7XjQzv%2BUugIrn1wWRbg8li0bUKg%2FSJmeqlIHt374Abb5jEj6vriqRDNapd3j31NE5VxYwCWmzGjWWGU%2BMxIWLLOOtnnyaBESsmjoGA2xvV%2BMzueHkDCBLdrPlVG1od5iUprTu0tJp4nTENLEPbtCgIUVQ8PHLaT%2BtUZxhYaMZuoUeCTP24LFmnAkMwpRDzXHFPr5%2F%2FDdftYI91U9aAZn2z7xTOMlagBKXR%2BaIaG3LBlbnaDvKO%2BQOlvbLq6BYlcTCIQc9z1JXZSHwt4kDcrbPWIXlVquvZsacG3MPLTCsRifibxc6kSunjVh5A8A0r%2Bn%2Fp4tXlxgmW7D%2BBd%2F7qMyyibjUw3qmSfcD4GHcSC96TBn2rj9X5TC%2B0aK%2FEYmy8np9e7PO2b5gt%2F%2B7hpfmisMVaODPNHfw9L3Y6GVWbHz1lOpPJMpe1QVvdsWYZsLEuYcZLR845o9m2S1tilKFiUTH3tAFj%2B4Fi21izY8qi1o%2FWcNe8UgaEVoEafS8LMo5b9fro3QwWe1NuassY4aOims%2BQIgxrh%2F%2BZh5zYnfkNg%2B%2F4H9YaWvwGMxz%2By3RHNkf3iK%2B%2BRK8RDQkiSHEVIh8v43igIdzNzyK4w1oyDygY6pgHdSTp4voUahV5BZNts6MhPNH4%2FQtzvTaj0JafTapDnZvYwTG%2BXADsv5ux%2FU4%2BN6n78l%2BUHcjJgooxY%2BVrE0GJDOdqfAM766uiQDAV76ygWaNtbPr9YSaiCUOexWexzCziIyafHZEM7lRiRXJlnP%2Fv%2FgtPlrQqeGRWZab2UV3L91aj8pRpePfjDLHAN99H%2BX1cBEcc3omxodK%2FVcEO5wE2x63kzVWxX&X-Amz-Signature=9250fc060b8dd73d65444cd4e68783f78ef13cb0f384a4b401c25527869db68e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTVAENG3%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBkYxv25MlOcNaRwk6vX%2F1vaQ3KOra7Y80n6CFOKHmeAiAmagl1juH1LJiHhGUUrGa2Ln9RocOxBRp%2Fs7N74rONCCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMV2TW1kCmvN%2FzjbIFKtwDrb04y%2BBj29tKfOu8O86OFGLcfXXda7XjQzv%2BUugIrn1wWRbg8li0bUKg%2FSJmeqlIHt374Abb5jEj6vriqRDNapd3j31NE5VxYwCWmzGjWWGU%2BMxIWLLOOtnnyaBESsmjoGA2xvV%2BMzueHkDCBLdrPlVG1od5iUprTu0tJp4nTENLEPbtCgIUVQ8PHLaT%2BtUZxhYaMZuoUeCTP24LFmnAkMwpRDzXHFPr5%2F%2FDdftYI91U9aAZn2z7xTOMlagBKXR%2BaIaG3LBlbnaDvKO%2BQOlvbLq6BYlcTCIQc9z1JXZSHwt4kDcrbPWIXlVquvZsacG3MPLTCsRifibxc6kSunjVh5A8A0r%2Bn%2Fp4tXlxgmW7D%2BBd%2F7qMyyibjUw3qmSfcD4GHcSC96TBn2rj9X5TC%2B0aK%2FEYmy8np9e7PO2b5gt%2F%2B7hpfmisMVaODPNHfw9L3Y6GVWbHz1lOpPJMpe1QVvdsWYZsLEuYcZLR845o9m2S1tilKFiUTH3tAFj%2B4Fi21izY8qi1o%2FWcNe8UgaEVoEafS8LMo5b9fro3QwWe1NuassY4aOims%2BQIgxrh%2F%2BZh5zYnfkNg%2B%2F4H9YaWvwGMxz%2By3RHNkf3iK%2B%2BRK8RDQkiSHEVIh8v43igIdzNzyK4w1oyDygY6pgHdSTp4voUahV5BZNts6MhPNH4%2FQtzvTaj0JafTapDnZvYwTG%2BXADsv5ux%2FU4%2BN6n78l%2BUHcjJgooxY%2BVrE0GJDOdqfAM766uiQDAV76ygWaNtbPr9YSaiCUOexWexzCziIyafHZEM7lRiRXJlnP%2Fv%2FgtPlrQqeGRWZab2UV3L91aj8pRpePfjDLHAN99H%2BX1cBEcc3omxodK%2FVcEO5wE2x63kzVWxX&X-Amz-Signature=293bba22374c764ff641adeabb71db1b8860f47e128ab0a16d9faf78d7d1d104&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



