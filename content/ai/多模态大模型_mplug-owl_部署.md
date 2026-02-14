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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5FEYNY%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQD4toG1AybUaCB7cYkIk1TCrguVP2XQWu6a2%2Bp%2B415WcwIgWWGpCFAHoTJVL2wiVDJCnbTbs7xQMfaVjJdaRmwP4pMqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwuDE5HgN2e97cIlyrcA%2BFVspnl14imzS7Gi463f21%2Fk%2FuoJxhluOA0BIcnJ%2BH4NQqX4lTYA%2F6DFMD8lPw%2BpvTuO%2BXGfKa34WcMkK%2FEBjWoopq%2BXdL3Y%2F%2Bs%2F3bSZaqabIsABf1WWht0SIYANTqH8l38fOlEE0%2FFxD8DGk1XrQ1aKCyQbOnDUjjqw6YUrZ75hW68V8TUD6gEO5iLgDqJYDlNqFqp47W3HoYiH8wtzXMA5jHRRybuAwjxP%2B8q1tk4cTu47iRob5hwXwsIKK%2BWRlSCMrApchoCr6YCYFT1eEO3fWWUsfH%2BvsqeehM9NDDNgEEWYcHtV9nkHBxlzSesNNvBnYOeboi%2BnbQSC8TiK1GNVOFJliERV0QDhTPZWT%2FBbSWqMhYWgb1gHfzSP2oA1K7LRreVlOkZNMQ2rd7cxDL9deAJmCw6ueRBzQHMChjm%2Fm9tpUIHJFApXpfo8EXKRWiyInLCBPK85I5q%2FjIG%2FxX9TDJDUSQdH7EwyKOkcb0afd0vO3JqantNeWumJ5JaRKbWgARXjQssGDtOHSGdpPknAOrCDGhaM76eNfjWoB%2B4zt%2FsE23gLvvWviFCh%2FsttRVrX3IPCsNvvRqB7CSZPV3WlLECvVcW27g4g4korgjfUBnN58FGOGUqDO29MI%2FAv8wGOqUBG5Ot5ZjBQPL1Izf45jiUs%2F4bPKAHHxiNjIaRQtciA2BfQZt1oq6U8wcF%2BIpjPLTN%2F0pjPyPPvzqXpvsyCS%2B0PdVFcwdvrEz07ARVwFqpWbHPJKxyCUQy03CB6BtgQd7w6xpUEf9Lp%2BzJpddwHlA1quujLX1qsuirIwGGIRBbL3syEm8B3llDRnxoDJ9LD9xlRz5yhy6Eclfna36paK29s8fw8Wnb&X-Amz-Signature=619da698d1c047e3fa27a13847dd6e3bf5ca6af8d3490074b0ce3c05b7c00f4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5FEYNY%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQD4toG1AybUaCB7cYkIk1TCrguVP2XQWu6a2%2Bp%2B415WcwIgWWGpCFAHoTJVL2wiVDJCnbTbs7xQMfaVjJdaRmwP4pMqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwuDE5HgN2e97cIlyrcA%2BFVspnl14imzS7Gi463f21%2Fk%2FuoJxhluOA0BIcnJ%2BH4NQqX4lTYA%2F6DFMD8lPw%2BpvTuO%2BXGfKa34WcMkK%2FEBjWoopq%2BXdL3Y%2F%2Bs%2F3bSZaqabIsABf1WWht0SIYANTqH8l38fOlEE0%2FFxD8DGk1XrQ1aKCyQbOnDUjjqw6YUrZ75hW68V8TUD6gEO5iLgDqJYDlNqFqp47W3HoYiH8wtzXMA5jHRRybuAwjxP%2B8q1tk4cTu47iRob5hwXwsIKK%2BWRlSCMrApchoCr6YCYFT1eEO3fWWUsfH%2BvsqeehM9NDDNgEEWYcHtV9nkHBxlzSesNNvBnYOeboi%2BnbQSC8TiK1GNVOFJliERV0QDhTPZWT%2FBbSWqMhYWgb1gHfzSP2oA1K7LRreVlOkZNMQ2rd7cxDL9deAJmCw6ueRBzQHMChjm%2Fm9tpUIHJFApXpfo8EXKRWiyInLCBPK85I5q%2FjIG%2FxX9TDJDUSQdH7EwyKOkcb0afd0vO3JqantNeWumJ5JaRKbWgARXjQssGDtOHSGdpPknAOrCDGhaM76eNfjWoB%2B4zt%2FsE23gLvvWviFCh%2FsttRVrX3IPCsNvvRqB7CSZPV3WlLECvVcW27g4g4korgjfUBnN58FGOGUqDO29MI%2FAv8wGOqUBG5Ot5ZjBQPL1Izf45jiUs%2F4bPKAHHxiNjIaRQtciA2BfQZt1oq6U8wcF%2BIpjPLTN%2F0pjPyPPvzqXpvsyCS%2B0PdVFcwdvrEz07ARVwFqpWbHPJKxyCUQy03CB6BtgQd7w6xpUEf9Lp%2BzJpddwHlA1quujLX1qsuirIwGGIRBbL3syEm8B3llDRnxoDJ9LD9xlRz5yhy6Eclfna36paK29s8fw8Wnb&X-Amz-Signature=f85680a48e271241ff0e506cba4492b97604c1c8c1a8abec44eff70d4e74b6df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

