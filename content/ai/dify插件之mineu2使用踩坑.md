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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCDV7VQC%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAFtyOYUSl6Ymwkz%2BW6AVMta9uYuZkdzq0B%2FJYN0n9DUAiEAk0xKV3ryd0qKAghuUgzdTd1fkX5MSe3baYLJ%2BukX5X8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOi%2FPiubOoothFMZyrcAxA%2B5cpoS0CPp3BGkrYEAnd5MsVTQfa0xgvVg7CLOfRGJ2SnQS2xhsNVSDEO0ezyfam0pJFT1XiDFKRHgfklglVYXAROunf%2FukP8Ye3qzU%2BsveIwJgFnBS3cM7bht8A7ZYG27iB9XyOYiTuRM7rEDfFSknEIsw36TKXWR1Yi4g%2FMNPNUUKkxr4lllETSfa5MZd3DsUnBDTJa7%2Bb0IEwF7vqmWs229bNXhN5IL5FjEQJuQjuYdfh%2FoTNEqkGa1GDYnUIQisgXUKZuaB28LYq%2BAleZTUHfXzoJx2AuntfMkHaRGHfaYZ3WE8PPd7WoHJYKnegcBBdVA3sChTSQ18iufJ7M22z%2FrbCX8wgUY%2BJ4y%2FEEv02KhJo8KWdFxww5vxqE0nt2FHPxY2u0mdCGVc%2FbCXUhq3tyyZRZud96uLQOL7xcI6KQ6D6oPN0mAyrKUn3GKCprc%2B3y2u0uSYrvrkawAevuUBvUkR3lhtArC2%2FGQtiDucanhYuIk6gQlNyCV0qkFbygLKGIbYFQ%2B%2FLuM5kMUnAYnsY92UqkcwOF8KgwWSkos7%2BD%2BNrTfFftWNSlKZ5YxcMnRhP8axDsLcfIe75uGH91uFPg5oUz5C1XBcYG%2Fbccv46W%2BpG31AP0G%2BEoMOn4nMoGOqUBSgR00PsMDNsVlj3sAvjJ5lh87a%2FzSMp91xXNRkXeuOH6JwHasKirrynp2vPPZHOlGKZU0k8ZfdbcRVTT6iVGGWeDRTO%2FZAx8Cypr%2Fl%2FTSsI1afAsIi%2FkeZl1eBnfNQIK1hddzf4f4y8%2F2cqOp158kzcYkuonDWBWDkoWer96WIm9fdFvJRraO6JO7R0CBg%2Fi59neP4GhMtuKXhcYVzOZJ9Okj%2BW%2F&X-Amz-Signature=cad214feec79a8106eb75e3abe5895d43d347ee09da961cc713c2538b9f5f649&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCDV7VQC%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAFtyOYUSl6Ymwkz%2BW6AVMta9uYuZkdzq0B%2FJYN0n9DUAiEAk0xKV3ryd0qKAghuUgzdTd1fkX5MSe3baYLJ%2BukX5X8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOi%2FPiubOoothFMZyrcAxA%2B5cpoS0CPp3BGkrYEAnd5MsVTQfa0xgvVg7CLOfRGJ2SnQS2xhsNVSDEO0ezyfam0pJFT1XiDFKRHgfklglVYXAROunf%2FukP8Ye3qzU%2BsveIwJgFnBS3cM7bht8A7ZYG27iB9XyOYiTuRM7rEDfFSknEIsw36TKXWR1Yi4g%2FMNPNUUKkxr4lllETSfa5MZd3DsUnBDTJa7%2Bb0IEwF7vqmWs229bNXhN5IL5FjEQJuQjuYdfh%2FoTNEqkGa1GDYnUIQisgXUKZuaB28LYq%2BAleZTUHfXzoJx2AuntfMkHaRGHfaYZ3WE8PPd7WoHJYKnegcBBdVA3sChTSQ18iufJ7M22z%2FrbCX8wgUY%2BJ4y%2FEEv02KhJo8KWdFxww5vxqE0nt2FHPxY2u0mdCGVc%2FbCXUhq3tyyZRZud96uLQOL7xcI6KQ6D6oPN0mAyrKUn3GKCprc%2B3y2u0uSYrvrkawAevuUBvUkR3lhtArC2%2FGQtiDucanhYuIk6gQlNyCV0qkFbygLKGIbYFQ%2B%2FLuM5kMUnAYnsY92UqkcwOF8KgwWSkos7%2BD%2BNrTfFftWNSlKZ5YxcMnRhP8axDsLcfIe75uGH91uFPg5oUz5C1XBcYG%2Fbccv46W%2BpG31AP0G%2BEoMOn4nMoGOqUBSgR00PsMDNsVlj3sAvjJ5lh87a%2FzSMp91xXNRkXeuOH6JwHasKirrynp2vPPZHOlGKZU0k8ZfdbcRVTT6iVGGWeDRTO%2FZAx8Cypr%2Fl%2FTSsI1afAsIi%2FkeZl1eBnfNQIK1hddzf4f4y8%2F2cqOp158kzcYkuonDWBWDkoWer96WIm9fdFvJRraO6JO7R0CBg%2Fi59neP4GhMtuKXhcYVzOZJ9Okj%2BW%2F&X-Amz-Signature=dc997619cc892241ad74ca7da20e015800a2bad307eb27d546902774e56102e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



