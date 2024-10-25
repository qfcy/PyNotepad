import sys,os
from setuptools import setup

try:
    os.chdir(os.path.split(__file__)[0])
except OSError:pass

try:
    long_desc=open("README.rst",encoding="utf-8").read()
except OSError:
    long_desc=notepad.__doc__

try:os.rename("pynotepad.pyw","pynotepad.py") # 重命名pyw文件为py文件，便于打包
except OSError:pass
import pynotepad

setup(
    name='pynotepad',
    version=pynotepad.__version__,
    description="A featured open-source text editor using tkinter.一款功能齐全的tkinter文本编辑器程序。",
    long_description=long_desc,
    author=pynotepad.__author__,
    author_email=pynotepad.__email__,
    url="https://github.com/qfcy/pynotepad",
    py_modules=['pynotepad'], #这里是代码所在的文件名称
    keywords=["text","editor","notepad","tkinter","pynotepad","文本编辑器"],
    classifiers=[
        'Programming Language :: Python',
        "Topic :: Text Editors",
        "Topic :: Software Development :: User Interfaces",
        "Natural Language :: Chinese (Simplified)"],
    requires=["chardet","windnd"]
)
try:os.rename("pynotepad.py","pynotepad.pyw")
except OSError:pass
