def initRuntimeEnvironment(start_script):
    """
    初始化运行环境
    :param start_script: 启动脚本路径
    :return:
    """
    import os
    import sys
    import site

    # 重定向输出流到控制台窗口
    try:
        fd = os.open('CONOUT$', os.O_RDWR | os.O_BINARY)
        fp = os.fdopen(fd, 'w')
        sys.stdout = fp
        sys.stderr = fp
    except Exception as e:
        fp = open(os.devnull, 'w')
        sys.stdout = fp
        sys.stderr = fp

    def MessageBox(msg, info='Message'):
        import ctypes
        ctypes.windll.user32.MessageBoxW(None, str(msg), str(info), 0)
        return 0

    # 初始化工作目录和Python搜索路径
    script = os.path.abspath(start_script)  # 启动脚本.py的路径
    home = os.path.dirname(script)  # 工作目录
    os.chdir(home)  # 重新设定工作目录
    for n in ['.', '.site-packages']:  # 将模块目录添加到python搜索路径中
        path = os.path.abspath(os.path.join(home, n))
        if os.path.exists(path):
            site.addsitedir(path)

    # 初始化Qt搜索路径，采用相对路径，避免中文路径编码问题
    try:
        from PySide6.QtCore import QCoreApplication
        QCoreApplication.addLibraryPath('./.site-packages/Pyside2/plugins')
    except Exception as e:
        print(e)
        MessageBox(f'addLibraryPath fail!\n\n{e}')
        sys.exit(0)
    print("Init runtime environment complete!")



if __name__ == '__main__':
    initRuntimeEnvironment(__file__)  # 初始化运行环境

    from gui import app_logic
    backendClick = app_logic.AppLogic("..\\config.ini")
    backendClick.main()
