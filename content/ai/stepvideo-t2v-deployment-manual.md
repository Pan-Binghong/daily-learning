---
title: Stepvideo-t2v Deployment Manual
date: '2025-04-22T00:43:00.000Z'
lastmod: '2025-04-23T02:58:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 记录部署阶跃星辰发布的stepvideo-ti2v (图片生成视频)模型，全流程。含踩坑记录，以及webui展示代码。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSTY5ME2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbnTt7aP27u8aQuiXGWlt5ivubQxBlwqPAu7A5FQQPpAIhAOOkG11vFbdBHjVmXKRjfbUcMRQylI558%2BVWdc%2FxOWchKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuhzU7aIS%2FQraaVKcq3AN%2FMr08a16XqZrvQiEpTfmLoe1OrUz%2FAH8a6dXN3bjd5%2BZoRkQMj7v9JOWms6LkDjO21zs%2FjB3MSto2Jx%2FhTw9byTLPaDtoJFsbsgweulneLjpm6lzJNZqKfNG7jlVJt9d1PX%2FPJ2DSLVJKYzzIpwWZviCPW558ZZt7%2BgKJ2q7AmnzYaNSVAv1eYoWwxzQPHNpzHBUidvE7EC7zuG4SkZcerMD8coFVFCgTk00%2FnPq9WPspvxFHjjAlf4JFFxabV0079bGmKsdxpxt%2BGQx7ie8Bdl76Y6YdyvldyJwreMJ49o9LQ6lzaiGhOW4J85nQ7sIdXmU5DKP7Qcnb9PmrPyRHAwm6QzIzK1PVPyZx91mmjf7TOP64nWEV6GMNSawRqqTiYWhAkX%2BNH3qTzlJ%2Fkf3ZG3pN9auKLM1xtLgigK6a4GXGOlGzeHDDPuQ7HN5cvsNowDS1ShUjHtWu%2FLVLbu3G45IeUU5i2ckg9I8yuBRyedjplwTk2Ccv%2BeM6UxLkmV%2BepQGBycINDTI3jDqJhNpAcn9Dk2a66h48mQma6boAsGiJLQqTizmjza958QRmGTt3xGr890m4SSrvenl1ivvb4y4tneuNG6aHcDRh%2B4FzbEFtxBCKq9G7D%2FbeLDDrlqXMBjqkAVT7KzUk6094bM84AiyH5%2Bzy7ld5hLpjHMVaRE%2BjtTstVfvWtcwY%2BxaN4XGN9vBk0mWQQE9sFUa%2FKJxz28QUahu5j6vIU4vTnDDhjRY7HM%2BZWSAKqm7robogO2W937MBoKUcCyO027PjdCz92HR%2B58zd351Ih4HBO0y5oMLMdFO%2FrxRAYgL9UC%2BRn39o6aMFK1pvx2%2BlgQOYZtZ6YyG0vtgFLspC&X-Amz-Signature=c51586ee18d08505fd678f39e3eb4672b2e4a18d79d22aa27778ec13177ea397&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 环境安装

## 1.1 拉取Docker镜像

```bash
docker pull nvcr.io/nvidia/pytorch:23.10-py3
docker run -dit --gpus all --privileged  --ipc=host --net host --name=stepfun--shm-size=100g --ulimit memlock=-1 -v /data/:/data/ 镜像ID  /bin/bash
docker exec -it stepfun /bin/bash
```

推荐拉取该镜像，在此镜像基础上进行模型的安装运行。忽略docker的安装。

## 1.2安装StepVideo环境

演示所用的webui基于streamlit库进行开发，其中的numpy版本与stepvideo有冲突，首先安装streamlit。

```bash
pip install streamlit
```

```bash
git clone https://github.com/stepfun-ai/Step-Video-TI2V.git
cd StepFun-StepVideo
pip install -e .
```

opencv报错：如遇到 xxx 报错，利用opencv-fixer工具进行清理更新

```bash
pip install opencv-fixer==0.2.5
python -c "from opencv_fixer import AutoFix; AutoFix()"
```

<details><summary>requirements.txt</summary>

</details>

---

# 2. 模型下载

