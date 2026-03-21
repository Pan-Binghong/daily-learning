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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TXMF5BE%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD%2FNDeXx9Hfk9Zu2pLuashILU2S1%2F3NymthTrxr7no8pQIhAM9qwXdCfNJH9bwYtXPDRzOdcofNb6rIIDqxNmG1SoCwKv8DCEQQABoMNjM3NDIzMTgzODA1IgxClQEXgGS%2BN3sK3Pwq3AMK5i77%2B3x74E5u00wJ15548RFWiPYwPw6j1YhFAe72nE4bunPpeq5As4PUs9etlC7p%2BQmr4r0fEevKzNaC986Lr0wpwkRqnRrCuhHJChUvAb93wxr%2BagN3l8W%2BcKgD8BGuLnnZ0MXCsYih0GU0cTMkMYmx95Z7kImN0zfXOuOz8wvaFGcpk3PAcZI2CZ2SAqa2LrFDAumeMToYlpi%2Bs65xcrDQp0L1Vg7DI4CAHer07sEMAlKy%2FScrG0llPQsQq6DM0ue%2B9FgCD%2Bh41%2BaLgkbO%2FO6vjTxiMdUdp7hdUzVluzYENr%2FLlCKOwxEJ%2BbA5bZqMiS0R84qC%2BMKuKqijjGlesbD8LDBChjcsyCdd0lCoDT7%2FOlMRpsK25h%2BPWcjR63hOfRTTzHj1xBXoJV1lO%2B2gXt8OE3smtyc65FIovVuLMucsXcKuUrPZ2KmDLbh%2FNNiJy2Fsj80e07HAozcAmOkiBeKbdjVcmxyFfUFC4o8rnL7fl5%2BA8YusCsgJYjWoNeSKx4iEJP6crymmLc00BXu3XklsxgQsD439Wtm5WX%2FKd%2FN%2Fr0XkdZuqHFfA9qT9v5u7kdyWKrmcRVwUqef4sfNsq5X8TvPPG04UvSD%2F1P%2Flj2DbFdypsk%2BLz1crJjC1j%2FjNBjqkAeZYCAy1UBT6lkzd3fOrDrw6%2BqT4nzpv2jpzIpXbdfJwHHHhhvmbGQpE9ERJeO9j%2FLKwJBKmVvgIsxxtuDiY9Megug4qYkxNqpoVjtUQoFdcDBo0GLzWDCGz43YHlMHZ2qnEgDBrmx%2FpfqP6dwOMfXHBemjT3GsoBL46EsLmVkAohYVr0ZDsIHgH3XnkckBsgcrqxB83xajAoDcWr7ubD%2FlOy8So&X-Amz-Signature=fb60654e02ef629ad010b4cec28014899cf2533abaac7cecfb8a8849cc3e89cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TXMF5BE%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD%2FNDeXx9Hfk9Zu2pLuashILU2S1%2F3NymthTrxr7no8pQIhAM9qwXdCfNJH9bwYtXPDRzOdcofNb6rIIDqxNmG1SoCwKv8DCEQQABoMNjM3NDIzMTgzODA1IgxClQEXgGS%2BN3sK3Pwq3AMK5i77%2B3x74E5u00wJ15548RFWiPYwPw6j1YhFAe72nE4bunPpeq5As4PUs9etlC7p%2BQmr4r0fEevKzNaC986Lr0wpwkRqnRrCuhHJChUvAb93wxr%2BagN3l8W%2BcKgD8BGuLnnZ0MXCsYih0GU0cTMkMYmx95Z7kImN0zfXOuOz8wvaFGcpk3PAcZI2CZ2SAqa2LrFDAumeMToYlpi%2Bs65xcrDQp0L1Vg7DI4CAHer07sEMAlKy%2FScrG0llPQsQq6DM0ue%2B9FgCD%2Bh41%2BaLgkbO%2FO6vjTxiMdUdp7hdUzVluzYENr%2FLlCKOwxEJ%2BbA5bZqMiS0R84qC%2BMKuKqijjGlesbD8LDBChjcsyCdd0lCoDT7%2FOlMRpsK25h%2BPWcjR63hOfRTTzHj1xBXoJV1lO%2B2gXt8OE3smtyc65FIovVuLMucsXcKuUrPZ2KmDLbh%2FNNiJy2Fsj80e07HAozcAmOkiBeKbdjVcmxyFfUFC4o8rnL7fl5%2BA8YusCsgJYjWoNeSKx4iEJP6crymmLc00BXu3XklsxgQsD439Wtm5WX%2FKd%2FN%2Fr0XkdZuqHFfA9qT9v5u7kdyWKrmcRVwUqef4sfNsq5X8TvPPG04UvSD%2F1P%2Flj2DbFdypsk%2BLz1crJjC1j%2FjNBjqkAeZYCAy1UBT6lkzd3fOrDrw6%2BqT4nzpv2jpzIpXbdfJwHHHhhvmbGQpE9ERJeO9j%2FLKwJBKmVvgIsxxtuDiY9Megug4qYkxNqpoVjtUQoFdcDBo0GLzWDCGz43YHlMHZ2qnEgDBrmx%2FpfqP6dwOMfXHBemjT3GsoBL46EsLmVkAohYVr0ZDsIHgH3XnkckBsgcrqxB83xajAoDcWr7ubD%2FlOy8So&X-Amz-Signature=200714e0d324de246469480b39d97651aeaaf7c54f59fbd136df6b0790781356&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



