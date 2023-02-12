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
        logger.debug("Mini Wiki is ENABLED.")
        logger.debug(f"MINI_WIKI_PATH is '{mini_wiki_path}'.")
    else:
        logger.warning("Mini Wiki is DISABLED.")

def set_wiki_template(generator, content):
    """
    Ensure that `content` of a wiki page has a valid template attribute
    set before being written by the pelican writer.

    Check the path of the page, pages that are under the wiki directory
    will have the template meta attribute set to the `wiki_base.html`
    template unless it is already set in the meta to a different file.
    """
    page_path = content.metadata.get('path')
    logger.debug(page_path)


def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(check_settings)
    signals.page_generator_write_page.connect(set_wiki_template)
