# utils/api_helper.py
import requests
from config import API_URL, APP_ID, APP_SECRET, ACCESS_TOKEN, REDIRECT_URI


def generate_authorization_url():
    """
    Gera a URL de autorização para o fluxo OAuth.
    """
    scope = "ad_account reporting measurement"
    state = "1234"  # Você pode modificar para um valor único por solicitação
    url = (
        f"https://business-api.tiktok.com/open_api/v1.3/oauth/authorize?"
        f"app_id={APP_ID}&state={state}&redirect_uri={REDIRECT_URI}&scope={scope}"
    )
    return url


def exchange_code_for_token(auth_code):
    """
    Troca o Authorization Code pelo Access Token.
    """
    url = "https://business-api.tiktok.com/open_api/v1.3/oauth/token/"
    data = {
        "app_id": "743292597010008",
        "secret": "63b4bfe51fc1f4dc3435aeb0c023447cc370ae81",
        "auth_code": auth_code,
        "grant_type": "authorization_code",
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao trocar o código pelo token:", response.json())
        return None



def get_ad_accounts():
    """
    Retorna as informações das contas de anúncios associadas ao token de acesso.
    """
    url = f"{API_URL}advertiser/info/"
    headers = {
        "Access-Token": ACCESS_TOKEN,
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar contas de anúncios:", response.json())
        return None
