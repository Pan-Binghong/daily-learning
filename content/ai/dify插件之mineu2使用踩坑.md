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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PI34LK2%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFJYD9sjfh9M%2BnHFFprOqRZQsvWrGG6apmFDYadmAlBFAiEA8cVuGp3wfbsahbhaD2eDjVEqPNqTcXYzOLrEGp7AjPcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDzt3dfSiMDyE2uhRSrcAwYH5hBKzIdkz2PeeQlbwnkZ1Q466G0%2BO1PphdZriw%2ByeHG2lSbZOMvXpFUmU5GorenbxFMheBhxa07hmE4pmeGlkMHrS37p9ly9XZcvAWubekzpUKdpl5mlfanoEzpFdFtLIZxn7OcbVh%2FxeKnOZQ8cgAww%2F6Il3gT3lPgaPBvIsbm%2FVOyUGa1Ga2KAtApQc957%2B4BDhB38kNoLBMUX7XJURoXtvHV72phLNtbDhUwK5%2BtBVb4PI3REbQ5RCZKItLjUyQVHOazdS9Di1%2Bwj0b6ykk7aKe%2FitXZvEdj0glfeqfkJzN8A3K03eQF%2Bhz43Jt7ibBd6dZgotngaGnJJmU8cUFjX5AmnypXV7urDxsEidv5ePwn%2BM7X8E4NV7aEvwkXgulTnsOou3YCPt9QL%2FrfV3HcWf39xvymrd0AS27FtG%2Bag6PJC7Q3m0tTClvSGiFc19x4iLTRQoyDW1XX2rKlszKg%2F%2FuZUQVnAGXeJfc%2FiUG9nl05Qh1e9U0FZAC6CjWKPuL09BFZRqT2%2BmqmzHylljijMQj4JOZ8UwuK4d7Bs6niyi6cg6MayyGDIXo3%2BBnL%2BvekUEZpfknGdHoA0S%2BJmDeUywkIBQRIBNiBSu5U4dzfX%2BFMrGq8LKNotMOKY78gGOqUBrrA9ualbnH6vQN325pU1luTfefO2hrRDR2Pxkn9HaBcPL30BMBvJmHnzOb4DgvWK75nWEzXD%2B9HQSzR45Y7ykbravGnqGCjMhAEmQcv08IjLbK4fQ321Dq5GT4wyXYDlpgR6dE%2BZkvES1xkggK9kBdGBhWLLCg9kGyHJsyyZeNKOpkgZr7IFOsePLFi1SxaTn8yjIAcO1NrmLKy2q%2FxVRah%2F1DrC&X-Amz-Signature=da5578b1140eaf4d4db3f557e073cae9402a3312d4b5ce7b6ca39de165211232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PI34LK2%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFJYD9sjfh9M%2BnHFFprOqRZQsvWrGG6apmFDYadmAlBFAiEA8cVuGp3wfbsahbhaD2eDjVEqPNqTcXYzOLrEGp7AjPcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDzt3dfSiMDyE2uhRSrcAwYH5hBKzIdkz2PeeQlbwnkZ1Q466G0%2BO1PphdZriw%2ByeHG2lSbZOMvXpFUmU5GorenbxFMheBhxa07hmE4pmeGlkMHrS37p9ly9XZcvAWubekzpUKdpl5mlfanoEzpFdFtLIZxn7OcbVh%2FxeKnOZQ8cgAww%2F6Il3gT3lPgaPBvIsbm%2FVOyUGa1Ga2KAtApQc957%2B4BDhB38kNoLBMUX7XJURoXtvHV72phLNtbDhUwK5%2BtBVb4PI3REbQ5RCZKItLjUyQVHOazdS9Di1%2Bwj0b6ykk7aKe%2FitXZvEdj0glfeqfkJzN8A3K03eQF%2Bhz43Jt7ibBd6dZgotngaGnJJmU8cUFjX5AmnypXV7urDxsEidv5ePwn%2BM7X8E4NV7aEvwkXgulTnsOou3YCPt9QL%2FrfV3HcWf39xvymrd0AS27FtG%2Bag6PJC7Q3m0tTClvSGiFc19x4iLTRQoyDW1XX2rKlszKg%2F%2FuZUQVnAGXeJfc%2FiUG9nl05Qh1e9U0FZAC6CjWKPuL09BFZRqT2%2BmqmzHylljijMQj4JOZ8UwuK4d7Bs6niyi6cg6MayyGDIXo3%2BBnL%2BvekUEZpfknGdHoA0S%2BJmDeUywkIBQRIBNiBSu5U4dzfX%2BFMrGq8LKNotMOKY78gGOqUBrrA9ualbnH6vQN325pU1luTfefO2hrRDR2Pxkn9HaBcPL30BMBvJmHnzOb4DgvWK75nWEzXD%2B9HQSzR45Y7ykbravGnqGCjMhAEmQcv08IjLbK4fQ321Dq5GT4wyXYDlpgR6dE%2BZkvES1xkggK9kBdGBhWLLCg9kGyHJsyyZeNKOpkgZr7IFOsePLFi1SxaTn8yjIAcO1NrmLKy2q%2FxVRah%2F1DrC&X-Amz-Signature=fe43ae059b6209e88d666073642c7bc33be5892205343cc570d7a81125fb2a78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



