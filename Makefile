VERSION := $(shell grep '  version=' addon.xml |cut -d\" -f2)
FILES = addon.xml default.py changelog.txt  icon.png    LICENSE.txt
REPO_PLUGINS ?= ../repo-plugins
RELEASE_BRANCH ?= jarvis

all:

dist:
	mkdir -p plugin.video.frikanalen
	cp $(FILES) plugin.video.frikanalen/
	zip -r plugin.video.frikanalen-$(VERSION).zip plugin.video.frikanalen/
	rm -r plugin.video.frikanalen

prepare_release:
	git -C $(REPO_PLUGINS) stash
	git -C $(REPO_PLUGINS) checkout $(RELEASE_BRANCH)
	rm -rf $(REPO_PLUGINS)/plugin.video.frikanalen
	mkdir $(REPO_PLUGINS)/plugin.video.frikanalen
	cp $(FILES) $(REPO_PLUGINS)/plugin.video.frikanalen/

clean:
	rm *.zip
