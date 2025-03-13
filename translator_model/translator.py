from langdetect import detect, DetectorFactory
from googletrans import Translator

DetectorFactory.seed = 42

def detect_language(query):
    try:
        lang = detect(query)
        return lang 
    except Exception as e:
        return 'Network issue'

def translate_to_english(query, query_lang):
    translator = Translator()
    if query_lang != 'en':
        translated = translator.translate(query, src=query_lang, dest='en')
        return translated.text
    return query
    
def process_query(query):
    query_lang = detect_language(query)
    
    if query_lang:
        translated_query = translate_to_english(query, query_lang)
        return translated_query
    else:
        return query  

queries = [
    "आप कौन हो?",   #Hindi
    "Who are you?",  #English
    "तू कोण आहेस?" #Marathi
]

for query in queries:
    print(f"\nOriginal query: {query}")
    processed_query = process_query(query)
    print(f"Processed query: {processed_query}")