
# Agitar Script para Jogo

Este projeto automatiza o processo de clicar no botão "Agitar" de um jogo usando Python. O script usa **PyAutoGUI** para controle do mouse e **OpenCV** para reconhecimento de imagem, identificando o botão "Agitar" na tela e clicando nele.

## Requisitos

Antes de rodar o script, você precisa instalar as dependências necessárias. Siga as etapas abaixo para configurar o ambiente.

### Passo 1: Baixar ou Clonar o Repositório

Baixe o código ou clone este repositório no seu computador.

```bash
git clone <URL_do_repositorio>
```

### Passo 2: Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do seu projeto.

#### No Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

#### No Linux ou MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar as Dependências

Após ativar o ambiente virtual, instale as dependências necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

### Passo 4: Rodar o Script

Com o ambiente virtual ativo e as dependências instaladas, você pode executar o script com o comando abaixo:

```bash
python agitar_script.py
```

### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Você pode ver o conteúdo do arquivo aqui:

```txt
pyautogui==0.9.53
opencv-python==4.7.0.72
numpy==1.23.5
```

### Observações

- O script utiliza um template de imagem (`template_agitar.png`) que deve ser criado inicialmente ao rodar o script pela primeira vez. Ele capturará a área ao redor do botão "Agitar".
- O script faz a movimentação do mouse de forma errática para tentar enganar o jogo, como se fosse um movimento mais natural.

### Problemas Conhecidos

- Certifique-se de que o jogo esteja em uma janela visível para o script identificar corretamente o botão "Agitar".
- Em alguns jogos, pode ser necessário ajustar os parâmetros de confiança ou a amplitude do movimento errático.

## Contribuição

Se você encontrar bugs ou tiver sugestões de melhorias, fique à vontade para abrir uma **issue** ou **pull request**.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
