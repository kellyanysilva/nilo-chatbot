# Nilo - Assistente Virtual da Conecta Tech
# Projeto acadêmico: Introdução à Inteligência Artificial
# Versão inicial: chatbot baseado em regras e palavras-chave (PLN básico)

import unicodedata
from datetime import datetime

FAQ = {
    "horario": {
        "keywords": ["horario", "abre", "fecha", "funciona", "atendimento"],
        "answer": (
            "Nosso horário fictício de atendimento é de segunda a sexta, "
            "das 9h às 18h, e aos sábados, das 9h às 13h."
        ),
    },
    "produtos": {
        "keywords": ["produto", "vende", "vendem", "acessorio", "acessorios",
                     "celular", "fone", "carregador", "cabo", "teclado", "mouse"],
        "answer": (
            "A Conecta Tech é uma loja fictícia de tecnologia. Trabalhamos, "
            "no exemplo acadêmico, com celulares, carregadores, cabos, fones, "
            "capas, películas, teclados e mouses. A disponibilidade precisa "
            "ser confirmada com a equipe."
        ),
    },
    "pagamento": {
        "keywords": ["pagamento", "pagar", "pix", "cartao", "credito", "debito",
                     "dinheiro", "parcelar", "parcelamento"],
        "answer": (
            "Neste exemplo, aceitamos Pix, cartões de débito e crédito e dinheiro "
            "em compras presenciais. Parcelamento e condições devem ser confirmados "
            "com a equipe."
        ),
    },
    "entrega": {
        "keywords": ["entrega", "entregam", "frete", "prazo", "receber", "pedido"],
        "answer": (
            "O prazo e o custo de entrega dependem do endereço e da disponibilidade "
            "do produto. Para consultar um pedido real, é necessário confirmar os "
            "dados com a equipe."
        ),
    },
    "troca": {
        "keywords": ["troca", "trocar", "devolucao", "devolver", "arrependimento"],
        "answer": (
            "Para solicitar uma troca ou devolução, entre em contato com a equipe "
            "e tenha o comprovante de compra em mãos. A solicitação será avaliada "
            "conforme a legislação aplicável e a política oficial da empresa."
        ),
    },
    "garantia": {
        "keywords": ["garantia", "defeito", "danificado", "quebrado", "problema"],
        "answer": (
            "A garantia depende do produto, do fabricante e das regras legais. "
            "Guarde a nota fiscal e fale com a equipe para verificar as condições "
            "aplicáveis ao seu caso."
        ),
    },
    "privacidade": {
        "keywords": ["privacidade", "dados", "lgpd", "senha", "seguranca"],
        "answer": (
            "Compartilhe apenas os dados necessários para o atendimento. Nunca envie "
            "senhas, códigos de autenticação ou o número completo do cartão. Em uma "
            "empresa real, o tratamento de dados deve seguir a LGPD."
        ),
    },
    "atendente": {
        "keywords": ["atendente", "humano", "pessoa", "funcionario", "falar com alguem"],
        "answer": (
            "Claro! Esta versão é um protótipo acadêmico e não transfere a conversa "
            "automaticamente. Em uma implantação real, aqui seria acionado o canal "
            "de atendimento humano."
        ),
    },
}

def normalizar(texto: str) -> str:
    """Converte para minúsculas e remove acentos para facilitar a comparação."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")

def identificar_intencao(mensagem: str):
    """Identifica uma intenção pela presença de palavras-chave."""
    texto = normalizar(mensagem)
    melhor_intencao = None
    melhor_pontuacao = 0

    for intencao, dados in FAQ.items():
        pontuacao = sum(1 for palavra in dados["keywords"] if normalizar(palavra) in texto)
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_intencao = intencao

    # Evita responder quando não há evidência suficiente.
    if melhor_pontuacao == 0:
        return None
    return melhor_intencao

def mostrar_menu():
    print("\nPosso ajudar com:")
    print("  1. Horário de atendimento")
    print("  2. Produtos")
    print("  3. Pagamentos")
    print("  4. Entregas e pedidos")
    print("  5. Trocas e devoluções")
    print("  6. Garantia")
    print("  7. Privacidade e segurança")
    print("  8. Falar com atendente")
    print("Digite sua pergunta ou escreva 'sair' para encerrar.")

def registrar_pergunta_sem_resposta(mensagem: str):
    """Registra perguntas desconhecidas sem solicitar dados pessoais."""
    with open("perguntas_sem_resposta.txt", "a", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{data_hora}] {mensagem.strip()}\n")

def executar_chatbot():
    print("=" * 58)
    print("Olá! Eu sou o Nilo, assistente virtual da Conecta Tech.")
    print("Sou um protótipo acadêmico e posso ajudar com dúvidas comuns.")
    print("=" * 58)
    mostrar_menu()

    while True:
        mensagem = input("\nVocê: ").strip()

        if not mensagem:
            print("Nilo: Digite uma pergunta para começarmos.")
            continue

        comando = normalizar(mensagem)
        if comando in {"sair", "tchau", "encerrar", "fim"}:
            print("Nilo: Obrigado pelo contato! Até logo.")
            break

        if comando in {"menu", "ajuda", "opcoes", "opções"}:
            mostrar_menu()
            continue

        intencao = identificar_intencao(mensagem)

        if intencao:
            print(f"Nilo: {FAQ[intencao]['answer']}")
            avaliacao = input("Nilo: Esta resposta ajudou? (sim/não/pular): ").strip()
            avaliacao_norm = normalizar(avaliacao)

            if avaliacao_norm in {"nao", "não", "n"}:
                print("Nilo: Sinto muito. Você pode reformular a pergunta ou digitar 'atendente'.")
            elif avaliacao_norm in {"sim", "s"}:
                print("Nilo: Que bom! Obrigado pela avaliação.")
        else:
            print(
                "Nilo: Ainda não tenho uma resposta confirmada para essa pergunta. "
                "Para não fornecer uma informação incorreta, você pode reformular "
                "a pergunta, digitar 'menu' ou pedir 'atendente'."
            )
            registrar_pergunta_sem_resposta(mensagem)
            print("Nilo: Registrei a dúvida sem solicitar dados pessoais para que "
                  "a equipe possa avaliá-la e, se apropriado, atualizar a FAQ.")

if __name__ == "__main__":
    executar_chatbot()
