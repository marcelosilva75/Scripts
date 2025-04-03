# MassDNS Parser

## 📌 Sobre o Projeto
O **MassDNS Parser** é um script em Python para analisar e processar arquivos binários gerados pelo [MassDNS](https://github.com/blechschmidt/massdns), uma ferramenta de resolução de DNS em massa. Ele permite a extração e interpretação dos resultados das consultas DNS, convertendo os dados binários em um formato legível.

## 🚀 Funcionalidades
- **Leitura e análise** de arquivos binários de saída do MassDNS
- **Extração de informações DNS** como timestamps, resolvers e respostas
- **Conversão para formato legível** utilizando a biblioteca `dnspython`
- **Compatível com IPv4 e IPv6**

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **dnspython** (para manipulação de pacotes DNS)
- **ipaddress** (para tratamento de IPs)

## 📂 Estrutura do Repositório
```
/
├── massdns_parser.py  # Script principal
├── example_data.bin   # Exemplo de arquivo binário do MassDNS
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```

## 📌 Como Usar
### 1️⃣ Pré-requisitos
Antes de executar o script, instale as dependências necessárias:
```sh
pip install -r requirements.txt
```

### 2️⃣ Execução do Script
Para processar um arquivo de saída do MassDNS, utilize o seguinte comando:
```sh
python massdns_parser.py <arquivo_massdns.bin>
```
Exemplo:
```sh
python massdns_parser.py example_data.bin
```

### 3️⃣ Exemplo de Saída
```
8.8.8.8:53, 02 Abr 2025 14:32:10 UTC
www.example.com. 300 IN A 93.184.216.34
```

## 📖 Referências
- [MassDNS - Repositório Oficial](https://github.com/blechschmidt/massdns)
- [dnspython - Biblioteca para manipulação de DNS](https://www.dnspython.org/)

## 🤝 Contribuição
Sinta-se à vontade para abrir *issues* e *pull requests* para melhorias no código ou documentação.

## 📜 Licença
Este projeto está licenciado sob a **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.


