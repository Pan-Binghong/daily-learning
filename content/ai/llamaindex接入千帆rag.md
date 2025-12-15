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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHQ766HJ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIF8EnZ8tgLAEck35C2VNUADbnIklBqn7opp%2BcwTyCXzqAiAZrgv%2FhuorCXlDBYQTJPUaBHZhLt%2FJLFXxXFDGpb655Cr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM41CwDu2xSEprH9CMKtwDMKv8yg7mPguM0tnlD97YaArt2GhrbY%2Fj7EVkpUsQE%2B5%2F4lxDwQ%2FP%2FDS26LCJsP%2FeYWcXFUg7ArBRth1cA4vepJVNyLQZKyN0qNLHu8NyQ5hCuXSXagnmBVtO%2Bw8MzHdvtx6MB%2BhCNYVrNq3%2Fy6jTBlpTHNt8qnDSbfM02k9cbtBgYUTTxZKfxsKzphDXKG4Met5B0328mvIPFEBjUh8kx7luYac8e7AgO4mkp7WGE1MjbG42KDufgiGfozz%2FlZFBqbvtNiJTSlBiyhZap8IDuxOpR5%2BBz3wrmeN9csRsUWhQxLUxLtpOId8rJKPshAJ%2B3pwS3X330zlhUUJxqXMbCH2C%2FBoeYrNAgwAry2bfnyd40iTFRqF3cEpoh4shp3wRlX2h%2FXq0Jwg6A9EdIBpualy6BRtEywkcpmdnGs0GarcMyeUGlH4PNFkvxMZ8e3Gv2rxtEt5QHy0gD4kFH233WzATbr3QK8ByodI86rwbPRS2jEzDocR4xVjute40Moc0svNiBAWmHFmB0F60cOnETbVcWFzFS9P2m9OsIv%2FABNevPcvCohvvUsmLYjJmbRQdvsQpaTAEGASBb5FNA%2BoEUTeGiLCHYnLfGXO2Jxj7KZeMXLrZrnw24G3wjsgw%2Bdr8yQY6pgG890mXsUPPlBY83fZ2dk37VQUGbeShOfXfOpRc%2B5AbD3Ydmv4bZAKHapSP4wiU0K2kWY%2B2VtaI%2Fjx%2BYeHDqt7UOoZ5Heub5PpxssIHeNu30TGn6FJM%2BCXxEjnRydNyv%2FgdPJ2YRFuZ%2BrnuS8Z%2F8Z9poAaTNil9LtDecocUS7uEZIoR9u%2F5%2B0n%2ByFyBCm3nYxrngvWiOf%2BfjIdX6QphCQG9P1nIANc3&X-Amz-Signature=b05b37681292db2f785922694643f09e84ce33e7a0808aaab73bde20b7b78d3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHQ766HJ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIF8EnZ8tgLAEck35C2VNUADbnIklBqn7opp%2BcwTyCXzqAiAZrgv%2FhuorCXlDBYQTJPUaBHZhLt%2FJLFXxXFDGpb655Cr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM41CwDu2xSEprH9CMKtwDMKv8yg7mPguM0tnlD97YaArt2GhrbY%2Fj7EVkpUsQE%2B5%2F4lxDwQ%2FP%2FDS26LCJsP%2FeYWcXFUg7ArBRth1cA4vepJVNyLQZKyN0qNLHu8NyQ5hCuXSXagnmBVtO%2Bw8MzHdvtx6MB%2BhCNYVrNq3%2Fy6jTBlpTHNt8qnDSbfM02k9cbtBgYUTTxZKfxsKzphDXKG4Met5B0328mvIPFEBjUh8kx7luYac8e7AgO4mkp7WGE1MjbG42KDufgiGfozz%2FlZFBqbvtNiJTSlBiyhZap8IDuxOpR5%2BBz3wrmeN9csRsUWhQxLUxLtpOId8rJKPshAJ%2B3pwS3X330zlhUUJxqXMbCH2C%2FBoeYrNAgwAry2bfnyd40iTFRqF3cEpoh4shp3wRlX2h%2FXq0Jwg6A9EdIBpualy6BRtEywkcpmdnGs0GarcMyeUGlH4PNFkvxMZ8e3Gv2rxtEt5QHy0gD4kFH233WzATbr3QK8ByodI86rwbPRS2jEzDocR4xVjute40Moc0svNiBAWmHFmB0F60cOnETbVcWFzFS9P2m9OsIv%2FABNevPcvCohvvUsmLYjJmbRQdvsQpaTAEGASBb5FNA%2BoEUTeGiLCHYnLfGXO2Jxj7KZeMXLrZrnw24G3wjsgw%2Bdr8yQY6pgG890mXsUPPlBY83fZ2dk37VQUGbeShOfXfOpRc%2B5AbD3Ydmv4bZAKHapSP4wiU0K2kWY%2B2VtaI%2Fjx%2BYeHDqt7UOoZ5Heub5PpxssIHeNu30TGn6FJM%2BCXxEjnRydNyv%2FgdPJ2YRFuZ%2BrnuS8Z%2F8Z9poAaTNil9LtDecocUS7uEZIoR9u%2F5%2B0n%2ByFyBCm3nYxrngvWiOf%2BfjIdX6QphCQG9P1nIANc3&X-Amz-Signature=3b68e723393d37a3db2229d1fed13fe67608874b616dfad98f34622127699b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

