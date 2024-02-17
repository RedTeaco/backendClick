项目介绍
=
在捕获窗口后，便可以将该窗口放置于后台（但不要最小化），此时配置好的鼠标/键盘事件可以发送给在后台的窗口。  
开发原因：用于Minecraft/PalWorld或其他游戏的单一重复动作，但注意，**请不要将本项目用于网游作弊**。  
**软件GUI截图：**  
  
  ![GUI](https://github.com/EdenLeaf/backendClick/assets/88274143/8df143c0-0903-4e31-898b-4732be4c1ba1)

  
**原理：** 利用PostMessageW函数向目标窗口发送指定的键盘/鼠标事件信息

源代码中,package/Appdata中的代码为打包时所用的代码，如需直接用python源文件打开应用，则只需使用最外层的application.py

使用说明
=
仅在Windows系统上测试
本项目手动打包，可在release中选择 **backend_click.zip** 直接下载后解压运行.
可后台发送鼠标/键盘事件到指定窗口

项目环境
=
本项目使用Python3.11版本
若下载release中的版本，则最小化项目环境已经配备，无需担心因缺少环境而无法运行的情况

鸣谢：
=
使用Pyside6制作图形化界面
本项目使用经由[hiroi-sora](https://github.com/hiroi-sora/PyStand-Sora/commits?author=hiroi-sora)改造的[PyStand-Sora](https://github.com/hiroi-sora/PyStand-Sora),原项目地址:[PyStand](https://github.com/skywind3000/PyStand)
