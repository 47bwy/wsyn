# coding: utf-8
import os

from wsyn import Scan, wsyn_cmd_parser

ENV = 'PluginDirs'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_PATH = [os.path.join(BASEDIR, path) for path in ["plugins"]]

def main():
    args = wsyn_cmd_parser().parse_args()
    PLUGINS_DIRS = args.plugin_dirs or os.environ.get(ENV, DEFAULT_PATH)
    scan = Scan(dirs=PLUGINS_DIRS, target=args.url)
    scan.run()

if __name__ == "__main__":
    main()