# 🧮 Calculadora Minimalista em Python (Dark Mode)

Aplicação desktop moderna e minimalista desenvolvida em **Python** com interface gráfica elegante em **Dark Mode** (inspirada no estilo macOS/iOS). O projeto conta com arquitetura modular, histórico lateral retrátil de cálculos, suporte a atalhos de teclado e testes automatizados.

---

## ✨ Funcionalidades

- **Design Minimalista Dark Mode:** Visual escuro em tons refinados (`#18181b`, `#27272a`), botões arredondados e tipografia limpa.
- **Operações Básicas:** Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
- **Porcentagem Integrada (%):** Suporte tanto a cálculo percentual composto (ex: `200 + 15% = 230`) quanto isolado (ex: `50% = 0.5`).
- **Funções Especiais:** Limpar tudo (`AC`), alternar sinal (`+/-`) e controle de casas decimais.
- **Painel de Histórico Retrátil:** Histórico lateral expansível com opção de reutilizar o resultado com um clique e botão para limpar histórico.
- **Atalhos do Teclado:** Controle completo pelo teclado numérico, teclas de operação, `Enter`, `Backspace` e `Esc`.
- **Arquitetura Modular:** Separação estrita entre a interface gráfica (`calculadora.py`), as funções matemáticas puras (`operacoes.py`) e os testes unitários (`test_operacoes.py`).

---

## 📁 Estrutura do Projeto

```text
├── calculadora.py       # Interface gráfica moderna em Dark Mode (customtkinter)
├── operacoes.py         # Módulo com funções puras de cálculo matemático
├── test_operacoes.py    # Testes unitários automatizados (unittest)
├── requirements.txt     # Dependências do projeto (customtkinter)
└── README.md            # Documentação do projeto
```

---

## 🚀 Como Executar no Windows

### 1. Instalar as Dependências
Abra o Prompt de Comando ou PowerShell na pasta do projeto e execute:
```bash
py -m pip install -r requirements.txt
```

### 2. Executar a Calculadora
```bash
py calculadora.py
```

### 3. Rodar os Testes Automatizados
```bash
py -m unittest -v test_operacoes.py
```

---

## ⌨️ Atalhos de Teclado Suportados

| Tecla | Ação |
| :--- | :--- |
| `0` a `9` | Digitação numérica |
| `,` ou `.` | Ponto decimal |
| `+`, `-`, `*`, `/` | Operações matemáticas |
| `%` | Cálculo de porcentagem |
| `Enter` ou `=` | Calcular resultado |
| `Backspace` | Apagar último dígito |
| `Esc` ou `C` | Limpar visor (`AC`) |

---

## 👤 Autor

Desenvolvido durante a **Imersão Alura**.
