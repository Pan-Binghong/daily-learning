---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBS7KBR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCBQk59GDVrfmPT5FHh8n3B0qSX6GDNA7zcPTCeN6L4UQIhAIeZH72C1g5SoPWxa8FVTKbQ3OWKM7E5u0VnKiHSJZwtKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuFHG1QXh0BTYYbvgq3AOh5lPJq8jYr6v05i%2Fn657RY11SznPJGQQKxbbSciNsqttuCZfNLbDbk6mwzOpdhfhkk%2FXfP2qrf7YzsqkILd3NEegaKydoGTsO1LoQ0sJe30AbVutP8H6Q6%2BQ%2FXUJTcKrnivrxfzAeirjqEmIXGImjGAoSQ60n7aCJaO8uOMQlSd6sve0x788h4lPOxQWsmoGveQ6tEETWnhpCBBRg%2FDih2iiz8SdzuQ7FYZ%2FHMkcn1Ufj4cKuGWUYTQHgzyhskit87GSyN%2F2Olh11ohMqUN71ViIA172eNR0nYha%2B9cP4ZyVutyXLd1u3T75tbKiaI%2B2uQWohsvN6F620dVlmi4tMTLOTVHH643%2BduKcn8oNfOluLIQeiveqMnQEUGD9lTPJ27R%2BQVsAY0mgVsIBPZitVzLiS6xzxPQ0x0HXq3HdGePqrPbpexrL3BeGtEP18nel%2FuXQ8F9BaOag1aAveTdw5femImiRbZBL6FMyhEuhXlwhMKkfDTaCR2MVS2F112oBuadfTOw72iTooOKfxNgRuaWLFD2ObFbNdSemrwH6K8cH1rSbE03qipspF3o1ztF8AkOP5v5BuRGLoIoJaRuWIR%2FNSYJGzYzoDvZxDbZQHHOad677XWziCDsO8bzCEntfKBjqkAcbCt96rRW3uJLP3dB6cp9HnrjS0EuuviAV3TbXBTi0Sj3YE%2Fcj3NrxFDQi6HP9lB19ehRCCkIjrtQaziYuLmTf6EatmawJnOtdRd7hRFr0ecVNWMIGymqNKF8HAtgCWaeLelCe15eGmAEXnIXhvw5t3owX3JK1ge2to6AiLNz0%2B6GSRP5P9x9jwiiGrmPUN48PpaSFE86mM02FZ0gr2PoQohxLu&X-Amz-Signature=8b1ef034361c2012bdb9bb5c30008e2cc26c4914d8a302e08b752ea95b075f56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBS7KBR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCBQk59GDVrfmPT5FHh8n3B0qSX6GDNA7zcPTCeN6L4UQIhAIeZH72C1g5SoPWxa8FVTKbQ3OWKM7E5u0VnKiHSJZwtKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuFHG1QXh0BTYYbvgq3AOh5lPJq8jYr6v05i%2Fn657RY11SznPJGQQKxbbSciNsqttuCZfNLbDbk6mwzOpdhfhkk%2FXfP2qrf7YzsqkILd3NEegaKydoGTsO1LoQ0sJe30AbVutP8H6Q6%2BQ%2FXUJTcKrnivrxfzAeirjqEmIXGImjGAoSQ60n7aCJaO8uOMQlSd6sve0x788h4lPOxQWsmoGveQ6tEETWnhpCBBRg%2FDih2iiz8SdzuQ7FYZ%2FHMkcn1Ufj4cKuGWUYTQHgzyhskit87GSyN%2F2Olh11ohMqUN71ViIA172eNR0nYha%2B9cP4ZyVutyXLd1u3T75tbKiaI%2B2uQWohsvN6F620dVlmi4tMTLOTVHH643%2BduKcn8oNfOluLIQeiveqMnQEUGD9lTPJ27R%2BQVsAY0mgVsIBPZitVzLiS6xzxPQ0x0HXq3HdGePqrPbpexrL3BeGtEP18nel%2FuXQ8F9BaOag1aAveTdw5femImiRbZBL6FMyhEuhXlwhMKkfDTaCR2MVS2F112oBuadfTOw72iTooOKfxNgRuaWLFD2ObFbNdSemrwH6K8cH1rSbE03qipspF3o1ztF8AkOP5v5BuRGLoIoJaRuWIR%2FNSYJGzYzoDvZxDbZQHHOad677XWziCDsO8bzCEntfKBjqkAcbCt96rRW3uJLP3dB6cp9HnrjS0EuuviAV3TbXBTi0Sj3YE%2Fcj3NrxFDQi6HP9lB19ehRCCkIjrtQaziYuLmTf6EatmawJnOtdRd7hRFr0ecVNWMIGymqNKF8HAtgCWaeLelCe15eGmAEXnIXhvw5t3owX3JK1ge2to6AiLNz0%2B6GSRP5P9x9jwiiGrmPUN48PpaSFE86mM02FZ0gr2PoQohxLu&X-Amz-Signature=6e6109fdcc514337746c843916fe34df5e94b409ca4f81ab85fa4fea26a83d25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBS7KBR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCBQk59GDVrfmPT5FHh8n3B0qSX6GDNA7zcPTCeN6L4UQIhAIeZH72C1g5SoPWxa8FVTKbQ3OWKM7E5u0VnKiHSJZwtKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuFHG1QXh0BTYYbvgq3AOh5lPJq8jYr6v05i%2Fn657RY11SznPJGQQKxbbSciNsqttuCZfNLbDbk6mwzOpdhfhkk%2FXfP2qrf7YzsqkILd3NEegaKydoGTsO1LoQ0sJe30AbVutP8H6Q6%2BQ%2FXUJTcKrnivrxfzAeirjqEmIXGImjGAoSQ60n7aCJaO8uOMQlSd6sve0x788h4lPOxQWsmoGveQ6tEETWnhpCBBRg%2FDih2iiz8SdzuQ7FYZ%2FHMkcn1Ufj4cKuGWUYTQHgzyhskit87GSyN%2F2Olh11ohMqUN71ViIA172eNR0nYha%2B9cP4ZyVutyXLd1u3T75tbKiaI%2B2uQWohsvN6F620dVlmi4tMTLOTVHH643%2BduKcn8oNfOluLIQeiveqMnQEUGD9lTPJ27R%2BQVsAY0mgVsIBPZitVzLiS6xzxPQ0x0HXq3HdGePqrPbpexrL3BeGtEP18nel%2FuXQ8F9BaOag1aAveTdw5femImiRbZBL6FMyhEuhXlwhMKkfDTaCR2MVS2F112oBuadfTOw72iTooOKfxNgRuaWLFD2ObFbNdSemrwH6K8cH1rSbE03qipspF3o1ztF8AkOP5v5BuRGLoIoJaRuWIR%2FNSYJGzYzoDvZxDbZQHHOad677XWziCDsO8bzCEntfKBjqkAcbCt96rRW3uJLP3dB6cp9HnrjS0EuuviAV3TbXBTi0Sj3YE%2Fcj3NrxFDQi6HP9lB19ehRCCkIjrtQaziYuLmTf6EatmawJnOtdRd7hRFr0ecVNWMIGymqNKF8HAtgCWaeLelCe15eGmAEXnIXhvw5t3owX3JK1ge2to6AiLNz0%2B6GSRP5P9x9jwiiGrmPUN48PpaSFE86mM02FZ0gr2PoQohxLu&X-Amz-Signature=b753be172e55e8cdd4bb8fcd6cbf78e055a9aafbf29b48752fa81f2279befca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

