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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEIEYJQE%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVZMFhNOCEVdudFm9LGp54KhWygoW1i8vHQNUxVdqd9AiEAryVEit46dHu0Xb6gwsQO%2Bhof0HWxSNNLmtnfr7iQgmYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAerOmz%2BAISn8OyWtSrcA2W%2FHojvuYYSFbfty%2FBBEq6M5jm0qN3G8LRGFj3Wa5knCoU6OX8wCRGt7t1eZSQe%2BksATx0sCaXoPEPyARKjPLLJXIaczk4WgFT6Mm4PBOyT5ilhJicK7IJ0ZbnCzqI9myR0KYw6L3wZeUPNCeJuScPjeJU%2FpuwDcAM2JRQMIJcvBmHH35%2BHTFY9MtVTAjt0P4OtaNdkK7ojP%2F6vPUEJZnWcC%2FdjpU%2FUOahfpf0AsVi4qIWCHk9MLRAwdFNABLCufzhXUk5a1YiWrlNK4e1erqOwcF1di4wsn3eAKOrGJkIwWT6hMb1XBiAk8JRt0mGFThJKViFyKG2xVyk0tZxPSxw%2BBX59xTsIajgsXbbljNGgE%2FnQABpOkiugjAXbnX7RXGyn6KvUx%2FCA3XVW8WFZMfJeWHKd8fIS2Mon6R71RcD%2FVvXvwMzTqEP1N4rwAdu5%2BepMlygKWXKZ3pPOEATQWft71Dx0I9GF5xAp7%2Bn13y7godInkynd2RILEVTKZVg27Edvzq%2FvWANziTc5a8x%2FBDXioqCVtMRmZECaUvblW0DjbVZYxsT8c1mup93vU5fYKS%2BG%2BUpoEXYnEhPg%2BINenqq1TSXGhZ5oMCoLPBj3Gh5p5xUAXh%2BcxuwAsdx0MPrIjcoGOqUBU2MmH7aaRhESxSvFaekligjIKTapY%2F4xJRM%2FwRrPZZWaot2gH05MEsQJ%2BR1VYOvF%2BpXX%2FDr45QQRA4Pwe7aykdx%2BM5nvf7HcdvQT2uYPjc646Q4shgleBUshyXMw%2FC1%2BlQoijZTbRybgLrm7vTveMQ4y3XgsxLrT%2FLyx5RwcWAi%2FzWO3xcdgWuxdu8iM80HDSce8GYWxtwvYJ%2BjHl%2FxrlA%2FmQkeD&X-Amz-Signature=642e7e5873fd24830a12f77e6fdf389ed835d85325595cc1b28f6ae5a53846ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEIEYJQE%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVZMFhNOCEVdudFm9LGp54KhWygoW1i8vHQNUxVdqd9AiEAryVEit46dHu0Xb6gwsQO%2Bhof0HWxSNNLmtnfr7iQgmYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAerOmz%2BAISn8OyWtSrcA2W%2FHojvuYYSFbfty%2FBBEq6M5jm0qN3G8LRGFj3Wa5knCoU6OX8wCRGt7t1eZSQe%2BksATx0sCaXoPEPyARKjPLLJXIaczk4WgFT6Mm4PBOyT5ilhJicK7IJ0ZbnCzqI9myR0KYw6L3wZeUPNCeJuScPjeJU%2FpuwDcAM2JRQMIJcvBmHH35%2BHTFY9MtVTAjt0P4OtaNdkK7ojP%2F6vPUEJZnWcC%2FdjpU%2FUOahfpf0AsVi4qIWCHk9MLRAwdFNABLCufzhXUk5a1YiWrlNK4e1erqOwcF1di4wsn3eAKOrGJkIwWT6hMb1XBiAk8JRt0mGFThJKViFyKG2xVyk0tZxPSxw%2BBX59xTsIajgsXbbljNGgE%2FnQABpOkiugjAXbnX7RXGyn6KvUx%2FCA3XVW8WFZMfJeWHKd8fIS2Mon6R71RcD%2FVvXvwMzTqEP1N4rwAdu5%2BepMlygKWXKZ3pPOEATQWft71Dx0I9GF5xAp7%2Bn13y7godInkynd2RILEVTKZVg27Edvzq%2FvWANziTc5a8x%2FBDXioqCVtMRmZECaUvblW0DjbVZYxsT8c1mup93vU5fYKS%2BG%2BUpoEXYnEhPg%2BINenqq1TSXGhZ5oMCoLPBj3Gh5p5xUAXh%2BcxuwAsdx0MPrIjcoGOqUBU2MmH7aaRhESxSvFaekligjIKTapY%2F4xJRM%2FwRrPZZWaot2gH05MEsQJ%2BR1VYOvF%2BpXX%2FDr45QQRA4Pwe7aykdx%2BM5nvf7HcdvQT2uYPjc646Q4shgleBUshyXMw%2FC1%2BlQoijZTbRybgLrm7vTveMQ4y3XgsxLrT%2FLyx5RwcWAi%2FzWO3xcdgWuxdu8iM80HDSce8GYWxtwvYJ%2BjHl%2FxrlA%2FmQkeD&X-Amz-Signature=a29f07fc134124ea293f2ebe7705899c8b5a9abc58a662c8032b06e25bdc5efa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEIEYJQE%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVZMFhNOCEVdudFm9LGp54KhWygoW1i8vHQNUxVdqd9AiEAryVEit46dHu0Xb6gwsQO%2Bhof0HWxSNNLmtnfr7iQgmYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAerOmz%2BAISn8OyWtSrcA2W%2FHojvuYYSFbfty%2FBBEq6M5jm0qN3G8LRGFj3Wa5knCoU6OX8wCRGt7t1eZSQe%2BksATx0sCaXoPEPyARKjPLLJXIaczk4WgFT6Mm4PBOyT5ilhJicK7IJ0ZbnCzqI9myR0KYw6L3wZeUPNCeJuScPjeJU%2FpuwDcAM2JRQMIJcvBmHH35%2BHTFY9MtVTAjt0P4OtaNdkK7ojP%2F6vPUEJZnWcC%2FdjpU%2FUOahfpf0AsVi4qIWCHk9MLRAwdFNABLCufzhXUk5a1YiWrlNK4e1erqOwcF1di4wsn3eAKOrGJkIwWT6hMb1XBiAk8JRt0mGFThJKViFyKG2xVyk0tZxPSxw%2BBX59xTsIajgsXbbljNGgE%2FnQABpOkiugjAXbnX7RXGyn6KvUx%2FCA3XVW8WFZMfJeWHKd8fIS2Mon6R71RcD%2FVvXvwMzTqEP1N4rwAdu5%2BepMlygKWXKZ3pPOEATQWft71Dx0I9GF5xAp7%2Bn13y7godInkynd2RILEVTKZVg27Edvzq%2FvWANziTc5a8x%2FBDXioqCVtMRmZECaUvblW0DjbVZYxsT8c1mup93vU5fYKS%2BG%2BUpoEXYnEhPg%2BINenqq1TSXGhZ5oMCoLPBj3Gh5p5xUAXh%2BcxuwAsdx0MPrIjcoGOqUBU2MmH7aaRhESxSvFaekligjIKTapY%2F4xJRM%2FwRrPZZWaot2gH05MEsQJ%2BR1VYOvF%2BpXX%2FDr45QQRA4Pwe7aykdx%2BM5nvf7HcdvQT2uYPjc646Q4shgleBUshyXMw%2FC1%2BlQoijZTbRybgLrm7vTveMQ4y3XgsxLrT%2FLyx5RwcWAi%2FzWO3xcdgWuxdu8iM80HDSce8GYWxtwvYJ%2BjHl%2FxrlA%2FmQkeD&X-Amz-Signature=1d5bdd2ade1e1fecbfa0fb10d949d6a889e2b6e3aadfdb1dd4f075b1d94ecb8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

