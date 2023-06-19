import subprocess, os, argparse, polib, mtranslate
from mtranslate import translate
from django.core.management import call_command



def make_messages():
    extensions = [".html"]
    languages = ["ar", "en"]
    for language in languages:
        extension_args = " ".join(f"-e {ext}" for ext in extensions)
        cmd = f"python manage.py makemessages --locale={language} {extension_args}"
        subprocess.run(cmd, shell=True)




def translate_po_file():
    # Path to the .po file for translation to Arabic ('ar')
    ar_po_file_path = './locale/ar/LC_MESSAGES/django.po'
    
    # Path to the .po file for translation to English ('en')
    en_po_file_path = './locale/en/LC_MESSAGES/django.po'

    # Load the .po file for translation to Arabic
    ar_po = polib.pofile(ar_po_file_path)

    # Load the .po file for translation to English
    en_po = polib.pofile(en_po_file_path)

    # Translate the words to Arabic
    for entry in ar_po:
        entry.msgstr = translate(entry.msgid, 'ar')

    # Translate the words to English
    for entry in en_po:
        entry.msgstr = translate(entry.msgid, 'en')

    # Save the translated .po files
    ar_po.save(ar_po_file_path)
    en_po.save(en_po_file_path)




def compile_translations():
    # Run the compilemessages command
    call_command('compilemessages')