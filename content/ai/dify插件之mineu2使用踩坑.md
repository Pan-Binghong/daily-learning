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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645VSNYEM%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCID3GB%2F60GSJXGbkcSlGNDh96JjgSMCPtf3v4I8G27Rr%2FAiAx2mvC95iE0ReHP0sCRAZ002pG5iikmWl7qn5CrVhg1yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHLYlVO1XQC%2FjBv1QKtwDttvcmGbc5DrmKZPcmP6beEo6EcMuCfvUTKDWo%2BJLwtPXrpldMD6EuYqx2fUs%2FPhS9UXgF5gv5YipwLlVi%2Fi7LuUlTfEGPHC1R%2FTYogiPARTPszYEZ25YcMvynikLxnfK6uxu3WTtbAOwZsInlcvlbiXg6UBuFZiXRSFiU7ApkAQkbZb8BYCQvvu0sjTaPC4CRqva1jSHgBlhKaKwK9iM7KwmdW7zQvNPNX9MasRDklLZjTnsEJNpL%2F%2Feiy9cSgn37sBLJl%2BI5jYlQbYrL%2BiWH5jCLoSc1fAPAORSPpwRDaNmVkXsqAf812f%2F5f%2B0OIwufAJG%2FzguiQ5iB8TOmoF1rjQWMjfnz%2BUWhSSNMXhI2hlJFvhb17iB1DToakBtGzSplSOXamAafR1yowi%2BkduipUJ77ckkbBF1u%2Blq6v0BnndZxyGHLqhFVPa0p23A%2Bhha2%2FLylxjWsq4lVfmIyAW8L7lXQj2Rr3PCumFl5LSt5fWRioKEct7USgcFz2nueff5cbs2afUSBMYUXidKsB8fOWo1%2FxY8M0wXqFbx7n92gj4rOGQMDyugWDP6UE%2F8qPhmYAO0g64EpQCtaYHvY48quOPYE7uvi066HcDAFqz6yo1T6nhUpB0XiT7M8R8wgpXKzAY6pgEf%2FK5kEZddH24YDqqVz30bD0YW73I%2B5z6psa6Dk7yK%2F0KnI5jCzK6jHYmxHzmJtQVmE%2FTIEcpjc%2F%2FhRokc2%2Faq5avBBMSeipAnjyVSBM9LNxjctseW37VMVJV7Mz4DgoVzW8lNdC6LvhWgBsq%2BPXrAaJEyX%2BWGWeEe15bSgM%2FYhxivs6A9gSFgSvoeIzpBvxFHz%2BHmohgsrF2t%2BpQnMR%2FDXaTF3fgw&X-Amz-Signature=dbbfcc6cde8b7b82943b8604e0a0beba4439824f0a0e1d5455e840f93b35f466&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645VSNYEM%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCID3GB%2F60GSJXGbkcSlGNDh96JjgSMCPtf3v4I8G27Rr%2FAiAx2mvC95iE0ReHP0sCRAZ002pG5iikmWl7qn5CrVhg1yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHLYlVO1XQC%2FjBv1QKtwDttvcmGbc5DrmKZPcmP6beEo6EcMuCfvUTKDWo%2BJLwtPXrpldMD6EuYqx2fUs%2FPhS9UXgF5gv5YipwLlVi%2Fi7LuUlTfEGPHC1R%2FTYogiPARTPszYEZ25YcMvynikLxnfK6uxu3WTtbAOwZsInlcvlbiXg6UBuFZiXRSFiU7ApkAQkbZb8BYCQvvu0sjTaPC4CRqva1jSHgBlhKaKwK9iM7KwmdW7zQvNPNX9MasRDklLZjTnsEJNpL%2F%2Feiy9cSgn37sBLJl%2BI5jYlQbYrL%2BiWH5jCLoSc1fAPAORSPpwRDaNmVkXsqAf812f%2F5f%2B0OIwufAJG%2FzguiQ5iB8TOmoF1rjQWMjfnz%2BUWhSSNMXhI2hlJFvhb17iB1DToakBtGzSplSOXamAafR1yowi%2BkduipUJ77ckkbBF1u%2Blq6v0BnndZxyGHLqhFVPa0p23A%2Bhha2%2FLylxjWsq4lVfmIyAW8L7lXQj2Rr3PCumFl5LSt5fWRioKEct7USgcFz2nueff5cbs2afUSBMYUXidKsB8fOWo1%2FxY8M0wXqFbx7n92gj4rOGQMDyugWDP6UE%2F8qPhmYAO0g64EpQCtaYHvY48quOPYE7uvi066HcDAFqz6yo1T6nhUpB0XiT7M8R8wgpXKzAY6pgEf%2FK5kEZddH24YDqqVz30bD0YW73I%2B5z6psa6Dk7yK%2F0KnI5jCzK6jHYmxHzmJtQVmE%2FTIEcpjc%2F%2FhRokc2%2Faq5avBBMSeipAnjyVSBM9LNxjctseW37VMVJV7Mz4DgoVzW8lNdC6LvhWgBsq%2BPXrAaJEyX%2BWGWeEe15bSgM%2FYhxivs6A9gSFgSvoeIzpBvxFHz%2BHmohgsrF2t%2BpQnMR%2FDXaTF3fgw&X-Amz-Signature=c7728397bb97ac33cd00eb64e2975905b6da14caf7878de5f9a16e6d117bfd03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



