import pandas as pd
import os

print(" Excel Table Analyzer")


while True:
    excel_file = input("Enter full path to your Excel file (e.g., C:/Users/You/Downloads/SaleData.xlsx): ").strip()
    if os.path.exists(excel_file):
        break
    print(" File not found. Please try again.")


xls = pd.ExcelFile(excel_file)
print("\n Sheets Found:")
for i, sheet in enumerate(xls.sheet_names):
    print(f"{i + 1}. {sheet}")
while True:
    try:
        sheet_index = int(input("\nEnter the sheet number to analyze: "))
        sheet_name = xls.sheet_names[sheet_index]
        break
    except (ValueError, IndexError):
        print(" Invalid input. Please    enter a valid sheet number.")


df = xls.parse(sheet_name)
print(f"\n Loaded sheet: {sheet_name}")
print("\n First 5 rows of the table:\n")
print(df.head())


profit_col = next((col for col in df.columns if 'profit' in col.lower()), None)
if profit_col:
    total_profit = df[profit_col].sum()
    print(f"\n Total Profit (from '{profit_col}'): {total_profit}")
else:
    print("\n Could not find a column containing 'profit'.")

sales_col = next((col for col in df.columns if 'sale' in col.lower()), None)
item_col = next((col for col in df.columns if 'item' in col.lower() or 'product' in col.lower()), None)

if sales_col and item_col:
    item_sales = df.groupby(item_col)[sales_col].sum()
    top_item = item_sales.idxmax()
    top_sales = item_sales.max()
    print(f"\n Item with highest total sales: '{top_item}' — Total Sales: {top_sales}")
else:
    print("\n Could not find both 'sales' and 'item/product' columns.")

print("\nAnalysis Complete!")


