# FavDropper
This simple tool does exactly one thing. It symlinks files scattered across the filesystem into a single target directory using drag-and-drop. 

![screenshot](screenshot.png)

Pick a target directory, move FavDropper to the corner of your screen and start collecting files. Very useful to e.g. create a folder containing your favorit holiday pictures without actually copying or moving them. **Pro tip**: Running multiple instances with different target directories effectively allows to tag files. Create photo collections of landscapes, cities, or people simply by dragging the photos on the corresponding windows.


## Main Features
* KISS: Just one simple function - Easily create symlinks.
* Symlinks are relative to target directory. Use this tool on USB drives, network shares, or move your collections around later. The links will stay!
* Pure symlinks. No proprietary meta data. The links will stay even if the tool is gone.
* Cross-platform compatible. Works with any OS supporting Python 3, PyQt5, and symbolic links (tested on Linux and macOS).
