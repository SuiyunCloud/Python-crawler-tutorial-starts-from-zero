

# 安装

   * conda install selenium 或 pip install selenium
   * 下载浏览器驱动。在 selenium 的 download 页面，Third Party Drivers 处下载对应浏览器驱动，或使用下方链接
        Chrome [driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
        Mozilla Firefox [driver](https://github.com/mozilla/geckodriver/)
        Safari [driver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
   * Linux 和 MacOS 用户下载好之后, 将下载好的”geckodriver”文件放在你的计算机的 “/usr/bin” 或 “/usr/local/bin” 目录。并赋予执行权限，如下所示：
```shell
sudo cp geckodriver /usr/local/bin
sudo chmod +x /usr/local/bin/geckodriver
```

或者在代码中引用文件所在位置，如下：
``python
  from selenium import webdriver
  path="D:\\chromedriver.exe" #替换成geckodriver实际所在目录
  driver=webdriver.Chrome(path)
  driver.get("http://www.yahoo.com")
  driver.close()
  driver.quit()
``


## 安装火狐浏览器插件Katalon Recorder

    该组件用于录制用户在浏览器中的操作，并生成python等代码，省去了自己写代码的麻烦。类似按键精灵，可以参考莫烦的视频教程。

    工具>附加组件>搜索 Katalon Recorder >安装
    在需要录制的页面打开 Katalon Recorder ，点击录制，然后完成你想录制的操作，点击停止录制，导出代码。
