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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTWFSQ4%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDTpS%2FD8pqKGgaLRrruN9F6QtlGz3evWwAM4mGTJSXgsQIgTuEC%2F3RwHIxpInrfPopkxUxRx2cmsi0mndS2al6HbP8q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDP6Ig805Sa13c0diQCrcAzhzjl5RY4tVhAlohKsUhKNWy%2BzZugubZjLaDuFa9RDZMG0Mr1pDbbLxSfSAWMUrS1VCS1f%2B0iWXVOkhoSQunPjPDCnlQoT7GVDw7ZRBgReouv3jReswidnDTYfxVONpL%2Bn%2F2XfM5A0UBrWtJ6vG3jrsw0tf0H%2FDbY2P5u7jDbTclJNnqJa5Q3rUabpW%2FLU%2F3I2qfnVekA4opEehstSKQ09pY5Qkxild25ZysTe7l8lRTUIacLG1frZ9lSxWc5ksMTGNLZZR9BHeaN4m079BvC%2F7cwiX%2FsPpOHTyn7G2Xim%2FSCO04wCK8fcwtar9%2B0DtsAfVXX2x%2FqnekWJOLBYmC8xwwZmYFK6afTPdnhl%2Bw%2Btxtc8B3CvLMpgKg4s4w9bjO7inaE3jW1PlsCMQ%2BZ4UaYSlcMLvqfl600GCbqTKlxL6pFN8NgXB7Te5aCklNNoS1Sh1vVOtBA%2FWsD2tnaTXCxfl%2Bn%2FtElvSHuzUPMxXztQvI5ZA5ZSn9KcCYvNOKv0L9uEgx%2BiIUMGimzgLrzXN07QKlMy2pP8%2BGxCIVwTKRutXnHi9a4f9b3%2Bvciyok9ggPY0BxHMjiflq%2BXzFa7t%2Fm%2FLVA0IrFF3rlyCYEME6b0sNERLBWcTcHG138eSeMMG38s0GOqUBZPGSmOuZ%2BdYbRcUVjT%2FhOlS3dOR6s9tMC%2FPEa9nNsMBk%2B0T5zqCwCXJtMlB7B8Bnzvg2NBx1Kv2%2FzLWu%2Fs7eEZCnC5w1ocKL5qSX8qJA5IgpwOvVVZUhgbttbaeQrlIRF22Kvy7Dx7TDkPEzB0L9fZBBqYXJb7Nd6kNmKYDDM6munqNCs7%2Bo8CHfeNRcrxqlOXzYK32WsCNS9kd0Tz%2BlRTw1gdTY&X-Amz-Signature=3b873e272c5046ed9d425410ab5ed6ec84f429c4569214e218756bb29857da81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTWFSQ4%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDTpS%2FD8pqKGgaLRrruN9F6QtlGz3evWwAM4mGTJSXgsQIgTuEC%2F3RwHIxpInrfPopkxUxRx2cmsi0mndS2al6HbP8q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDP6Ig805Sa13c0diQCrcAzhzjl5RY4tVhAlohKsUhKNWy%2BzZugubZjLaDuFa9RDZMG0Mr1pDbbLxSfSAWMUrS1VCS1f%2B0iWXVOkhoSQunPjPDCnlQoT7GVDw7ZRBgReouv3jReswidnDTYfxVONpL%2Bn%2F2XfM5A0UBrWtJ6vG3jrsw0tf0H%2FDbY2P5u7jDbTclJNnqJa5Q3rUabpW%2FLU%2F3I2qfnVekA4opEehstSKQ09pY5Qkxild25ZysTe7l8lRTUIacLG1frZ9lSxWc5ksMTGNLZZR9BHeaN4m079BvC%2F7cwiX%2FsPpOHTyn7G2Xim%2FSCO04wCK8fcwtar9%2B0DtsAfVXX2x%2FqnekWJOLBYmC8xwwZmYFK6afTPdnhl%2Bw%2Btxtc8B3CvLMpgKg4s4w9bjO7inaE3jW1PlsCMQ%2BZ4UaYSlcMLvqfl600GCbqTKlxL6pFN8NgXB7Te5aCklNNoS1Sh1vVOtBA%2FWsD2tnaTXCxfl%2Bn%2FtElvSHuzUPMxXztQvI5ZA5ZSn9KcCYvNOKv0L9uEgx%2BiIUMGimzgLrzXN07QKlMy2pP8%2BGxCIVwTKRutXnHi9a4f9b3%2Bvciyok9ggPY0BxHMjiflq%2BXzFa7t%2Fm%2FLVA0IrFF3rlyCYEME6b0sNERLBWcTcHG138eSeMMG38s0GOqUBZPGSmOuZ%2BdYbRcUVjT%2FhOlS3dOR6s9tMC%2FPEa9nNsMBk%2B0T5zqCwCXJtMlB7B8Bnzvg2NBx1Kv2%2FzLWu%2Fs7eEZCnC5w1ocKL5qSX8qJA5IgpwOvVVZUhgbttbaeQrlIRF22Kvy7Dx7TDkPEzB0L9fZBBqYXJb7Nd6kNmKYDDM6munqNCs7%2Bo8CHfeNRcrxqlOXzYK32WsCNS9kd0Tz%2BlRTw1gdTY&X-Amz-Signature=97d64943aec62d4f26d3acc8a5d84d71c289a6a4f995b1dc913718bde641c83d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

