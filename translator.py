from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url_lt = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/971ca9f6-ea42-4f03-86bd-f290c32de433"
apikey_lt = "_wETvMMpcZVt0YObpse2_jToi-pE07zyfP0CBDsfkAQe"
version_lt ="2018-05-01"
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
    
def eng_french(eng_text):    

    French_translation=language_translator.translate(text=eng_text , model_id='en-fr').get_result()
    translation = French_translation['translations'][0]['translation']
    return(translation)

def french_eng(french_text): 
    
    english_translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    translation = english_translation['translations'][0]['translation']
    return(translation)