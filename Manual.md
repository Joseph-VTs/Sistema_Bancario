# 🏦 Manual de Uso — Banco Sentar 

📌 [Repositório no GitHub](https://github.com/Joseph-VTs)
📌 [Linkedin](www.linkedin.com/in/joseph-vts-98460a35a)

---

## 📁 Sumário

- [Início do Sistema](#início-do-sistema)
- [Cadastro de Cliente](#cadastro-de-cliente)
- [Login](#login)
- [Área do Cliente](#área-do-cliente)
  - [Operações na Agência](#operações-na-agência)
  - [Operações no Caixa Eletrônico](#operações-no-caixa-eletrônico)
  - [Configurações](#configurações)
- [Operações Bancárias](#operações-bancárias)
  - [Depósito](#depósito)
  - [Saque](#saque)
  - [Transferência](#transferência)
  - [Pix](#pix)
- [Extrato](#extrato)
- [Exportar Extrato](#exportar-extrato)
- [Cancelamento de Operações](#cancelamento-de-operações)
- [Validações Inteligentes](#validações-inteligentes)
- [Funções Internas](#funções-internas)

---

## 🏁 Início do Sistema

Execute o arquivo `Arquivao.py`. O menu principal será exibido com as opções:

- `[1] 👤 - Entrar`
- `[2] 🆕 - Cadastrar-Se`
- `[3] 📄 - Lista de Clientes`
- `[0] 🔐 - Sair`

---

## 🆕 Cadastro de Cliente

O sistema solicitará:

- Primeiro nome (somente letras)
- Segundo nome (somente letras)
- Idade (entre 18 e 120)
- Senha (4 dígitos numéricos)

A conta será criada com número aleatório de 6 dígitos e adicionada à lista `Contas_Criadas`.

---

## 👤 Login

Informe:

- Número da conta
- Senha

Se os dados estiverem corretos, você acessará a **Área do Cliente**.

---

## 🏦 Área do Cliente

### 🏢 Operações na Agência

- `[1] 💰 - Consultar Saldo`
- `[2] 📄 - Extrato Detalhado`
- `[3] 💸 - Saque`
- `[4] 💵 - Depósito`
- `[5] 🔁 - Transferência`
- `[6] 📝 - Exportar Extrato para .txt`
- `[0] 🔙 - Voltar`

### 🏧 Operações no Caixa Eletrônico

- `[1] 💸 - Saque`
- `[2] 💵 - Depósito`
- `[0] 🔙 - Voltar`

### ⚙️ Configurações

- Alterar nome, idade, senha ou número da conta.

---

## 💳 Operações Bancárias

### 💵 Depósito

- **Agência**: valor livre via `Ver_Float()`
- **Caixa Eletrônico**: apenas notas de R$20, R$50 ou R$100

### 💸 Saque

- **Agência**: valor livre via `Ver_Float()`
- **Caixa Eletrônico**: apenas notas de R$20, R$50 ou R$100
- Verificação de saldo antes da operação

### 🔁 Transferência

- Informe número da conta de destino
- Valor deve ser positivo e dentro do saldo
- Histórico atualizado para ambas as contas
- Comprovante exibido com data, valor e titulares

### ⚡ Pix

- Funciona como transferência, com ícone e descrição diferentes no histórico

---

## 📄 Extrato

Exibe:

- Todas as transações com data, tipo e valor
- Saldo atual
- Separadores visuais para organização

---

## 📝 Exportar Extrato

- Gera arquivo `.txt` com:
  - Titular
  - Número da conta
  - Data da consulta
  - Histórico completo
  - Saldo final

---

## 🛑 Cancelamento de Operações

Em qualquer entrada interativa (nome, idade, senha, valor), digite: sair

## Opções do Menu Principal

1.  **Entrar (Login):** Permite acesso à sua conta usando o número da conta e senha.
2.  **Cadastrar-Se:** Permite a criação de uma nova conta de cliente. Requer Nome, Sobrenome, Idade (mínimo 18 anos) e Senha (4 dígitos).
3.  **Lista de Clientes:** Exibe todos os clientes cadastrados no banco.
4.  **Manual do Usuário:** Exibe este manual.
5.  **Sair:** Encerra o programa.

## Área do Cliente

Após o login, você pode acessar:

* **Operações na Agência (1):** Saque, Depósito, Transferência, Extrato Detalhado.
* **Operações no Caixa Eletrônico (2):** Saque e Depósito com restrição de notas (R$20, R$50, R$100).
* **Configurações (3):** Alterar Nome, Idade, Senha, e outros dados da conta.

## Notas Importantes

* A senha é sempre de 4 dígitos numéricos.
* Em operações de Saque e Depósito no Caixa Eletrônico, apenas notas de R$20, R$50 e R$100 são aceitas.