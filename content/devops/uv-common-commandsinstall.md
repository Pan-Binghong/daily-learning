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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=553cf57fb0f2cde9b97bdbd602e29e1bfaf2bd12437eeeb9c6c73ab6c297a848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=1dcf570619ce72da944fcecd4f767d32a3a7e8ccb469f201eb64890688236f78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=0cc36fb5fb81af8593731dd2eb8ea58227ab62af7e81682461a786eeb0eee442&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

