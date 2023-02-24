# 简介

[Getting Started - pip documentation v23.0.dev0 (pypa.io)](https://pip.pypa.io/en/latest/getting-started/)

Python有两个著名的包管理工具easy_install和pip。在Python2.7的安装包中，easy_install是默认安装的，而pip需要我们手动安装。

随着Python版本的提高，easy_install已经逐渐被淘汰，但是一些比较老的第三方库，在现在仍然只能通过easy_install进行安装。

目前，pip已经成为主流的安装工具，自Python2 >=2.7.9或者Python3.4以后默认都安装有pip。

pip也有pip、pip2、pip3之分。pip是从属于Python的，对应的pip负责给对应的Python安装第三方模块。

我们不要关心pip后面跟的数字，核心的问题是这个pip命令对应的是哪个Python解释器。

# 安装pip

1. 使用easy_install安装： 各种进入到easy_install脚本的目录下，然后运行easy_inatall pip

2. 使用get-pip.py安装： 在下面的url下载get-pip.py脚本 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py然后运行：python get-pip.py 这个脚本会同时安装setuptools和wheel工具。

3. 在linux下使用包管理工具安装pip： 例如，ubuntu下：sudo apt-get install python-pip。Fedora系下：sudo yum install python-pip
4. 在windows下安装pip： 在......Python\Python38\Scripts下运行easy_install pip进行安装。

刚安装完毕的pip可能需要先升级一下自身： 在Linux或masOS中：pip install -U pip 在windows中：python -m pip install -U pip



# pip命令

路径和版本：pip -V

帮助：pip -helpe 

## pip install

从以下位置安装软件包：

- PyPI (and other indexes) using requirement specifiers.
- VCS project urls.
- Local project directories.
- Local or remote source archives.

```css
python -m pip install [options] <requirement specifier> [package-index-options] ...
python -m pip install [options] -r <requirements file> [package-index-options] ...
python -m pip install [options] [-e] <vcs project url> ...
python -m pip install [options] [-e] <local project path> ...
python -m pip install [options] <archive url/path> ...
```

Options：

- **-r**, **--requirement** <file>：根据依赖文件批量安装库，该选项可以重复添加
- **-c**, **--constraint** <file>：使用给定的约束文件约束版本，该选项可以重复添加
- **--no-deps**：不安装包的任何依赖项
- **--pre**：包含预发布版本和开发版本，默认只会包行稳定的版本
- **-e**, **--editable** <path/url>：在可编辑模式下从一个本地的项目路径或 VCS URL 中安装一个项目 ( 例如，setuptools 的 「 开发者模式 」 )
- **--dry-run**：实际上不要安装任何东西，只需打印会是什么。可以与 --ignore-install 结合使用以“解决”需求。
- **-t**, **--target** <dir>：将包安装到指定目录，默认情况下，该选项并不会覆盖 `<dir>` 目录中已经存在的文件或目录，但可以使用 `--upgrade` 选项将已经存在的包更新到最新的版本
- **--platform** <platform>：仅使用与<平台>兼容的wheels。默认为正在运行的系统的平台。多次使用此选项可指定目标解释器支持的多个平台。
- **--python-version** <python_version>：用于wheel和“Requires-Python”的Python解释器版本 兼容性检查。默认为interpreter的版本。最多可以使用三个点分隔来指定版本（例如，“3”表示 3.0.0，“3.7”表示 3.7.0，或“3.7.3”）。major-minor版本也可以作为不带点的字符串给出（例如，“37”表示 3.7.0）。
- **--implementation** <implementation>：仅使用与 Python 实现<实现>兼容的wheels，例如“pp”、“jy”、“cp”或“ip”。如果未指定，则使用当前的解释器实现。使用“py”强制实现无关的wheels。
- **--abi** <abi>：仅使用与Python abi<abi>兼容的wheels，例如“pypy_41”。如果未指定，则使用当前解释器 abi 标记。多次使用此选项可指定目标解释器支持的多个 abis。通常，使用此选项时需要指定 --implementation、--platform 和 --python-version。
- **--user**：将所有的包安装到我们的平台的Python 用户安装目录，通常为 `~/.local/` 或 Windows 上为 `%APPDATA%Python` ( 更多详细信息，可以查看 Python 文档中的 `site.USER_BASE` 部分 )
- **--root** <dir>：安装与此备用根目录 `<dir>` 包含的所有内容
- **--prefix** <dir>：安装时，`lib` 、`bin` 和其它顶级目录的存放目录，也就是这些目录的路径前缀
- **--src** <dir>：用于存放迁出的可编辑项目在虚拟环境中，默认的目录为 `<venv path>/src`， 在全局安装中，默认的目录为 `<current dir>/src`
- **-U**, **--upgrade**：更新所有指定的包到最新的可用版本。 依赖项的处理取决于所使用的升级策略
- **--upgrade-strategy** <upgrade_strategy>：确定应如何处理依赖项升级 ( 默认值：「 仅在需要时 」)

  - `eager` - 无论当前安装的版本是否满足升级包的要求，都会升级依赖项
  - `only-if-needed` - 仅在不满足升级包的要求时才升级
- **--force-reinstall**：重新安装所有的包，即使它们已经是最新的版本
- **-I**, **--ignore-installed**：忽略已经安装的包 ( 用重新安装取代 )
- **--ignore-requires-python**：忽略 Requires-Python 信息
- **--no-build-isolation**：在构建现代的源代码分发包是禁用隔离，如果使用了此选项，则必须已安装 PEP518 规定的构建依赖项
- **--use-pep517**：使用 PEP 517 构建源代码发行版（使用 --no-use-pep517 强制旧行为）。
- **--check-build-dependencies**：使用 PEP517 时检查构建依赖项。
- **--config-settings** <settings>：要传递到 PEP 517 生成后端的配置设置。设置采用 KEY=VALUE 的形式。使用多个 --config-settings 选项将多个密钥传递到后端。
- **--install-option** <options>：安装时提供给 `setup.py` 安装命令的额外参数( 使用方法类似于 `--install-option="--install-scripts=/usr/local/bin"` )。可以使用多个 `--install-option` 选项将多个选项传递给 `setup.py install`，如果你使用带有目录路径的选项，请确保使用绝对路径
- **--global-option** <options>：在 `bdist_wheel` 命令之前提供给 `setup.py` 调用的额外全局选项
- **--compile**：将 Python 源代码编译为 bytecode
- **--no-compile**：不要将 Python 源代码编译为 `bytecode`
- **--no-warn-script-location**：当安装脚本不在 `PATH` 路径中时不要发出警告
- **--no-warn-conflicts**：出现已损坏的依赖关系时不要发出警告
- **--no-binary** <format_control>：不使用二进制包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：

  - `:all:` ：禁用所有二进制包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--only-binary** <format_control>：不使用源代码包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：
  - `:all:` ：禁用所有源代码包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--prefer-binary**：首选较旧的二进制包而不是较新的源包。
- **--require-hashes**：对于可重复安装，需要根据哈希值来检查每个需求，如果需求文件中的任何一项包含了 `--hash` 选项，则隐式包含此选项
- **--progress-bar** <progress_bar>：用于指定要显示的进度条类型，可选项有：
  - on、ascii、off、pretty、emoji，默认为on
  
- **--root-user-action** <root_user_action>：如果 pip 以根用户身份运行，则执行操作。默认情况下，将显示一条警告消息。
- **--report** <file>：生成一个 JSON 文件，描述 pip 如何安装提供的需求。可以与--dry-run和--ignore-install结合使用，以“解决”需求。当 - 用作文件名时，它会写入标准输出。写入标准输出时，请与 --quiet 选项结合使用，以避免将 pip 日志记录输出与 JSON 输出混合使用。
- **--no-clean**：不要清空构建目录
- **-i**, **--index-url** <url>：Python 包索引的基础 URL 地址，默认为 https://pypi.org/simple
- **--extra-index-url** <url>：除了 `--index-url` 之外的附加的 Python 包索引 URL，规则和 `--index-url` 一样
- **--no-index**：忽略包索引，使用 `--find-links` 指定的 URL
- **-f**, **--find-links** <url>：如果提供的 URL 或路径链接到一个 html 文件，则会解析该 html 文件以获取归档。如果是本地目录，或 `file://url` 指向的是一个目录，那么就在该目录中查找归档。
- **--process-dependency-links**：启用依赖关系链接的处理
- -b, --build <dir>：用于存放解压缩的包和构建的包。请注意，初始构建仍发生在临时目录中。可以通过适当地设置 `TMPDIR` 环境变量 （ Windows上的 `TEMP` ) 来控制临时目录的位置。如果使用了该参数，当构建发生故障时，并不会清空构建目录

