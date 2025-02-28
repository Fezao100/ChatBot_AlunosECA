# Chatbot para Estudantes de ECA - UNESP Sorocaba

## 📌 Visão Geral
Este chatbot foi desenvolvido utilizando **Rasa** com o objetivo de auxiliar estudantes do curso de Engenharia de Controle e Automação (ECA) da UNESP Sorocaba. Ele fornece informações sobre disciplinas, instituições estudantis, processos acadêmicos e outras dúvidas comuns dos alunos.

## 🛠 Tecnologias Utilizadas
- **Rasa** (para construção do chatbot)
- **Python** (linguagem base do Rasa)
- **NLU (Natural Language Understanding)** para compreensão das perguntas dos usuários

## 🚀 Funcionalidades
- **Disciplinas**: Informações sobre as matérias de cada ano do curso.
- **Instituições Estudantis**: Detalhes sobre grupos acadêmicos e como ingressar.
- **Dúvidas Acadêmicas**: Esclarecimentos sobre iniciação científica, trancamento de disciplinas, carteirinha estudantil, moradia e horas complementares.

## 📦 Como Rodar o Projeto
### 1️⃣ Clone o Repositório
```sh
git clone https://github.com/seu-usuario/chatbot-eca.git
cd chatbot-eca
```

### 2️⃣ Instale as Dependências
Certifique-se de ter o Python instalado. Depois, instale as bibliotecas necessárias:
```sh
pip install rasa
```

### 3️⃣ Treine o Modelo
```sh
rasa train
```

### 4️⃣ Execute o Chatbot
```sh
rasa shell
```
Agora você pode interagir com o chatbot no terminal.

## 📌 Exemplo de Uso
```sh
Você: Olá
Chatbot: Hey estudante de Eca, como posso te ajudar?

Você: Quais são as matérias do segundo ano?
Chatbot: As matérias do segundo ano são: CDI III, EP, ETM, ITPE, CE I, ESD, CJS...

Você: Como faço iniciação científica?
Chatbot: A iniciação científica é um projeto que utiliza metodologia científica...
```

---
🔹 Desenvolvido para ajudar os novos estudantes de ECA da UNESP Sorocaba! 😊

