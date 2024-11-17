
# Script para FISCH roblox.

Este projeto automatiza o processo de clicar no botão "Agitar" de um jogo usando Python. O script usa **PyAutoGUI** para controle do mouse e **OpenCV** para reconhecimento de imagem, identificando o botão "Agitar" na tela e clicando nele.

## Requisitos

Antes de rodar o script, você precisa instalar as dependências necessárias. Siga as etapas abaixo para configurar o ambiente.

### Passo 1: Baixar ou Clonar o Repositório

Baixe o código ou clone este repositório no seu computador.

```bash
git clone https://github.com/MarcosStanquini/script-fisch-roblox.git
```

### Passo 2: Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do seu projeto.

#### No Windows:
```bash
python -m venv venv
venv/Scripts/activate
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

### Passo 4: Instalar o Mouse Jiggler

Após instalar as dependências, instale o Mouse Jiggler e o inicialize com essas configurações:

![image](https://github.com/user-attachments/assets/60f15124-de49-459d-8019-0848888e631b)



### Passo 5: Rodar o Script

Com o ambiente virtual ativo e as dependências instaladas, você pode executar o script com o comando abaixo:

```bash
python agitar_script.py
```


### Observações

- O script utiliza um template de imagem (`template_agitar.png`) que deve ser criado inicialmente ao rodar o script pela primeira vez. Ele capturará a área ao redor do botão "Agitar".

### Problemas Conhecidos

- Certifique-se de que o jogo esteja em uma janela visível para o script identificar corretamente o botão "Agitar".

## Contribuição

Se você encontrar bugs ou tiver sugestões de melhorias, fique à vontade para abrir uma **issue** ou **pull request**.
