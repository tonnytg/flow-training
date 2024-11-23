import os
import pandas as pd

def list_and_display_csv(directory):
    """
    Lista todos os arquivos .csv em um diretório e exibe as primeiras 5 linhas de cada arquivo.
    
    :param directory: Caminho do diretório onde procurar os arquivos .csv.
    """
    # Listando arquivos no diretório
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    if not csv_files:
        print("Nenhum arquivo .csv encontrado no diretório.")
        return
    
    print(f"Arquivos .csv encontrados no diretório '{directory}':")
    for csv_file in csv_files:
        print(f" - {csv_file}")
    
    # Exibindo as primeiras 5 linhas de cada arquivo
    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)
        print(f"\nConteúdo do arquivo: {csv_file}")
        try:
            df = pd.read_csv(file_path)
            print(df.head(5))
        except Exception as e:
            print(f"Erro ao ler o arquivo {csv_file}: {e}")

# Exemplo de uso
# Substitua 'caminho_do_diretorio' pelo caminho onde estão os arquivos .csv
directory_path = './caminho_do_diretorio'
list_and_display_csv(directory_path)

