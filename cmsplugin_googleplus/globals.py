from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

# The following language codes are available for search methods in people
# and activities resources
# https://developers.google.com/+/api/search#available-languages
AFRIKAANS = 'af'
AMHARIC = 'am'
ARABIC = 'ar'
BASQUE = 'eu'
BENGALI = 'bn'
BULGARIAN = 'bg'
CATALAN = 'ca'
CHINESE_HONG_KONG = 'zh-HK'
CHINESE_SIMPLIFIED = 'zh-CN'
CHINESE_TRADITIONAL = 'zh-TW'
CROATIAN = 'hr'
CZECH = 'cs'
DANISH = 'da'
DUTCH = 'nl'
ENGLISH_UK = 'en-GB'
ENGLISH_US = 'en-US'
ESTONIAN = 'et'
FILIPINO = 'fil'
FINNISH = 'fi'
FRENCH = 'fr'
FRENCH_CANADIAN = 'fr-CA'
GALICIAN = 'gl'
GERMAN = 'de'
GREEK = 'el'
GUJARATI = 'gu'
HEBREW = 'iw'
HINDI = 'hi'
HUNGARIAN = 'hu'
ICELANDIC = 'is'
INDONESIAN = 'id'
ITALIAN = 'it'
JAPANESE = 'ja'
KANNADA = 'kn'
KOREAN = 'ko'
LATVIAN = 'lv'
LITHUANIAN = 'lt'
MALAY = 'ms'
MALAYALAM = 'ml'
MARATHI = 'mr'
NORWEGIAN = 'no'
PERSIAN = 'fa'
POLISH = 'pl'
PORTUGUESE_BRAZIL = 'pt-BR'
PORTUGUESE_PORTUGAL = 'pt-PT'
ROMANIAN = 'ro'
RUSSIAN = 'ru'
SERBIAN = 'sr'
SLOVAK = 'sk'
SLOVENIAN = 'sl'
SPANISH = 'es'
SPANISH_LATIN_AMERICA = 'es-419'
SWAHILI = 'sw'
SWEDISH = 'sv'
TAMIL = 'ta'
TELUGU = 'te'
THAI = 'th'
TURKISH = 'tr'
UKRAINIAN = 'uk'
URDU = 'ur'
VIETNAMESE = 'vi'
ZULU = 'zu'

GOOGLEPLUS_PLUGIN_LANGUAGE_CHOICES = (
    (AFRIKAANS, _('Afrikaans')),
    (AMHARIC, _('Amharic')),
    (ARABIC, _('Arabic')),
    (BASQUE, _('Basque')),
    (BENGALI, _('Bengali')),
    (BULGARIAN, _('Bulgarian')),
    (CATALAN, _('Catalan')),
    (CHINESE_HONG_KONG, _('Chinese (Hong Kong)')),
    (CHINESE_SIMPLIFIED, _('Chinese (Simplified)')),
    (CHINESE_TRADITIONAL, _('Chinese (Traditional)')),
    (CROATIAN, _('Croatian')),
    (CZECH, _('Czech')),
    (DANISH, _('Danish')),
    (DUTCH, _('Dutch')),
    (ENGLISH_UK, _('English (UK)')),
    (ENGLISH_US, _('English (US)')),
    (ESTONIAN, _('Estonian')),
    (FILIPINO, _('Filipino')),
    (FINNISH, _('Finnish')),
    (FRENCH, _('French')),
    (FRENCH_CANADIAN, _('French (Canadian)')),
    (GALICIAN, _('Galician')),
    (GERMAN, _('German')),
    (GREEK, _('Greek')),
    (GUJARATI, _('Gujarati')),
    (HEBREW, _('Hebrew')),
    (HINDI, _('Hindi')),
    (HUNGARIAN, _('Hungarian')),
    (ICELANDIC, _('Icelandic')),
    (INDONESIAN, _('Indonesian')),
    (ITALIAN, _('Italian')),
    (JAPANESE, _('Japanese')),
    (KANNADA, _('Kannada')),
    (KOREAN, _('Korean')),
    (LATVIAN, _('Latvian')),
    (LITHUANIAN, _('Lithuanian')),
    (MALAY, _('Malay')),
    (MALAYALAM, _('Malayalam')),
    (MARATHI, _('Marathi')),
    (NORWEGIAN, _('Norwegian')),
    (PERSIAN, _('Persian')),
    (POLISH, _('Polish')),
    (PORTUGUESE_BRAZIL, _('Portuguese (Brazil)')),
    (PORTUGUESE_PORTUGAL, _('Portuguese (Portugal)')),
    (ROMANIAN, _('Romanian')),
    (RUSSIAN, _('Russian')),
    (SERBIAN, _('Serbian')),
    (SLOVAK, _('Slovak')),
    (SLOVENIAN, _('Slovenian')),
    (SPANISH, _('Spanish')),
    (SPANISH_LATIN_AMERICA, _('Spanish (Latin America)')),
    (SWAHILI, _('Swahili')),
    (SWEDISH, _('Swedish')),
    (TAMIL, _('Tamil')),
    (TELUGU, _('Telugu')),
    (THAI, _('Thai')),
    (TURKISH, _('Turkish')),
    (UKRAINIAN, _('Ukrainian')),
    (URDU, _('Urdu')),
    (VIETNAMESE, _('Vietnamese')),
    (ZULU, _('Zulu')),
)


BEST = 'best'
RECENT = 'recent'

GOOGLEPLUS_PLUGIN_ORDER_BY_CHOICES = (
    (BEST, _('best')),
    (RECENT, _('recent'))
)
