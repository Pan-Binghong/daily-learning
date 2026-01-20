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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP4JHMO2%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2AaYcNky5l043AtPMU%2Fqsgaf%2B2Awku41aJaTTH81vhAiAC3eQFEq9jf%2FCzTbpVFakQ4Er3chj0qjkJtmHgbR7J1CqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZttrOU4M%2FSbeb5jKtwDZW0ikAjtmeJvNbRHf2JJkJHpdn%2Bq7j8AYOZMka4g38uyPpP7PadY92DKRLy8KtimycoZoFI2v%2FPZVjCHEzR50g84J130uvTcJCeO7Zri6VR0wLcKv1soPl9gKPlP3zhn07DyGdJUdWUfDtlDr%2FpjycFOSgygK%2B0unRAeozzwCNHw0thSFa1hMK5z4psLJ8oXHnnccI2kwsXHZsd%2F3%2F%2BlEWr2rbTqz%2FrTRMhDCnVAAdazL6HfBGD10zzs9CnHG0xft1C%2Bu6XglwhNjpTPn4Dz3o1HDwk8JU6tv%2ByatwZXXYDAy12zjNR%2FTmWxV%2FgS5YFGnByk3LHiYzo49rGSsVxkX%2Bkbf6073dfdej2JOzNre7pPOyb5AT2WvQvuw0FISKO2M7dOZByEIwtwJPcbr5VGxxuwTnNXHVWXd%2B%2FVn4jMiXca%2BhbyquzGJLERb8uXgw8lXfo%2Be0dlHIAN%2F8I71AagSKWqicX7fy6x0qgNlkb4Q8pbzc7BH8tZVTBRZoRGuw%2Fk%2F6CrDvh0AZBOsc%2BW6ZypmuL48nnQIcKHYO4%2FaZcVyXD23jSnE8KGBy4XPu%2FXeiC3kov6pbQxtd5dU%2FPygWYqB8v4gbFN8rxvohZMyJ6KghSUFkVfUFmHZvsO4%2Fww1PS6ywY6pgGBxmu1fj8d3qxScGsISVWrQ0ldnjecSbYype94VXcTEbCctTtYa%2BVHpBvOztpW1UzXL5oVyM6rVKdaRqoJoz2edtd39L1DAKmgAybcJVakRlkUFgq23hnvtVa2G54lSRgaSW5V%2BiiWIG3HknqN6dDJT5cvVyTT8mNqEWJp4q3XLkjWomb1ej3etBShEAjrjOUn3XUFPVj6rm5efizLOilqwAQ%2B5BAe&X-Amz-Signature=fcb12e53a72c7943f4058c7450bdfba9cd1192ad7d6291206f77972a6fb54f4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP4JHMO2%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2AaYcNky5l043AtPMU%2Fqsgaf%2B2Awku41aJaTTH81vhAiAC3eQFEq9jf%2FCzTbpVFakQ4Er3chj0qjkJtmHgbR7J1CqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZttrOU4M%2FSbeb5jKtwDZW0ikAjtmeJvNbRHf2JJkJHpdn%2Bq7j8AYOZMka4g38uyPpP7PadY92DKRLy8KtimycoZoFI2v%2FPZVjCHEzR50g84J130uvTcJCeO7Zri6VR0wLcKv1soPl9gKPlP3zhn07DyGdJUdWUfDtlDr%2FpjycFOSgygK%2B0unRAeozzwCNHw0thSFa1hMK5z4psLJ8oXHnnccI2kwsXHZsd%2F3%2F%2BlEWr2rbTqz%2FrTRMhDCnVAAdazL6HfBGD10zzs9CnHG0xft1C%2Bu6XglwhNjpTPn4Dz3o1HDwk8JU6tv%2ByatwZXXYDAy12zjNR%2FTmWxV%2FgS5YFGnByk3LHiYzo49rGSsVxkX%2Bkbf6073dfdej2JOzNre7pPOyb5AT2WvQvuw0FISKO2M7dOZByEIwtwJPcbr5VGxxuwTnNXHVWXd%2B%2FVn4jMiXca%2BhbyquzGJLERb8uXgw8lXfo%2Be0dlHIAN%2F8I71AagSKWqicX7fy6x0qgNlkb4Q8pbzc7BH8tZVTBRZoRGuw%2Fk%2F6CrDvh0AZBOsc%2BW6ZypmuL48nnQIcKHYO4%2FaZcVyXD23jSnE8KGBy4XPu%2FXeiC3kov6pbQxtd5dU%2FPygWYqB8v4gbFN8rxvohZMyJ6KghSUFkVfUFmHZvsO4%2Fww1PS6ywY6pgGBxmu1fj8d3qxScGsISVWrQ0ldnjecSbYype94VXcTEbCctTtYa%2BVHpBvOztpW1UzXL5oVyM6rVKdaRqoJoz2edtd39L1DAKmgAybcJVakRlkUFgq23hnvtVa2G54lSRgaSW5V%2BiiWIG3HknqN6dDJT5cvVyTT8mNqEWJp4q3XLkjWomb1ej3etBShEAjrjOUn3XUFPVj6rm5efizLOilqwAQ%2B5BAe&X-Amz-Signature=362515f8de6284564ff115b3c1359fae61908582c16badc8f2c2e7c81a7792aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



