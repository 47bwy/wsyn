# coding:utf-8
'''
This code fragment from DaLao @lotuc
'''
import contextlib
import imp
import os
import sys
import uuid
from functools import partial

import urllib3
import requests

# from webdog.lib.log import get_logger

# LOG = get_logger()


def load_file_as_module(dir_or_file, filename=None):
    """加载plugin 为python module

    :param dir_or_file: 当@param{filename}为空时, 将该参数作为文件路径加载
    :param filename:  不为空时,将@param{dir_or_file}的目录下该文件加载
    :return imp.load_source 结果
    """
    if filename is None:
        (dirpath, name) = (os.path.dirname(dir_or_file),
                           os.path.basename(dir_or_file))
    else:
        (dirpath, name) = (dir_or_file, filename)

    pathbase = os.path.basename(name)
    is_compiled = pathbase.endswith('.pyc')
    mod_name = '{}-{}'.format(
        pathbase.rstrip('.pyc') if is_compiled else pathbase.rstrip('.py'),
        str(uuid.uuid4())
    ).replace('.', '_')
    poc_file = os.path.join(dirpath, name)
    try:
        # LOG.debug('Loading %s', poc_file)
        if is_compiled:
            return imp.load_compiled(
                'WdPlugin.{}'.format(mod_name), poc_file)
        else:
            return imp.load_source(
                'WdPlugin.{}'.format(mod_name), poc_file)
    except Exception as err:
        # LOG.warning('Error loading %s %s', poc_file, err)
        print(err)
        raise


def iter_modules(root_dirpath, ignore_dirs=['.venv']):
    """递归加载目录下除了 __init__.py/__init__.pyc/*.pyc 的所有 .py 文件
    加载失败的直接跳过

    :param root_dirpath: 需要加载的根目录
    :param ignore_dirs: 忽略目录名
    :returns (加载的模块, 目录, 文件名)
    """
    for (root, dirs, files) in os.walk(root_dirpath):
        for ignore_dir in ignore_dirs:
            if ignore_dir in dirs:
                dirs.remove(ignore_dir)
        for filename in files:
            if (not filename.endswith('.py') and
                    filename.endswith('.pyc')) \
                    or filename == '__init__.py' \
                    or filename == '__init__.pyc':
                continue
            try:
                mod = load_file_as_module(root, filename)
                yield (mod, root, filename)
            except Exception:
                pass


class partialmethod(partial):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        instance.headers['Accept-Encoding'] = 'deflate'
        return partial(self.func, instance,
                       *(self.args or ()),
                       **(self.keywords or {}))


@contextlib.contextmanager
def no_ssl_verification(session=requests.Session):
    old_request = session.request
    session.request = partialmethod(old_request, verify=False)
    urllib3.disable_warnings()
    yield
    session.request = old_request
