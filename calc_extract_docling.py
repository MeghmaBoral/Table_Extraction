from docling.document_converter import DocumentConverter
pdf_path = "C:/Users/KIIT0001/Downloads/ifrs-2024-example-financial-statements.pdf"


converter = DocumentConverter()


result = converter.convert(pdf_path)


if result.document.tables:
    for i, table in enumerate(result.document.tables):
        print(f"\n Table {i+1}:\n" + "-"*40)
        for row in table.data:
            row_data = [cell.text.strip() for cell in row]
            print(row_data)
else:
    print("No tables found in the PDF.")
