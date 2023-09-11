import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

        return text

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    output_folder = input("Enter the path to the output folder: ")
    output_filename = input("Enter the desired output filename (without extension): ")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extracted_text = extract_text_from_pdf(pdf_path)
    truncated_text = extracted_text[:22000]

    output_filepath = os.path.join(output_folder, f"{output_filename}.txt")
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        output_file.write(truncated_text)

    print(f"Extracted and saved 22000 characters from the PDF to {output_filepath}")

if __name__ == "__main__":
    main()
