# coding: utf-8
import argparse

_wsyn = """
██╗    ██╗███████╗██╗   ██╗███╗   ██╗
_██║    ██║██╔════╝╚██╗ ██╔╝████╗  ██║
_██║ █╗ ██║███████╗ ╚████╔╝ ██╔██╗ ██║
_██║███╗██║╚════██║  ╚██╔╝  ██║╚██╗██║
_╚███╔███╔╝███████║   ██║   ██║ ╚████║
_ ╚══╝╚══╝ ╚══════╝   ╚═╝   ╚═╝  ╚═══╝                                   
"""


def wsyn_cmd_parser():
    '''命令行解释器'''
    parser = argparse.ArgumentParser(
        description=_wsyn, formatter_class=argparse.RawTextHelpFormatter)
    # target
    parser.add_argument("-u", "--url", dest="url", required=False,
                        help="目标 URL (e.g. http://www.wsyn.com/)")
    # plugins dir
    parser.add_argument(
        "-d", "--plugin-dirs", dest="plugin_dirs", required=False,
        help="指定插件目录(多个以逗号隔开)(e.g. -p=PATH1,PATH2...)")
    # plugins
    parser.add_argument(
        "-p", "--plugins", dest="plugins", required=False,
        help="指定插件进行扫描(多个以逗号隔开)(e.g. -p=NAME1,NAME2...)")
    return parser
