"""
Calculadora Minimalista Dark Mode em Python (GUI)
Interface moderna com customtkinter e suporte a histórico e atalhos de teclado.
"""

import customtkinter as ctk
from operacoes import somar, subtrair, multiplicar, dividir, porcentagem

# Configurações globais de tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Paleta de Cores Estilo macOS/iOS Dark Mode
COLOR_BG = "#18181b"          # Fundo principal da janela
COLOR_DISPLAY_BG = "#121214"  # Fundo do visor
COLOR_NUM_BTN = "#27272a"     # Botões numéricos (cinza escuro)
COLOR_NUM_HOVER = "#3f3f46"
COLOR_FUNC_BTN = "#3f3f46"    # Botões de controle AC, +/-, %
COLOR_FUNC_HOVER = "#52525b"
COLOR_OP_BTN = "#ff9f0a"      # Botões de operação (laranja)
COLOR_OP_HOVER = "#ffb340"
COLOR_TEXT = "#ffffff"
COLOR_MUTED = "#a1a1aa"

class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Minimalista")
        self.geometry("380x600")
        self.resizable(False, False)
        self.configure(fg_color=COLOR_BG)

        # Estado da Calculadora
        self.current_value = "0"
        self.first_operand = None
        self.active_operator = None
        self.reset_screen = False
        self.history = []
        self.history_visible = False

        # Configuração do Layout Principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._criar_barra_superior()
        self._criar_visor()
        self._criar_teclado()
        self._criar_painel_historico()
        self._configurar_atalhos_teclado()

    def _criar_barra_superior(self):
        """Barra de título com estilo limpo e botão de alternar histórico."""
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="ew")
        top_bar.grid_columnconfigure(1, weight=1)

        # Três pontos decorativos estilo macOS
        dots_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        dots_frame.grid(row=0, column=0, sticky="w")
        for color in ["#ff5f56", "#ffbd2e", "#27c93f"]:
            dot = ctk.CTkLabel(dots_frame, text="●", text_color=color, font=("Arial", 14), width=16)
            dot.pack(side="left", padx=1)

        # Botão para expandir/ocultar histórico
        self.btn_history_toggle = ctk.CTkButton(
            top_bar,
            text="🕒 Histórico",
            width=90,
            height=28,
            corner_radius=14,
            fg_color="#27272a",
            hover_color="#3f3f46",
            text_color=COLOR_MUTED,
            font=("Arial", 12, "bold"),
            command=self.toggle_historico
        )
        self.btn_history_toggle.grid(row=0, column=2, sticky="e")

    def _criar_visor(self):
        """Visor digital com indicador discreto da operação anterior e valor atual grande."""
        display_frame = ctk.CTkFrame(self, fg_color=COLOR_DISPLAY_BG, corner_radius=18)
        display_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Linha superior: operação anterior
        self.lbl_operation = ctk.CTkLabel(
            display_frame,
            text="",
            text_color=COLOR_MUTED,
            font=("Arial", 14),
            anchor="e"
        )
        self.lbl_operation.pack(fill="x", padx=18, pady=(14, 0))

        # Linha inferior: valor atual
        self.lbl_display = ctk.CTkLabel(
            display_frame,
            text="0",
            text_color=COLOR_TEXT,
            font=("Arial", 42, "bold"),
            anchor="e"
        )
        self.lbl_display.pack(fill="x", padx=18, pady=(0, 14))

    def _criar_teclado(self):
        """Teclado com cantos arredondados, botões bem espaçados e cores temáticas."""
        self.keypad_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.keypad_frame.grid(row=2, column=0, padx=20, pady=(5, 20), sticky="nsew")

        for col in range(4):
            self.keypad_frame.grid_columnconfigure(col, weight=1)
        for row in range(5):
            self.keypad_frame.grid_rowconfigure(row, weight=1)

        botoes = [
            # Linha 0
            ("AC", 0, 0, 1, COLOR_FUNC_BTN, COLOR_FUNC_HOVER, lambda: self.acao_limpar()),
            ("+/-", 0, 1, 1, COLOR_FUNC_BTN, COLOR_FUNC_HOVER, lambda: self.acao_alternar_sinal()),
            ("%", 0, 2, 1, COLOR_FUNC_BTN, COLOR_FUNC_HOVER, lambda: self.acao_porcentagem()),
            ("÷", 0, 3, 1, COLOR_OP_BTN, COLOR_OP_HOVER, lambda: self.acao_operador("/")),

            # Linha 1
            ("7", 1, 0, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("7")),
            ("8", 1, 1, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("8")),
            ("9", 1, 2, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("9")),
            ("×", 1, 3, 1, COLOR_OP_BTN, COLOR_OP_HOVER, lambda: self.acao_operador("*")),

            # Linha 2
            ("4", 2, 0, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("4")),
            ("5", 2, 1, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("5")),
            ("6", 2, 2, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("6")),
            ("−", 2, 3, 1, COLOR_OP_BTN, COLOR_OP_HOVER, lambda: self.acao_operador("-")),

            # Linha 3
            ("1", 3, 0, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("1")),
            ("2", 3, 1, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("2")),
            ("3", 3, 2, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("3")),
            ("+", 3, 3, 1, COLOR_OP_BTN, COLOR_OP_HOVER, lambda: self.acao_operador("+")),

            # Linha 4
            ("0", 4, 0, 2, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_digito("0")),
            (",", 4, 2, 1, COLOR_NUM_BTN, COLOR_NUM_HOVER, lambda: self.inserir_decimal()),
            ("=", 4, 3, 1, COLOR_OP_BTN, COLOR_OP_HOVER, lambda: self.acao_calcular()),
        ]

        for texto, r, c, cspan, bg_c, hover_c, cmd in botoes:
            btn = ctk.CTkButton(
                self.keypad_frame,
                text=texto,
                font=("Arial", 20, "bold"),
                fg_color=bg_c,
                hover_color=hover_c,
                text_color=COLOR_TEXT,
                corner_radius=26,
                command=cmd
            )
            btn.grid(row=r, column=c, columnspan=cspan, padx=4, pady=5, sticky="nsew")

    def _criar_painel_historico(self):
        """Painel lateral retrátil para visualização dos últimos cálculos."""
        self.history_frame = ctk.CTkFrame(self, fg_color=COLOR_DISPLAY_BG, corner_radius=18)
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(1, weight=1)

        # Cabeçalho do Histórico
        hist_header = ctk.CTkFrame(self.history_frame, fg_color="transparent")
        hist_header.grid(row=0, column=0, padx=15, pady=12, sticky="ew")
        hist_header.grid_columnconfigure(0, weight=1)

        lbl_hist_title = ctk.CTkLabel(
            hist_header,
            text="Histórico Recente",
            font=("Arial", 14, "bold"),
            text_color=COLOR_TEXT
        )
        lbl_hist_title.grid(row=0, column=0, sticky="w")

        btn_limpar = ctk.CTkButton(
            hist_header,
            text="Limpar",
            width=60,
            height=24,
            corner_radius=12,
            fg_color="#ef4444",
            hover_color="#dc2626",
            font=("Arial", 11, "bold"),
            command=self.limpar_historico
        )
        btn_limpar.grid(row=0, column=1, sticky="e")

        # Lista rolável de itens
        self.scroll_history = ctk.CTkScrollableFrame(
            self.history_frame,
            fg_color="transparent",
            scrollbar_button_color="#3f3f46",
            scrollbar_button_hover_color="#52525b"
        )
        self.scroll_history.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.lbl_vazio = ctk.CTkLabel(
            self.scroll_history,
            text="Nenhum cálculo registrado.",
            text_color=COLOR_MUTED,
            font=("Arial", 12, "italic")
        )
        self.lbl_vazio.pack(pady=40)

    def _configurar_atalhos_teclado(self):
        """Permite usar a calculadora pelo teclado físico."""
        self.bind("<Key>", self._ao_pressionar_tecla)

    def _ao_pressionar_tecla(self, event):
        key = event.keysym
        char = event.char

        if char in "0123456789":
            self.inserir_digito(char)
        elif char in [",", "."]:
            self.inserir_decimal()
        elif char == "+":
            self.acao_operador("+")
        elif char == "-":
            self.acao_operador("-")
        elif char == "*":
            self.acao_operador("*")
        elif char == "/":
            self.acao_operador("/")
        elif char == "%":
            self.acao_porcentagem()
        elif key in ["Return", "KP_Enter"] or char == "=":
            self.acao_calcular()
        elif key in ["BackSpace"]:
            self.acao_backspace()
        elif key in ["Escape"] or char.lower() == "c":
            self.acao_limpar()

    # --- Lógica de Operações ---

    def _atualizar_display(self):
        """Formata e atualiza os números no visor com ajuste de tamanho."""
        valor = self.current_value
        if len(valor) > 12:
            self.lbl_display.configure(font=("Arial", 26, "bold"))
        elif len(valor) > 8:
            self.lbl_display.configure(font=("Arial", 32, "bold"))
        else:
            self.lbl_display.configure(font=("Arial", 42, "bold"))

        self.lbl_display.configure(text=valor.replace(".", ","))

    def _formatar_numero(self, num):
        """Retorna inteiro se não houver casas decimais, ou float formatado."""
        if isinstance(num, str):
            return num
        if num == int(num):
            return str(int(num))
        return f"{num:.6f}".rstrip("0").rstrip(".")

    def inserir_digito(self, digito):
        if self.reset_screen:
            self.current_value = digito
            self.reset_screen = False
        else:
            if self.current_value == "0":
                self.current_value = digito
            else:
                self.current_value += digito
        self._atualizar_display()

    def inserir_decimal(self):
        if self.reset_screen:
            self.current_value = "0."
            self.reset_screen = False
        elif "." not in self.current_value:
            self.current_value += "."
        self._atualizar_display()

    def acao_limpar(self):
        self.current_value = "0"
        self.first_operand = None
        self.active_operator = None
        self.reset_screen = False
        self.lbl_operation.configure(text="")
        self._atualizar_display()

    def acao_alternar_sinal(self):
        if self.current_value != "0":
            if self.current_value.startswith("-"):
                self.current_value = self.current_value[1:]
            else:
                self.current_value = "-" + self.current_value
            self._atualizar_display()

    def acao_backspace(self):
        if not self.reset_screen and len(self.current_value) > 1:
            self.current_value = self.current_value[:-1]
        else:
            self.current_value = "0"
        self._atualizar_display()

    def acao_porcentagem(self):
        """Calcula porcentagem de forma integrada."""
        try:
            atual = float(self.current_value)
            if self.first_operand is not None and self.active_operator in ["+", "-"]:
                # Exemplo: 200 + 15% -> 15% de 200 = 30
                pct = porcentagem(self.first_operand, atual)
                self.current_value = self._formatar_numero(pct)
            else:
                # Exemplo isolado: 50% -> 0.5
                self.current_value = self._formatar_numero(atual / 100)
            self._atualizar_display()
        except ValueError:
            self.current_value = "0"
            self._atualizar_display()

    def acao_operador(self, op):
        simbolos = {"+": "+", "-": "−", "*": "×", "/": "÷"}
        try:
            val = float(self.current_value)
            if self.first_operand is not None and not self.reset_screen:
                self.acao_calcular()
                val = float(self.current_value)

            self.first_operand = val
            self.active_operator = op
            self.reset_screen = True
            self.lbl_operation.configure(
                text=f"{self._formatar_numero(self.first_operand)} {simbolos.get(op, op)}"
            )
        except ValueError:
            pass

    def acao_calcular(self):
        if self.first_operand is None or self.active_operator is None:
            return

        simbolos = {"+": "+", "-": "−", "*": "×", "/": "÷"}
        try:
            segundo_operando = float(self.current_value)
            op = self.active_operator
            a = self.first_operand
            b = segundo_operando

            if op == "+":
                resultado = somar(a, b)
            elif op == "-":
                resultado = subtrair(a, b)
            elif op == "*":
                resultado = multiplicar(a, b)
            elif op == "/":
                resultado = dividir(a, b)
            else:
                resultado = 0

            # Verifica mensagem de erro (ex: divisão por zero)
            if isinstance(resultado, str):
                self.lbl_operation.configure(text=f"{self._formatar_numero(a)} {simbolos.get(op, op)} {self._formatar_numero(b)} =")
                self.current_value = resultado
                self.first_operand = None
                self.active_operator = None
                self.reset_screen = True
                self._atualizar_display()
                return

            res_formatado = self._formatar_numero(resultado)
            calc_str = f"{self._formatar_numero(a)} {simbolos.get(op, op)} {self._formatar_numero(b)} = {res_formatado}"
            self._adicionar_ao_historico(calc_str, res_formatado)

            self.lbl_operation.configure(text=f"{self._formatar_numero(a)} {simbolos.get(op, op)} {self._formatar_numero(b)} =")
            self.current_value = res_formatado
            self.first_operand = None
            self.active_operator = None
            self.reset_screen = True
            self._atualizar_display()

        except Exception:
            self.current_value = "Erro"
            self._atualizar_display()

    # --- Histórico ---

    def _adicionar_ao_historico(self, expressao, resultado):
        self.history.append((expressao, resultado))
        if len(self.history) == 1:
            self.lbl_vazio.pack_forget()

        # Cria um card de histórico clicável
        item_frame = ctk.CTkFrame(self.scroll_history, fg_color="#18181b", corner_radius=10)
        item_frame.pack(fill="x", pady=4, padx=2)

        lbl_exp = ctk.CTkLabel(
            item_frame,
            text=expressao,
            font=("Arial", 12),
            text_color=COLOR_TEXT,
            anchor="w"
        )
        lbl_exp.pack(fill="x", padx=10, pady=(6, 2))

        # Ao clicar no item, reutiliza o resultado na calculadora
        def usar_resultado(res=resultado):
            self.current_value = str(res)
            self.reset_screen = True
            self._atualizar_display()

        btn_usar = ctk.CTkButton(
            item_frame,
            text="Reutilizar",
            height=20,
            width=65,
            corner_radius=8,
            fg_color="#27272a",
            hover_color="#3f3f46",
            font=("Arial", 10),
            command=usar_resultado
        )
        btn_usar.pack(anchor="e", padx=10, pady=(0, 6))

    def limpar_historico(self):
        self.history.clear()
        for widget in self.scroll_history.winfo_children():
            widget.destroy()
        self.lbl_vazio = ctk.CTkLabel(
            self.scroll_history,
            text="Nenhum cálculo registrado.",
            text_color=COLOR_MUTED,
            font=("Arial", 12, "italic")
        )
        self.lbl_vazio.pack(pady=40)

    def toggle_historico(self):
        """Expande ou recolhe a janela para exibir a aba de histórico lateral."""
        if not self.history_visible:
            self.geometry("680x600")
            self.history_frame.grid(row=0, column=1, rowspan=3, padx=(0, 20), pady=15, sticky="nsew")
            self.grid_columnconfigure(1, weight=1)
            self.btn_history_toggle.configure(fg_color="#ff9f0a", text_color="#ffffff")
            self.history_visible = True
        else:
            self.history_frame.grid_forget()
            self.grid_columnconfigure(1, weight=0)
            self.geometry("380x600")
            self.btn_history_toggle.configure(fg_color="#27272a", text_color=COLOR_MUTED)
            self.history_visible = False


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()
