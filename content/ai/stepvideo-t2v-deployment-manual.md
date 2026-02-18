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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZYR3I7L%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcoTWfdw4sZmhh8gmgORJpTnSReVJf8gljsHFu6mheFAIgYH8Q4mLexWF7wM4i2SFTj2PsKsxzmG0wapeRWuVF3%2FIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOZlvSSxNmVv2AEhJyrcA0XoIY4YFlVIt0HgzJi4hz6paOgmTRVL0JqJ8zI%2FHjls9G3WV05TPJ9i%2FSmvCyXhz6tCueXQcl6d5eFhzLPiyEj%2B%2Bw%2FWsKffDRZs0kWBsBz%2FtIasmyhLPuIDTtUJXTPhq22t%2Bjv0YjOC3Y8c2nGhzdRxoMKbKM6UwHkdGakBd7bEFj1vkqc%2F3cZToyuOC0y9OWJADWWVrOy1MEkhYIN7ZmhhbgGnRoGR8mMIxyvDevbC4KMXWew8SwfhXPmwZgNj%2BcMN2fVJEDeR3oD46l3ncDjjU%2B70aX05Vcq%2FPmZjAICELXKivsZRbTqkYHaWHPCXVtULM50ODGNuiX90dG7yoQGhrh9ypWDVmPf%2FVjAcbIewRsRqZTfzFGxrvH03y7CBVzVvne0u8p2ujg569CeELaLSaol6KIBWJpRvXQim9%2By9YW%2B9F8KA9at1Mos%2BaLpW8PJ3t3v%2F2RHiEB4IKHU0FrN3gC3IOWnajVjx5C5Io2igXm7Xg9Fx2eHzCvCWYhgU2pzGmCT%2F00Fj%2BrEB3ZKiM2gvnQjCbg6AOxXYKYCSubZzhAsfHt%2Bw1cyX12lz9A6tKd%2F2DfMel%2BzBMfajce3MMEhI1BcG6jcJJrsvkmW%2Bw89g6hAqgC4s3dwbQnSOMPif1MwGOqUBe%2BN39TqRzzvOapC6hM%2BOXqbNIDmEtlOMa4rNjCo4kxbApepOJxGlMTfapY28W8ym%2BJiRJg9mKf2dUqnMMKJ9tKr7ckMwG4qFa85Wh3lsR3bJrjBrCBCGi7YV6Ssbgt9bQbh6Z1N16RIYW9%2BLWz0z3NVpo5fgGNx4U7y0omEB7pDuhmfTzzXHbkJnfBRur%2BxNcI2KlS7rfN96kjGH%2FdbznHNs%2BZr7&X-Amz-Signature=b81379f4475934f65826c45c2e6c13835b4b57f6780af1af1c71c2fdbad26491&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZYR3I7L%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcoTWfdw4sZmhh8gmgORJpTnSReVJf8gljsHFu6mheFAIgYH8Q4mLexWF7wM4i2SFTj2PsKsxzmG0wapeRWuVF3%2FIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOZlvSSxNmVv2AEhJyrcA0XoIY4YFlVIt0HgzJi4hz6paOgmTRVL0JqJ8zI%2FHjls9G3WV05TPJ9i%2FSmvCyXhz6tCueXQcl6d5eFhzLPiyEj%2B%2Bw%2FWsKffDRZs0kWBsBz%2FtIasmyhLPuIDTtUJXTPhq22t%2Bjv0YjOC3Y8c2nGhzdRxoMKbKM6UwHkdGakBd7bEFj1vkqc%2F3cZToyuOC0y9OWJADWWVrOy1MEkhYIN7ZmhhbgGnRoGR8mMIxyvDevbC4KMXWew8SwfhXPmwZgNj%2BcMN2fVJEDeR3oD46l3ncDjjU%2B70aX05Vcq%2FPmZjAICELXKivsZRbTqkYHaWHPCXVtULM50ODGNuiX90dG7yoQGhrh9ypWDVmPf%2FVjAcbIewRsRqZTfzFGxrvH03y7CBVzVvne0u8p2ujg569CeELaLSaol6KIBWJpRvXQim9%2By9YW%2B9F8KA9at1Mos%2BaLpW8PJ3t3v%2F2RHiEB4IKHU0FrN3gC3IOWnajVjx5C5Io2igXm7Xg9Fx2eHzCvCWYhgU2pzGmCT%2F00Fj%2BrEB3ZKiM2gvnQjCbg6AOxXYKYCSubZzhAsfHt%2Bw1cyX12lz9A6tKd%2F2DfMel%2BzBMfajce3MMEhI1BcG6jcJJrsvkmW%2Bw89g6hAqgC4s3dwbQnSOMPif1MwGOqUBe%2BN39TqRzzvOapC6hM%2BOXqbNIDmEtlOMa4rNjCo4kxbApepOJxGlMTfapY28W8ym%2BJiRJg9mKf2dUqnMMKJ9tKr7ckMwG4qFa85Wh3lsR3bJrjBrCBCGi7YV6Ssbgt9bQbh6Z1N16RIYW9%2BLWz0z3NVpo5fgGNx4U7y0omEB7pDuhmfTzzXHbkJnfBRur%2BxNcI2KlS7rfN96kjGH%2FdbznHNs%2BZr7&X-Amz-Signature=115d5b08450cdfc7cfe3f14ce80477cb5072bc299d5782ddefb828400d8073ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZYR3I7L%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcoTWfdw4sZmhh8gmgORJpTnSReVJf8gljsHFu6mheFAIgYH8Q4mLexWF7wM4i2SFTj2PsKsxzmG0wapeRWuVF3%2FIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOZlvSSxNmVv2AEhJyrcA0XoIY4YFlVIt0HgzJi4hz6paOgmTRVL0JqJ8zI%2FHjls9G3WV05TPJ9i%2FSmvCyXhz6tCueXQcl6d5eFhzLPiyEj%2B%2Bw%2FWsKffDRZs0kWBsBz%2FtIasmyhLPuIDTtUJXTPhq22t%2Bjv0YjOC3Y8c2nGhzdRxoMKbKM6UwHkdGakBd7bEFj1vkqc%2F3cZToyuOC0y9OWJADWWVrOy1MEkhYIN7ZmhhbgGnRoGR8mMIxyvDevbC4KMXWew8SwfhXPmwZgNj%2BcMN2fVJEDeR3oD46l3ncDjjU%2B70aX05Vcq%2FPmZjAICELXKivsZRbTqkYHaWHPCXVtULM50ODGNuiX90dG7yoQGhrh9ypWDVmPf%2FVjAcbIewRsRqZTfzFGxrvH03y7CBVzVvne0u8p2ujg569CeELaLSaol6KIBWJpRvXQim9%2By9YW%2B9F8KA9at1Mos%2BaLpW8PJ3t3v%2F2RHiEB4IKHU0FrN3gC3IOWnajVjx5C5Io2igXm7Xg9Fx2eHzCvCWYhgU2pzGmCT%2F00Fj%2BrEB3ZKiM2gvnQjCbg6AOxXYKYCSubZzhAsfHt%2Bw1cyX12lz9A6tKd%2F2DfMel%2BzBMfajce3MMEhI1BcG6jcJJrsvkmW%2Bw89g6hAqgC4s3dwbQnSOMPif1MwGOqUBe%2BN39TqRzzvOapC6hM%2BOXqbNIDmEtlOMa4rNjCo4kxbApepOJxGlMTfapY28W8ym%2BJiRJg9mKf2dUqnMMKJ9tKr7ckMwG4qFa85Wh3lsR3bJrjBrCBCGi7YV6Ssbgt9bQbh6Z1N16RIYW9%2BLWz0z3NVpo5fgGNx4U7y0omEB7pDuhmfTzzXHbkJnfBRur%2BxNcI2KlS7rfN96kjGH%2FdbznHNs%2BZr7&X-Amz-Signature=27ac9f0ee098513cb2626a7bdb15f675dd34f8ff5d2ddd39bd54fbc7e224af2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZYR3I7L%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcoTWfdw4sZmhh8gmgORJpTnSReVJf8gljsHFu6mheFAIgYH8Q4mLexWF7wM4i2SFTj2PsKsxzmG0wapeRWuVF3%2FIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOZlvSSxNmVv2AEhJyrcA0XoIY4YFlVIt0HgzJi4hz6paOgmTRVL0JqJ8zI%2FHjls9G3WV05TPJ9i%2FSmvCyXhz6tCueXQcl6d5eFhzLPiyEj%2B%2Bw%2FWsKffDRZs0kWBsBz%2FtIasmyhLPuIDTtUJXTPhq22t%2Bjv0YjOC3Y8c2nGhzdRxoMKbKM6UwHkdGakBd7bEFj1vkqc%2F3cZToyuOC0y9OWJADWWVrOy1MEkhYIN7ZmhhbgGnRoGR8mMIxyvDevbC4KMXWew8SwfhXPmwZgNj%2BcMN2fVJEDeR3oD46l3ncDjjU%2B70aX05Vcq%2FPmZjAICELXKivsZRbTqkYHaWHPCXVtULM50ODGNuiX90dG7yoQGhrh9ypWDVmPf%2FVjAcbIewRsRqZTfzFGxrvH03y7CBVzVvne0u8p2ujg569CeELaLSaol6KIBWJpRvXQim9%2By9YW%2B9F8KA9at1Mos%2BaLpW8PJ3t3v%2F2RHiEB4IKHU0FrN3gC3IOWnajVjx5C5Io2igXm7Xg9Fx2eHzCvCWYhgU2pzGmCT%2F00Fj%2BrEB3ZKiM2gvnQjCbg6AOxXYKYCSubZzhAsfHt%2Bw1cyX12lz9A6tKd%2F2DfMel%2BzBMfajce3MMEhI1BcG6jcJJrsvkmW%2Bw89g6hAqgC4s3dwbQnSOMPif1MwGOqUBe%2BN39TqRzzvOapC6hM%2BOXqbNIDmEtlOMa4rNjCo4kxbApepOJxGlMTfapY28W8ym%2BJiRJg9mKf2dUqnMMKJ9tKr7ckMwG4qFa85Wh3lsR3bJrjBrCBCGi7YV6Ssbgt9bQbh6Z1N16RIYW9%2BLWz0z3NVpo5fgGNx4U7y0omEB7pDuhmfTzzXHbkJnfBRur%2BxNcI2KlS7rfN96kjGH%2FdbznHNs%2BZr7&X-Amz-Signature=915ee33477d77f09433f5033ec2ccbdfbede7c35925aebb66d8b4746ce27cde6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



