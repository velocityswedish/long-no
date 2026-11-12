"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY NORWEGIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "NORWEGIAN"
HANDLE = "@velocitynorwegian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'nb',
 'name': 'Norwegian',
 'native_name': 'Norsk',
 'history_key': 'norwegian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'nb-NO-FinnNeural',
 'native_fallback_voice': 'nb-NO-PernilleNeural',
 'native_engine': 'edge',
 'native_lang_code': 'nb',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'NORSK',
 'translit_label': 'SAY IT LIKE',
 'flag': 'no',
 'greeting': 'Hei!',
 'encouragement': 'Fantastisk!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅæøå'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivasjon',
 'Love': 'Kjærlighet',
 'Success': 'Suksess',
 'Wisdom': 'Visdom',
 'Happiness': 'Lykke',
 'Self Improvement': 'Selvutvikling',
 'Gratitude': 'Takknemlighet',
 'Friendship': 'Vennskap',
 'Hope': 'Håp',
 'Creativity': 'Kreativitet',
 'Inner Peace': 'Indre Fred',
 'Confidence': 'Selvtillit',
 'Perseverance': 'Utholdenhet',
 'Inspiration': 'Inspirasjon',
 'Positive Life': 'Positivt Liv',
 'Courage': 'Mot',
 'Kindness': 'Vennlighet',
 'Patience': 'Tålmodighet',
 'Forgiveness': 'Tilgivelse',
 'Strength': 'Styrke',
 'Joy': 'Glede',
 'Balance': 'Balanse',
 'Growth': 'Vekst',
 'Purpose': 'Formål',
 'Mindfulness': 'Oppmerksomhet',
 'Travel & Airport': 'Reise og flyplass',
 'Ordering Food & Dining': 'Bestille mat og spise ute',
 'Shopping & Prices': 'Shopping og priser',
 'Asking for Directions': 'Spørre om veien',
 'Hotel & Accommodation': 'Hotell og overnatting',
 'Daily Routine': 'Daglig rutine',
 'Meeting People & Greetings': 'Møte folk og hilse',
 'Emergency & Health': 'Nødsituasjoner og helse',
 'Public Transportation': 'Kollektivtransport',
 'Work & Office': 'Jobb og kontor',
 'Weather & Small Talk': 'Vær og småprat',
 'Coffee Shop & Bakery': 'Kafé og bakeri',
 'Family & Home': 'Familie og hjem',
 'Hobbies & Free Time': 'Hobbyer og fritid',
 'Dating & Romance': 'Dating og romantikk',
 'Phone Calls & Messages': 'Telefonsamtaler og meldinger',
 'Banking & Money': 'Bank og penger',
 'Doctor & Pharmacy': 'Lege og apotek',
 'Sports & Fitness': 'Sport og trening',
 'Celebrations & Parties': 'Feiringer og fester',
 'Feelings & Emotions': 'Følelser',
 'Agreeing & Disagreeing': 'Enig og uenig',
 'Making Plans': 'Lage planer',
 'Common Native Slang': 'Vanlig gatespråk',
 'Cultural Traditions': 'Kulturtradisjoner'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnnorwegian',
 '#norwegianlessons',
 '#norwegianforbeginners',
 '#languagelearning',
 '#norwegianvocabulary',
 '#velocitynorwegian',
 '#dailynorwegian',
 '#norwegian',
 '#learnlanguages',
 '#speaknorwegian']
# ==== HASHTAGS END ====
