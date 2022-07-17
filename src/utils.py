from django.utils.translation import gettext_lazy as _

LANGUAGES=(
        ('af', _('Afrikaans')),
        ('ar', _('Arabic')),
        ('ar-dz', _('Algerian Arabic')),
        ('ast', _('Asturian')),
        ('az', _('Azerbaijani')),
        ('bg', _('Bulgarian')),
        ('be', _('Belarusian')),
        ('bn', _('Bengali')),
        ('br', _('Breton')),
        ('bs', _('Bosnian')),
        ('ca',_('Catalan')),
        ('cs',_('Czech')),
        ('cy',_('Welsh')),
        ('da',_('Danish')),
        ('de',_('German')),
        ('dsb',_('Lower Sorbian')),
        ('el', _('Greek')),
        ('en',_('English')),
        ('en-au', _('Australian English')),
        ('en-gb',_('British English')),
        ('eo',_('Esperanto')),
        ('es',_('Spanish')),
        ('es-ar',_('Argentinian Spanish')),
        ('es-co',_('Colombian Spanish')),
        ('es-mx',_('Mexican Spanish')),
        ('es-ni',_('Nicaraguan Spanish')),
        ('es-ve',_('Venezuelan Spanish')),
        ('et', _('Estonian')),
        ('eu', _('Basque')),
        ('fa', _('Persian')),
        ('fi', _('Finnish')),
        ('fr', _('French')),
        ('fy', _('Frisian')),
        ('ga', _('Irish')),
        ('gd', _('Scottish Gaelic')),
        ('gl', _('Galician')),
        ('he', _('Hebrew')),
        ('hi', _('Hindi')),
        ('hr', _('Croatian')),
        ('hsb', _('Upper Sorbian')),
        ('hu', _('Hungarian')),
        ('hy', _('Armenian')),
        ('ia', _('Interlingua')),
        ('id', _('Indonesian')),
        ('ig', _('Igbo')),
        ('io', _('Ido')),
        ('is', _('Icelandic')),
        ('it', _('Italian')),
        ('ja', _('Japanese')),
        ('ka', _('Georgian')),
        ('kab', _('Kabyle')),
        ('kk', _('Kazakh')),
        ('km', _('Khmer')),
        ('kn', _('Kannada')),
        ('ko', _('Korean')),
        ('ky', _('Kyrgyz')),
        ('lb', _('Luxembourgish')),
        ('lt', _('Lithuanian')),
        ('lv', _('Latvian')),
        ('mk', _('Macedonian')),
        ('ml', _('Malayalam')),
        ('mn', _('Mongolian')),
        ('mr', _('Marathi')),
        ('my', _('Burmese')),
        ('nb', _('Norwegian Bokmål')),
        ('ne', _('Nepali')),
        ('nl', _('Dutch')),
        ('nn', _('Norwegian Nynorsk')),
        ('os', _('Ossetic')),
        ('pa', _('Punjabi')),
        ('pl', _('Polish')),
        ('pt', _('Portuguese')),
        ('pt-br', _('Brazilian Portuguese')),
        ('ro', _('Romanian')),
        ('ru', _('Russian')),
        ('sk', _('Slovak')),
        ('sl', _('Slovenian')),
        ('sq', _('Albanian')),
        ('sr', _('Serbian')),
        ('sr-latn', _('Serbian Latin')),
        ('sv', _('Swedish')),
        ('sw', _('Swahili')),
        ('ta', _('Tamil')),
        ('te', _('Telugu')),
        ('tg', _('Tajik')),
        ('th', _('Thai')),
        ('tk', _('Turkmen')),
        ('tr', _('Turkish')),
        ('tt', _('Tatar')),
        ('udm', _('Udmurt')),
        ('uk', _('Ukrainian')),
        ('ur', _('Urdu')),
        ('uz', _('Uzbek')),
        ('vi', _('Vietnamese')),
        ('zh-hans', _('Simplified Chinese')),
        ('zh-hant', _('Traditional Chinese')),
    )







def getSimplifiedNumber(num):
    if num < 1000:
        return num
    elif num < 1000000:
        num = num / 1000
        num = round(num, 1)
        return f"{num}k"
    elif num < 1000000000:
        num = num / 1000000
        num = round(num, 1)
        return f"{num}M"
    elif num < 1000000000000:
        num = num / 1000000000
        num = round(num, 1)
        return f"{num}B"
    return num

