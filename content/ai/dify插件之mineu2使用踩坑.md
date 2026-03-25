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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PYYDF6J%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFemOxgsr1gsE3oa4U2QP4kDBGakrpgQRckJzmeDcVQAiEAzlv2pHK9ed0NEkTFYYBFB81Xwhn0%2FS4uhzDsLJXAFHkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMRLNf8k%2BsI2lmDnircA7bdrUUdj40gCZ58BCOIsjRSZvPcE6aoJ5l7vT9d5piQ27i%2Fs6wMhko58JGeoZ%2BGPYjMNdCuxBlbxsqvZROP8kXcgPR1I1i32P3DQPkZqlojPRjY6NcPeYSorq%2B1GBC8UEvBmTpkSRi0mhVkgKlnhdTNUANGi33pM9R8NyS7sB3S9RrD3df8BEmNtnZPHGzpiC6jMfL3ftTyUTxXV6KHMIJXL99CnRdo4ZU8lnWrugV4nrEP0lcNdZkxuXV9RUpsUpvYrbi08gyEmj8IvuJN4hVUKPn%2FYbgfqJHtEbyhKkVu6lvq6Ovg7c0D7uOrrTU9kv3rJmvPx1oJSJa0GNmYwp9FovSX3UaPGIq67bgyRCl6coylLpKbIfB6rd1lmAnAcufyozFrYv5dtXWDggmcaWVFV9NQjyacjkaGpdnBfcybvwgK%2FCqt%2FEQfRW5IuhPlokJScdT5bcKxk9a8eanN5uMXF0Zt7oUwGV5Epbpr6RINV%2BRHm9%2BsPJFGxTN79Kpj%2F3T6KJtavDfHYHv8qBmmzc5xt0WDbXsuknEm%2FT84SeK03oMn2uAsKqvk%2F3vDd0ehAMRt9WLzii%2BHwccqBcicdlYT0rUlaPGXUBhoAE40o1jQC9BbnABHGch6A7EXMMukjc4GOqUBJcPvaZF5juuE8kwnna5seRpvq2%2BgCwEjphAwIztHYpi8kBigOPI3%2BsZ95JHqOidowB7DtjgI%2Bxlnjcw%2BG961oPGtKGZ7jjn%2BnpYJ7STDTdYHEzu889%2FTKYjw6avA6Ih%2FBHPrmDHVaBck372%2FuUCTsWprr8uXG0DdRMDdrADDZN%2FNlNqnd76k995J%2FLmtMaNR1K30%2BuZZ2PnEQBL3l%2F5dz36LQD%2Bv&X-Amz-Signature=e7f3d8c541fc15e7ebd9bb171f63feb6fccca7bc9d4e07db39fa7929ea34879f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PYYDF6J%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFemOxgsr1gsE3oa4U2QP4kDBGakrpgQRckJzmeDcVQAiEAzlv2pHK9ed0NEkTFYYBFB81Xwhn0%2FS4uhzDsLJXAFHkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMRLNf8k%2BsI2lmDnircA7bdrUUdj40gCZ58BCOIsjRSZvPcE6aoJ5l7vT9d5piQ27i%2Fs6wMhko58JGeoZ%2BGPYjMNdCuxBlbxsqvZROP8kXcgPR1I1i32P3DQPkZqlojPRjY6NcPeYSorq%2B1GBC8UEvBmTpkSRi0mhVkgKlnhdTNUANGi33pM9R8NyS7sB3S9RrD3df8BEmNtnZPHGzpiC6jMfL3ftTyUTxXV6KHMIJXL99CnRdo4ZU8lnWrugV4nrEP0lcNdZkxuXV9RUpsUpvYrbi08gyEmj8IvuJN4hVUKPn%2FYbgfqJHtEbyhKkVu6lvq6Ovg7c0D7uOrrTU9kv3rJmvPx1oJSJa0GNmYwp9FovSX3UaPGIq67bgyRCl6coylLpKbIfB6rd1lmAnAcufyozFrYv5dtXWDggmcaWVFV9NQjyacjkaGpdnBfcybvwgK%2FCqt%2FEQfRW5IuhPlokJScdT5bcKxk9a8eanN5uMXF0Zt7oUwGV5Epbpr6RINV%2BRHm9%2BsPJFGxTN79Kpj%2F3T6KJtavDfHYHv8qBmmzc5xt0WDbXsuknEm%2FT84SeK03oMn2uAsKqvk%2F3vDd0ehAMRt9WLzii%2BHwccqBcicdlYT0rUlaPGXUBhoAE40o1jQC9BbnABHGch6A7EXMMukjc4GOqUBJcPvaZF5juuE8kwnna5seRpvq2%2BgCwEjphAwIztHYpi8kBigOPI3%2BsZ95JHqOidowB7DtjgI%2Bxlnjcw%2BG961oPGtKGZ7jjn%2BnpYJ7STDTdYHEzu889%2FTKYjw6avA6Ih%2FBHPrmDHVaBck372%2FuUCTsWprr8uXG0DdRMDdrADDZN%2FNlNqnd76k995J%2FLmtMaNR1K30%2BuZZ2PnEQBL3l%2F5dz36LQD%2Bv&X-Amz-Signature=4a3d4b842ceb8c2849059905e52fb14b4014056dd523ee19b7c8d3d7c521b3f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



