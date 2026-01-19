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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OXPETDF%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhspLbncO6RWCUdcYZqOq%2Fs0x70i55pvj1CG5RnZjZwAiEAmEF%2BEACjX2NPk0wRHYfYhcoTHf1qJByEfgcdIxpFxREqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcBsQJJ0LjeQmlxcircA%2BJQcGWHk9pFVz4SvZF6C8lVwWRApqmgXXvdVqkuKJ8LGrfkhX4YI%2FOnv4n0%2FN%2BGjvAPIzaswVOZZeX4CzqBBbFc8o1VPz7sclVXk4SiNQizGZCye%2FNJq4SVAKIk8a3UqGJlEPU9De1kMfHHhd8K5nv6RvVNARExhlykDvKjWqUgnxOh6uHgErj4r8KgXB%2BmiwIY5qRwD2VqSk%2BYlW3%2BxQ51xfSLwUdgeQR9NWBi3cexhoF9jnNxTmFomeXYgyuMDGmEE7YOpFNivsTtWQpRIfdPlzqwTADm2V2zyXw2kh9HYXHk%2Bq%2Fjj3sfRRDCw3X7Zl6t%2Bj93j%2BhXPyN%2FopuAIpOEhYQUAqEp7H775Y7BPe%2BXTUeorj59s1GX0MZRkmZKc9ruKh313p7a1HRo4k6T3rXZPlTWT9Vxvf5UAaNW3MpF2QAISMs58TCS2dM3x6ziz6g29uEJVANRsfflO%2F8pGjZJB3OYyvVg8k4TMyqyhihHvNklflHdLEpO6IW0H0sza44JAZVynwQbPQy1YaseWDQji6LWavJN1my6WEbW7soNqlcGa2yh1jV7HDpgS98RKiP7k%2FnEbjplRq5v9CzAnpqrVYdrKxW7mudLNab90oMrtKG4eAUDwjeHteZ%2FMO%2FdtcsGOqUBxW8TRL8Nq1AeZShrX1fQ3sEGbYlNjhs2Jdr2%2B%2Be0tTGlXtvcCF1c3gnY%2BclOMVbvDzQlV%2Fh6S6Oufn2OSaCLvZ0HeBqZT9YTMrHTVC57bl0G6NeaBOB2OwaQI0lFkuJv2U9tC2HzejtDhGwd%2BZgCtEMNhmWuDdBTf4RsZTVwT8nIXBrR%2Fb1jhMyMR7YfPA5Rsb65uW2Adb2uynMWDafnGR0pIIXB&X-Amz-Signature=7c670aecdb03c93c58fbc2fcc2c941b8c2260ecbdfeaf5503f8dd9bf601f0c07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OXPETDF%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhspLbncO6RWCUdcYZqOq%2Fs0x70i55pvj1CG5RnZjZwAiEAmEF%2BEACjX2NPk0wRHYfYhcoTHf1qJByEfgcdIxpFxREqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcBsQJJ0LjeQmlxcircA%2BJQcGWHk9pFVz4SvZF6C8lVwWRApqmgXXvdVqkuKJ8LGrfkhX4YI%2FOnv4n0%2FN%2BGjvAPIzaswVOZZeX4CzqBBbFc8o1VPz7sclVXk4SiNQizGZCye%2FNJq4SVAKIk8a3UqGJlEPU9De1kMfHHhd8K5nv6RvVNARExhlykDvKjWqUgnxOh6uHgErj4r8KgXB%2BmiwIY5qRwD2VqSk%2BYlW3%2BxQ51xfSLwUdgeQR9NWBi3cexhoF9jnNxTmFomeXYgyuMDGmEE7YOpFNivsTtWQpRIfdPlzqwTADm2V2zyXw2kh9HYXHk%2Bq%2Fjj3sfRRDCw3X7Zl6t%2Bj93j%2BhXPyN%2FopuAIpOEhYQUAqEp7H775Y7BPe%2BXTUeorj59s1GX0MZRkmZKc9ruKh313p7a1HRo4k6T3rXZPlTWT9Vxvf5UAaNW3MpF2QAISMs58TCS2dM3x6ziz6g29uEJVANRsfflO%2F8pGjZJB3OYyvVg8k4TMyqyhihHvNklflHdLEpO6IW0H0sza44JAZVynwQbPQy1YaseWDQji6LWavJN1my6WEbW7soNqlcGa2yh1jV7HDpgS98RKiP7k%2FnEbjplRq5v9CzAnpqrVYdrKxW7mudLNab90oMrtKG4eAUDwjeHteZ%2FMO%2FdtcsGOqUBxW8TRL8Nq1AeZShrX1fQ3sEGbYlNjhs2Jdr2%2B%2Be0tTGlXtvcCF1c3gnY%2BclOMVbvDzQlV%2Fh6S6Oufn2OSaCLvZ0HeBqZT9YTMrHTVC57bl0G6NeaBOB2OwaQI0lFkuJv2U9tC2HzejtDhGwd%2BZgCtEMNhmWuDdBTf4RsZTVwT8nIXBrR%2Fb1jhMyMR7YfPA5Rsb65uW2Adb2uynMWDafnGR0pIIXB&X-Amz-Signature=083c1f73bfa115f1dc969f29b56e29e556322c660ff48ced7061d9d19d749a8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

