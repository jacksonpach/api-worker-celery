# Aplicação FastAPI-Celery-Redis

## Descrição

Esta é uma aplicação construída usando FastAPI, Celery e Redis para simular o processamento assíncrono de tarefas e retornar o resultado ao ser consultado.

## Componentes Principais

1. **FastAPI:** Um framework web moderno e rápido para construir APIs. Nesta aplicação, ele é usado para criar rotas HTTP e definir a lógica de negócios.
2. **Celery:** Uma fila de tarefas assíncronas baseada em mensagens distribuídas. É utilizado para lidar com tarefas que podem ser executadas em segundo plano.
3. **Redis:** Um armazenamento de dados em valor-chave em memória que serve como banco de dados, cache e broker de mensagens. Nesta aplicação, ele é usado como um broker de mensagens para o Celery.

## Funcionalidades

### 1. Enviar Tarefa (`/send-task/`):
- **Método:** POST
- **Parâmetros:** `a` e `b` (inteiros)
- **Ação:** Esta rota inicia uma tarefa em segundo plano usando o Celery. A tarefa simula um processamento por 10 segundos e depois calcula a soma de `a` e `b`.
- **Resposta:** Retorna um ID de tarefa gerado pelo Celery, que pode ser usado posteriormente para consultar o status e o resultado da tarefa.

### 2. Consultar Status da Tarefa (`/task-status/{task_id}`):
- **Método:** GET
- **Parâmetros:** `task_id` (string)
- **Ação:** Esta rota verifica o status da tarefa usando o ID fornecido. Se a tarefa estiver concluída, ela retornará o resultado. Caso contrário, informará que a tarefa ainda está em processamento.
- **Resposta:** Retorna o status da tarefa (por exemplo, "SUCCESS" ou "PENDING") e, se concluída, o resultado da soma.

## Fluxo de Uso

1. O usuário chama a rota `/send-task/` com dois inteiros como parâmetros.
2. A aplicação inicia uma tarefa em segundo plano para calcular a soma dos inteiros após simular um processamento por 10 segundos.
3. O usuário recebe um ID de tarefa em resposta.
4. O usuário pode usar esse ID de tarefa para consultar o status e o resultado da tarefa através da rota `/task-status/{task_id}`.

## Benefícios

- Permite processamento assíncrono, de modo que o usuário não precisa esperar que tarefas demoradas sejam concluídas.
- Escalabilidade: Como as tarefas são gerenciadas pelo Celery e executadas em segundo plano, é possível escalar horizontalmente adicionando mais workers conforme necessário.
- Flexibilidade: O uso do Redis como broker de mensagens facilita a comunicação entre a aplicação principal e os workers do Celery.

---

Caso tenha dúvidas, sugestões ou feedbacks, fique à vontade para contribuir ou abrir uma issue!
