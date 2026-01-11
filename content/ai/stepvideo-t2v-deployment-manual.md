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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NOM7ZCK%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQC7T6uo547IXnVTev2xaX5WbLhbbNStbM0mfbfI7GbwowIhAIC6ntSNIlsk5kLHqovVAtS%2FYXUMVhSD4J1mvL1%2BB2hIKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxf4%2B5QCbUAGUe78cwq3AMSG6ZYuBo6ltK7FeF9UL5Dbaguyyl5oM4zLjw0Zp%2BD5qq8KCz%2FLDdst5LTijfe01CMabxK43QuKT01FTstiAG%2FxITgRkJ10evn%2Bu6SGD18g7O0hGuwSQdfH9anzrXq6MnMs%2FkNL%2BBUV0vGC6MzhOK4xphm5U2HYxQ6PmkcYU%2B0OVC%2B6ZvM1HCoYaDBYjlR1lP4pJvvwMwlKlZCwJC86uU7zRhWg7KHo97mu5zQTHeyomBQVbdFViCYt8Qovu4vAOyBa2q4wwBvrSfKMczojbgrx4yixk%2BMmQv%2B9RKgfCX2NPhiCATGKRLiVUrgs8uUA1q4OBsKxIhuTcqJnlKm0TeYQWA5svwqNFdgsDmI8sNqUMvqPBGZNuOvrBzpSq82nKX%2FxB0yVYRUseQcvM8PsjaqV859GVpYbfWgiF2GDewSLwnpr1w3h8gBacvy%2Fl%2BRu3WpKb5zYm2cPekDc%2BgIK4Hgags62c2VjZa%2BNNMaPw4Xh8OIErGE6fCAwLeVvpdxJmMjiZMcEYmWGx0msBkmQGgH6sQ2ERA6ZnhyMZmGA7FGMi7P9GbCBPVQTMFhJ76CKDz%2BwrZrsJCXkxGIxGAAG9LM5JK1opEkWXRBdeYys%2Fc3MvHvSfakl5sX9jf%2FWDDX%2FovLBjqkAWER0MLwMEaxzDgF9m%2BmZYH%2Fut80mUBC%2BmhQEw4s0GDWrvB4cvKE484E94z8PI5VeygZ49WG25A1k28ryJI1xmkJEQyoLiUZKMlbkw%2BkH26uz9C%2FCGgfWPUxIEW1Ee7ds20Pw%2F7jTZVmQ84jyG4%2FRDFxv3O5MtEkoMKvTYmDFcJHrSc3Oy5GMreDuG7D6Uaj9ywO9cCTtdHo5HfGdn48pyr1hNyA&X-Amz-Signature=5303eccab214cda7b1aeff691b4ca40f1e2c3e7a1d4de8cd1b9a0aaca22aa750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NOM7ZCK%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQC7T6uo547IXnVTev2xaX5WbLhbbNStbM0mfbfI7GbwowIhAIC6ntSNIlsk5kLHqovVAtS%2FYXUMVhSD4J1mvL1%2BB2hIKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxf4%2B5QCbUAGUe78cwq3AMSG6ZYuBo6ltK7FeF9UL5Dbaguyyl5oM4zLjw0Zp%2BD5qq8KCz%2FLDdst5LTijfe01CMabxK43QuKT01FTstiAG%2FxITgRkJ10evn%2Bu6SGD18g7O0hGuwSQdfH9anzrXq6MnMs%2FkNL%2BBUV0vGC6MzhOK4xphm5U2HYxQ6PmkcYU%2B0OVC%2B6ZvM1HCoYaDBYjlR1lP4pJvvwMwlKlZCwJC86uU7zRhWg7KHo97mu5zQTHeyomBQVbdFViCYt8Qovu4vAOyBa2q4wwBvrSfKMczojbgrx4yixk%2BMmQv%2B9RKgfCX2NPhiCATGKRLiVUrgs8uUA1q4OBsKxIhuTcqJnlKm0TeYQWA5svwqNFdgsDmI8sNqUMvqPBGZNuOvrBzpSq82nKX%2FxB0yVYRUseQcvM8PsjaqV859GVpYbfWgiF2GDewSLwnpr1w3h8gBacvy%2Fl%2BRu3WpKb5zYm2cPekDc%2BgIK4Hgags62c2VjZa%2BNNMaPw4Xh8OIErGE6fCAwLeVvpdxJmMjiZMcEYmWGx0msBkmQGgH6sQ2ERA6ZnhyMZmGA7FGMi7P9GbCBPVQTMFhJ76CKDz%2BwrZrsJCXkxGIxGAAG9LM5JK1opEkWXRBdeYys%2Fc3MvHvSfakl5sX9jf%2FWDDX%2FovLBjqkAWER0MLwMEaxzDgF9m%2BmZYH%2Fut80mUBC%2BmhQEw4s0GDWrvB4cvKE484E94z8PI5VeygZ49WG25A1k28ryJI1xmkJEQyoLiUZKMlbkw%2BkH26uz9C%2FCGgfWPUxIEW1Ee7ds20Pw%2F7jTZVmQ84jyG4%2FRDFxv3O5MtEkoMKvTYmDFcJHrSc3Oy5GMreDuG7D6Uaj9ywO9cCTtdHo5HfGdn48pyr1hNyA&X-Amz-Signature=bff9553fc49cad1e2f67b2e3063632c2368f6548380038f75ee8776d567a3c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NOM7ZCK%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQC7T6uo547IXnVTev2xaX5WbLhbbNStbM0mfbfI7GbwowIhAIC6ntSNIlsk5kLHqovVAtS%2FYXUMVhSD4J1mvL1%2BB2hIKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxf4%2B5QCbUAGUe78cwq3AMSG6ZYuBo6ltK7FeF9UL5Dbaguyyl5oM4zLjw0Zp%2BD5qq8KCz%2FLDdst5LTijfe01CMabxK43QuKT01FTstiAG%2FxITgRkJ10evn%2Bu6SGD18g7O0hGuwSQdfH9anzrXq6MnMs%2FkNL%2BBUV0vGC6MzhOK4xphm5U2HYxQ6PmkcYU%2B0OVC%2B6ZvM1HCoYaDBYjlR1lP4pJvvwMwlKlZCwJC86uU7zRhWg7KHo97mu5zQTHeyomBQVbdFViCYt8Qovu4vAOyBa2q4wwBvrSfKMczojbgrx4yixk%2BMmQv%2B9RKgfCX2NPhiCATGKRLiVUrgs8uUA1q4OBsKxIhuTcqJnlKm0TeYQWA5svwqNFdgsDmI8sNqUMvqPBGZNuOvrBzpSq82nKX%2FxB0yVYRUseQcvM8PsjaqV859GVpYbfWgiF2GDewSLwnpr1w3h8gBacvy%2Fl%2BRu3WpKb5zYm2cPekDc%2BgIK4Hgags62c2VjZa%2BNNMaPw4Xh8OIErGE6fCAwLeVvpdxJmMjiZMcEYmWGx0msBkmQGgH6sQ2ERA6ZnhyMZmGA7FGMi7P9GbCBPVQTMFhJ76CKDz%2BwrZrsJCXkxGIxGAAG9LM5JK1opEkWXRBdeYys%2Fc3MvHvSfakl5sX9jf%2FWDDX%2FovLBjqkAWER0MLwMEaxzDgF9m%2BmZYH%2Fut80mUBC%2BmhQEw4s0GDWrvB4cvKE484E94z8PI5VeygZ49WG25A1k28ryJI1xmkJEQyoLiUZKMlbkw%2BkH26uz9C%2FCGgfWPUxIEW1Ee7ds20Pw%2F7jTZVmQ84jyG4%2FRDFxv3O5MtEkoMKvTYmDFcJHrSc3Oy5GMreDuG7D6Uaj9ywO9cCTtdHo5HfGdn48pyr1hNyA&X-Amz-Signature=72934e5d3f622b9c9291755377b7141dfe212897b69aa7865379c6e8b7e9fe82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NOM7ZCK%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQC7T6uo547IXnVTev2xaX5WbLhbbNStbM0mfbfI7GbwowIhAIC6ntSNIlsk5kLHqovVAtS%2FYXUMVhSD4J1mvL1%2BB2hIKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxf4%2B5QCbUAGUe78cwq3AMSG6ZYuBo6ltK7FeF9UL5Dbaguyyl5oM4zLjw0Zp%2BD5qq8KCz%2FLDdst5LTijfe01CMabxK43QuKT01FTstiAG%2FxITgRkJ10evn%2Bu6SGD18g7O0hGuwSQdfH9anzrXq6MnMs%2FkNL%2BBUV0vGC6MzhOK4xphm5U2HYxQ6PmkcYU%2B0OVC%2B6ZvM1HCoYaDBYjlR1lP4pJvvwMwlKlZCwJC86uU7zRhWg7KHo97mu5zQTHeyomBQVbdFViCYt8Qovu4vAOyBa2q4wwBvrSfKMczojbgrx4yixk%2BMmQv%2B9RKgfCX2NPhiCATGKRLiVUrgs8uUA1q4OBsKxIhuTcqJnlKm0TeYQWA5svwqNFdgsDmI8sNqUMvqPBGZNuOvrBzpSq82nKX%2FxB0yVYRUseQcvM8PsjaqV859GVpYbfWgiF2GDewSLwnpr1w3h8gBacvy%2Fl%2BRu3WpKb5zYm2cPekDc%2BgIK4Hgags62c2VjZa%2BNNMaPw4Xh8OIErGE6fCAwLeVvpdxJmMjiZMcEYmWGx0msBkmQGgH6sQ2ERA6ZnhyMZmGA7FGMi7P9GbCBPVQTMFhJ76CKDz%2BwrZrsJCXkxGIxGAAG9LM5JK1opEkWXRBdeYys%2Fc3MvHvSfakl5sX9jf%2FWDDX%2FovLBjqkAWER0MLwMEaxzDgF9m%2BmZYH%2Fut80mUBC%2BmhQEw4s0GDWrvB4cvKE484E94z8PI5VeygZ49WG25A1k28ryJI1xmkJEQyoLiUZKMlbkw%2BkH26uz9C%2FCGgfWPUxIEW1Ee7ds20Pw%2F7jTZVmQ84jyG4%2FRDFxv3O5MtEkoMKvTYmDFcJHrSc3Oy5GMreDuG7D6Uaj9ywO9cCTtdHo5HfGdn48pyr1hNyA&X-Amz-Signature=db6b5499e72d99c67f3a4e2ff242856d1f94f1a017a2c55056101826f877cf91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



