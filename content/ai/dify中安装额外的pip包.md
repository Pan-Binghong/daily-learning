---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGZK4M76%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQDmbxTD4q4gwZzrjhg2zTO2FO7paEjmywH0H47M0WhLxgIhAMv8FvdLtNlVP6oCTYAnherd31Xdc%2FB9WDqazGp0O4jbKv8DCDsQABoMNjM3NDIzMTgzODA1IgwNmDm6tTtwR%2BSBz3Mq3AOhH3mVJy%2FwV9BvqNlp33K%2FUlqER7swx2WE4DQUDhzQvpyXZaoonEPTDVivPEyQyLvfa%2FNeH4g362PojEL7D6E%2BjBXkDpEYpKXEnxHc1jd%2FZsh4ns0OzUQxJsO1TAxJlSXp69Eqr5KcL4TNHpAJx75SWPBKlY2E4N0oPtxy0jk3dnvIrr%2BqW2PXqD%2BJv8mhjuwlCtMN%2F48WPAyBoHtExi53rS7O62Lgiyipu7ELaJFLdQQELpwiEUx7fx0y21K1z58Ip3GFLXB37c59yIgAYfuwSTEbonjGbfwxWM4m6jbSBhEDeScsRfnD7SIUr6dvY1EN8qfWuhnYtMQtlSVu3MekNEGgHHZ9S9204Oumc%2Fd7jt8Y0Aq6fxsMXoXmvnuN22VrmBoTbCaqf2xUhf3EneMiy9cud2WpNO4xicdI9ePkgfOdnQr9IG0iFUvzJUunx7PaOaZx2Pkvb0Om1fE9JP6EQuBpf0QmAdEsQNKQvRG3j8rfxyltPaAhrjA0gciXfq%2BnOfJYKgO1r7wv6pDoaCX2Vv7965%2FzRP5H7mocKi7dfp73DuZ8OHFtenvKGp2%2FycYoa9WwW%2BlKhGmcJ02sUnq9FqQmMVh0tzJxwP15%2FxDlitqOamzFdyw7ATUn1jDPvezKBjqkAejSZiPFgs%2Fw3uhaRSzirgCNqu8XzcuHf97Xe6CMAFzmsIjr3AYwQiXdGUR4bj4CZM98%2F%2FCx39kCfrIfUZXPDHaVduO2SK%2FdTyysWE7W0pQ1%2FMdqObHkEsHKVzMEM2Mz2n%2FtVQRgtp%2F%2BpZEiVVOGKP%2FDj4UuNKffL%2BDxsfGeNXpg%2FYxc3DPqhYFyesl%2BULGUj7vhYhbBH94ozJQK%2BhVkeI%2F9q2pd&X-Amz-Signature=7fd11ce580b08d737775be0d9ecb12045a547cf2aa2ec463e30ee19c0f06efa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

