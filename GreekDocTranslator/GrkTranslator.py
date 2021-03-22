import docx
from google_trans_new import google_translator
translator = google_translator()  
from pdf2docx import Converter

#Path to the Document you want converted
filename = 'C:\\Path\\to\\really\\important\\document.docx'
#Path to the location where you want the new document
newdoc = 'C:\\Location\\of\\fresh_document.docx'

doc = docx.Document(filename)
for para in doc.paragraphs:
    if para.text in para.text:
        try:
            para.text = para.text.replace(para.text,
                                          translator.translate(para.text, lang_tgt='el'))
        except:
            continue
        doc.save(newdoc)
