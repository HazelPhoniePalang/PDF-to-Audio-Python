import pyttsx3
import PyPDF2
import os

is_running = True

while is_running:
    # Get directory and filename from user
    directory = input("Enter the directory path (e.g., /home/user/documents): ")
    filename = input("Enter the PDF filename (e.g., include .pdf):  ")

    # Construct full file path
    file_path = os.path.join(directory, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
    else:
        try:
            # Open and read PDF
            file = open(file_path, "rb")
            pdf_reader = PyPDF2.PdfReader(file) 
            total_pages = len(pdf_reader.pages)
            print(f"The PDF has {total_pages} pages.")
            
            # Initialize text-to-speech
            speak = pyttsx3.init()
            speak.setProperty('rate', 150)  # Adjust speed if needed

            start_page = int(input(f"What page should I start? (1-{total_pages}): "))

            if start_page < 1 or start_page > total_pages:
                print("Invalid page number.")
                continue

            for page_number in range(start_page - 1, total_pages):
                print(f"Reading page {page_number + 1}...")

                page = pdf_reader.pages[page_number]
                text = page.extract_text()

                if text and text.strip():
                    speak.say(text)
                    speak.runAndWait()
                else:
                    print(f"Page {page_number + 1} has no readable text.")
            
            file.close()
            print("Done reading the PDF!")
            
        except Exception as e:
            print(f"Error: {e}")

    user_choice = int(input("\nDo you want to read another PDF? (yes/no) ")).lower()

    if user_choice not in ["yes", "y"]:
        print("Thank you for using this program. ")
        break