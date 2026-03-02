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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQV2G4IZ%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1RLYP9fXP6xuAzHCqqSMsYVU9DFXXEiGhGRmZwj73fAiEA0Qx%2BENexk0OGRD6pc2do7NWaw%2FyeJRadUiO2HlC%2FALAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDK%2FYrbse0GBV6NAGNircA8497WGngvUdtABc88yvF6o0sP74t58oQyy7Pg3kuENeINIO1JUdezxNaj9Kz4Vj34ucksFCdh9peUOq78w5SrGMOBrV5HEprqPP7PNFSKZBkcN5AUDCvP2eCrVoXARkyDcX6YqmZzsjoObNH3VUbxWgQzsjA1pN7QeEe3%2FpNWtkHCzscEyfrDyI%2FlUO6ceMIBOar8DVR%2B9Jx1HL4FuuaJr1Do9w%2BVt1D5ssDN%2B1eO13PggrFb%2BNlHAsC5Wu1cAEKb%2FU6ArKwRLpfK8w69CV1DPCydbOT7xZC2dpCxQuad1%2BH7mWS0oT77xNFL7xN5%2BdDOnGVppCL3k0cStd5iwqnMMmM1iiPAo24zoMiIotAm%2BykbLd9toDYjRDNBPOFa3IlKW4ecIy1RtlVT2ZRIYG7EI0EyR2L5UwV85hL19IiTjVqK0KHiYGhqw%2FtfC8He2k95cl2ooJ%2BBr0OvRG7wCIz0Rebyde7PcTRfwjh8GYXg3P8s%2FbzirKYft2q%2FasU2D0X%2BTrZ3KlGhWFY0Yana6H%2BHPVn1uxN9%2BJCAdScyoIFUHVXEr1euoTrC%2BvcoICY7cwJU0d%2FQL10Gt56wgXiKwYlUHKVzVHYvCzMe3i0jMAEU1xU2cR00MWr%2BKsUW5SMIn9k80GOqUBbEWDQm2gGg11BHIEeXz2IrsAqu7mnWLEBzPgihIZ1BCQ5UMnuzgeOXOYAPywfROqvguj7zKgKBkKBpEb%2Fr5mhNP1OQZ3zYK3hgWTR1YxmBk6kUpYtFn4GX4eFStOVtjw%2FtZxxudV88oyyr6aelJZuzYWN4THqr2hBiW%2Bn5JU%2BSF6t9BP0Nro0r5gXtpdUsV0QlVw3ab4SA0JznzjK75iJgH5VnPA&X-Amz-Signature=eda4c50b04bc62c3d890d665d33c2d9179ccf3017531dfb581102b0447765a85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQV2G4IZ%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1RLYP9fXP6xuAzHCqqSMsYVU9DFXXEiGhGRmZwj73fAiEA0Qx%2BENexk0OGRD6pc2do7NWaw%2FyeJRadUiO2HlC%2FALAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDK%2FYrbse0GBV6NAGNircA8497WGngvUdtABc88yvF6o0sP74t58oQyy7Pg3kuENeINIO1JUdezxNaj9Kz4Vj34ucksFCdh9peUOq78w5SrGMOBrV5HEprqPP7PNFSKZBkcN5AUDCvP2eCrVoXARkyDcX6YqmZzsjoObNH3VUbxWgQzsjA1pN7QeEe3%2FpNWtkHCzscEyfrDyI%2FlUO6ceMIBOar8DVR%2B9Jx1HL4FuuaJr1Do9w%2BVt1D5ssDN%2B1eO13PggrFb%2BNlHAsC5Wu1cAEKb%2FU6ArKwRLpfK8w69CV1DPCydbOT7xZC2dpCxQuad1%2BH7mWS0oT77xNFL7xN5%2BdDOnGVppCL3k0cStd5iwqnMMmM1iiPAo24zoMiIotAm%2BykbLd9toDYjRDNBPOFa3IlKW4ecIy1RtlVT2ZRIYG7EI0EyR2L5UwV85hL19IiTjVqK0KHiYGhqw%2FtfC8He2k95cl2ooJ%2BBr0OvRG7wCIz0Rebyde7PcTRfwjh8GYXg3P8s%2FbzirKYft2q%2FasU2D0X%2BTrZ3KlGhWFY0Yana6H%2BHPVn1uxN9%2BJCAdScyoIFUHVXEr1euoTrC%2BvcoICY7cwJU0d%2FQL10Gt56wgXiKwYlUHKVzVHYvCzMe3i0jMAEU1xU2cR00MWr%2BKsUW5SMIn9k80GOqUBbEWDQm2gGg11BHIEeXz2IrsAqu7mnWLEBzPgihIZ1BCQ5UMnuzgeOXOYAPywfROqvguj7zKgKBkKBpEb%2Fr5mhNP1OQZ3zYK3hgWTR1YxmBk6kUpYtFn4GX4eFStOVtjw%2FtZxxudV88oyyr6aelJZuzYWN4THqr2hBiW%2Bn5JU%2BSF6t9BP0Nro0r5gXtpdUsV0QlVw3ab4SA0JznzjK75iJgH5VnPA&X-Amz-Signature=a68471ecc953237cc141aeb16a4cf848f9cf6d0ae4fcffd2ea449d4743d477eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

