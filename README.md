# Sistema Distribuído de Assinaturas

## Descrição

Este projeto consiste no desenvolvimento de um protótipo de Sistema Distribuído para gerenciamento de assinaturas, implementado em Python como atividade da disciplina de Sistemas Distribuídos da Universidade Federal do Pará (UFPA).

O sistema foi desenvolvido com o objetivo de demonstrar, de forma prática, conceitos fundamentais da computação distribuída por meio da comunicação entre serviços independentes, sincronização de eventos e persistência de dados.

---

## Objetivos

O protótipo busca implementar os seguintes conceitos de Sistemas Distribuídos:

- Comunicação entre processos utilizando sockets TCP;
- Execução de serviços independentes;
- Sincronização temporal utilizando o protocolo NTP;
- Ordenação lógica dos eventos utilizando Relógios de Lamport;
- Persistência de informações em banco de dados SQLite.

---

## Arquitetura

O sistema é composto pelos seguintes serviços:

- Interface Web (Flask);
- Serviço de Cobrança;
- Serviço de Auditoria;
- Serviço de Notificação;
- Banco de Dados SQLite.

A comunicação entre os componentes ocorre através de conexões TCP, permitindo que cada serviço execute de forma independente.

---

## Estrutura do Projeto

```
SistemaAssinaturasDistribuido/

├── auditoria/
│   ├── server.py
│
├── cobranca/
│   ├── server.py
│   ├── cliente_auditoria.py
│
├── notificacao/
│   ├── server.py
│   ├── cliente_notificacao.py
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── lamport.py
│   └── ntp_cliente.py
│
├── app.py
├── banco.py
├── assinaturas.db
├── requirements.txt
└── README.md
```

---

## Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- Socket TCP/IP
- ntplib
- HTML
- CSS

---

## Requisitos

- Python 3.10 ou superior;
- Biblioteca Flask;
- Biblioteca ntplib.

As dependências podem ser instaladas por meio do arquivo `requirements.txt`.

```
pip install -r requirements.txt
```

---

## Execução

Inicialmente, execute os serviços distribuídos em terminais distintos.

### Serviço de Auditoria

```
python auditoria/server.py
```

### Serviço de Notificação

```
python notificacao/server.py
```

### Serviço de Cobrança

```
python cobranca/server.py
```

### Aplicação Web

```
python app.py
```

Após iniciar todos os serviços, acesse:

```
http://127.0.0.1:5000
```

---

## Funcionamento

O fluxo de execução ocorre conforme descrito abaixo:

1. O usuário realiza uma solicitação de assinatura pela interface Web.
2. A aplicação Flask envia a solicitação ao Serviço de Cobrança.
3. O Serviço de Cobrança:
   - registra o Relógio de Lamport;
   - obtém o horário sincronizado via NTP;
   - armazena os dados no banco SQLite;
   - encaminha o evento ao Serviço de Auditoria;
   - encaminha o evento ao Serviço de Notificação.
4. Os serviços processam a solicitação e retornam uma confirmação ao Serviço de Cobrança.
5. O usuário recebe a confirmação da operação.

---

## Conceitos de Sistemas Distribuídos Aplicados

O projeto contempla os seguintes conceitos estudados na disciplina:

- Comunicação TCP entre serviços;
- Processos independentes;
- Sincronização por NTP;
- Relógios Lógicos de Lamport;
- Persistência de dados em SQLite.

---

## Limitações

Este projeto possui finalidade acadêmica e, portanto, apresenta algumas limitações:

- comunicação síncrona entre os serviços;
- utilização de banco SQLite local;
- ausência de balanceamento de carga;
- ausência de replicação dos serviços;
- inexistência de mecanismos de autenticação e criptografia;
- ausência de tolerância automática a falhas.

---

## Trabalhos Futuros

Como possíveis evoluções do sistema destacam-se:

- utilização de RabbitMQ ou Apache Kafka;
- conteinerização com Docker;
- orquestração utilizando Kubernetes;
- substituição do SQLite por PostgreSQL;
- implementação de autenticação e TLS;
- monitoramento com Prometheus e Grafana;
- replicação dos serviços e balanceamento de carga.

---

## Referências

COULOURIS, G.; DOLLIMORE, J.; KINDBERG, T.; BLAIR, G. *Sistemas Distribuídos: Conceitos e Projeto*. 5. ed. Pearson, 2013.

LAMPORT, L. *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM, v. 21, n. 7, p. 558–565, 1978.

Python Software Foundation. Disponível em: <https://www.python.org>.

Flask Documentation. Disponível em: <https://flask.palletsprojects.com/>.

SQLite Documentation. Disponível em: <https://www.sqlite.org/>.

---

## Autora

**Mylena Reis**

Universidade Federal do Pará – UFPA

Faculdade de Computação

Disciplina: Sistemas Distribuídos

2026
