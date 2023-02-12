import logging
from pelican import signals

logger = logging.getLogger(__name__)

def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(check_settings)
