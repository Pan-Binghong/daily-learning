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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCXSBFAB%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAzZwUYNU8wpEGvGJebH0OUHQrmShnfIxGWqN8ySrj21AiEA6M34JcqKKMfWN%2FAzhbdCFwp73HugCeFye1aKkJVRAO4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDK1qXVw%2BhO%2Fkjqk%2BjCrcA2s76tDO96FWsldtrHVNtCrDubt3%2BCXsSh6UUNSyXK6Vn65SByppQtSol39TDF3dgmC2Ph30WVonotw616Pnaw4H59QNvPYOCVpMNCebaDrh5csxB1nW%2FkyXKV9kZxDBgDQEGmGviHXT4mUBTM8%2FQpaO9H5U%2BRycvtZKAin2gpqqPxPFfc0lVqHgxBeXKRTUDaBX6KsfTRrDwqj1cSMrch3kablk91ta%2FKUptr1JwbEaOa3tQGyW%2FAOQNwXy41UlU6EAii%2FNAMH3gR192JsMP2S1mq99y2OGd0f8h74g8ncpsuI%2FH79TbgksFC1pl2fqxqzyYleCJd5zC07WHavBPl8xltCqlI7xgnb9UHXostLTh9zBK9U6a9ji0oiWninKng3VZ6GhQP45UnDmQh3L3e5XLa0q%2BxkOIDQBcKdzZWKXNGqAdbCtdG4biE4NAlzywroZy20Y09kQMEv3CFdCy1vgeZ06XuVkjArYDa2l5re3KmllgaU8AXX2%2BsngM8x3uJJH9Z8ikwBP5J3WAcH%2FR83DJkFkgHvBiA6Zuhar2fvxclO07%2B8W6j36N3FgCOZ3osWF0WYJa6zrD7tV3QJejO70COs44iN1DiwfaP1seQ5ivhbDplE4ijiePuhpMMvpvM4GOqUBZBfhCOPbYRa3ELUsAhe1MMN0ZaZR0gI2VeXzZFevh08ZxWEo6giH3Cf%2BfQbqlv4WCh0YYBT6vRNBR6dZwsmR%2FP7fe3Dt2oPNXPTuyeBizRy9r%2BsNdblZ2RL310MvrgOLNGWFCyo5jJwd4PN2ZqrOnVUpWRmopVi3pjCEPPHvLdX5uJ7rHPT5Atok4a3pTmnLvT%2B05kemkDv0Vjdwl6BUz6ADe6XU&X-Amz-Signature=1540667c02af63510c9b828b9157264323e36cb2f5be3f10504398bcbb6aeac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

