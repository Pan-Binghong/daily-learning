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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBW424DB%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpRAf9ZDUOtqlqvzKvJNoeFGWIKnCphgDhLAVwZgMk0AiEA4vRFQptYP9Ihrd2r2jDdfU%2BVq9EtFboy9pUKMRIncBIq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDH%2FrirG7OYadWyq1bSrcA1DPe5kb%2BnkpojrtNjMcGvrrBJD6Kc%2F%2BVMd3Kyaxn%2FGe%2B2BCAKyXJkYFl212oDiJtlB3hp2E8PJUL9%2BBDO5x%2BMljiuaIQl4Eqan8XaMBNt%2Fvs7MWnPska8xMgMVnfO%2F6zDjmJQnHADcoUxG2nHnNhMdr%2F6ebG2BTCcMLHYtW9%2FttHK69JpqHCpZQjwUTATRVpu%2Fc9H%2FhEvf2KX1TOF2Y823ETMfRi5UXnKl49AMrdRsoiBeBpW5Ek1BuhlXUTMYlg1ao30jRiQHMAdPiA6MMXkny1Tb5Yre%2F8XmuXmUajr6Q72RrE5pd64zl3bHUyw0Rbaz0hdtN4h%2BWka99BQS2jMlFxTq8onVUP5UqdfPY3T9eAPIqmnt81RrwAzXHPlxp9TlR6G7eIHkQ4vEJ5ytXZWFWPMwKu5Qc03922Ti4Vp58Y%2BWZ5c1w0fGNjmaUbwNpiN7QMuKQ3BlILY7h%2FdS%2FrMrFC2fckbVNujWKOFlNp1grziWuy7OdfdrUrIEElnKvjyZMBOGOn5WP13lU3X73dtcn7YVLDN8%2Bg2Mfl8znhEVyIk8a7Jk4AKJUyvrG4xT0bq9eWObBE8NJ1WO4uem8U9LBUSY0nkLPazGl5jzJ0T64ESPBUo4YMGzFYK9AMJDFmswGOqUBXriMzYnwILrzsYOQfUkUiIIPvkolMK2d7JBCK%2BUe3RAp7MMAhU4bYxEUn3xqILC2QSpu%2FUG%2BCYZ7pmzb5DR57OvpClWAI7Cyo4BfoOKaoBjS7xHpdGUl9ILA1dWsjwb6BpMJi%2FyCeMphH4ux8im17Na3rNY8TRgkUHHKz6K1ewbCbL%2BI1qNYkbQM0Sk0YyKUx1j9gjJoiHzhVwq2b2GUy7jsz6aJ&X-Amz-Signature=2ede0740de61c5dea3c96f47c36d06955cf132dd903ea3f1bf73f68e38999d9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBW424DB%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpRAf9ZDUOtqlqvzKvJNoeFGWIKnCphgDhLAVwZgMk0AiEA4vRFQptYP9Ihrd2r2jDdfU%2BVq9EtFboy9pUKMRIncBIq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDH%2FrirG7OYadWyq1bSrcA1DPe5kb%2BnkpojrtNjMcGvrrBJD6Kc%2F%2BVMd3Kyaxn%2FGe%2B2BCAKyXJkYFl212oDiJtlB3hp2E8PJUL9%2BBDO5x%2BMljiuaIQl4Eqan8XaMBNt%2Fvs7MWnPska8xMgMVnfO%2F6zDjmJQnHADcoUxG2nHnNhMdr%2F6ebG2BTCcMLHYtW9%2FttHK69JpqHCpZQjwUTATRVpu%2Fc9H%2FhEvf2KX1TOF2Y823ETMfRi5UXnKl49AMrdRsoiBeBpW5Ek1BuhlXUTMYlg1ao30jRiQHMAdPiA6MMXkny1Tb5Yre%2F8XmuXmUajr6Q72RrE5pd64zl3bHUyw0Rbaz0hdtN4h%2BWka99BQS2jMlFxTq8onVUP5UqdfPY3T9eAPIqmnt81RrwAzXHPlxp9TlR6G7eIHkQ4vEJ5ytXZWFWPMwKu5Qc03922Ti4Vp58Y%2BWZ5c1w0fGNjmaUbwNpiN7QMuKQ3BlILY7h%2FdS%2FrMrFC2fckbVNujWKOFlNp1grziWuy7OdfdrUrIEElnKvjyZMBOGOn5WP13lU3X73dtcn7YVLDN8%2Bg2Mfl8znhEVyIk8a7Jk4AKJUyvrG4xT0bq9eWObBE8NJ1WO4uem8U9LBUSY0nkLPazGl5jzJ0T64ESPBUo4YMGzFYK9AMJDFmswGOqUBXriMzYnwILrzsYOQfUkUiIIPvkolMK2d7JBCK%2BUe3RAp7MMAhU4bYxEUn3xqILC2QSpu%2FUG%2BCYZ7pmzb5DR57OvpClWAI7Cyo4BfoOKaoBjS7xHpdGUl9ILA1dWsjwb6BpMJi%2FyCeMphH4ux8im17Na3rNY8TRgkUHHKz6K1ewbCbL%2BI1qNYkbQM0Sk0YyKUx1j9gjJoiHzhVwq2b2GUy7jsz6aJ&X-Amz-Signature=32d71c62d2a58e34f205bfa9d9c2db3945eafb56a409b99b497c5cb0c56d0971&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

