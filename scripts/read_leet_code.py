import pandas as pd
from pathlib import Path

file_path = 'leet_code_practise.xlsx'
output_path = 'automation/leet_code_summary.txt'

try:
    xl = pd.ExcelFile(file_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Excel Summary: {file_path}\n")
        f.write(f"Sheets: {xl.sheet_names}\n\n")
        
        for sheet_name in xl.sheet_names:
            f.write(f"{'='*20}\n")
            f.write(f"Sheet: {sheet_name}\n")
            f.write(f"{'='*20}\n")
            df = xl.parse(sheet_name)
            df = df.dropna(how='all')
            
            # Print columns
            f.write(f"Columns: {list(df.columns)}\n\n")
            
            # Focus on rows that have remarks or logic hints
            f.write("Sample Data (Latest 20 entries):\n")
            f.write(df.tail(20).to_string())
            f.write("\n\n")
            
            # Extract common themes from remarks if they exist
            rem_cols = [c for c in df.columns if c.lower() in ['remarks', 'remarks ', 'hints', 'notes', 'solutions']]
            if rem_cols:
                f.write("Key Insights/Mistakes identified:\n")
                for col in rem_cols:
                    f.write(f"--- Column: {col} ---\n")
                    f.write(df[col].dropna().astype(str).tail(30).to_string())
                    f.write("\n")
            
            f.write("\n\n")
            
    print(f"Summary written to {output_path}")

except Exception as e:
    print(f"Error: {e}")
