#!/usr/bin/python3

import os
import yaml
from argparse import ArgumentParser


def show_themes(alacritty_dir):
    files = os.listdir(path=alacritty_dir + "/themes")
    print(f"Available themes {len(files)}:")
    print("\n".join([file.split('.')[0] for file in files]))


def chg_theme(alacirtty_dir, theme):
    cfg = open(alacritty_dir + "/alacritty.yml", "r")
    cfg = yaml.load(cfg, Loader=yaml.Loader)
    themes = os.listdir(path=alacritty_dir + "/themes")
    if not theme + ".yml" in themes:
        print(f'error: theme "{theme}" not found!')
        exit(1)
    del cfg["colors"]
    theme = open(alacritty_dir + "/themes/" + theme + ".yml", "r")
    theme = yaml.load(theme, Loader=yaml.Loader)
    cfg.update(theme)  
    new_file = open(alacritty_dir + "/alacritty.yml", "w")
    yaml.dump(cfg, new_file)



parser = ArgumentParser(description="Alacritty theme switcher")
parser.add_argument("-s", "--set-theme", default=False,
                    metavar="theme",type=str, help="set theme")
parser.add_argument("-l", "--list-themes", action="store_true",
                    help="show available themes")
parser.add_argument("-b", "--backup", action="store_true",
                    help="save current config to .bak file")
args = parser.parse_args()

alacritty_dir = f"/home/{os.getlogin()}/.config/alacritty"

if not os.path.exists(alacritty_dir):
    print("error: ~/.config/alacritty doesn't exists!")
    exit(1)

if not os.path.exists(alacritty_dir + "/themes"):
    print("error ~/.config/alacritty/themes doesn't exists!")
    exit(1)

if args.backup:
    os.system("cp ~/.config/alacritty/alacritty.yml \
              ~/.config/alacritty/alacritty.yml.bak")

if args.list_themes:
    show_themes(alacritty_dir)

if args.set_theme != False:
    chg_theme(alacritty_dir, args.set_theme)
