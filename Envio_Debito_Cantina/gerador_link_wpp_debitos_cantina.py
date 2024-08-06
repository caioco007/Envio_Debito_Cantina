import pandas as pd
from urllib.parse import quote

# Função para criar o link do WhatsApp
def criar_link(numero, nome, valor, chave_pix):
    texto = (
        f"Débito Cantina - PIBMS\n"
        f"Olá *{nome}*,\n\n"
        f"Estamos enviando esta mensagem para informar que seu débito na cantina da igreja é de *{valor}*.\n\n"
        f"Por favor, realize o pagamento via PIX utilizando a seguinte chave: *{chave_pix}*.\n\n"
        f"Após o pagamento, envie o comprovante para confirmarmos o recebimento.\n\n"
        f"Agradecemos pela compreensão e cooperação.\n\n"
        f"Que Deus abençoe!"
    )
    texto_codificado = quote(texto)
    link = f"https://api.whatsapp.com/send?phone=55{numero}&text={texto_codificado}"
    return link

# Ler o arquivo .csv com delimitador ';'
df = pd.read_csv('debitos.csv', delimiter=',')

# Definir a chave PIX
chave_pix = "27993092446"

# Iterar sobre as linhas do dataframe e criar os links
links = []
for index, row in df.iterrows():
    numero = row['numero']
    nome = row['nome']
    valor = row['valor']
    link = criar_link(numero, nome, valor, chave_pix)
    links.append({"Nome": nome, "Numero": numero, "Valor": valor, "Link": link})

# Criar um DataFrame com os links
links_df = pd.DataFrame(links)

# Salvar os links em um arquivo Excel
links_df.to_excel('links_whatsapp.xlsx', index=False)

print("Links salvos em links_whatsapp.xlsx")


