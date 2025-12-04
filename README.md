# 🤖 CRM Multi-Agente com LangGraph

Sistema de atendimento automatizado com múltiplos agentes especializados (Suporte, Vendas e Gerente) usando LangGraph e LLMs.

---

## 📋 Pré-requisitos

Antes de começar, você precisará instalar o Python na sua máquina.

---

## 🐧 Instalação no Linux (Ubuntu/Debian)

### Passo 1: Instalar o Python

```bash
# Atualizar repositórios
sudo apt update

# Instalar Python 3 e pip
sudo apt install python3 python3-pip python3-venv -y

# Verificar instalação
python3 --version
pip3 --version
```

### Passo 2: Criar e Ativar Ambiente Virtual

```bash
# Criar pasta do projeto
mkdir crm-agentes
cd crm-agentes

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
# Atualizar pip
pip install --upgrade pip

# Instalar todas as dependências
pip install langchain-openai langchain-core langgraph pydantic typing-extensions
```

### Para Desativar o Ambiente Virtual (quando terminar)

```bash
deactivate
```

---

## 🪟 Instalação no Windows

### Passo 1: Instalar o Python

1. **Baixar o Python:**
   - Acesse: https://www.python.org/downloads/
   - Clique em "Download Python" (versão mais recente)

2. **Instalar:**
   - Execute o instalador baixado
   - ⚠️ **IMPORTANTE:** Marque a opção **"Add Python to PATH"**
   - Clique em "Install Now"
   - Aguarde a instalação concluir

3. **Verificar Instalação:**
   - Abra o **Prompt de Comando** (CMD) ou **PowerShell**
   - Digite:
   ```cmd
   python --version
   pip --version
   ```

### Passo 2: Criar e Ativar Ambiente Virtual

```cmd
# Criar pasta do projeto
mkdir crm-agentes
cd crm-agentes

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

**Nota:** No PowerShell, se houver erro de permissão, execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Passo 3: Instalar Dependências

```cmd
# Atualizar pip
python -m pip install --upgrade pip

# Instalar todas as dependências
pip install langchain-openai langchain-core langgraph pydantic typing-extensions
```

### Para Desativar o Ambiente Virtual (quando terminar)

```cmd
deactivate
```

---

## 📦 Dependências do Projeto

| Pacote | Versão Mínima | Descrição |
|--------|---------------|-----------|
| langchain-openai | - | Integração com APIs OpenAI |
| langchain-core | - | Componentes base do LangChain |
| langgraph | - | Framework para grafos de agentes |
| pydantic | - | Validação de dados |
| typing-extensions | - | Extensões de tipagem |

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────┐
│  Supervisor │  ← Roteia para o agente correto
└──────┬──────┘
       │
   ┌───┴────┬────────┬─────────┐
   │        │        │         │
┌──▼──┐  ┌─▼───┐  ┌─▼────┐  ┌─▼──────┐
│Supor│  │Venda│  │Geren │  │Finaliza│
│te   │  │s    │  │te    │  │r       │
└─────┘  └─────┘  └──────┘  └────────┘
```

### Agentes:

- **Supervisor**: Analisa a mensagem e roteia para o agente adequado
- **Suporte**: Responde dúvidas e consulta pedidos
- **Vendas**: Cria novos pedidos
- **Gerente**: Cancela pedidos (apenas PENDENTES)

---

## 🐛 Solução de Problemas Comuns

### Erro: "python não é reconhecido como comando"
**Windows:** Python não foi adicionado ao PATH durante instalação
- Solução: Reinstale o Python marcando "Add Python to PATH"

**Linux:** Use `python3` ao invés de `python`

### Erro: "No module named 'langchain'"
Você não instalou as dependências
```bash
pip install langchain-openai langchain-core langgraph pydantic typing-extensions
```

### Erro de Permissão (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro de Conexão com API
Verifique:
- Conexão com internet
- URL da API está correta
- API Key é válida

### Banco de Dados Corrompido
Delete o arquivo `ecommerce_v2.db` e execute o programa novamente.

---

## 🔄 Atualizando Dependências

Para atualizar todas as bibliotecas para as versões mais recentes:

```bash
pip install --upgrade langchain-openai langchain-core langgraph pydantic typing-extensions
```

---

**Desenvolvido com ❤️ usando LangGraph e LangChain**