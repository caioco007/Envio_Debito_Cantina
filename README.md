# Projetos: Gerador de Links para Débitos da Cantina

## Projeto 1: import_docx.py

## Descrição
O projeto `import_docx.py` é um script Python desenvolvido para automatizar a extração de informações de débitos de um documento do Word e exportá-las para uma planilha Excel. O script lê um arquivo .docx contendo nomes de devedores e valores de débitos, organiza essas informações e gera um arquivo CSV com uma coluna adicional para números de telefone.

### Funcionalidades:
- **Leitura de Documento Word**: O script carrega um documento .docx e lê seu conteúdo para identificar nomes e valores de débitos.
- **Extração de Dados**: As informações de nomes e valores são extraídas e organizadas em listas.
- **Criação de DataFrame**: Um DataFrame do pandas é criado a partir das listas de nomes e valores.
- **Adição de Coluna para Número de Telefone**: Uma coluna vazia para números de telefone é adicionada ao DataFrame.
- **Exportação para CSV**: O DataFrame é salvo em um arquivo CSV (`debitos.csv`).
- **Geração de Planilha Excel**: O DataFrame é salvo em uma planilha Excel (`debitos.xlsx`).

### Uso:
1. **Preparação do Ambiente**: Instale as bibliotecas necessárias (`pandas`, `python-docx`, `openpyxl`).
2. **Execução do Script**: Execute o script `import_docx.py`.
3. **Arquivos de Saída**: Verifique os arquivos `debitos.csv` e `debitos.xlsx` para acessar os dados extraídos e organizados.



## Projeto 2: Geração de Links WhatsApp para Débitos

Este projeto tem como objetivo gerar links personalizados do WhatsApp para notificar os membros da igreja sobre débitos na cantina.

### Funcionalidades:
- **Leitura de Dados**: O script lê um arquivo CSV contendo os nomes, números de telefone e valores dos débitos dos membros.
- **Geração de Links**: Para cada membro, é gerado um link do WhatsApp contendo uma mensagem personalizada com os detalhes do débito e informações de pagamento via PIX.
- **Exportação para Excel**: Os links gerados são exportados para um arquivo Excel, onde cada link é formatado como um hyperlink clicável.

### Uso:
1. **Preparação do Ambiente**: Instale as bibliotecas necessárias (`pandas`, `openpyxl`).
2. **Execução do Script**: Execute o script `gerador_link_wpp_debitos_cantina.py`.
3. **Arquivo de Saída**: Verifique o arquivo `links_whatsapp.xlsx` para acessar os links gerados.
