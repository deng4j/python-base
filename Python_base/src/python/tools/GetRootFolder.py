import os

"""
获取项目根目录工具
"""


def getContentRootPath(projectPath='Python_base'):
    """
    请使用path_from_content_root拼接
    :param projectPath:
    :return: contentRootPath
    """
    if projectPath is None or projectPath.isspace():
        raise Exception("项目名为空")
    curPath = os.getcwd()
    contentRootPath = curPath[:curPath.find(projectPath) + len(projectPath) + 1]
    return contentRootPath


def getRelativePathsByContentRoot(projectPath, path_from_content_root):
    if projectPath is None or projectPath.isspace():
        raise Exception("项目名为空")
    curPath = os.getcwd()
    rootPath = curPath[:curPath.find(projectPath) + len(projectPath) + 1]
    dataPath = rootPath + path_from_content_root
    return dataPath


def getRepositoryRootPath(projectPath='Python_base'):
    """
    请使用ppath_from_repository_root拼接
    :param projectPath:
    :return: rootPath
    """
    if projectPath is None or projectPath.isspace():
        raise Exception("项目名为空")
    curPath = os.getcwd()
    rootPath = curPath[:curPath.find(projectPath)]
    return rootPath


def getRelativePathsByRepositoryRoot(projectPath, path_from_repository_root):
    if projectPath is None or projectPath.isspace():
        raise Exception("项目名为空")
    if path_from_repository_root is None or path_from_repository_root.isspace():
        raise Exception("路径为空")
    curPath = os.getcwd()
    rootPath = curPath[:curPath.find(projectPath)]
    dataPath = rootPath + path_from_repository_root
    return dataPath


if __name__ == '__main__':
    contentPath = getContentRootPath()
    print(contentPath)

    contentRoot = getRelativePathsByContentRoot('Python_base', 'src/resources/file/folder1/print.txt')
    print(contentRoot)  # 获取相对路径

    repositoryPath = getRepositoryRootPath()
    print(repositoryPath)

    repositoryRoot = getRelativePathsByRepositoryRoot('Python_base',
                                                      'Python_base/src/resources/file/folder1/print.txt')
    print(repositoryRoot)  # 获取相对路径