```css
import platform
print(platform.architecture())  # 查看平台支持

Win32 -> 指的就是Windows系统；
64 bit- > 指的是Windows是64位的；
AMD64 -> 指的就是 CPU是x64的  
```

```css
避免没配置python环境变量：python -m pip install pip==22.2.2
指定安装位置（最好别用，有很多文件丢失）：pip install django -t=D:\development\venv3.8.5\Lib\site-packages
安装包：pip install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
安装包：pip install Flask-WTF-0.10.0.tar.gz
升级pip：pip install -U pip
安装稳定的包：pip install --pre SomePackage
从连接中安装：pip install SomePackage -i https://mirrors.aliyun.com/pypi/simple/
添加用户信息安装，防止sip机制不允许命令行写入内容到系统目录：pip3 install jupyter --user
不验证SSL：pip --trusted-host pypi.python.org install SomePackage
```

使用pip安装特定版本的package，默认安装最新版本，通过使用==, >=, <=, >, <来指定一个版本号，如：pip install 'Markdown<2.0' 或 pip install 'Markdown>2.0,<2.0.3

| Operator | Description                                                  | Example                                           |
| -------- | ------------------------------------------------------------ | ------------------------------------------------- |
| `>`      | Any version greater than the specified version.              | `>3.1`: any version greater than `3.1`.           |
| `<`      | Any version less than the specified version.                 | `<3.1`: any version less than `3.1`.              |
| `<=`     | Any version less than or equal to the specified version.     | `<=3.1`: any version less than or equal to `3.1`. |
| `>=`     | Any version greater than or equal to the specified version.  | `>=3.1`: version `3.1` and greater.               |
| `==`     | Exactly the specified version.                               | `==3.1`: only `3.1`.                              |
| `!=`     | Any version not equal to the specified version.              | `!=3.1`: any version other than `3.1`.            |
| `~=`     | Any compatible1 version.                                     | `~=3.1`: any version compatible1 with `3.1`.      |
| `*`      | Can be used at the end of a version number to represent *all*. | `==3.1.*`: any version that starts with `3.1`.    |

