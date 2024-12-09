from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para salvar o Authorization Code
@app.route("/save_auth_code", methods=["POST"])
def save_auth_code():
    data = request.get_json()
    auth_code = data.get("auth_code")

    if auth_code:
        try:
            # Atualiza o valor do Authorization Code no arquivo config.py
            with open("config.py", "r") as file:
                lines = file.readlines()

            with open("config.py", "w") as file:
                for line in lines:
                    if line.startswith("AUTHORIZATION_CODE ="):
                        file.write(f'AUTHORIZATION_CODE = "{auth_code}"\n')
                    else:
                        file.write(line)

            print(f"Authorization Code recebido e salvo no config.py: {auth_code}")
            return jsonify({"message": "Authorization Code salvo com sucesso!"}), 200
        except Exception as e:
            print(f"Erro ao salvar o Authorization Code: {e}")
            return jsonify({"error": "Erro ao salvar o Authorization Code."}), 500
    else:
        return jsonify({"error": "Authorization Code não encontrado."}), 400


if __name__ == "__main__":
    app.run(port=5000)
