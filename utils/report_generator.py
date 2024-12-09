# utils/report_generator.py
import pandas as pd


def generate_report(data, output_path):
    """
    Gera um relatório Excel a partir dos dados fornecidos.
    """
    if not data:
        print("Nenhum dado disponível para gerar o relatório.")
        return
    
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    print(f"Relatório salvo em: {output_path}")
