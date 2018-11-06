VERSION := $(shell grep '  version=' addon.xml |cut -d\" -f2)
FILES = addon.xml resources addon.py frikanalen.py main.py changelog.txt icon.png LICENSE.txt
REPO_PLUGINS ?= ../repo-plugins
REPO_PLUGINS_REPOSITORY ?= https://github.com/Frikanalen/repo-plugins
RELEASE_BRANCH ?= jarvis
TEST_PI_ADDRESS ?=192.168.0.20
TEST_PI_USER ?= root

all: dist

dist:
	mkdir -p plugin.video.frikanalen
	cp -r $(FILES) plugin.video.frikanalen/
	zip -r plugin.video.frikanalen-$(VERSION).zip plugin.video.frikanalen/
	rm -r plugin.video.frikanalen

prepare_release:
	if ! test -d $(REPO_PLUGINS); then \
	  git clone $(REPO_PLUGINS_REPOSITORY) $(REPO_PLUGINS); \
	fi
	git -C $(REPO_PLUGINS) stash
	git -C $(REPO_PLUGINS) checkout $(RELEASE_BRANCH)
	rm -rf $(REPO_PLUGINS)/plugin.video.frikanalen
	mkdir $(REPO_PLUGINS)/plugin.video.frikanalen
	cp -r $(FILES) $(REPO_PLUGINS)/plugin.video.frikanalen/

test_deploy: dist
	scp plugin.video.frikanalen-*.zip $(TEST_PI_USER)@$(TEST_PI_ADDRESS):

tt: dist
	rm -rvf ~/.kodi
	mv plugin.video.frikanalen-*.zip ~/Downloads/
	kodi

clean:
	rm *.zip

show:
	tail -f ~/.kodi/temp/kodi.log
