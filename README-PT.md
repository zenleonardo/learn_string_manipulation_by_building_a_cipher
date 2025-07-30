# Transformação de Dados Baseada em Regras: Uma Cifra de Vigenère com Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
</p>

[Read in English / Ler em Inglês](README.md)

## 📖 Sobre o Projeto

Desenvolvido como parte do curso "Computação Científica com Python" da freeCodeCamp, este repositório é uma demonstração prática de **técnicas essenciais de transformação de dados usando Python**. Embora o resultado seja uma Cifra de Vigenère clássica, o processo demonstra a habilidade de processar dados entrada por entrada, aplicar lógicas complexas baseadas em regras e lidar com a qualidade dos dados — competências fundamentais em Engenharia de Dados.

O programa pode tanto criptografar quanto descriptografar mensagens, servindo como um excelente exemplo da construção de funções de transformação de dados que são invertíveis.

### ✨ Habilidades Chave para Engenharia de Dados

Este projeto demonstra habilidades fundamentais para a construção de pipelines de dados robustos:

- **Lógica de Transformação de Dados**: Implementação de um algoritmo de mapeamento baseado em regras, análogo ao 'T' em um processo de ETL/ELT.
- **Processamento Granular (Nível a Nível)**: Iterar sobre um conjunto de dados (neste caso, uma string) para aplicar transformações em um nível detalhado, caractere por caractere.
- **Código Modular e Reutilizável**: Construção de funções limpas e reutilizáveis (`encrypt`, `decrypt`) que podem atuar como componentes em um workflow de dados maior.
- **Limpeza e Validação de Dados**: Tratamento eficaz de dados não conformes (caracteres não alfabéticos) para garantir a integridade do pipeline e prevenir falhas.

### 🚀 Como Executar

1.  Clone o repositório.
2.  Navegue até a pasta do projeto.
3.  Crie e ative um ambiente virtual.
4.  Execute o script principal para ver o exemplo de decodificação:
    ```bash
    python3 src/main.py
    ```

### 💻 Exemplo de Saída

Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: freecodecamp is awesome