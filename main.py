# Import the required module
import pyttsx3
 
# Create a string
string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."
 
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
 
# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')
 
# Wait until above command is not finished.
engine.runAndWait()


# # Open the PDF file in read-binary mode using a context manager
# with open('demo.pdf', 'rb') as pdf_file:
#     # Create a PDF reader object
#     pdf_reader = PdfReader(pdf_file)

#     # Get the total number of pages in the PDF file
#     num_pages = len(pdf_reader.pages)

#     # Create a text variable to store the content of the PDF file
#     text = ''

#     # Iterate over each page in the PDF file
#     for page in range(num_pages):
#         # Get the page object
#         pdf_page = pdf_reader.pages[page]

#         # Extract the text from the page
#         page_text = pdf_page.extract_text()

#         # Add the text to the text variable
#         text += page_text

# # Create a text-to-speech engine object
# engine = pyttsx3.init()

# # Convert the text to speech
# engine.say(text)
# engine.runAndWait()




# import pyttsx3,PyPDF2
# speacker = pyttsx3.init()

# texts = ["This is an example of text-to-speech conversion", "Hello World"]
# speacker.save_to_file (texts, "d.mp3")
# speacker.say('hello')
# # pdfreader = PyPDF2.PdfReader(open('demo.pdf','rb'))
# # for page_num in range (len(pdfreader.pages)):
# #     text  = pdfreader.pages[page_num].extract_text()
# #     clean_text = text.strip().replace('\n', ' ')
# #     print(clean_text)
# # speacker.save_to_file(clean_text, 'audio.mp3')
# # speacker.runAndWait()
# # speacker.stop()