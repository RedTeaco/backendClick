项目介绍
=
在捕获窗口后，便可以将被捕获的窗口放置于后台（但不要最小化），此时配置好的鼠标/键盘事件可以发送给在后台的窗口。  
开发原因：用于Minecraft/PalWorld或其他游戏的单一重复动作，但注意，**请不要将本项目用于网游作弊**。  
**软件GUI截图：**  
  
![GUI](https://github.com/RedTeaco/backendClick/assets/88274143/cf211851-b7ed-468d-8365-9eb33bb9c48e)

  
**原理：** 利用PostMessageW函数向目标窗口发送指定的键盘/鼠标事件信息

使用说明
=
仅在**Windows**系统上测试  
本项目为手动打包，可在release中选择 **backend_click.zip** 下载后解压运行.  
界面左侧为鼠标事件的列表，界面右侧为键盘事件的列表，可根据需求自行添加，支持同时按下多个按键以及同时点击鼠标左右键。  
可后台发送鼠标/键盘事件到指定窗口

项目环境
=
本项目使用Python3.11,PySide6.6.1
若下载release中的版本，则最小化项目环境已经配备，可直接运行。

鸣谢：
=
使用Pyside6制作图形化界面
本项目使用经由[hiroi-sora](https://github.com/hiroi-sora/PyStand-Sora/commits?author=hiroi-sora)改造的[PyStand-Sora](https://github.com/hiroi-sora/PyStand-Sora),原项目地址:[PyStand](https://github.com/skywind3000/PyStand)
