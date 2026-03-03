---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJZZ5ZNN%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCO9Q5MRSht9NLf5bTqFP%2Bp%2Ba8aLEvrh4EB2AqUtMnQ6QIgClqbdrNjw4H2hG2gpsU4kM%2Fh74k2Fu6VChb3EYR7BDUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTZYYgsbjujjYBZWCrcA9SXNVlLOIrj%2Bc2sq5%2BEs%2FlVg4bMcwpnIY6OhYLBr%2BQ8tUlSdjqgNmwv3hYy3FDA%2FOnNEbUaZgaraKQQM%2FsjuyfMEq1eTSaQmRPVnehOiH0TmVd%2BP9e02JZVadhVVbrw86MiyygrUW2hdoYTlHZOD0MBci%2BzKD38CXfL9bh4RnJ4luP6rdPrjoMi6XjtH6iVIjqksYVslxt65TCrySPfoUVP8x1P9ag5ojUC5Wf4KsES%2FZnstOwJpv%2BV7e3BMqPMBdIdwuXqOu55WcwXvFJMqE6DgnjtqtUq3J5Yms6oJEIE8vJqCdyNpzKQ3CP0dvhi5aFOjcN3smKONgAyjUa7ZyAjLHz7cXRsvaMZ5LVHaKczvxd5wvN%2FheeV5g2e2TtMh6X8HS5lPJVBYRZXRkj1Yxu4Qo%2FO%2B3vVpzn2LtBSpXJrVMNZ9fCXEYIhp%2BbrYR6ZBibtmBNX%2F%2F29IxUh14MzFvKkf08JOyC9Iu4JyBiJXCucD9RvHHzm%2FIv%2FvrgkqgUBdWMuHzw8lwLOFkMNpImj7SnYusheUP9zd%2BhnJTS6RLLC%2B15jBV4Od0lA32V2afRT1m4XnWeEYfTvaN%2FOnJm%2FLCFCIOBkDeUOONIqhShOvz1YMDmZvw0qXjij1ao1MP%2B1mM0GOqUBqdJTb%2BvYQ7X53RpgJmNUIghTLE7P3sqerMa%2BrSG9seBqq0ymS2ORBFer2a5z404uyr%2F0b0yFtI5%2FNvAKL%2BKD3l5rCVq69nZHQUbAmPVdU4ehmkGNDoMr%2FuFfwzwnTFuAQOiqLCnlDPlwJHZMf47U28pwBwXNKOSzTZSVn9deZUSID4amWqvlcohmJ1QxeOa0pke1jR5%2BR32LttFoxWrJZbojoJMk&X-Amz-Signature=2d313c80b5bb686f2b2cb4bf1f94ca61174ad965a935607209a22492a0bd99de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

