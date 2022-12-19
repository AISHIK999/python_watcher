# Python watcher

## Description:
* A python script that views twitch streams
* Made using [Selenim](https://www.selenium.dev/)
* Default browser set as [Microsoft Edge](https://www.microsoft.com/en-us/edge) and uses [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). [VeePN](https://chrome.google.com/webstore/detail/free-vpn-for-chrome-vpn-p/majdfhpaihoncoakbjgbdhglocklcgno?hl=en) extension is used.

## Instructions:
* Make sure [Python](https://www.python.org/) is installed in the system.
* Install selenium using
```python
pip install selenium
```
* Clone the repository :<br>
```bash 
git clone https://github.com/AISHIK999/python_viewbot.git
```
* Move into the directory:<br>
```bash 
cd python_viewbot
```
* Give executable permissions to the edgedriver:<br>
```bash
chmod +x msedgedriver
```
* Make changes to the script:
Open the <code>main.py</code> in a text editor.
Replace the <b>my_channel</b> value assigned to the variable: <b>channel_name</b> and save it.
<br>
Now open the <code>bot.sh</code> file in a text editor and change the active instances and the sleep time as directed by the comments. Save and exit.<br>

* Run the script:
```bash
bash bot.sh
```

# DISCLAIMER:
This script was created only for educational purposes. I am in no way to be held responsible for any kind of damage dealt (public or personal) to someone for using this script. 