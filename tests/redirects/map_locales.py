# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import flatten, url_test

# supported locales
LOCALES = [
    'ar', 'ast', 'bg', 'bn-IN', 'ca', 'cs', 'de', 'dsb', 'el', 'en-GB',
    'en-US', 'es-CL', 'es-ES', 'fr', 'fy-NL', 'gd', 'it', 'ja', 'ko', 'nl',
    'pt-BR', 'pt-PT', 'ru', 'son', 'sv-SE', 'ta', 'tr', 'uk', 'zh-CN', 'zh-TW']

# List of some locale name variants including unsupported short names and
# obsolete ab-CD-style names, which could be included in the visitors'
# Accept-Language HTTP header and should be redirected to the respective
# canonical locales
LOCALE_VARIANTS = {
    'en-US': ['en', 'en-CA'],
    'es-ES': ['es', 'es-419'],
    'fr': ['fr-FR'],
    'ja': ['ja-JP-mac'],
    'pt-BR': ['pt'],
    'ta': ['ta-LK']}

_urls = []
for locale in LOCALES:
    variants = [locale]
    variants.extend(LOCALE_VARIANTS.get(locale, []))
    for variant in variants:
        # check the landing page redirects for each locale variant
        _urls.append(url_test('/', '/{locale}/'.format(locale=locale),
                              req_headers={'Accept-Language': variant}))

URLS = flatten(_urls)