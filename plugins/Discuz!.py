from wsyn import ABPlugin, PluginType

class Plugin(ABPlugin):
    name = "Discuz!"
    ptype = PluginType.cms

    fingerprints = [
        {"text": "Powered by Discuz!"}
    ]