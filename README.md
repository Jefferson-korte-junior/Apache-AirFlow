# Estudos e Práticas com Apache Airflow

Este repositório reúne **estudos, práticas e experimentos** com o **Apache Airflow**, desenvolvidos ao longo de cursos, bootcamps e treinamentos pessoais, com foco em **orquestração de pipelines de dados**.

O objetivo principal é consolidar conceitos fundamentais do Airflow, como DAGs, tarefas, dependências, agendamento e boas práticas de organização.

---

## Objetivos do Repositório
- Praticar a criação de DAGs no Apache Airflow
- Entender o fluxo de execução de pipelines de dados
- Aplicar conceitos de ETL (Extração, Transformação e Carga)
- Consolidar o aprendizado obtido em cursos e bootcamps
- Servir como repositório de estudo e consulta futura

---

## Tecnologias Utilizadas
- Python
- Apache Airflow
- Conceitos de ETL
- Orquestração de dados

---

## Estrutura dos Arquivos

### DAGs de Prática e Estudo
- **`meu_primeiro_dag_pratica.py`**  
  Meu primeiro DAG criado no Apache Airflow, com foco em aprendizado e entendimento da estrutura básica.

- **`DAG_pratica.py`**  
  DAG criado exclusivamente para fins de treino e experimentação.

---

### 🔹 DAGs Desenvolvidos em Cursos e Bootcamps
- **`dados_climaticos_aulaAlura.py`**  
  DAG desenvolvido durante aulas do curso da Alura, aplicando conceitos apresentados em aula.

- **`forex_data_pipeline_aula.py`**  
  DAG desenvolvido durante atividades de curso/bootcamp para praticar a criação de pipelines de dados no Apache Airflow.  
  Esse pipeline automatiza o fluxo de dados de câmbio (Forex), realizando:
  - Verificação se a API de taxas de câmbio está disponível
  - Verificação da existência de um arquivo CSV com as moedas
  - Coleta das taxas de câmbio a partir de uma API externa
  - Armazenamento dos dados no HDFS
  - Criação de uma tabela externa no Hive
  - Processamento dos dados utilizando Apache Spark
  - Envio de notificações por e-mail e Slack ao final da execução  

  O DAG simula um pipeline de dados próximo ao cenário real, integrando diferentes ferramentas do ecossistema de dados.


---

### Relatórios e Documentação
- **`Relatorio Bootcamp.pdf`**  
  Relatório técnico relacionado às atividades desenvolvidas no bootcamp, contendo explicações e imagens.

- **`Relatorio Curso Alura.pdf`**  
  Relatório referente ao curso da Alura, com descrições das práticas realizadas e evidências visuais.

---

## Observações Importantes
- Este repositório **não representa um único projeto final**, mas sim um **conjunto de práticas e estudos**.
- Alguns arquivos foram desenvolvidos no contexto de cursos e bootcamps, enquanto outros são práticas autorais para aprendizado.
- O foco está no **processo de aprendizado**, não apenas no resultado final.

---

## Próximos Passos / Possíveis Evoluções
- Padronização dos DAGs
- Criação de um pipeline mais completo e autoral
- Separação futura de projetos maiores em repositórios dedicados
- Inclusão de diagramas de fluxo dos DAGs

---

## 📌 Autor
Jefferson Korte  
Estudante de Ciência de Dados e Machine Learning  
GitHub: https://github.com/Jefferson-korte-junior
