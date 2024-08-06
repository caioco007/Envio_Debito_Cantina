import docx
import pandas as pd

# Carregar o documento do Word
doc = docx.Document(r'C:/Users/caioc/Downloads/Cópia de DÉBITOS DA CANTINA (1).docx')

# Inicializar listas para armazenar os nomes e valores
nomes = []
valores = []

# Ler o conteúdo do documento
for para in doc.paragraphs:
    if '–' in para.text:
        nome, valor = para.text.split('–')
        nomes.append(nome.strip())
        valores.append(valor.strip())

# Criar um DataFrame do pandas
df = pd.DataFrame({
    'nome': nomes,
    'valor': valores
})
df['numero'] = '999999'  # Adicionar uma coluna para o número de telefone

# Salvar o DataFrame em um arquivo CSV
df.to_csv('debitos.csv', index=False)
