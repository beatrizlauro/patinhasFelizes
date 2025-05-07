# Sistema Petshop - Disciplina de Engenharia de Software II

**Documentação da Tarefa proposta na disciplina de Engenharia de Software II**

Link da atividade: [Documento da Tarefa](https://docs.google.com/document/d/1y9HBSY1gsrNC-xEbGwjuEfI2Wr5PJ3He9fnHHXhFyz4/edit?usp=sharing)

---

## Descrição

Este projeto implementa um sistema simples de **Cadastro**, **Consulta** e **Listagem** de pets, aplicando conceitos de arquitetura lógica (camadas Model-Controller-View) e arquitetura física (infraestrutura local).

## Arquitetura Lógica

* **Model**: persistência de dados em SQLite (`model.py`).
* **Controller**: lógica de negócio e mediação entre Model e View (`controller.py`).
* **View**: interface gráfica utilizando CustomTkinter (`view.py`).

Cada camada está separada em seu próprio arquivo, respeitando o princípio de responsabilidades únicas e facilitando manutenção e evolução.

## Arquitetura Física

* **Banco de Dados**: SQLite local (`petshop.db` criado automaticamente).
* **Servidor de Aplicação**: todo o código roda localmente em um único processo Python, sem servidor separado.
* **Cliente**: GUI baseada em CustomTkinter, executada no mesmo processo.
* **Comunicação**: imports e chamadas de função diretas em memória.

## Estrutura de Pastas

```
petshop/            # pasta raiz do projeto
├── model.py        # camada de persistência (Model)
├── controller.py   # camada de negócio (Controller)
├── view.py         # camada de interface (View)
├── petshop.db      # banco de dados SQLite (gerado automaticamente)
└── requirements.txt# dependências do projeto
```

## Requisitos

* Python 3.7 ou superior
* Biblioteca `customtkinter`

## Instalação e Execução

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/beatrizlauro/patinhasFelizes.git
   cd petshop
   ```
2. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```
3. **Executar a aplicação**

   ```bash
   python view.py
   ```

Após a execução, a interface **Patinhas Felizes** será exibida, permitindo:

* **Cadastro** de novos pets.
* **Consulta** da lista de pets.
* **Busca**, **Atualização** e **Exclusão** de registros.

---

## Observações

* O banco `petshop.db` é criado automaticamente na primeira execução.
* Para migrar para um ambiente de produção, recomenda-se usar um SGBD mais robusto (ex.: PostgreSQL) e separar o Controller como uma API REST.