# Introduction
This repository contains the [slides](./presentation-slides/PyCon_Wroclaw_Serverless_Presentation.pdf) of the talk _Serverless Computing and Python: Security Challenges and Ongoing Research_ presented at [PyCon Wroclaw 2024](https://www.pyconwroclaw.com/). The [code examples](./code-examples) are included as well. 

# Talk Abstract
The serverless computing paradigm has become increasingly popular in recent years. Thanks to its cost-effectiveness and the possibility of relying on a cloud provider to manage the underlying infrastructure, companies making use of serverless platforms can fully focus on developing the business logic of their products. However, adopting the serverless model also implies facing new security-related challenges. Considering the growing popularity of Python in this domain, it is therefore important to understand how Python developers can address these challenges, and what are the alternative solutions that security researchers are currently exploring. 

In this talk, the preliminary results of [research](https://doi.org/10.1109/SANER60148.2024.00072) focused on static analysis of serverless applications are presented and discussed. Static analysis is undoubtedly advantageous, but it remains particularly challenging due to the complexity of the cloud services and the event-driven nature of the serverless model. To overcome these issues, the proposed approach consists of two steps. First, information extracted from the infrastructure and the application code is combined. Second, the application code is instrumented in order to obtain a synchronous-like program execution flow. This enables the developer to find security vulnerabilities statically by running a general-purpose tool capable of identifying data flows, such as the Python-specific [Pysa](https://pyre-check.org/docs/pysa-basics/). A prototype implementation was evaluated against a novel suite of [security-oriented microbenchmarks](https://github.com/giusepperaffa/serverless-security-microbenchmarks), and the results confirm the potential of this technique. 

To illustrate how the discussed static analysis approach works in practice, the talk ends by presenting some examples focused on Abstract Syntax Tree (AST)-based processing of the application code.
