---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF32MY6A%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9KJPuaXj%2FzCQ%2FSbjvTEsSmBZYNXftHS%2F4h9zp6rxuWgIgAj0PenAzXP%2FlKpndDiEe3lVgLwdxhF4uus3dqN5f9sIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJN8QhNqxtpWFCK2YircA2WJWGAa3u%2FFDtn8tbhSQveSg5StrjHl6OdVgzIUPg0pMs9yV9gNfNYMCmo8gZ2czLaNB4fJpk%2FPjLxbh5JiCxgABqC7ZgbtkYhkk2SUvPrEABqedWjJI6hq5d%2Fm%2FwppQXGe%2BUNWPXxRWOU4jgcUpYXEd7byakhiaqj5djw54JgYtmgGvZlthf6c%2BKPMbnrH7Y0uCfR4tipl2EEb2f297RdWg9Iy7aQGFH5k7N1IOi6LNvUHXlI3F503XnHVAIYlBqzvhe3xDr0M%2BhuXFbKCXD01CS4PLeqWw9j6TBOEaJvQBVFbeUxI%2BjDPZR1Sdwf2m%2FbhWInBnHSdRNoBue2ZCHmxqwV%2BmUiawAynK%2F%2FL0u6CcfVnjJDG23dckznFSoOdJ0RiKUt%2BC6z3vMfvTpgfr3V4ZIoW9MabMshdhuq9uiM5EDh1JT%2BxyfKJIB5ACKQBcCqlD7xBQt7fOHv4sUe9e8eTayvP6PwySDGb0BZelo%2FYKNC6CgJIQJk%2BEawUNevcAYyGXueYJ0NBkxfytjhsJPbM7PzQVOn3zLJMCMVY6VNINo%2BRvz3bevfPA5U%2Fdx7Ag8ZjBd5L8WoryFFvA34CbqUcMoT%2BbQwdGPUw9jb4IzdFDMv5YnD1c3C6he%2BwMPaVsMgGOqUBxjcjAo2oWRf35ORwp7BxbU24mP0Z%2F1BmE%2Bj%2Bu95hsf4VqNlPCmb9Jo3hePBQSEChn2Xb7vKiIwRAWECNbY%2FWFrnmEzH%2FXEHTTHvvMEHVoP%2B7B5Wm5YbuALCYn6M5mfMPd32Bj3Fyfu5yWo4L3whB6EY8%2BEQZk4FGrPdU9AwrxeqFJEazgs0jqSoFbURYmupL%2BdWhLAgxSmrcG8IpQh%2BP3N9kecKc&X-Amz-Signature=f9d7a18c6a9aeda7cea327a6a36edcc6102a3c0dbdec88bca7aaaf6b8b563484&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF32MY6A%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9KJPuaXj%2FzCQ%2FSbjvTEsSmBZYNXftHS%2F4h9zp6rxuWgIgAj0PenAzXP%2FlKpndDiEe3lVgLwdxhF4uus3dqN5f9sIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJN8QhNqxtpWFCK2YircA2WJWGAa3u%2FFDtn8tbhSQveSg5StrjHl6OdVgzIUPg0pMs9yV9gNfNYMCmo8gZ2czLaNB4fJpk%2FPjLxbh5JiCxgABqC7ZgbtkYhkk2SUvPrEABqedWjJI6hq5d%2Fm%2FwppQXGe%2BUNWPXxRWOU4jgcUpYXEd7byakhiaqj5djw54JgYtmgGvZlthf6c%2BKPMbnrH7Y0uCfR4tipl2EEb2f297RdWg9Iy7aQGFH5k7N1IOi6LNvUHXlI3F503XnHVAIYlBqzvhe3xDr0M%2BhuXFbKCXD01CS4PLeqWw9j6TBOEaJvQBVFbeUxI%2BjDPZR1Sdwf2m%2FbhWInBnHSdRNoBue2ZCHmxqwV%2BmUiawAynK%2F%2FL0u6CcfVnjJDG23dckznFSoOdJ0RiKUt%2BC6z3vMfvTpgfr3V4ZIoW9MabMshdhuq9uiM5EDh1JT%2BxyfKJIB5ACKQBcCqlD7xBQt7fOHv4sUe9e8eTayvP6PwySDGb0BZelo%2FYKNC6CgJIQJk%2BEawUNevcAYyGXueYJ0NBkxfytjhsJPbM7PzQVOn3zLJMCMVY6VNINo%2BRvz3bevfPA5U%2Fdx7Ag8ZjBd5L8WoryFFvA34CbqUcMoT%2BbQwdGPUw9jb4IzdFDMv5YnD1c3C6he%2BwMPaVsMgGOqUBxjcjAo2oWRf35ORwp7BxbU24mP0Z%2F1BmE%2Bj%2Bu95hsf4VqNlPCmb9Jo3hePBQSEChn2Xb7vKiIwRAWECNbY%2FWFrnmEzH%2FXEHTTHvvMEHVoP%2B7B5Wm5YbuALCYn6M5mfMPd32Bj3Fyfu5yWo4L3whB6EY8%2BEQZk4FGrPdU9AwrxeqFJEazgs0jqSoFbURYmupL%2BdWhLAgxSmrcG8IpQh%2BP3N9kecKc&X-Amz-Signature=35271e0c05a8bca7679b97bc9755b461892a732ba316f3a03ef27e2e3a77565f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



