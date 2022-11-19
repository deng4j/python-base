"""
open_code(path)：以 'rb' 模式打开提供的文件。将文件内容作为可执行代码。
    path 应当为 str 类型并且是一个绝对路径。
"""
import io

from src.python.tools.GetRootFolder import getRepositoryRootPath

root_paths = getRepositoryRootPath()

f = io.open_code(root_paths + "Python_base/src/resources/file/folder1/code.txt")

code = f.read()

exec(code)
