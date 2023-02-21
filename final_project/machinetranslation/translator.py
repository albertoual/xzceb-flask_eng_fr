"""
Methods for translating French to English and English to French
using IBM Watson Language Translator API
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ.get('apikey')
URL = os.environ.get('url')
VERSION = os.environ.get('version')

if not APIKEY or not URL or not VERSION:
    raise ValueError('Missing required environment variables')

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator,
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates the text input in English to French and returns the French text
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    except ApiException as ex:
        raise ValueError(f"Failed to translate English to French: {ex.message}") from ex

def french_to_english(french_text):
    """
    Translates the text input in French to English and returns the English text
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except ApiException as ex:
        raise ValueError(f"Failed to translate French to English: {ex.message}") from ex
