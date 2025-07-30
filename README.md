# Rule-Based Data Transformation: A Vigenère Cipher in Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
</p>

[Read in Portuguese / Ler em Português](README-PT.md)

## 📖 About the Project

Developed as a project for the freeCodeCamp "Scientific Computing with Python" course, this repository is a practical demonstration of **core data transformation techniques using Python**. While the output is a classic Vigenère cipher, the underlying process showcases the ability to process data entry by entry, apply complex rule-based logic, and handle data quality issues—all fundamental skills in Data Engineering.

The program can both encrypt and decrypt messages, serving as an excellent example of building invertible data transformation functions.

### ✨ Key Skills for Data Engineering

This project demonstrates foundational skills essential for building robust data pipelines:

- **Data Transformation Logic**: Implementation of a rule-based mapping algorithm, analogous to the 'T' in an ETL/ELT process.
- **Row-Level Processing**: Iterating through a dataset (a string, in this case) to apply transformations on a granular, character-by-character level.
- **Modular & Reusable Code**: Building clean, reusable functions (`encrypt`, `decrypt`) that can be components in a larger data workflow.
- **Data Cleaning & Validation**: Effectively handling non-conforming data (non-alphabetic characters) to ensure the pipeline's integrity and prevent failures.

### 🚀 How to Run

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Create and activate a virtual environment.
4.  Run the main script to see the example decryption:
    ```bash
    python3 src/main.py
    ```

### 💻 Example Output

Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: freecodecamp is awesome