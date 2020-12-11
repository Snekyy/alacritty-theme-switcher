#!/usr/bin/python3

import os
import yaml
from argparse import ArgumentParser

def showThemes():
    # Get all files from themes directory
    themes = os.listdir(path=alacritty_dir + "themes/")
    print(f"Total themes found {len(themes)}:")
    # Del extentions, sort by alphabet, print
    for theme in sorted(map(lambda x: x.split(".")[0], themes)):
        print(theme)

def setTheme(theme):
    if not os.path.exists(alacritty_dir + "themes/" + theme + ".yml"):
        exit(f"error: theme {theme} doesn't exists")
    with open(alacritty_dir + "alacritty.yml", "r") as cfg:
        cfg = yaml.load(cfg, Loader=yaml.Loader)
        del cfg["colors"]
    with open(alacritty_dir + "themes/" + theme + ".yml", "r") as theme:
        theme = yaml.load(theme, Loader=yaml.Loader)
        cfg.update(theme)
        new_file = open(alacritty_dir + "alacritty.yml", "w")
        yaml.dump(cfg, new_file)
        new_file.close()
          
        

def main():
    parser = ArgumentParser(description="Theme switcher \
                                     for Alacirtty terminal emulator")
    parser.add_argument("-l", "--list-themes", action="store_true",
                        help="print list of available themes")
    parser.add_argument("-s", "--set-theme", help="123") 
    args = parser.parse_args()
    
    # Check alacritty config dir
    global alacritty_dir
    alacritty_dir = f"/home/{os.getlogin()}/.config/alacritty/" 
    
    if not os.path.exists(alacritty_dir):
        exit(f"error: {alacritty_dir} doesn't exists")
    if not os.path.exists(alacritty_dir + "alacritty.yml"):
        exit(f"error: {alacirtty_dir}alacritty.yml doesn't exists")
    if not os.path.exists(alacritty_dir + "themes/"):
        exit(f"error: {alacritty_dir}themes/ doesn't exists")
    
    # Filter command line arguments 
    # to avoid bugs
    if not args.set_theme and not args.list_themes:
        parser.error("Missing argument -l/-s/-h")
    
    if args.list_themes:
        showThemes()
        exit(0)
    if args.set_theme:
        setTheme(args.set_theme)
        exit(0)


if __name__ == "__main__":
    main()
