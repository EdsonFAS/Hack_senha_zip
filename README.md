# hack.exe — Quebra de senha por dicionário

> Ferramenta de linha de comando para demonstrar, de forma educativa, como um ataque de dicionário pode ser utilizado para testar a resistência de arquivos ZIP protegidos por senha.

---

## ⚠️ Aviso de Segurança

**Uso somente para fins educacionais e testes autorizados.** Quebrar senhas de arquivos sem permissão é **ilegal e antiético**. Utilize esta ferramenta apenas em ambientes controlados e com autorização explícita do proprietário dos arquivos. A equipe do projeto não se responsabiliza por usos indevidos.

---

## 📋 Conteúdo deste README

* [Descrição](#descrição)
* [Requisitos](#requisitos)
* [Como usar (executável)](#como-usar-executável)
* [Exemplos](#exemplos)
* [Formato da wordlist](#formato-da-wordlist)
* [Saída esperada](#saída-esperada)
* [Boas práticas de segurança](#boas-práticas-de-segurança)


---

## Descrição

Este projeto fornece um executável (`hack.exe`) que realiza um ataque de dicionário contra arquivos ZIP protegidos por senha. A ferramenta testa senhas de uma wordlist (arquivo `.txt` com uma senha por linha) até encontrar a correta. É ideal para aprendizado sobre segurança e para avaliar a força de senhas em ambientes autorizados.

---

## Requisitos

* Windows (ou ambiente compatível com o `.exe`)
* Ter em mãos:

  * o executável `hack.exe`
  * o arquivo ZIP protegido
  * a wordlist (arquivo `.txt`)

> Não é necessária instalação do Python para executar o `.exe`.

---

## Como Usar (Executável)

1. Coloque `hack.exe`, o arquivo ZIP e a wordlist na mesma pasta (ou informe caminhos absolutos).
2. Abra o PowerShell ou Prompt de Comando e navegue até a pasta.
3. Execute:

```bash
.\hack.exe <caminho_para_zip> <caminho_para_wordlist>
```

### Exemplo:

```bash
.\hack.exe Arquivo_Secreto.zip TOP500.txt
```

---

## Exemplos de uso e dicas rápidas

* Caminhos relativos:

```bash
.\hack.exe ".\zips\segredo.zip" ".\wordlists\meu_wordlist.txt"
```

* Caminhos absolutos (caso os arquivos estejam em pastas diferentes):

```bash
.\hack.exe "C:\\Users\\Você\\Downloads\\segredo.zip" "C:\\wordlists\\TOP500.txt"
```

---

## Formato da wordlist

* Arquivo `.txt`
* Cada linha contém uma senha candidata
* Exemplo de conteúdo:

```
123456
password
qwerty
senha123
```

---

## Saída esperada

A ferramenta exibirá no terminal tentativas de senha (dependendo da implementação) e, ao encontrar a senha correta, deverá apresentar algo do tipo:

```
[+] Senha encontrada: senha_correta
```

*(Se o seu executável tiver comportamento diferente, siga as mensagens exibidas por ele.)*

---

## Boas práticas de segurança

* Execute apenas em máquinas de teste ou com permissão.
* Faça backup dos dados antes de testar.
* Use wordlists apropriadas e limitadas ao escopo do teste.
* Documente as autorizações por escrito quando realizar testes em ambientes de terceiros.

---