```bash
mkdir stepfun
cd stepfun
pip install modelscope
modelscope download --model stepfun-ai/stepvideo-ti2v  --local_dir .
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSTY5ME2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbnTt7aP27u8aQuiXGWlt5ivubQxBlwqPAu7A5FQQPpAIhAOOkG11vFbdBHjVmXKRjfbUcMRQylI558%2BVWdc%2FxOWchKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuhzU7aIS%2FQraaVKcq3AN%2FMr08a16XqZrvQiEpTfmLoe1OrUz%2FAH8a6dXN3bjd5%2BZoRkQMj7v9JOWms6LkDjO21zs%2FjB3MSto2Jx%2FhTw9byTLPaDtoJFsbsgweulneLjpm6lzJNZqKfNG7jlVJt9d1PX%2FPJ2DSLVJKYzzIpwWZviCPW558ZZt7%2BgKJ2q7AmnzYaNSVAv1eYoWwxzQPHNpzHBUidvE7EC7zuG4SkZcerMD8coFVFCgTk00%2FnPq9WPspvxFHjjAlf4JFFxabV0079bGmKsdxpxt%2BGQx7ie8Bdl76Y6YdyvldyJwreMJ49o9LQ6lzaiGhOW4J85nQ7sIdXmU5DKP7Qcnb9PmrPyRHAwm6QzIzK1PVPyZx91mmjf7TOP64nWEV6GMNSawRqqTiYWhAkX%2BNH3qTzlJ%2Fkf3ZG3pN9auKLM1xtLgigK6a4GXGOlGzeHDDPuQ7HN5cvsNowDS1ShUjHtWu%2FLVLbu3G45IeUU5i2ckg9I8yuBRyedjplwTk2Ccv%2BeM6UxLkmV%2BepQGBycINDTI3jDqJhNpAcn9Dk2a66h48mQma6boAsGiJLQqTizmjza958QRmGTt3xGr890m4SSrvenl1ivvb4y4tneuNG6aHcDRh%2B4FzbEFtxBCKq9G7D%2FbeLDDrlqXMBjqkAVT7KzUk6094bM84AiyH5%2Bzy7ld5hLpjHMVaRE%2BjtTstVfvWtcwY%2BxaN4XGN9vBk0mWQQE9sFUa%2FKJxz28QUahu5j6vIU4vTnDDhjRY7HM%2BZWSAKqm7robogO2W937MBoKUcCyO027PjdCz92HR%2B58zd351Ih4HBO0y5oMLMdFO%2FrxRAYgL9UC%2BRn39o6aMFK1pvx2%2BlgQOYZtZ6YyG0vtgFLspC&X-Amz-Signature=b81c0b6e7bb2ed6bad5d55d6f0af5aea825f48d6814b455bcf2c0a103a6897c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 推理脚本

## 3.1 启动API服务

```bash
python api/call_remote_server.py --model_dir /data/stepfun & 
```

运行此操作后，可观察到服务器内的最后一张卡，有大约45%的显存占用。

## 3.2 图生视频

> 💡 本次测试环境在H800 * 8的裸金属服务器内，目前模型存在显存过大的问题。如果使用H20（单卡显存141G），可取消标红的配置参数。

```bash
# 优化显存使用，减少碎片
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

```bash
torchrun --nproc_per_node 4 run_parallel.py \
    --model_dir /data/stepfun \ ## 权重路劲
    --vae_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --caption_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --ulysses_degree  4 \ ## 4卡运行
    --prompt "男孩快速长大" \ 
    --first_image_path ./assets/demo.png \ ## 图片路径
    --infer_steps 50 \ ## 视频降噪参数
    --save_path ./results \ ## 生成视频保存路径
    --cfg_scale 9.0 \ ## 内置提示词关联度参数，详见config.py
    --motion_score 5.0 \ ## 帧间变化参数
    --time_shift 12.573 \ ## 降噪相关参数
    --use-cpu-offload ## 使用内存加载权重
```

---

# 4. WebUI推理

## 4.1 代码

### 将以下代码放入StepFun-StepVideo文件夹内

---

## 4.2 运行服务

streamlit run webui.py —server.port 8080

---

