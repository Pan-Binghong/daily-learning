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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7YFDCJ%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHu%2FmY8AmCPMN3IGOzJL7cth7z90DMHLI7A2%2FSOsjuq4AiB1t%2FoduBbIPF2bvqP56965h6pJL3vpE8HimEw1UjqLpyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs4Zf1sVD622ccYlgKtwDeZ8hVQn%2F9P1osGRi0%2BL8xVhfLi89Ekb0MHPldUaDoZ4RGjUz4r4QMW%2FtwPL8E9xvD9CnA8AVqICn9GPLdTVw%2BbwKCytU0xqf6yUDrYpiEs61X5K%2BkPvStO0RCCuhM5RoJTwiqhaufMrAp10VAz4heMbfjj6K4YevVizFWM0qs%2BrQz%2FAN9D%2BR8VTJOb4K9rjnORc6KV%2Fpi%2FtiCspxaWjxmK9WRnWWIIyGgED2rSrolmhAKQJIFFFyYWrI3cu6SO5eeLCl251vVfajUXMHV2Ve%2FyIBO0ri7avfZHD4rrn0aL55vPDv%2FgBZRiKnva96%2FUZe68fELgbiLTwjNmzy7R3OgSPtwN%2BEVcqPTbeZfPrsU5zoJV%2FV4hbMM6VjWs6dWCWaFlsMatpnwNvwzHoYnqVAkYqzylkO7DucYSpG6HOA3%2FcPwczmcQ0D2rGAMhM09cyDTqbApChqurDTpe5qDofDttj3Z4tcAUy3znuknRHkBqYa1AjzAqCzrIrzcb5DuLMFOPAjSJAyysr%2Bdal6C3nHq6xsxGNQ%2BjC0w4CtbKfm0l%2FT0zZ8rueMgg39xo1GCBl9Z9S5kqbfjrTCXQpY4DvT99cNWXA6oLrK2dawwOEqAG54c7U47Rb3bNJdd04woLXcygY6pgGkWUA6H2lYxl%2FJ6Wm9KGrEAd%2Be%2FutUqNpbDa%2FSAIOD873kDQSpdfUyb5zgL5SupkQcwvjyVc%2FX2pM0CT1Q6UHt9HqCpDoBH8Xmap8T%2FfeLl4u5m5E61wJkL9eQ0utML6nfrMV3GjkS9UsZi5ev5%2FLrEQcvoaAMRw9x7hJhZVnJYT7j3SD1XqniNNI89OEwRRMH72bJ075jrCXERjFH3DKugYzEEFfx&X-Amz-Signature=a591c763e495f02addc5f3a5daeb99b28bd067432e4dbe8462b9066d2531cb55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7YFDCJ%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHu%2FmY8AmCPMN3IGOzJL7cth7z90DMHLI7A2%2FSOsjuq4AiB1t%2FoduBbIPF2bvqP56965h6pJL3vpE8HimEw1UjqLpyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs4Zf1sVD622ccYlgKtwDeZ8hVQn%2F9P1osGRi0%2BL8xVhfLi89Ekb0MHPldUaDoZ4RGjUz4r4QMW%2FtwPL8E9xvD9CnA8AVqICn9GPLdTVw%2BbwKCytU0xqf6yUDrYpiEs61X5K%2BkPvStO0RCCuhM5RoJTwiqhaufMrAp10VAz4heMbfjj6K4YevVizFWM0qs%2BrQz%2FAN9D%2BR8VTJOb4K9rjnORc6KV%2Fpi%2FtiCspxaWjxmK9WRnWWIIyGgED2rSrolmhAKQJIFFFyYWrI3cu6SO5eeLCl251vVfajUXMHV2Ve%2FyIBO0ri7avfZHD4rrn0aL55vPDv%2FgBZRiKnva96%2FUZe68fELgbiLTwjNmzy7R3OgSPtwN%2BEVcqPTbeZfPrsU5zoJV%2FV4hbMM6VjWs6dWCWaFlsMatpnwNvwzHoYnqVAkYqzylkO7DucYSpG6HOA3%2FcPwczmcQ0D2rGAMhM09cyDTqbApChqurDTpe5qDofDttj3Z4tcAUy3znuknRHkBqYa1AjzAqCzrIrzcb5DuLMFOPAjSJAyysr%2Bdal6C3nHq6xsxGNQ%2BjC0w4CtbKfm0l%2FT0zZ8rueMgg39xo1GCBl9Z9S5kqbfjrTCXQpY4DvT99cNWXA6oLrK2dawwOEqAG54c7U47Rb3bNJdd04woLXcygY6pgGkWUA6H2lYxl%2FJ6Wm9KGrEAd%2Be%2FutUqNpbDa%2FSAIOD873kDQSpdfUyb5zgL5SupkQcwvjyVc%2FX2pM0CT1Q6UHt9HqCpDoBH8Xmap8T%2FfeLl4u5m5E61wJkL9eQ0utML6nfrMV3GjkS9UsZi5ev5%2FLrEQcvoaAMRw9x7hJhZVnJYT7j3SD1XqniNNI89OEwRRMH72bJ075jrCXERjFH3DKugYzEEFfx&X-Amz-Signature=9c0b4e243cfc5d804b1234143715ad9068353b45e699af2654164649f6cddd2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7YFDCJ%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHu%2FmY8AmCPMN3IGOzJL7cth7z90DMHLI7A2%2FSOsjuq4AiB1t%2FoduBbIPF2bvqP56965h6pJL3vpE8HimEw1UjqLpyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs4Zf1sVD622ccYlgKtwDeZ8hVQn%2F9P1osGRi0%2BL8xVhfLi89Ekb0MHPldUaDoZ4RGjUz4r4QMW%2FtwPL8E9xvD9CnA8AVqICn9GPLdTVw%2BbwKCytU0xqf6yUDrYpiEs61X5K%2BkPvStO0RCCuhM5RoJTwiqhaufMrAp10VAz4heMbfjj6K4YevVizFWM0qs%2BrQz%2FAN9D%2BR8VTJOb4K9rjnORc6KV%2Fpi%2FtiCspxaWjxmK9WRnWWIIyGgED2rSrolmhAKQJIFFFyYWrI3cu6SO5eeLCl251vVfajUXMHV2Ve%2FyIBO0ri7avfZHD4rrn0aL55vPDv%2FgBZRiKnva96%2FUZe68fELgbiLTwjNmzy7R3OgSPtwN%2BEVcqPTbeZfPrsU5zoJV%2FV4hbMM6VjWs6dWCWaFlsMatpnwNvwzHoYnqVAkYqzylkO7DucYSpG6HOA3%2FcPwczmcQ0D2rGAMhM09cyDTqbApChqurDTpe5qDofDttj3Z4tcAUy3znuknRHkBqYa1AjzAqCzrIrzcb5DuLMFOPAjSJAyysr%2Bdal6C3nHq6xsxGNQ%2BjC0w4CtbKfm0l%2FT0zZ8rueMgg39xo1GCBl9Z9S5kqbfjrTCXQpY4DvT99cNWXA6oLrK2dawwOEqAG54c7U47Rb3bNJdd04woLXcygY6pgGkWUA6H2lYxl%2FJ6Wm9KGrEAd%2Be%2FutUqNpbDa%2FSAIOD873kDQSpdfUyb5zgL5SupkQcwvjyVc%2FX2pM0CT1Q6UHt9HqCpDoBH8Xmap8T%2FfeLl4u5m5E61wJkL9eQ0utML6nfrMV3GjkS9UsZi5ev5%2FLrEQcvoaAMRw9x7hJhZVnJYT7j3SD1XqniNNI89OEwRRMH72bJ075jrCXERjFH3DKugYzEEFfx&X-Amz-Signature=d46a1c9f7b05c079a0f15d791b5000204db4ce8fc26fbc2d7b790e71c6f077ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

