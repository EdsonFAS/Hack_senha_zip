Descrição

Este projeto é uma ferramenta de linha de comando para demonstrar como um ataque de dicionário pode ser usado para encontrar a senha de arquivos ZIP protegidos. A ferramenta testa senhas de uma lista de palavras (wordlist) até encontrar a correta. É ideal para fins educacionais e testes de segurança autorizados.

Como Usar (Executável)

Como você já tem o executável (.exe), o uso da ferramenta é muito simples e não requer a instalação do Python.

1. Baixe os Arquivos

Baixe o arquivo executável (.exe) do seu repositório.

Tenha em mãos os outros dois arquivos necessários:

O arquivo ZIP protegido por senha.

Uma wordlist (um arquivo de texto com uma senha por linha).

2. Abra o Terminal e Execute

Abra seu terminal (como o PowerShell ou Prompt de Comando no Windows) e navegue até a pasta onde você salvou todos os arquivos.

Em seguida, execute a ferramenta com a seguinte sintaxe:

.\hack.exe <caminho_para_zip> <caminho_para_wordlist>

Exemplo:
.\hack.exe Arquivo_Secreto.zip TOP500.txt

Observações de Segurança

Este projeto foi desenvolvido estritamente para fins educacionais e testes autorizados. A quebra de senha de arquivos sem permissão é ilegal e antiética. Use esta ferramenta apenas em ambientes controlados e com a devida autorização.