## 4.3 页面效果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSTY5ME2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbnTt7aP27u8aQuiXGWlt5ivubQxBlwqPAu7A5FQQPpAIhAOOkG11vFbdBHjVmXKRjfbUcMRQylI558%2BVWdc%2FxOWchKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuhzU7aIS%2FQraaVKcq3AN%2FMr08a16XqZrvQiEpTfmLoe1OrUz%2FAH8a6dXN3bjd5%2BZoRkQMj7v9JOWms6LkDjO21zs%2FjB3MSto2Jx%2FhTw9byTLPaDtoJFsbsgweulneLjpm6lzJNZqKfNG7jlVJt9d1PX%2FPJ2DSLVJKYzzIpwWZviCPW558ZZt7%2BgKJ2q7AmnzYaNSVAv1eYoWwxzQPHNpzHBUidvE7EC7zuG4SkZcerMD8coFVFCgTk00%2FnPq9WPspvxFHjjAlf4JFFxabV0079bGmKsdxpxt%2BGQx7ie8Bdl76Y6YdyvldyJwreMJ49o9LQ6lzaiGhOW4J85nQ7sIdXmU5DKP7Qcnb9PmrPyRHAwm6QzIzK1PVPyZx91mmjf7TOP64nWEV6GMNSawRqqTiYWhAkX%2BNH3qTzlJ%2Fkf3ZG3pN9auKLM1xtLgigK6a4GXGOlGzeHDDPuQ7HN5cvsNowDS1ShUjHtWu%2FLVLbu3G45IeUU5i2ckg9I8yuBRyedjplwTk2Ccv%2BeM6UxLkmV%2BepQGBycINDTI3jDqJhNpAcn9Dk2a66h48mQma6boAsGiJLQqTizmjza958QRmGTt3xGr890m4SSrvenl1ivvb4y4tneuNG6aHcDRh%2B4FzbEFtxBCKq9G7D%2FbeLDDrlqXMBjqkAVT7KzUk6094bM84AiyH5%2Bzy7ld5hLpjHMVaRE%2BjtTstVfvWtcwY%2BxaN4XGN9vBk0mWQQE9sFUa%2FKJxz28QUahu5j6vIU4vTnDDhjRY7HM%2BZWSAKqm7robogO2W937MBoKUcCyO027PjdCz92HR%2B58zd351Ih4HBO0y5oMLMdFO%2FrxRAYgL9UC%2BRn39o6aMFK1pvx2%2BlgQOYZtZ6YyG0vtgFLspC&X-Amz-Signature=effaece2274f02ee36fcff443eede4309baed4a4396aef597b98ec5cf00d241d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSTY5ME2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbnTt7aP27u8aQuiXGWlt5ivubQxBlwqPAu7A5FQQPpAIhAOOkG11vFbdBHjVmXKRjfbUcMRQylI558%2BVWdc%2FxOWchKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuhzU7aIS%2FQraaVKcq3AN%2FMr08a16XqZrvQiEpTfmLoe1OrUz%2FAH8a6dXN3bjd5%2BZoRkQMj7v9JOWms6LkDjO21zs%2FjB3MSto2Jx%2FhTw9byTLPaDtoJFsbsgweulneLjpm6lzJNZqKfNG7jlVJt9d1PX%2FPJ2DSLVJKYzzIpwWZviCPW558ZZt7%2BgKJ2q7AmnzYaNSVAv1eYoWwxzQPHNpzHBUidvE7EC7zuG4SkZcerMD8coFVFCgTk00%2FnPq9WPspvxFHjjAlf4JFFxabV0079bGmKsdxpxt%2BGQx7ie8Bdl76Y6YdyvldyJwreMJ49o9LQ6lzaiGhOW4J85nQ7sIdXmU5DKP7Qcnb9PmrPyRHAwm6QzIzK1PVPyZx91mmjf7TOP64nWEV6GMNSawRqqTiYWhAkX%2BNH3qTzlJ%2Fkf3ZG3pN9auKLM1xtLgigK6a4GXGOlGzeHDDPuQ7HN5cvsNowDS1ShUjHtWu%2FLVLbu3G45IeUU5i2ckg9I8yuBRyedjplwTk2Ccv%2BeM6UxLkmV%2BepQGBycINDTI3jDqJhNpAcn9Dk2a66h48mQma6boAsGiJLQqTizmjza958QRmGTt3xGr890m4SSrvenl1ivvb4y4tneuNG6aHcDRh%2B4FzbEFtxBCKq9G7D%2FbeLDDrlqXMBjqkAVT7KzUk6094bM84AiyH5%2Bzy7ld5hLpjHMVaRE%2BjtTstVfvWtcwY%2BxaN4XGN9vBk0mWQQE9sFUa%2FKJxz28QUahu5j6vIU4vTnDDhjRY7HM%2BZWSAKqm7robogO2W937MBoKUcCyO027PjdCz92HR%2B58zd351Ih4HBO0y5oMLMdFO%2FrxRAYgL9UC%2BRn39o6aMFK1pvx2%2BlgQOYZtZ6YyG0vtgFLspC&X-Amz-Signature=a7f53ac2621fd5e29f255b3ce7d4b63677bc72b50eab98b5969a1a270c5c78ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



