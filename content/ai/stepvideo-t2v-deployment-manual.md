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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIM473C%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCICt8zGLfdc2WRaQWmwpD1HsQjJNziW6XozqFM3OLf8cnAiEA0xzW5BezUr2jqyMkbi2kLjcrc4VaigD9ywR679aA2RkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2Fn0V9zVizTddd4DircA%2Fh6SPVfSea%2BLnSFrmLQCBGcNrEwhKCNMUoqlK69X1xV6MqJkwS5q0%2Bz7ZD23lGNhmOCVyKJYU3jkfF2ld0SIEFU3D1myQMWm7AtQPMO3l1IAYEe7DIsgwmfM%2BmvTwStgOgtKHs3AISyx9jWCCo6MaxjmSJxXflvFQ7uaiBmLPezcoNxraTVHykZGdYSUFjLaS57eGaZxVg%2F33Ijy0jg%2Frn7faSSsF4Mxj4oP4xcKJ3gJWxsOb0BVfndiPQsy1x3vCEkQKld%2BfY0E2vUvh%2FU8Cb06Tyifz4aqeSP2pz2%2BtaEUCxgXLPqfd0QheI0kSEfQm1TMnt9gnnsMeZ2NhKvQdAkecIE39Ha%2B7rOx9z1nEEKPWUQD24SH8ndVOo%2Fq%2F5YY7VizpguB1WEzj0t6KJNSMVvfZszf6KWuLeQfHYQhQjqM2NwqnYKg5QUuJD%2Fu%2BGgmYUxoiXARfE%2Fl%2Bts0vWFZ%2BuFK5JOEg86B2cZb%2Ff1bcTzBakadgykfla1m6HRvRksfUBeLdIs%2BEam%2Fpsj3YZztOEwpKTW3Zr1i6j48AuWj3KlX31cgGzHOTgs5WzeqMfZ06ek7Up3M3T3IGTvbNQWRX3kPkbIf7XA%2BCEjAtM51lZ%2BuUwCGBGHp94XYa1lMNS5uswGOqUBI04sM5gIWjKEv3mtrzUQG23RCdBbuJB%2FU1PYtwFHkgyWXnUfhZirgl1Ps9%2BYLY%2FlHpvhV3Zk6SoyzxKEqyvUpmaDUXtmUKFiq%2Fe7j8z6KsyzSrTJz8ZkQa7YOdbryOGNy5LaefEi0cZaZEFnZa2%2BuAsLR%2B8%2BvPN0g%2FJYLOWah5NFAR4bd2IYe%2Ff0T2dJ5L8AMqVCgSBIKDheAk6ItOCwJOgrc2ut&X-Amz-Signature=eae9af71bb4fe121be287d65c83b4d31be5e35cc28324b9fd1cc623e3af56bfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIM473C%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCICt8zGLfdc2WRaQWmwpD1HsQjJNziW6XozqFM3OLf8cnAiEA0xzW5BezUr2jqyMkbi2kLjcrc4VaigD9ywR679aA2RkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2Fn0V9zVizTddd4DircA%2Fh6SPVfSea%2BLnSFrmLQCBGcNrEwhKCNMUoqlK69X1xV6MqJkwS5q0%2Bz7ZD23lGNhmOCVyKJYU3jkfF2ld0SIEFU3D1myQMWm7AtQPMO3l1IAYEe7DIsgwmfM%2BmvTwStgOgtKHs3AISyx9jWCCo6MaxjmSJxXflvFQ7uaiBmLPezcoNxraTVHykZGdYSUFjLaS57eGaZxVg%2F33Ijy0jg%2Frn7faSSsF4Mxj4oP4xcKJ3gJWxsOb0BVfndiPQsy1x3vCEkQKld%2BfY0E2vUvh%2FU8Cb06Tyifz4aqeSP2pz2%2BtaEUCxgXLPqfd0QheI0kSEfQm1TMnt9gnnsMeZ2NhKvQdAkecIE39Ha%2B7rOx9z1nEEKPWUQD24SH8ndVOo%2Fq%2F5YY7VizpguB1WEzj0t6KJNSMVvfZszf6KWuLeQfHYQhQjqM2NwqnYKg5QUuJD%2Fu%2BGgmYUxoiXARfE%2Fl%2Bts0vWFZ%2BuFK5JOEg86B2cZb%2Ff1bcTzBakadgykfla1m6HRvRksfUBeLdIs%2BEam%2Fpsj3YZztOEwpKTW3Zr1i6j48AuWj3KlX31cgGzHOTgs5WzeqMfZ06ek7Up3M3T3IGTvbNQWRX3kPkbIf7XA%2BCEjAtM51lZ%2BuUwCGBGHp94XYa1lMNS5uswGOqUBI04sM5gIWjKEv3mtrzUQG23RCdBbuJB%2FU1PYtwFHkgyWXnUfhZirgl1Ps9%2BYLY%2FlHpvhV3Zk6SoyzxKEqyvUpmaDUXtmUKFiq%2Fe7j8z6KsyzSrTJz8ZkQa7YOdbryOGNy5LaefEi0cZaZEFnZa2%2BuAsLR%2B8%2BvPN0g%2FJYLOWah5NFAR4bd2IYe%2Ff0T2dJ5L8AMqVCgSBIKDheAk6ItOCwJOgrc2ut&X-Amz-Signature=7bf4bd979ec67ea1849e1d9e3fd868cd1ee3eeb5933c1374384ba8fab76fb6d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIM473C%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCICt8zGLfdc2WRaQWmwpD1HsQjJNziW6XozqFM3OLf8cnAiEA0xzW5BezUr2jqyMkbi2kLjcrc4VaigD9ywR679aA2RkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2Fn0V9zVizTddd4DircA%2Fh6SPVfSea%2BLnSFrmLQCBGcNrEwhKCNMUoqlK69X1xV6MqJkwS5q0%2Bz7ZD23lGNhmOCVyKJYU3jkfF2ld0SIEFU3D1myQMWm7AtQPMO3l1IAYEe7DIsgwmfM%2BmvTwStgOgtKHs3AISyx9jWCCo6MaxjmSJxXflvFQ7uaiBmLPezcoNxraTVHykZGdYSUFjLaS57eGaZxVg%2F33Ijy0jg%2Frn7faSSsF4Mxj4oP4xcKJ3gJWxsOb0BVfndiPQsy1x3vCEkQKld%2BfY0E2vUvh%2FU8Cb06Tyifz4aqeSP2pz2%2BtaEUCxgXLPqfd0QheI0kSEfQm1TMnt9gnnsMeZ2NhKvQdAkecIE39Ha%2B7rOx9z1nEEKPWUQD24SH8ndVOo%2Fq%2F5YY7VizpguB1WEzj0t6KJNSMVvfZszf6KWuLeQfHYQhQjqM2NwqnYKg5QUuJD%2Fu%2BGgmYUxoiXARfE%2Fl%2Bts0vWFZ%2BuFK5JOEg86B2cZb%2Ff1bcTzBakadgykfla1m6HRvRksfUBeLdIs%2BEam%2Fpsj3YZztOEwpKTW3Zr1i6j48AuWj3KlX31cgGzHOTgs5WzeqMfZ06ek7Up3M3T3IGTvbNQWRX3kPkbIf7XA%2BCEjAtM51lZ%2BuUwCGBGHp94XYa1lMNS5uswGOqUBI04sM5gIWjKEv3mtrzUQG23RCdBbuJB%2FU1PYtwFHkgyWXnUfhZirgl1Ps9%2BYLY%2FlHpvhV3Zk6SoyzxKEqyvUpmaDUXtmUKFiq%2Fe7j8z6KsyzSrTJz8ZkQa7YOdbryOGNy5LaefEi0cZaZEFnZa2%2BuAsLR%2B8%2BvPN0g%2FJYLOWah5NFAR4bd2IYe%2Ff0T2dJ5L8AMqVCgSBIKDheAk6ItOCwJOgrc2ut&X-Amz-Signature=bbcff05fc282c395acf409678899e204c66486884d0081e6cf58a298c4513aba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIM473C%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCICt8zGLfdc2WRaQWmwpD1HsQjJNziW6XozqFM3OLf8cnAiEA0xzW5BezUr2jqyMkbi2kLjcrc4VaigD9ywR679aA2RkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2Fn0V9zVizTddd4DircA%2Fh6SPVfSea%2BLnSFrmLQCBGcNrEwhKCNMUoqlK69X1xV6MqJkwS5q0%2Bz7ZD23lGNhmOCVyKJYU3jkfF2ld0SIEFU3D1myQMWm7AtQPMO3l1IAYEe7DIsgwmfM%2BmvTwStgOgtKHs3AISyx9jWCCo6MaxjmSJxXflvFQ7uaiBmLPezcoNxraTVHykZGdYSUFjLaS57eGaZxVg%2F33Ijy0jg%2Frn7faSSsF4Mxj4oP4xcKJ3gJWxsOb0BVfndiPQsy1x3vCEkQKld%2BfY0E2vUvh%2FU8Cb06Tyifz4aqeSP2pz2%2BtaEUCxgXLPqfd0QheI0kSEfQm1TMnt9gnnsMeZ2NhKvQdAkecIE39Ha%2B7rOx9z1nEEKPWUQD24SH8ndVOo%2Fq%2F5YY7VizpguB1WEzj0t6KJNSMVvfZszf6KWuLeQfHYQhQjqM2NwqnYKg5QUuJD%2Fu%2BGgmYUxoiXARfE%2Fl%2Bts0vWFZ%2BuFK5JOEg86B2cZb%2Ff1bcTzBakadgykfla1m6HRvRksfUBeLdIs%2BEam%2Fpsj3YZztOEwpKTW3Zr1i6j48AuWj3KlX31cgGzHOTgs5WzeqMfZ06ek7Up3M3T3IGTvbNQWRX3kPkbIf7XA%2BCEjAtM51lZ%2BuUwCGBGHp94XYa1lMNS5uswGOqUBI04sM5gIWjKEv3mtrzUQG23RCdBbuJB%2FU1PYtwFHkgyWXnUfhZirgl1Ps9%2BYLY%2FlHpvhV3Zk6SoyzxKEqyvUpmaDUXtmUKFiq%2Fe7j8z6KsyzSrTJz8ZkQa7YOdbryOGNy5LaefEi0cZaZEFnZa2%2BuAsLR%2B8%2BvPN0g%2FJYLOWah5NFAR4bd2IYe%2Ff0T2dJ5L8AMqVCgSBIKDheAk6ItOCwJOgrc2ut&X-Amz-Signature=3b42aa082bbf81f857df648188bf0e68a6352dfc65ec7a328170c9c3be02572d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



