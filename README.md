# 🧮 Calculadora Minimalista em Python (Dark Mode) - Imersão Alura

Projeto desenvolvido originalmente durante a **Imersão Python da Alura** e evoluído para uma aplicação desktop completa com interface gráfica moderna em **Dark Mode** (inspirada no design do macOS/iOS), suporte a histórico de cálculos, porcentagem e arquitetura modular com testes automatizados.

---

## 🚀 Funcionalidades

- **Design Minimalista Dark Mode:** Interface elegante em tons escuros (`#18181b`), botões arredondados, fontes limpas e visual refinado.
- **5 Operações Matemáticas:**
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`) com prevenção contra divisão por zero
  - Porcentagem (`%`) integrada (cálculos compostos como `200 + 15%` e cálculos diretos)
- **Funções Especiais:** Limpeza de visor (`AC`), inversor de sinal (`+/-`) e casas decimais.
- **Painel de Histórico Retrátil:** Histórico lateral expansível para conferir os cálculos recentes, com opção de **Reutilizar** o resultado com um clique e botão **Limpar**.
- **Atalhos do Teclado:** Controle completo pelo teclado físico (números, operadores, `Enter`, `Backspace` e `Esc`).
- **Testes Automatizados:** Testes unitários para validar a exatidão das funções matemáticas.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Interface Gráfica:** CustomTkinter (Dark Mode nativo moderno)
- **Testes:** Unittest (módulo nativo do Python)

---

## 📁 Estrutura de Arquivos

```text
├── calculadora.py       # Interface gráfica desktop em Dark Mode
├── operacoes.py         # Módulo com funções puras de cálculo matemático
├── test_operacoes.py    # Testes unitários automatizados (unittest)
├── requirements.txt     # Dependências externas do projeto (customtkinter)
└── README.md            # Documentação completa do projeto
```

---

## 💻 Como Instalar e Rodar no Windows

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

### 1. Instalar o Python (caso ainda não tenha)
1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Baixe e execute o instalador.
3. ⚠️ **MUITO IMPORTANTE:** Na primeira tela de instalação, marque a caixinha **"Add python.exe to PATH"**.
4. Clique em **Install Now** e aguarde concluir.

### 2. Baixar o Projeto
- Clique no botão verde **Code** no topo da página do repositório e selecione **Download ZIP**.
- Extraia a pasta baixada no seu computador.

### 3. Instalar as Dependências
1. Abra a pasta do projeto no Explorador de Arquivos.
2. Clique na barra de endereços no topo da pasta, digite `cmd` e aperte **Enter**.
3. No terminal que se abriu, instale a biblioteca gráfica executando:
   ```bash
   py -m pip install -r requirements.txt
   ```

### 4. Executar a Calculadora
No mesmo terminal, basta digitar:
```bash
py calculadora.py
```
*(ou `python calculadora.py`)*

### 5. Executar os Testes Automatizados
Para conferir se todas as operações matemáticas estão calculando perfeitamente:
```bash
py -m unittest -v test_operacoes.py
```

---

## ⌨️ Atalhos de Teclado Suportados

| Tecla | Ação |
| :--- | :--- |
| `0` a `9` | Digitação numérica |
| `,` ou `.` | Ponto / vírgula decimal |
| `+`, `-`, `*`, `/` | Operações matemáticas |
| `%` | Cálculo de porcentagem |
| `Enter` ou `=` | Calcular resultado |
| `Backspace` | Apagar último dígito digitado |
| `Esc` ou `C` | Limpar visor (`AC`) |

---

## 👤 Autor

Desenvolvido por **Ian Firmino**  
GitHub: [@ianfirminotc](https://github.com/ianfirminotc)
