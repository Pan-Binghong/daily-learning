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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQCI5OTH%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC3eE9eI1k3MGqagtn0hel8lO6%2BN58F8EB7q8GrYGGn5gIgX8YPbLUrLS8d7GLfGUudW%2BJG5l5ivrhQbj18nqUaW5wq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDA0jKK7d2peF5SPc2SrcA6vLaWfezv0IYajOedE%2FHKzFjOkpnHouYPkr1bsbZhHN5c%2F8OoDFiElZ%2BlAZqxD01SO476gqyn6%2F268Uamwyp1ptSQYlSanefwsjkGf0nysNLgR%2FgW8o4zJGdNzY4Kbdc%2FfBBpatGSrnrtbeGmj9DuF4xI6tCBcTKqGtWrbbWF9AzJYCvKkYB%2BopmsCHlCgjt%2BOkwsC%2FBRmSTYEUqIPoKZxRK49y1wPTDXbhyt0n36dCdvXYqOijwPuhB8b6UlF6skpPoDN86QkhQMcPwHPThKhJl4W3H1vVlJx1%2BcuSX%2F%2FJi27efffbqS%2FKt2IkqyL4X4%2F%2F1WmQ2mlApRPbW%2BnEf7z8nxgqmUfdqz6q46Z9OAMNu5in1poOldylx6DJveaKcgAQyBjWgSTn2OP5MrWx6clVEohzKPZ%2BECzUh244Tn1tuZObUohhpFr3uY%2BRcZVCPutYR4fiyCKDwAgzqHppzBhUutxRIm56q6mKrT1cV1%2BCaqA3pwR69p%2FfsorZZp0V9WzznzgD7hofxv%2Fr%2BttPV%2FKiIsguny%2BtwLt3wvh%2BvGlmzyBuaAjMxdTgrG0wKt6ASr8o1puMeKGfhWPUs%2B6gNZFuTS1IeHUUxp0a7Pt9BOhaeJVoE3cr2edkTky1MKuf%2F8gGOqUBHXfRj%2FODrepmzAQcBIcqyh%2Bo1JOogK0ZHQ0kuGLZeMx1VI1Iiovp%2FA%2FYfdpEF0cW2kHk72%2FFKlhBAgk823BDQGJKjC335yP73VTAS4w60jS0amBSYL4kVdahkB6McVu340QCBdC3DMJk9EUJ%2B9fMOhNNgqW0axlAi8cITkU3cyeGgV2t4pCA0PWyllhg8oaE%2FDSskBgpXNZDSJgWt6pjIkGBJHvu&X-Amz-Signature=8f671baf6b452858656fa850e1a9285eccd96881eb8500441a66189a8e065618&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQCI5OTH%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC3eE9eI1k3MGqagtn0hel8lO6%2BN58F8EB7q8GrYGGn5gIgX8YPbLUrLS8d7GLfGUudW%2BJG5l5ivrhQbj18nqUaW5wq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDA0jKK7d2peF5SPc2SrcA6vLaWfezv0IYajOedE%2FHKzFjOkpnHouYPkr1bsbZhHN5c%2F8OoDFiElZ%2BlAZqxD01SO476gqyn6%2F268Uamwyp1ptSQYlSanefwsjkGf0nysNLgR%2FgW8o4zJGdNzY4Kbdc%2FfBBpatGSrnrtbeGmj9DuF4xI6tCBcTKqGtWrbbWF9AzJYCvKkYB%2BopmsCHlCgjt%2BOkwsC%2FBRmSTYEUqIPoKZxRK49y1wPTDXbhyt0n36dCdvXYqOijwPuhB8b6UlF6skpPoDN86QkhQMcPwHPThKhJl4W3H1vVlJx1%2BcuSX%2F%2FJi27efffbqS%2FKt2IkqyL4X4%2F%2F1WmQ2mlApRPbW%2BnEf7z8nxgqmUfdqz6q46Z9OAMNu5in1poOldylx6DJveaKcgAQyBjWgSTn2OP5MrWx6clVEohzKPZ%2BECzUh244Tn1tuZObUohhpFr3uY%2BRcZVCPutYR4fiyCKDwAgzqHppzBhUutxRIm56q6mKrT1cV1%2BCaqA3pwR69p%2FfsorZZp0V9WzznzgD7hofxv%2Fr%2BttPV%2FKiIsguny%2BtwLt3wvh%2BvGlmzyBuaAjMxdTgrG0wKt6ASr8o1puMeKGfhWPUs%2B6gNZFuTS1IeHUUxp0a7Pt9BOhaeJVoE3cr2edkTky1MKuf%2F8gGOqUBHXfRj%2FODrepmzAQcBIcqyh%2Bo1JOogK0ZHQ0kuGLZeMx1VI1Iiovp%2FA%2FYfdpEF0cW2kHk72%2FFKlhBAgk823BDQGJKjC335yP73VTAS4w60jS0amBSYL4kVdahkB6McVu340QCBdC3DMJk9EUJ%2B9fMOhNNgqW0axlAi8cITkU3cyeGgV2t4pCA0PWyllhg8oaE%2FDSskBgpXNZDSJgWt6pjIkGBJHvu&X-Amz-Signature=3db58bc5b7ad8edcbbeaadd742201fbdc4ef5cf37d3437f9d8dd25b4f0581e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



