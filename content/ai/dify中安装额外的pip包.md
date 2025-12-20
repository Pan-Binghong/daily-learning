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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJPL4PTQ%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZtPvfmUw8%2FJDzPlstsy%2BHnca3RDyDCZfKfPFiB%2FJrUQIgIXuLZXp8OshJlSuZ1TXaHYUFO9I62UR0sa9IOg3hF7IqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEh0Gji9lRVN6o0BBircA5zSSztKwuCdPRH1EiYVTUlp8uZ9wnD8F2azmiGOSFapLaORxiv0ktmVyDkn2yUfYEKH5%2BKXyrobvHh%2FBFh8VLvc5FJbczrfjEI3mYrcU%2BDNdY%2Fdp%2BT9Nj0V7bo9BUcsbb%2BqdaLDW9wVx6eJeZCNMW3ZLAHxYLAKIQMqn03FLhbQpJB8aKIHDUmejVxusYegDcD%2FVCcSLDLgSKVlnrsBXlsCooZayLYWOOyVEwXkLg5up23qyz1NwAbn52quDqJ6bwU22anTPuW9HqAoVIV38YjlhMRBqo1C8bl%2BzzTeSyys0dnaqihiMqu0qxPeG0vMPh1cnci3426Ck9K1FDTKN7gM7yHDjUjM6rFQV15b94O9i7emHY%2BC3wB56knAMn06PoZ19cwyWlZNEC5lS%2B3lgTLQ2pwebN%2FxtqbDzOCeVqwpgHpfKjXqlTOitKUYlnk%2F7h8zdJJMsIJR1vpaRmFZ%2FAbQZx3MYtRpbQVAfAFOMUlyE%2B58N95dP%2BQSyrw5%2B4trjckJ8GGB4612HRCIbCoA0cIyCKZ%2Fmuh%2FONszX0yq0fM6MRvQGzVQp8P5obLtkOpKDF%2BGiFgU99HT3iyv2GIuWu1DU7cWSPF8nwqdadetdts4NDp4%2Be2BeIzHH%2F%2BoMJuGmMoGOqUBz2E4FTsYIZs2BFHm6VRCUp17velxKfUnqLw5XFXr92V93gvV%2FywOOq%2Bm7Bpb01c6Krwjbtw%2BBBnnHZ%2BHOa2KMZQ9ahueNvya0zbOZb7TdhdHFrnYzVZv1R%2B1OyVHMJogzgzv5IlDLkzClC5xCYV247CkxdwAqmexK0Yuf8wi34cfPLqwZj2TzkCRj8k3rHdQlLae88x9UO3t6M304pn5GiDUNFjB&X-Amz-Signature=7147a52d5d16ba1ecc2a68b6bbe49f97473ab4fe9fb8f1db09da846ddfdfaae5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

