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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UVP6UPM%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIHA6D2V3Bmo4%2F87VFW7c0qOQaTMgII4HiGvmCM%2FjFQXyAiB3YwlUuGCC1shfa9KDtemaTFFLqEKrSHfJuApstI1AUyqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIswzBxPqMmF7UsaGKtwDEM8re9Obrvu97RevA8UliPm0SpttMnkrfPsujzm%2FfIFU5mOmcyIEPd8hsz2%2BEZSs2AMjWfVLiGkhP466mADeiohbvJ4NCKxKlEhpFBii2URw254e8rb5BfiWRTMICjHi5GTCVhozmkYueshdOZ4zTk6nvnZYYSb5DC4W2jo14I1DYnJWuy7zg1UjJhsRH%2FRVcZgsy4kXv5lDQ0zTrRSZ9jdagG%2F0sKaUWJqdZtpvCTl5tNJsOQ8qrkhnEIEO18%2BX5mMsGbAUz7kmx5Gnnp7%2B5v9YsEd8V78XD4Lwdd2%2BkyrB0pdE4YbSFfdMgNJmi9SaFaupetdY66smcaOvKueOU1MgEPIZb6sQhGRG28AcmXXLZ%2BUltJ5AFHfv1M0iCS7KU0jwrSw%2FZKrmpjx0LJ%2FOgG2pVFlHiOnTLDDmNUY9DzSX90Ij8bcMjXyab5EqHxE7HjuIflw4JLn71Xy6yTu00bz%2B5Qivr8nHkatf8lG0IQo61ZxNHIkBDgBxcHO5N3LCIn05%2Bo6gTnp6vzKpavWvli8QGEGmwzjt9Hh%2B9WltjIefDdcmli4QdRYlp4rTYkqKTlAkgSiwe%2BscRQLkE%2FkERVSJJrQ7Dzsym3DBulNPEVmuES90EG7bBFKYCEAw6e3FzwY6pgHTfJKld9IfxfuYvUk1ONkY%2BCyYruIF5avH2UyIMu%2FUQI413Eq2%2F9TkT4uMruGomuempPIz4w8a2hGid7inYirTp8U7wE4tofAjiQQ%2Ba2NtZVgWTCgbQgX%2FCo6hB%2B9lb5UYO6fHWjbM%2F7TxvkeIbFAOQ5OTDJhUdRlZClSTYFEVi8qb%2FmwmHNDjYqWhE%2FwOF7984W9Hqto3yphYlAQtFusUxr4xOzr7&X-Amz-Signature=841786ed6059b4d78f5071b0fde6cf44d9098dc9c608c48915e4f11f6456432f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UVP6UPM%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIHA6D2V3Bmo4%2F87VFW7c0qOQaTMgII4HiGvmCM%2FjFQXyAiB3YwlUuGCC1shfa9KDtemaTFFLqEKrSHfJuApstI1AUyqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIswzBxPqMmF7UsaGKtwDEM8re9Obrvu97RevA8UliPm0SpttMnkrfPsujzm%2FfIFU5mOmcyIEPd8hsz2%2BEZSs2AMjWfVLiGkhP466mADeiohbvJ4NCKxKlEhpFBii2URw254e8rb5BfiWRTMICjHi5GTCVhozmkYueshdOZ4zTk6nvnZYYSb5DC4W2jo14I1DYnJWuy7zg1UjJhsRH%2FRVcZgsy4kXv5lDQ0zTrRSZ9jdagG%2F0sKaUWJqdZtpvCTl5tNJsOQ8qrkhnEIEO18%2BX5mMsGbAUz7kmx5Gnnp7%2B5v9YsEd8V78XD4Lwdd2%2BkyrB0pdE4YbSFfdMgNJmi9SaFaupetdY66smcaOvKueOU1MgEPIZb6sQhGRG28AcmXXLZ%2BUltJ5AFHfv1M0iCS7KU0jwrSw%2FZKrmpjx0LJ%2FOgG2pVFlHiOnTLDDmNUY9DzSX90Ij8bcMjXyab5EqHxE7HjuIflw4JLn71Xy6yTu00bz%2B5Qivr8nHkatf8lG0IQo61ZxNHIkBDgBxcHO5N3LCIn05%2Bo6gTnp6vzKpavWvli8QGEGmwzjt9Hh%2B9WltjIefDdcmli4QdRYlp4rTYkqKTlAkgSiwe%2BscRQLkE%2FkERVSJJrQ7Dzsym3DBulNPEVmuES90EG7bBFKYCEAw6e3FzwY6pgHTfJKld9IfxfuYvUk1ONkY%2BCyYruIF5avH2UyIMu%2FUQI413Eq2%2F9TkT4uMruGomuempPIz4w8a2hGid7inYirTp8U7wE4tofAjiQQ%2Ba2NtZVgWTCgbQgX%2FCo6hB%2B9lb5UYO6fHWjbM%2F7TxvkeIbFAOQ5OTDJhUdRlZClSTYFEVi8qb%2FmwmHNDjYqWhE%2FwOF7984W9Hqto3yphYlAQtFusUxr4xOzr7&X-Amz-Signature=4532808a97a7bcb4594622735a6a9ee6bbcbd8c52116205aa7fbc51385f20288&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



