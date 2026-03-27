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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKSLRNPT%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIDd72CJ9OQhKGbyU5uYc0DpZxJfiZgiAzm%2FovCM4dvYOAiEA6be7l7h7zJh0s1BABmt%2F9MwM%2ByB1OawjOZoHmhrYnxcqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDkD%2FPHI2hrDx0UvyrcA01zBmYKja9loPMtVohLmmzmbNFzrvQcUht98O%2B1njzIcDIqspwUeEdinE5P4fkAS6GTuSuIZ04irGSay0BiY%2Fya4CXuXAjD78yuzi7QJCSc7Wzh83tlp35EsO9Ou9lD2wPYqE5kQN%2FSASsApL0R5fse%2BVbKmgnPfgxxXWZ0CCo2Z91eGBgCRENiP6GceT6B%2FqpExPT1dVui5gCynwx0MAVswPPP2bhVMNABv7BeOlrAED%2BuXwD%2B%2FH6A8O5W87h6utodggPfq43%2FslT56EKvhR02u7vM5jOQucoxhJT2Blw7v6zFL1LpOnHR6kgALSlnqq8OaYrj%2FcbobS6atIhK9IoGXkdi8WITeH2dMT55l%2BWCmnPaizZt5jG2mK9Ydv%2BI3tYQkNb8fuR9270%2BISA3Cfl2X1Ef9mQxwFo1AUXU6e24vGAHmKIjI%2F%2B00djPhoY%2Fsn7kTiM1vUJLRAovPC%2Ba2rhAVwUpYzkwHaI5fZbh%2B670oKw%2FIVE%2FyDrBciLqKKHd%2FlWDjEiWo3lFbc8Ktqlltht6u1D2A6kxkmyzeQHHyD%2BNTTajRIQN7cgkLIB6MAX%2BKM4xmpgIPyBL5g9xlKoHWjA3a3QhEozEF1W07HHjQK%2B2vEi9C4E6PyYvM3GEMLLtls4GOqUB98mZyLM8LEiI2m%2F9t1kwaVafXCrBzygLbZoYW0LCE6IFKGRtwjo3kiwSELucgDd1sffEjzEsRCUXMXrID%2BeGxaed4BkvunNZQ33J7v6I8YB6k0UY3Z6xbnFce6OlzPu8VUCHjG7q90aWJqF2cKLjNEo1zhB5w6OBh9xNaaiv%2F0b%2B39O%2BYXzs1aGo8LqBAVb4CG1S3gAEkatRRQd5JxE5JDOreDqH&X-Amz-Signature=fd8e6318ff7b09d76b99e737c542049e5e4e177abdf40916a4bf6fb989efe046&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

