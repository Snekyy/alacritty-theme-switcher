# alacritty-theme-switcher
Simple theme switcher for Alacritty terminal emulator

## Installation ##

1. Clone repository
2. Install required modules 
```bash
pip3 install -r requirements.txt
```
3. Create themes directory in alacritty config folder
```bash
mkdir ~/.config/alacritty/themes
```
4. Create some themes
```
touch ~/.config/alacritty/themes/<theme-name>.yml
```
This file should contain only "colors" part of alacritty.yml:</br>
Like in [nord theme](./themes/nord.yml):
## Usage ## alacritty-theme-switcher.py [-h] [-s theme] [-l] [-b]</br>
optional arguments:</br>
  -h, --help                    show this help message and exit</br>
  -s theme, --set-theme theme   set theme</br>
  -l, --list-themes             show available themes</br>
  -b, --backup                  save current config to .bak file</br>

To list themes in ~/.config/alacritty/themes/ :
```bash
python3 alacritty-theme-switcher -l
```
To set some theme:
```bash
python3 alacritty-theme-switcher -s nord
```
Config changes will take effect immediately:</br>
![](https://media.giphy.com/media/POwBlPAJZ7ZMhrj7s3/giphy.gif)


Themes were taken from - https://github.com/eendroroy/alacritty-theme
