from wsyn import ABPlugin, PluginType

class Plugin(ABPlugin):
    name = "WordPress"
    ptype = PluginType.cms

    fingerprints = [
        {"text": "WordPress"}
    ]