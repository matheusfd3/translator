# Translator

## Descrição

Este projeto captura o áudio do microfone em tempo real, transcreve e traduz para português.

## Requisitos

> **Nota:** Dependências adicionais podem ser necessárias. Caso apareça algum erro, tente instalá-las manualmente.

### 1. Chave API da OpenAI

Este projeto requer uma chave API da OpenAI para funcionar. Obtenha sua chave em [platform.openai.com](https://platform.openai.com/api-keys) e configure como variável de ambiente:

```bash
export OPENAI_API_KEY='sua-chave-api-aqui'
```

Para tornar permanente, adicione ao seu `~/.bashrc` ou `~/.zshrc`.

### 2. Python 3.12

Certifique-se de ter o Python 3.12 instalado em seu sistema.

### 3. Dependências do sistema (Linux)

```bash
sudo apt-get update
sudo apt-get install python3-dev portaudio19-dev python3-tk
```

### 4. FFmpeg

```bash
sudo apt update && sudo apt install ffmpeg
```

> **Nota:** A instalação do ffmpeg pode não ser realmente necessária para o funcionamento.

### 5. Dependências Python

```bash
pip install -r requirements.txt
```

## Como usar

1. Clone o repositório em sua máquina local:

```bash
git clone https://github.com/matheusfd3/translator.git
```

2. Entre no diretório do projeto:

```bash
cd translator
```

3. Configure sua chave API da OpenAI (se ainda não fez):

```bash
export OPENAI_API_KEY='sua-chave-api-aqui'
```

4. Verifique o índice do seu dispositivo de áudio e ajuste o `input_device_index` no arquivo `main.py`.

5. Execute o script:

```bash
python main.py
```

## Contribuição

Contribuições são bem-vindas! Se você encontrou um bug ou tem alguma sugestão para melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Este projeto foi desenvolvido por [matheusfd3](https://github.com/matheusfd3)
