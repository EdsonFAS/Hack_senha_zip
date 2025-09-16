import sys

# Tenta importar pyzipper para maior compatibilidade
try:
    import pyzipper
    USE_PYZIPPER = True
    print("Usando 'pyzipper' para suporte a múltiplos métodos de compressão.")
except ImportError:
    import zipfile
    USE_PYZIPPER = False
    print("Aviso: 'pyzipper' não encontrado. Usando 'zipfile' padrão. "
          "Pode não funcionar com todos os tipos de criptografia.")

def crack_zip(zip_file_path, wordlist_path):
    """
    Tenta quebrar a senha de um arquivo ZIP usando uma wordlist,
    com suporte a pyzipper.
    """
    if not USE_PYZIPPER:
        try:
            zip_file = zipfile.ZipFile(zip_file_path)
        except zipfile.BadZipFile:
            print("Erro: Arquivo ZIP corrompido ou inválido.")
            return None
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            wordlist = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Erro: A wordlist '{wordlist_path}' não foi encontrada.")
        return None

    print(f"Iniciando ataque em '{zip_file_path}' com {len(wordlist)} senhas.")
    
    for i, password in enumerate(wordlist):
        try:
            if USE_PYZIPPER:
                with pyzipper.AESZipFile(zip_file_path) as zf:
                    zf.pwd = password.encode('utf-8')
                    # Tenta ler o primeiro arquivo para verificar a senha
                    zf.read(zf.namelist()[0])
            else:
                zip_file.extractall(pwd=password.encode('utf-8'))
                
            print(f"\n[SUCESSO] Senha encontrada: '{password}' na tentativa #{i+1}.")
            return password
            
        except RuntimeError as e:
            # Senha incorreta ou erro de compressão, continuamos
            if "Bad password for file" in str(e) or "That compression method is not supported" in str(e):
                if (i + 1) % 100 == 0:
                    print(f"Tentativas: {i+1} | Última: '{password}'")
            else:
                print(f"Erro inesperado: {e}")
                return None
        except Exception as e:
            print(f"Ocorreu um erro durante a extração: {e}")
            return None

    print("\n[FALHA] A senha não foi encontrada na wordlist fornecida.")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python zip_cracker_v2.py <caminho_do_zip> <caminho_da_wordlist>")
        sys.exit(1)

    zip_file_path = sys.argv[1]
    wordlist_path = sys.argv[2]
    
    crack_zip(zip_file_path, wordlist_path)