在没有指定安装路径时，默认安装在pip所在在环境下。

## pip uninstall

卸载软件包，例外：

- 纯distutils软件包安装，其中 不留下任何元数据来确定安装了哪些文件。`python setup.py install`
- 脚本包装器安装者。`python setup.py develop`

```css
python -m pip uninstall [options] <package> ...
python -m pip uninstall [options] -r <requirements file> ...
```

Options:

- **-r**, **--requirement** <file>：卸载给定需求文件中列出的所有软件包。此选项可以多次使用。
- **-y**, **--yes**：不要求确认卸载删除。
- **--root-user-action** <root_user_action>：如果 pip 以根用户身份执行操作。默认情况下，将显示一条警告消息。

```css
卸载包：pip uninstall package_name1 package_name2
```



## pip inspect

检查 Python 环境的内容并生成 JSON 格式的报告。

```css
python -m pip inspect [options]
```

Options：

- **--local**：如果在具有全局访问权限的 virtualenv 中，请不要列出全局安装的软件包。
- **--user**：仅输出安装在用户站点中的包。
- **--path** <path>：限制为列出包的指定安装路径（可以多次使用）。

## pip list

列出已安装的软件包，包括可编辑的软件包。包按不区分大小写的排序顺序列出。

```css
python -m pip list [options]
```

Options：

