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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YJA3CWN%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0W8mr281aFNVhBjwxQEg2KeXZGvbtB5rKq%2FatTU%2BoJAiB9joo55zB2BWx2jlaqOXThuymF4GEWt7fFqqjuKvammyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0%2BuTqCikzs%2BBQb9%2FKtwDqfMpZzbFJIHIIEze63nC9co8zZX%2Bhn35geCFvrjVLG51mEbFc5wu2IZ7dxp3yvddOtteyaYvPk4wOnBAnHie2Dnwl8Ec4X%2BealX8GP0yI6tBAQZd9czrq4%2FNpiaSSHiME%2BKxn%2B17QbpS3S3LfWW8YR9TM6mwVI1pPlJtxlhqRIv5b%2BsztdbafYbN4Q7h5e17jHAj5r0ZqtQ%2B3%2FuoXsovT%2BlN2GRDhOoqyu45VmY9vDTHpB55nWff4E1k7YtpNVrBR2fvqATN3jEhwYQZ4Zjf7%2F5reVXX%2Bw5kt7z2sHYzMum3o7Hol3lCfWU1VG%2B4JPLI0geR16xqo4riwLBuDu32mRZegPeRu0aR4U14dP%2FybGmL2mbqBENNmA8IHwhFIflMww7c4dYWM8IOeDzUDBbsaoR9JN7wXa5WTMPl%2BiBOW4u%2BdUwIucNJvPc%2FLxjvKheWyMrIQByf3CNHEiT4pXpMH1czliEFI6HWbP5XvhQfc%2FrkajmaLEOa6pyr7m7IqUTHVN7StSslwP1d0TRdqX2AaeAAUainFkJOO91ga%2FTK3mBPZQRR%2FhhlusOyURW97W0ebAtmyI8TADisRx5UWiSCCclH%2B9OZpEdn25uYxJfHpY%2FEeM8opRLIR47j8nAw1%2FGwzwY6pgFJOhQdTFp0wnOyvmiIDixnxg%2FLXtsrdfutFTe2n4QdOqY2pXw%2BWnrlK38L3HlguNiGHa7PR6fe2IL9%2BxJwzdxTcaSbgOjZ5mGHg7FE13Nm3yvPIU%2BmbbsV03pO01mJZ%2F67JwoNp5WMOm%2FI%2FBw6UIAnuQbi2LS%2FeovI1nCtFD9%2F5YqrPlrH%2Bmf31AIdDHn4mmE44ethB6syzWwkJ4EnTc2u0Yhq4W%2Fd&X-Amz-Signature=e599d2593e5d1c969166ea7266408ae19153d9679c1a9667f834cb240a31f673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YJA3CWN%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0W8mr281aFNVhBjwxQEg2KeXZGvbtB5rKq%2FatTU%2BoJAiB9joo55zB2BWx2jlaqOXThuymF4GEWt7fFqqjuKvammyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0%2BuTqCikzs%2BBQb9%2FKtwDqfMpZzbFJIHIIEze63nC9co8zZX%2Bhn35geCFvrjVLG51mEbFc5wu2IZ7dxp3yvddOtteyaYvPk4wOnBAnHie2Dnwl8Ec4X%2BealX8GP0yI6tBAQZd9czrq4%2FNpiaSSHiME%2BKxn%2B17QbpS3S3LfWW8YR9TM6mwVI1pPlJtxlhqRIv5b%2BsztdbafYbN4Q7h5e17jHAj5r0ZqtQ%2B3%2FuoXsovT%2BlN2GRDhOoqyu45VmY9vDTHpB55nWff4E1k7YtpNVrBR2fvqATN3jEhwYQZ4Zjf7%2F5reVXX%2Bw5kt7z2sHYzMum3o7Hol3lCfWU1VG%2B4JPLI0geR16xqo4riwLBuDu32mRZegPeRu0aR4U14dP%2FybGmL2mbqBENNmA8IHwhFIflMww7c4dYWM8IOeDzUDBbsaoR9JN7wXa5WTMPl%2BiBOW4u%2BdUwIucNJvPc%2FLxjvKheWyMrIQByf3CNHEiT4pXpMH1czliEFI6HWbP5XvhQfc%2FrkajmaLEOa6pyr7m7IqUTHVN7StSslwP1d0TRdqX2AaeAAUainFkJOO91ga%2FTK3mBPZQRR%2FhhlusOyURW97W0ebAtmyI8TADisRx5UWiSCCclH%2B9OZpEdn25uYxJfHpY%2FEeM8opRLIR47j8nAw1%2FGwzwY6pgFJOhQdTFp0wnOyvmiIDixnxg%2FLXtsrdfutFTe2n4QdOqY2pXw%2BWnrlK38L3HlguNiGHa7PR6fe2IL9%2BxJwzdxTcaSbgOjZ5mGHg7FE13Nm3yvPIU%2BmbbsV03pO01mJZ%2F67JwoNp5WMOm%2FI%2FBw6UIAnuQbi2LS%2FeovI1nCtFD9%2F5YqrPlrH%2Bmf31AIdDHn4mmE44ethB6syzWwkJ4EnTc2u0Yhq4W%2Fd&X-Amz-Signature=c04e18c7b1abafca485a15554471b820d2fbea0b4f1b19b554513318eb69503d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



