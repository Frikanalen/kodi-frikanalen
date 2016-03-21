VERSION := $(shell grep '  version=' addon.xml |cut -d\" -f2)
FILES = addon.xml default.py icon.svg changelog.txt  icon.png    LICENSE.txt

all:

dist:
	mkdir -p plugin.video.frikanalen
	cp $(FILES) plugin.video.frikanalen/
	zip -r plugin.video.frikanalen-$(VERSION).zip plugin.video.frikanalen/
	rm -r plugin.video.frikanalen
