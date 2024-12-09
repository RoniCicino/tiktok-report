# main.py
from utils.api_helper import generate_authorization_url, exchange_code_for_token, get_ad_accounts


def main():
    print("=== TikTok Ads API Integration ===")
    
    # Passo 1: Gerar a URL de autorização
    print("\n1. Gerando a URL de autorização...")
    auth_url = generate_authorization_url()
    print("Acesse o link abaixo para autorizar o app:")
    print(auth_url)

    # Passo 2: Obter o Authorization Code do usuário
    auth_code = input("\n2. Após autorizar, cole o 'Authorization Code' aqui: ")

    # Passo 3: Trocar o código pelo Access Token
    print("\n3. Trocando o código pelo Access Token...")
    token_response = exchange_code_for_token(auth_code)
    if token_response and "data" in token_response:
        access_token = token_response["data"].get("access_token")
        print("Access Token gerado com sucesso:", access_token)
        
        # Atualizar manualmente no config.py
        print("\n⚠️ Atualize o arquivo config.py com o Access Token para continuar.")
    else:
        print("Erro ao gerar o Access Token. Verifique o código.")

    # Passo 4: Testar a conexão com as contas de anúncios
    print("\n4. Buscando contas de anúncios...")
    ad_accounts = get_ad_accounts()
    if ad_accounts and "data" in ad_accounts:
        print("Contas de anúncios encontradas:", ad_accounts["data"])
    else:
        print("Erro ao buscar contas de anúncios.")


if __name__ == "__main__":
    main()