- **-o**, **--outdated**：列出过时的软件包
- **-u**, **--uptodate**：列出最新软件包
- **-e**, **--editable**：列出可编辑的项目
- **-l**, **--local**：如果在具有全局访问权限的 virtualenv 中，请不要列出全局安装的软件包。
- **--user**：仅输出安装在用户站点中的包。
- **--path** <path>：限制为列出包的指定安装路径（可以多次使用）。
- **--pre**：包括预发布版本和开发版本。默认情况下，pip 只查找稳定版本。
- **--format** <list_format>：选择输出格式：columns (default), freeze,  json
- **--not-required**：列出不是已安装软件包的依赖项的包。
- **--exclude-editable**：从输出中排除可编辑包。
- **--include-editable**：包括输出中的可编辑包。
- **--exclude** <package>：从输出中排除指定的包
- **-i**, **--index-url** <url>：Python 包索引的基本 URL（默认https://pypi.org/simple）。这应该指向符合 PEP 503（简单存储库 API）的存储库或以相同格式布局的本地目录。
- **--extra-index-url** <url>：除了 --index-url 之外，还要使用的包索引的额外 URL。应遵循与 --index-url 相同的规则。
- **--no-index**：忽略包索引（只查看 --find-links URL）。
- **-f**, **--find-links** <url>：如果是 html 文件的 URL 或路径，则解析指向存档的链接，例如 sdist （.tar.gz） 或 wheel （.whl） 文件。如果本地路径或[file://](file:///) URL 是目录，则在目录列表中查找存档。不支持指向 VCS 项目 URL 的链接。

```css
列出已经安装的库：pip list
检查哪些包需要更新：pip list --outdated
按列表格式显示库列表：pip list --outdated --format columns
```



## pip show

显示一个或多个已安装软件包的信息。

```css
python -m pip show [options] <package> ...
```

Options：

- **-f**, **--files**：显示每个软件包的已安装文件的完整列表。

```css
简略查看某个已安装包：pip show sphinx
详细查看某个已安装包：pip show --files package_name
```

## pip freeze

以需求格式输出已安装的包。包按不区分大小写的排序顺序列出。

```css
python -m pip freeze [options]
```

Options：

- **-r**, **--requirement** <file>：将安装包的顺序及其注释输出到给定文件中。此选项可以多次使用。
- **-l**, **--local**：如果在具有全局访问权限的 virtualenv 中，则不要输出全局安装的软件包。
- **--user**：仅输出安装在用户站点中的包。
- **--path** <path>：限制为列出包的指定安装路径（可以多次使用）。
- **--all**：不要跳过这些包setuptools, wheel, pip, distribute
- **--exclude-editable**：从输出中排除可编辑包。
- **--exclude** <package>：从输出中排除指定的包

```css
输出已安装的包到控制台：python -m pip freeze
将已经安装的库列表保存到文本文件中：pip freeze > requirements.txt
```

## pip check

验证已安装的软件包是否具有兼容的依赖项。

```css
python -m pip check [options]
```

```css
如果所有依赖项都兼容：No broken requirements found.
如果缺少包：pyramid 1.5.2 requires WebOb, which is not installed.
如果包的版本错误：pyramid 1.5.2 has requirement WebOb>=1.3.1, but you have WebOb 0.8.
```

## pip download

从以下位置下载软件包：

- PyPI (and other indexes) using requirement specifiers.
- VCS project urls.
- Local project directories.
- Local or remote source archives.

pip 还支持从“需求文件”下载，提供 指定要下载的整个环境的简单方法。

```css
python -m pip download [options] <requirement specifier> [package-index-options] ...
python -m pip download [options] -r <requirements file> [package-index-options] ...
python -m pip download [options] <vcs project url> ...
python -m pip download [options] <local project path> ...
python -m pip download [options] <archive url/path> ...
```

Options：

- **-r**, **--requirement** <file>：根据依赖文件批量安装库，该选项可以重复添加
- **-c**, **--constraint** <file>：使用给定的约束文件约束版本，该选项可以重复添加
- **--no-deps**：不安装包的任何依赖项
- **--global-option** <options>：在 `bdist_wheel` 命令之前提供给 `setup.py` 调用的额外全局选项
- **--no-binary** <format_control>：不使用二进制包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：
  - `:all:` ：禁用所有二进制包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--only-binary** <format_control>：不使用源代码包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：
  - `:all:` ：禁用所有源代码包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--prefer-binary**：首选较旧的二进制包而不是较新的源包。
- **--src** <dir>：用于存放迁出的可编辑项目在虚拟环境中，默认的目录为 `<venv path>/src`， 在全局安装中，默认的目录为 `<current dir>/src`
- **--pre**：包含预发布版本和开发版本，默认只会包行稳定的版本
- **--require-hashes**：对于可重复安装，需要根据哈希值来检查每个需求，如果需求文件中的任何一项包含了 `--hash` 选项，则隐式包含此选项
- **--no-build-isolation**：在构建现代的源代码分发包是禁用隔离，如果使用了此选项，则必须已安装 PEP518 规定的构建依赖项
- **--use-pep517**：使用 PEP 517 构建源代码发行版（使用 --no-use-pep517 强制旧行为）。
- **--check-build-dependencies**：使用 PEP517 时检查构建依赖项。
- **--ignore-requires-python**：忽略 Requires-Python 信息
- **-d**, **--dest** <dir>：将软件包下载到 <dir>。
- **--platform** <platform>：仅使用与<平台>兼容的wheels。默认为正在运行的系统的平台。多次使用此选项可指定目标解释器支持的多个平台。
- **--python-version** <python_version>：用于wheel和“Requires-Python”的Python解释器版本 兼容性检查。默认为interpreter的版本。最多可以使用三个点分隔来指定版本（例如，“3”表示 3.0.0，“3.7”表示 3.7.0，或“3.7.3”）。major-minor版本也可以作为不带点的字符串给出（例如，“37”表示 3.7.0）。
- **--implementation** <implementation>：仅使用与 Python 实现<实现>兼容的wheels，例如“pp”、“jy”、“cp”或“ip”。如果未指定，则使用当前的解释器实现。使用“py”强制实现无关的wheels。
- **--abi** <abi>：仅使用与Python abi<abi>兼容的wheels，例如“pypy_41”。如果未指定，则使用当前解释器 abi 标记。多次使用此选项可指定目标解释器支持的多个 abis。通常，使用此选项时需要指定 --implementation、--platform 和 --python-version。
- **--no-clean**：不要清空构建目录
- **-i**, **--index-url** <url>：Python 包索引的基础 URL 地址，默认为 https://pypi.org/simple
- **--extra-index-url** <url>：除了 `--index-url` 之外的附加的 Python 包索引 URL，规则和 `--index-url` 一样
- **--no-index**：忽略包索引，使用 `--find-links` 指定的 URL
- **-f**, **--find-links** <url>：如果提供的 URL 或路径链接到一个 html 文件，则会解析该 html 文件以获取归档。如果是本地目录，或 `file://url` 指向的是一个目录，那么就在该目录中查找归档。

```css
下载安装包：pip download SomePackage

从url下载安装包到指定目录：pip download \
	--no-index --find-links=/tmp/wheelhouse \
	-d /tmp/otherwheelhouse SomePackage

下载指定信息的安装包：pip download \
   --only-binary=:all: \
   --platform macosx_10_10_x86_64 \
   --python-version 27 \
   --implementation cp \
   SomePackage
```

## pip wheel

根据您的要求和依赖关系构建wheel

```css
python -m pip wheel [options] <requirement specifier> ...
python -m pip wheel [options] -r <requirements file> ...
python -m pip wheel [options] [-e] <vcs project url> ...
python -m pip wheel [options] [-e] <local project path> ...
python -m pip wheel [options] <archive url/path> ...
```

Options：

- **-w**, **--wheel-dir** <dir>：将wheel构建到 <dir>中，其中默认为当前工作目录。
- **--no-binary** <format_control>：不使用二进制包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：
  - `:all:` ：禁用所有二进制包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--only-binary** <format_control>：不使用源代码包，该选项可以重复添加，每增加一个就会自增当前的值，可选的值有：
  - `:all:` ：禁用所有源代码包
  - `:none:` ：清空集合，或者使用逗号之间的一个或多个包名称
- **--prefer-binary**：首选较旧的二进制包而不是较新的源包。
- **--no-build-isolation**：在构建现代的源代码分发包是禁用隔离，如果使用了此选项，则必须已安装 PEP518 规定的构建依赖项
- **--use-pep517**：使用 PEP 517 构建源代码发行版（使用 --no-use-pep517 强制旧行为）。
- **--check-build-dependencies**：使用 PEP517 时检查构建依赖项。
- **-c**, **--constraint** <file>：使用给定的约束文件约束版本，该选项可以重复添加
- **-e**, **--editable** <path/url>：在可编辑模式下从一个本地的项目路径或 VCS URL 中安装一个项目 ( 例如，setuptools 的 「 开发者模式 」 )
- **-r**, **--requirement** <file>：根据依赖文件批量安装库，该选项可以重复添加
- **--src** <dir>：用于存放迁出的可编辑项目在虚拟环境中，默认的目录为 `<venv path>/src`， 在全局安装中，默认的目录为 `<current dir>/src`
- **--ignore-requires-python**：忽略 Requires-Python 信息
- **--no-deps**：不安装包的任何依赖项
- **--progress-bar** <progress_bar>：指定是否应使用进度条[on, off] (default: on)
- **--no-verify**：不要验证内置是否有效。
- **--config-settings** <settings>：要传递到 PEP 517 生成后端的配置设置。设置采用 KEY=VALUE 的形式。使用多个 --config-settings 选项将多个密钥传递到后端。
- **--build-option** <options>：要提供给的额外参数给 ‘setup.py bdist_wheel’
- **--global-option** <options>：在安装或bdist_wheel命令之前提供给 setup.py 调用的额外全局选项。
- **--pre**：包括预发布版本和开发版本。默认情况下，pip 只查找稳定版本。
- **--require-hashes**：对于可重复安装，需要根据哈希值来检查每个需求，如果需求文件中的任何一项包含了 `--hash` 选项，则隐式包含此选项
- **--no-clean**：不要清空构建目录
- **-i**, **--index-url** <url>：Python 包索引的基本 URL（默认https://pypi.org/simple）。这应该指向符合 PEP 503（简单存储库 API）的存储库或以相同格式布局的本地目录。
- **--extra-index-url** <url>：除了 `--index-url` 之外的附加的 Python 包索引 URL，规则和 `--index-url` 一样
- **--no-index**：忽略包索引，使用 `--find-links` 指定的 URL
- **-f**, **--find-links** <url>：如果提供的 URL 或路径链接到一个 html 文件，则会解析该 html 文件以获取归档。如果是本地目录，或 `file://url` 指向的是一个目录，那么就在该目录中查找归档。

```css
制作wheel：pip wheel --wheel-dir=/tmp/wheelhouse SomePackage
用源代码制作wheel：pip wheel --no-binary SomePackage SomePackage
```

## pip hash

计算本地包存档的哈希。

这些可以在需求文件requirements file中与 --hash 一起使用，以执行可重复性安装。

```css
python -m pip hash [options] <file> ...
```

Options：

- -a, --algorithm <algorithm>：使用其中一个hash算法，sha256, sha384, sha512

```css
查看hash值：pip hash ./pip_downloads/SomePackage-2.2.tar.gz
```

## pip search

根据关键字从url中搜索PyPI包

```css
python -m pip search [options] <query>
```

Options：

- **-i**, **--index** <url>：Python 包索引的基本 URL（默认https://pypi.org/pypi

```css
搜索包：pip search <搜索关键字>
```

## pip cache

查看和管理wheel cache

```css
pip cache dir
pip cache info
pip cache list [<pattern>] [--format=[human, abspath]]
pip cache remove <pattern>
pip cache purge
```

子命令：

- dir: 显示缓存目录。
- info: 显示有关缓存的信息。
- list: 列出存储在缓存中的包的文件名。
- remove: 删除一个或多个缓存
- purge: 从缓存中删除所有项目。

`<pattern>`可以是 glob 表达式或包名称。

Options：

- **--format** <list_format>：输出格式

## pip config

管理local或global配置

```css
pip config [<file-option>] list
pip config [<file-option>] [--editor <editor-path>] edit

pip config [<file-option>] get command.option
pip config [<file-option>] set command.option value
pip config [<file-option>] unset command.option
pip config [<file-option>] debug
```

子命令：

- list: 列出活动配置（或从指定的文件中列出）
- edit: 在编辑器中编辑配置文件
- get: 获取与 command.option 关联的值
- set: 设置command.option=value
- unset: 取消设置与command.option 关联的值
- debug: 列出配置文件及其下定义的值

如果未传递 --user、--global 和 --site 中的任何一个。虚拟环境配置文件处于活动状态并且文件处于活动状态，则使用文件 存在。否则，所有修改都发生在用户文件上违约

Options：

- **--editor** <editor>：用于编辑文件的编辑器。如果未提供，请使用可视化或编辑器环境变量。
- **--global**：仅使用系统范围的配置文件
- **--user**：仅使用用户配置文件
- **--site**：仅使用当前环境配置文件

```css
pip源的选择：
    指定阿里镜像版本：pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

清除镜像源：pip config unset global.index-url

清华：https://pypi.tuna.tsinghua.edu.cn/simple
中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
```



## pip debug

显示调试信息

```css
pip debug <options>
```

Options：

- **--platform** <platform>：仅使用与<平台>兼容的wheel。默认为正在运行的系统的平台。多次使用此选项可指定目标解释器支持的多个平台。
- **--python-version** <python_version>：用于wheel和“Requires-Python”的Python解释器版本 兼容性检查。默认为interpreter的版本。最多可以使用三个点分隔来指定版本（例如，“3”表示 3.0.0，“3.7”表示 3.7.0，或“3.7.3”）。major-minor版本也可以作为不带点的字符串给出（例如，“37”表示 3.7.0）。
- **--implementation** <implementation>：仅使用与 Python 实现<implementation>兼容的wheel，例如“pp”、“jy”、“cp”或“ip”。如果未指定，则使用当前的解释器实现。使用“py”强制实现无关的wheel。
- **--abi** <abi>：仅使用与Python abi<abi>兼容的wheel，例如“pypy_41”。如果未指定，则使用当前解释器 abi 标记。多次使用此选项可指定目标解释器支持的多个 abis。通常，使用此选项时需要指定 --implementation、--platform 和 --python-version。
