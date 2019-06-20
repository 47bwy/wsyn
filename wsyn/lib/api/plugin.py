# coding: utf-8
from abc import ABCMeta, abstractproperty
from enum import Enum
from typing import Any, Dict, List, Optional

from .target import Target


class PluginType(Enum):
    '''插件类型'''
    others = 0
    cms = 1


class ABPlugin(metaclass=ABCMeta):

    @abstractproperty
    def name(self) -> str:
        '''插件名称'''

    @abstractproperty
    def ptype(self) -> PluginType:
        '''插件类型'''

    @abstractproperty
    def fingerprints(self) -> List:
        '''插件指纹'''

    def make_match(self, target: Target, match: Dict[str, str],):
        '''
        return :
            {'has': True}
        '''
        r = {}
        search_context = target.response.text

        # text
        if match.get('text', ''):
            if search_context.find(match["text"]) != -1:
                r['has'] = True
        return r

    def run(self, target: Target):
        '''
        return :
             { 'has': True, 'name': self.name, 'ptype': self.ptype.name}
        '''
        r = {}
        # fingerprints
        for fp in self.fingerprints:
            _r = self.make_match(target, fp)
        if _r:
            r.update(_r)

        if r.get('has', False):
            r['name'] = self.name
            r['ptype'] = self.ptype.name
        return r
