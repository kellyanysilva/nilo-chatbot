# Nilo — Assistente Virtual da Conecta Tech

> Projeto acadêmico de aprendizagem desenvolvido em Python para praticar conceitos introdutórios de Inteligência Artificial e Processamento de Linguagem Natural (PLN).

## Sobre o projeto

O **Nilo** é um protótipo de chatbot para atendimento ao cliente de uma empresa fictícia chamada **Conecta Tech**, uma loja de tecnologia e acessórios.

O objetivo é demonstrar como um programa simples pode identificar o assunto de uma pergunta e apresentar uma resposta previamente cadastrada. O projeto foi criado para fins educacionais e pode ser ampliado gradualmente conforme novos conhecimentos forem adquiridos.

## Funcionalidades

- Responde perguntas frequentes sobre horário, produtos, pagamentos, entregas, trocas, garantia e privacidade.
- Identifica intenções por meio de palavras-chave.
- Normaliza textos para facilitar a comparação, incluindo a remoção de acentos.
- Oferece opções para o usuário continuar a conversa.
- Reconhece perguntas sem resposta cadastrada.
- Registra perguntas não reconhecidas em `perguntas_sem_resposta.txt` para análise posterior.
- Permite ao usuário avaliar se uma resposta ajudou.

## Tecnologias utilizadas

- **Python 3** — linguagem de programação.
- **Biblioteca padrão do Python** — módulos `unicodedata` e `datetime`, além de recursos de entrada e saída de arquivos.
- **Git e GitHub** — recomendados para controle de versão e publicação do código.

## Estrutura do projeto

```text
nilo-chatbot/
├── nilo_chatbot.py
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   └── README.md
└── docs/
    └── README.md
```

O arquivo `perguntas_sem_resposta.txt` é criado automaticamente na pasta de execução quando o chatbot recebe uma pergunta que não consegue reconhecer. Esse arquivo é local e está excluído do Git pelo `.gitignore`.

## Requisitos

- Python 3.10 ou superior recomendado.
- Terminal, Prompt de Comando ou terminal integrado do VS Code.

Não é necessário instalar pacotes externos nesta versão.

## Como executar

### 1. Baixe ou clone o repositório

Se você já instalou o Git, abra o terminal e execute:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço HTTPS do seu repositório no GitHub.

Se ainda não usa Git, também pode acessar o repositório no GitHub, clicar em **Code** e escolher **Download ZIP**.

### 2. Abra a pasta do projeto

Abra a pasta `nilo-chatbot` no Visual Studio Code ou no editor de sua preferência.

### 3. Execute o programa

No terminal, dentro da pasta do projeto, execute:

```bash
python nilo_chatbot.py
```

No Windows, se o comando anterior não funcionar, tente:

```bash
py nilo_chatbot.py
```

### 4. Faça perguntas de teste

Experimente perguntas como:

- `Qual é o horário de atendimento?`
- `Vocês aceitam Pix?`
- `Quais produtos vocês vendem?`
- `Como faço uma troca?`
- `Quero falar com um atendente`
- `Vocês recuperam arquivos de um celular molhado?`

Digite `sair` para encerrar ou `menu` para ver as opções.

## Como o Nilo funciona?

Nesta versão, o Nilo utiliza **regras e palavras-chave**. O programa normaliza a mensagem, procura termos associados a intenções cadastradas e apresenta a resposta correspondente.

Exemplo simplificado:

1. A pessoa pergunta: “Vocês aceitam Pix?”
2. O programa identifica termos relacionados a pagamento.
3. O chatbot seleciona a resposta cadastrada sobre formas de pagamento.
4. Se não identificar uma intenção, informa que não tem uma resposta confirmada e registra a pergunta para análise.

### Limitação importante

Esta versão é um **protótipo baseado em regras**. Embora demonstre conceitos básicos de processamento de texto e identificação de intenções, ela ainda não utiliza um modelo treinado de Machine Learning nem compreende a linguagem com a flexibilidade de um modelo de IA generativa.

As informações sobre a Conecta Tech são fictícias e servem apenas para demonstração. Não utilize essas respostas como políticas de uma empresa real sem revisá-las.

## Melhorias futuras

- Carregar as perguntas e respostas de um arquivo externo, como JSON ou CSV.
- Criar uma interface web para conversar com o Nilo pelo navegador.
- Adicionar testes automatizados.
- Avaliar um classificador de intenções com Machine Learning.
- Armazenar perguntas frequentes e avaliações em um banco de dados.
- Integrar o sistema a uma plataforma como Supabase, quando os conceitos básicos estiverem consolidados.
- Implementar encaminhamento real para um atendente, com as integrações necessárias.

## Privacidade e segurança

O protótipo registra mensagens não reconhecidas em um arquivo local. Evite digitar ou armazenar dados pessoais, senhas, códigos de autenticação ou dados financeiros. Em uma implantação real, será necessário definir uma política de privacidade, controlar o acesso aos registros e observar a legislação aplicável, incluindo a LGPD.

## Objetivo de aprendizagem

Este projeto ajuda a praticar:

- Variáveis, dicionários, funções e estruturas de repetição.
- Condicionais e comparação de textos.
- Leitura e gravação de arquivos.
- Organização de um pequeno projeto Python.
- Documentação de software.
- Uso inicial de Git e GitHub.

## Autoria

Projeto desenvolvido para fins de aprendizagem na disciplina **Introdução à Inteligência Artificial**, do curso de Bacharelado em Engenharia de Software.

**Autora:** [Seu nome]

---

Se você encontrar um erro ou tiver uma sugestão de melhoria, registre a questão e teste a alteração antes de incorporá-la ao projeto.
