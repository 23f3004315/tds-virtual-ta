---
chunk_id: discourse_topic_164277_post_35_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/35
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 1297
username: 23f1002382
post_number: 35
topic_id: 164277
---

 [Post #35](https://discourse.onlinedegree.iitm.ac.in/t/164277/35)

I had set up the environment and dependencies and everything was working fine. When i tried to recreate it from scratch in a new codespace it broke. I fixed almost everything except this error

---

`@ANdIeCOOl ➜ /workspaces/TDS-Project-1 (main) $ crewai create crew b2b
Traceback (most recent call last):
 File "/home/codespace/.python/current/bin/crewai", line 5, in &lt;module&gt;
 from crewai.cli.cli import crewai
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/__init__.py", line 3, in &lt;module&gt;
 from crewai.agent import Agent
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agent.py", line 7, in &lt;module&gt;
 from crewai.agents import CacheHandler
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/__init__.py", line 2, in &lt;module&gt;
 from .parser import CrewAgentParser
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/parser.py", line 6, in &lt;module&gt;
 from crewai.utilities import I18N
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/__init__.py", line 13, in &lt;module&gt;
 from .embedding_configurator import EmbeddingConfigurator
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/embedding_configurator.py", line 4, in &lt;module&gt;
 from chromadb import Documents, EmbeddingFunction, Embeddings
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/__init__.py", line 6, in &lt;module&gt;
 from chromadb.auth.token_authn import TokenTransportHeader
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py", line 24, in &lt;module&gt;
 from chromadb.telemetry.opentelemetry import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 13, in &lt;module&gt;
 from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/trace_exporter/__init__.py", line 25, in &lt;module&gt;
 from opentelemetry.exporter.otlp.proto.grpc.exporter import ( # noqa: F401
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py", line 72, in &lt;module&gt;
 from opentelemetry.sdk.metrics.export import MetricsData
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py", line 16, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal import Meter, MeterProvider
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py", line 56, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal.measurement_consumer import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py", line 29, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal.metric_reader_storage import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py", line 26, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal._view_instrument_match import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py", line 22, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal.aggregation import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py", line 48, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.exponent_mapping import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py", line 25, in &lt;module&gt;
 from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.ieee_754 import (
 File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py", line 15, in &lt;module&gt;
 from ctypes import c_double, c_uint64
 File "/usr/local/python/3.12.1/lib/python3.12/ctypes/__init__.py", line 8, in &lt;module&gt;
 from _ctypes import Union, Structure, Array
ImportError: /usr/local/python/3.12.1/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
`
i updated the libffi package using sudo but while breaking something else can someone pls help me? @carlton @Jivraj @s.anand
