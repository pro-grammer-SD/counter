[app]
title = Counter App
package.name = counterapp
package.domain = org.soumalya
source.dir = .
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/icon.png
source.include_exts = py, png, jpg, kv, atlas
version = 0.1
requirements = python3==3.11.0, asyncgui, asynckivy, kivy, materialyoucolor, pillow, https://github.com/kivymd/KivyMD/archive/master.zip
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.minapi = 31
android.target = 34
p4a.local_recipes = ./recipes

[buildozer]
log_level = 2
warn_on_root = 0
