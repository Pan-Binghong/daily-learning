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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBJHOANP%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWCJmB8k31T%2BgIZg8ue3h%2Fmk%2FnPJs35hDccJCdRwYYawIgcA7pEePL%2BZUHxRwJ8Bg3CZfeV718vC8d%2FeaADXGAL%2BUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnhYtZ%2BvddvPv4EsircA5vxIbfwzPv1CYJMqjdU5hJi8cFr13v1pQiPt3Breh3o6wb7hRVUCx0pQXHH03WwAhcfgvmlB3HJBSBWigtf2PN%2BEGtlpguptQkETWbwUjwArlcF7vPxZDAy3wpZgvWE0YNCQP1V3VbOjvY7sCSYrS2JtpNegP%2Fn6%2BXeOjfzZAX0FaGVSNtHvGQcCeMK%2Fkf4iBdIy6iHEdLaq9WPAAoCDtqbu11qJeYXy9%2FTmn%2BPmrVTxEq5I07u1SznuVYNQyAUPOvGklj7uq0Ogf%2FHzqLm3I5USn9gUFIDgqcDmZF8hbv7gVM%2BdW9OGHhAE8GBMFB1JWqwd7AjIis2GGrAGARJ9c2R2qK56CLmMr1Qnq2YSmvOsuXfjbOm8dZpwX%2Fb9GNqPoQ2tSINlqqnjqnSxFN2%2BWFt97vJ3Gbcj7NXhmAPQCLOxOA1hzs5Uud8efSPJAapTj4uVR3KK6xaqMFGvla5Rjc5RfgNvh0nyHUanhOvcc6LoG448Nqkcx%2FHIR6UaEHrKz9IbqYreOmHN%2FHwkFYq%2Bfh0FqV7YgSwZjONLQgXq6SUKT6XRhol3GudA2JfW6Bcna5NIbwuiK9QYpXRCgYl%2B1ayclkobgIGuZEmoi1bw%2BbPnv5x2cTC0%2F86BfWxMPSYqckGOqUBD%2FFyRhk3RoMg3WVYNjTA2eiDKms%2BozcqlfDv4GiJISxNH5LN2xjRbe7C%2FML4t0OMn8d5lEea0DLtmU%2FuIuhjpNQch%2FQ1qOW1vX4BuoL7MuGv2Bsm1b35IYKuKrsguRznmO%2BA1Q0JdViafCXcph%2FLL4oIR%2BVnQYWxRhKKDiLe8XtyCE718mXNrzPmSHz%2FBL30rox%2BafK9wJMP1aWc6p%2Bmx2EviHZE&X-Amz-Signature=329e0d7cbd4686f7ea675351f549bf8a28cee4671be37f1848b3b948bfca70f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBJHOANP%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWCJmB8k31T%2BgIZg8ue3h%2Fmk%2FnPJs35hDccJCdRwYYawIgcA7pEePL%2BZUHxRwJ8Bg3CZfeV718vC8d%2FeaADXGAL%2BUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnhYtZ%2BvddvPv4EsircA5vxIbfwzPv1CYJMqjdU5hJi8cFr13v1pQiPt3Breh3o6wb7hRVUCx0pQXHH03WwAhcfgvmlB3HJBSBWigtf2PN%2BEGtlpguptQkETWbwUjwArlcF7vPxZDAy3wpZgvWE0YNCQP1V3VbOjvY7sCSYrS2JtpNegP%2Fn6%2BXeOjfzZAX0FaGVSNtHvGQcCeMK%2Fkf4iBdIy6iHEdLaq9WPAAoCDtqbu11qJeYXy9%2FTmn%2BPmrVTxEq5I07u1SznuVYNQyAUPOvGklj7uq0Ogf%2FHzqLm3I5USn9gUFIDgqcDmZF8hbv7gVM%2BdW9OGHhAE8GBMFB1JWqwd7AjIis2GGrAGARJ9c2R2qK56CLmMr1Qnq2YSmvOsuXfjbOm8dZpwX%2Fb9GNqPoQ2tSINlqqnjqnSxFN2%2BWFt97vJ3Gbcj7NXhmAPQCLOxOA1hzs5Uud8efSPJAapTj4uVR3KK6xaqMFGvla5Rjc5RfgNvh0nyHUanhOvcc6LoG448Nqkcx%2FHIR6UaEHrKz9IbqYreOmHN%2FHwkFYq%2Bfh0FqV7YgSwZjONLQgXq6SUKT6XRhol3GudA2JfW6Bcna5NIbwuiK9QYpXRCgYl%2B1ayclkobgIGuZEmoi1bw%2BbPnv5x2cTC0%2F86BfWxMPSYqckGOqUBD%2FFyRhk3RoMg3WVYNjTA2eiDKms%2BozcqlfDv4GiJISxNH5LN2xjRbe7C%2FML4t0OMn8d5lEea0DLtmU%2FuIuhjpNQch%2FQ1qOW1vX4BuoL7MuGv2Bsm1b35IYKuKrsguRznmO%2BA1Q0JdViafCXcph%2FLL4oIR%2BVnQYWxRhKKDiLe8XtyCE718mXNrzPmSHz%2FBL30rox%2BafK9wJMP1aWc6p%2Bmx2EviHZE&X-Amz-Signature=6d9d31dfe103c93dfae4c01f55c17606d2e7a7582144899499116e7ac827a843&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

