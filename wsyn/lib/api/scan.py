# coding: utf-8
import copy
import re
from collections import OrderedDict
from typing import Any, Dict, Iterable, List, Optional

from wsyn.lib.utils import iter_modules

from .target import Response, Target


class Scan():
    '''wsyn 扫描接口'''

    def __init__(self, dirs: List, target: str = ''):
        self.__plugins = self.__plugin_yielder(dirs)
        self.__scan_report = ScanReport()
        if target:
            self.__target = Target(target)

    def __plugin_yielder(self, dirs: List, name: str = "Plugin"):
        '''
        :param dirs: 插件目录列表
        :param name: 对象名称
        '''
        for dir_path in dirs:
            for (mod, __dir_path, __filename) in iter_modules(dir_path):
                try:
                    obj = getattr(mod, name)
                    yield obj
                except Exception as err:
                    # LOG.debug("获取属性Plugin失败：%s" % err)
                    print(err)
                    pass

    def run(self):
        '''扫描所有插件'''
        target = copy.deepcopy(self.__target)
        for plugin in self.__plugins:
            r = plugin().run(target)
            report_result = self.__scan_report.merge_r(r)
        if not report_result is None:
            print(report_result)
        else:
            print("no names!")


class ScanReport:
    '''wsyn 输出结果'''

    def __init__(self):
        self.__result = OrderedDict()

    def merge_r(self, r: Dict[str, Any]):
        '''合并扫描结果'''
        if isinstance(r, Dict) and r != {}:
            if r.get('has', False):
                self.__result.setdefault('result', {})
                _tmp = {'name': r['name']}
                self.__result['result'].setdefault(r['ptype'], []).append(_tmp)
                return self.__result['result']
