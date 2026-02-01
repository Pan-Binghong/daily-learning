---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2547UKH%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg5IfPa6tksg8Il8h%2BSFTDAuZpCFzEH54vtoY6KbUMuQIgPbZu0NUYLBjAPyAHRomkWP4Rpipkk8AKRKlb0GjYEJMqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI97fGVx01ogg2b%2FcyrcAx7itdS9L64%2FqILx%2Fg3df2jSxPNtVGTQthQxtZLp%2Bau5W6%2B4A0LJCCeHQwt2qmTCX0TZ1J0Q52q9Ep39jUQxHfe2rJ8ojgiVDD%2BiM7nfwlICAQhWBSQ2Xw9CX%2F1gZTR5%2Bgl5Yc0dif9Stk0e28jBFVWJqpOICEvQiipc6XiSAxzqCo2%2F1FxnlvrN3Ygm5mTPFjIM3xRUtybxyOusibL%2B%2BaqKB6Tp6c%2FZnjSFAp5xriKqB9n32aUBt%2BRF8eNF4bBIN%2FXYGBusqkS5%2B8ujsycsJDqxKdUOvQ5d5Ply%2B%2F3ycRKrVGa6Njyk9mUnkj5rJCBNZblPkDyI2HRqPv5Sha1G3OQm0Re8XWKAtLTKeBZiLYz6RjJi08KUft2LQmCOPgrJQav4YPr1geNcmHoEUj0a5q%2ByZ0uLaWaWOV626XR1%2BBP7%2FzH881M4Tq9MVgPsPMi6vItu3WzPlCCmJFbRuWA82ATPTKy7A4MLFacfWktBGad5KH4JF1PnQUnN0jwWzbSP4LCyb%2Bi%2FQLQ1PRC0F1WULsb%2BmAS4kK44Rh2kow6tvwoobXVRX4r37t8mFXowAukbq4ev3s3WshEVOp%2BcdT8xwOdf3BOu9a9fq%2Ftv%2BdiNr0nYXt1xzU%2Bm0Vm5DVhSMMCV%2B8sGOqUBCz5KWmq%2FbEsxT2mNKcoQwnqnkJzAOxeVI3b2h47nmDO1pWIYztdQncLRIMjW1I62oBcY3gCKjVV86Vp0JKZzVCjYPJbdBpVyrRahvcBEMVWjiHmB4f8XBL%2Fp2uOjoQ2nKymepmzYl%2BePAJS%2B4kUqyAiSS5ydik6qcuq7m3GJaXobFbPULDYPu37BpfutqGnH5e1yfhlZqkw9uh%2BIAXWOf4aVBK6X&X-Amz-Signature=9a2cb0b7cb8cc5bf17c8224d17e4b5d9ffd893b999a43491f416a5897d97e616&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2547UKH%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg5IfPa6tksg8Il8h%2BSFTDAuZpCFzEH54vtoY6KbUMuQIgPbZu0NUYLBjAPyAHRomkWP4Rpipkk8AKRKlb0GjYEJMqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI97fGVx01ogg2b%2FcyrcAx7itdS9L64%2FqILx%2Fg3df2jSxPNtVGTQthQxtZLp%2Bau5W6%2B4A0LJCCeHQwt2qmTCX0TZ1J0Q52q9Ep39jUQxHfe2rJ8ojgiVDD%2BiM7nfwlICAQhWBSQ2Xw9CX%2F1gZTR5%2Bgl5Yc0dif9Stk0e28jBFVWJqpOICEvQiipc6XiSAxzqCo2%2F1FxnlvrN3Ygm5mTPFjIM3xRUtybxyOusibL%2B%2BaqKB6Tp6c%2FZnjSFAp5xriKqB9n32aUBt%2BRF8eNF4bBIN%2FXYGBusqkS5%2B8ujsycsJDqxKdUOvQ5d5Ply%2B%2F3ycRKrVGa6Njyk9mUnkj5rJCBNZblPkDyI2HRqPv5Sha1G3OQm0Re8XWKAtLTKeBZiLYz6RjJi08KUft2LQmCOPgrJQav4YPr1geNcmHoEUj0a5q%2ByZ0uLaWaWOV626XR1%2BBP7%2FzH881M4Tq9MVgPsPMi6vItu3WzPlCCmJFbRuWA82ATPTKy7A4MLFacfWktBGad5KH4JF1PnQUnN0jwWzbSP4LCyb%2Bi%2FQLQ1PRC0F1WULsb%2BmAS4kK44Rh2kow6tvwoobXVRX4r37t8mFXowAukbq4ev3s3WshEVOp%2BcdT8xwOdf3BOu9a9fq%2Ftv%2BdiNr0nYXt1xzU%2Bm0Vm5DVhSMMCV%2B8sGOqUBCz5KWmq%2FbEsxT2mNKcoQwnqnkJzAOxeVI3b2h47nmDO1pWIYztdQncLRIMjW1I62oBcY3gCKjVV86Vp0JKZzVCjYPJbdBpVyrRahvcBEMVWjiHmB4f8XBL%2Fp2uOjoQ2nKymepmzYl%2BePAJS%2B4kUqyAiSS5ydik6qcuq7m3GJaXobFbPULDYPu37BpfutqGnH5e1yfhlZqkw9uh%2BIAXWOf4aVBK6X&X-Amz-Signature=990b3068c7b7856cc19ddf4b8d00a1e23a80339a198b6754ab285234dc695536&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

