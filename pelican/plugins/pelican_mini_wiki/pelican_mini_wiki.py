import logging
from pelican import signals

logger = logging.getLogger(__name__)

def check_settings(pelican):
    """
    Log info as needed for configured settings.
    """
    mini_wiki = pelican.settings.get("MINI_WIKI", "")
    mini_wiki_path = pelican.settings.get("MINI_WIKI_PATH", "")

    if mini_wiki == True:
        logger.debug("MiniWiki is enabled.")
        if mini_wiki_path[-1] != "/":
            logger.warning("MINI_WIKI_PATH does not end with a forward slash (/).")
        else:
            logger.debug(f"MINI_WIKI_PATH is '{mini_wiki_path}'.")

def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(check_settings)
    signals.page_generator_write_page.connect(set_wiki_template)
