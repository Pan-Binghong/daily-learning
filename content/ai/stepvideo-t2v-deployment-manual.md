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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEWCWQDE%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkNN1r8BrWbVTd2SK8D1Q767g54nKvZPQ8020rT%2BvcnAiAu%2Fbk8xyW64d1gNWc5RgoOErDNd5FFvEbUvu3dlHXdLCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMhdHjVd%2FUIJfN4y7vKtwDQgShFf1xYNmMQKvP6EqGFhFu%2BjEdixtbpLA8hXkxsJ1mrdBB55qJz0g%2BpDZDSag%2Fw2Eu%2FAUaU8%2BB6gQdZ1ppKBSK927F9GgxP0xz6r37NiemLhDll6ISFf5bjLfag7NyVsAgCM9SCUc2bTx5vEzqDXKyMlMCkre6G71fmTVOFS0jQx6t0c3oxDQT651teVpHif8JPR03MMrGidSh6US5cTJ3p4Z6yeK4BPZ5bZwwbIxvjI2IcFD01AQtDu9Fymf85gHp%2BPg6vRq2EbwkaThiVyXzje2EHiHCWi58fXce65IBAWit5lXjLhdaoyUCVpbRq3dkI3PKcK7Dl59yu0%2FtHmh4lerG3MW8rkreVJgDFVHkQQlqs3%2Fy70k6aaAWWH4Ta%2BO8k0FfXhEXPdSBYY2sH%2BXaDXGBbUSLCxxthtjLIJx9%2BquL3PKFeIyNur3rvShRIZ8xAJfte69gOwHyTYJ9xX%2BuHGIwdYh%2F2m6CNUfSkl5HuKsCXrllIG2QqwFTgc%2FJzHS42Y3HFN1gpiX%2BZcg%2B1gIROVaQ79aUlYyC7huS88gN4YXc2GwDCUD0aucWZazmjQetYTqeZJGwWoA3gi8C%2FXdFiSmmDu9H8adCRs5ZGtcBD4I%2B1Ro1z8i7rqkwzqLrywY6pgEwSPiVVUA6Lds%2FTyn7bo3mXGf1fAgj611npSbGvmZg%2BHmFD416v9tjOcXzsKeXVNP43kl1mRQOATIqVIsaK9xcDqAswAFkeNEhAGpVixQV4q8tYa3xLL281XXUlZ1VQKmj4FUduz0OEP15CuQlxMbpt1xGzpStdQZ1hkoKKOseXC2j%2FiANtvvHNLbXo4pqSajr8XvlrvO%2FdBo8zHT3m2WoFi%2F0W4ON&X-Amz-Signature=68429da22069bfe537359c3cd3e3e1d9a93cd9c92e0ecd29d32570ba236249ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEWCWQDE%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkNN1r8BrWbVTd2SK8D1Q767g54nKvZPQ8020rT%2BvcnAiAu%2Fbk8xyW64d1gNWc5RgoOErDNd5FFvEbUvu3dlHXdLCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMhdHjVd%2FUIJfN4y7vKtwDQgShFf1xYNmMQKvP6EqGFhFu%2BjEdixtbpLA8hXkxsJ1mrdBB55qJz0g%2BpDZDSag%2Fw2Eu%2FAUaU8%2BB6gQdZ1ppKBSK927F9GgxP0xz6r37NiemLhDll6ISFf5bjLfag7NyVsAgCM9SCUc2bTx5vEzqDXKyMlMCkre6G71fmTVOFS0jQx6t0c3oxDQT651teVpHif8JPR03MMrGidSh6US5cTJ3p4Z6yeK4BPZ5bZwwbIxvjI2IcFD01AQtDu9Fymf85gHp%2BPg6vRq2EbwkaThiVyXzje2EHiHCWi58fXce65IBAWit5lXjLhdaoyUCVpbRq3dkI3PKcK7Dl59yu0%2FtHmh4lerG3MW8rkreVJgDFVHkQQlqs3%2Fy70k6aaAWWH4Ta%2BO8k0FfXhEXPdSBYY2sH%2BXaDXGBbUSLCxxthtjLIJx9%2BquL3PKFeIyNur3rvShRIZ8xAJfte69gOwHyTYJ9xX%2BuHGIwdYh%2F2m6CNUfSkl5HuKsCXrllIG2QqwFTgc%2FJzHS42Y3HFN1gpiX%2BZcg%2B1gIROVaQ79aUlYyC7huS88gN4YXc2GwDCUD0aucWZazmjQetYTqeZJGwWoA3gi8C%2FXdFiSmmDu9H8adCRs5ZGtcBD4I%2B1Ro1z8i7rqkwzqLrywY6pgEwSPiVVUA6Lds%2FTyn7bo3mXGf1fAgj611npSbGvmZg%2BHmFD416v9tjOcXzsKeXVNP43kl1mRQOATIqVIsaK9xcDqAswAFkeNEhAGpVixQV4q8tYa3xLL281XXUlZ1VQKmj4FUduz0OEP15CuQlxMbpt1xGzpStdQZ1hkoKKOseXC2j%2FiANtvvHNLbXo4pqSajr8XvlrvO%2FdBo8zHT3m2WoFi%2F0W4ON&X-Amz-Signature=e26d0fddda0c43e930232088749c3284f650b0c055eb352688edd3ac801b7453&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEWCWQDE%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkNN1r8BrWbVTd2SK8D1Q767g54nKvZPQ8020rT%2BvcnAiAu%2Fbk8xyW64d1gNWc5RgoOErDNd5FFvEbUvu3dlHXdLCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMhdHjVd%2FUIJfN4y7vKtwDQgShFf1xYNmMQKvP6EqGFhFu%2BjEdixtbpLA8hXkxsJ1mrdBB55qJz0g%2BpDZDSag%2Fw2Eu%2FAUaU8%2BB6gQdZ1ppKBSK927F9GgxP0xz6r37NiemLhDll6ISFf5bjLfag7NyVsAgCM9SCUc2bTx5vEzqDXKyMlMCkre6G71fmTVOFS0jQx6t0c3oxDQT651teVpHif8JPR03MMrGidSh6US5cTJ3p4Z6yeK4BPZ5bZwwbIxvjI2IcFD01AQtDu9Fymf85gHp%2BPg6vRq2EbwkaThiVyXzje2EHiHCWi58fXce65IBAWit5lXjLhdaoyUCVpbRq3dkI3PKcK7Dl59yu0%2FtHmh4lerG3MW8rkreVJgDFVHkQQlqs3%2Fy70k6aaAWWH4Ta%2BO8k0FfXhEXPdSBYY2sH%2BXaDXGBbUSLCxxthtjLIJx9%2BquL3PKFeIyNur3rvShRIZ8xAJfte69gOwHyTYJ9xX%2BuHGIwdYh%2F2m6CNUfSkl5HuKsCXrllIG2QqwFTgc%2FJzHS42Y3HFN1gpiX%2BZcg%2B1gIROVaQ79aUlYyC7huS88gN4YXc2GwDCUD0aucWZazmjQetYTqeZJGwWoA3gi8C%2FXdFiSmmDu9H8adCRs5ZGtcBD4I%2B1Ro1z8i7rqkwzqLrywY6pgEwSPiVVUA6Lds%2FTyn7bo3mXGf1fAgj611npSbGvmZg%2BHmFD416v9tjOcXzsKeXVNP43kl1mRQOATIqVIsaK9xcDqAswAFkeNEhAGpVixQV4q8tYa3xLL281XXUlZ1VQKmj4FUduz0OEP15CuQlxMbpt1xGzpStdQZ1hkoKKOseXC2j%2FiANtvvHNLbXo4pqSajr8XvlrvO%2FdBo8zHT3m2WoFi%2F0W4ON&X-Amz-Signature=948bf6ada3d16b3c11aef8a6fe7907edd11de7958e6c8ae2fba8456343cabf04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEWCWQDE%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkNN1r8BrWbVTd2SK8D1Q767g54nKvZPQ8020rT%2BvcnAiAu%2Fbk8xyW64d1gNWc5RgoOErDNd5FFvEbUvu3dlHXdLCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMhdHjVd%2FUIJfN4y7vKtwDQgShFf1xYNmMQKvP6EqGFhFu%2BjEdixtbpLA8hXkxsJ1mrdBB55qJz0g%2BpDZDSag%2Fw2Eu%2FAUaU8%2BB6gQdZ1ppKBSK927F9GgxP0xz6r37NiemLhDll6ISFf5bjLfag7NyVsAgCM9SCUc2bTx5vEzqDXKyMlMCkre6G71fmTVOFS0jQx6t0c3oxDQT651teVpHif8JPR03MMrGidSh6US5cTJ3p4Z6yeK4BPZ5bZwwbIxvjI2IcFD01AQtDu9Fymf85gHp%2BPg6vRq2EbwkaThiVyXzje2EHiHCWi58fXce65IBAWit5lXjLhdaoyUCVpbRq3dkI3PKcK7Dl59yu0%2FtHmh4lerG3MW8rkreVJgDFVHkQQlqs3%2Fy70k6aaAWWH4Ta%2BO8k0FfXhEXPdSBYY2sH%2BXaDXGBbUSLCxxthtjLIJx9%2BquL3PKFeIyNur3rvShRIZ8xAJfte69gOwHyTYJ9xX%2BuHGIwdYh%2F2m6CNUfSkl5HuKsCXrllIG2QqwFTgc%2FJzHS42Y3HFN1gpiX%2BZcg%2B1gIROVaQ79aUlYyC7huS88gN4YXc2GwDCUD0aucWZazmjQetYTqeZJGwWoA3gi8C%2FXdFiSmmDu9H8adCRs5ZGtcBD4I%2B1Ro1z8i7rqkwzqLrywY6pgEwSPiVVUA6Lds%2FTyn7bo3mXGf1fAgj611npSbGvmZg%2BHmFD416v9tjOcXzsKeXVNP43kl1mRQOATIqVIsaK9xcDqAswAFkeNEhAGpVixQV4q8tYa3xLL281XXUlZ1VQKmj4FUduz0OEP15CuQlxMbpt1xGzpStdQZ1hkoKKOseXC2j%2FiANtvvHNLbXo4pqSajr8XvlrvO%2FdBo8zHT3m2WoFi%2F0W4ON&X-Amz-Signature=2ecffcf451cac61d649a4556562f79adb5ae5f653e48d47d6aff560b90acccbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



