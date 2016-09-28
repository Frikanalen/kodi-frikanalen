kodi-frikanalen
===============

[Kodi/XBMC](https://kodi.tv/) plugin for
[Frikanalen](http://www.frikanalen.no/).

The latest version of this project is available from
https://github.com/Frikanalen/kodi-frikanalen

See https://github.com/tamland/xbmc-addon-nrk and
http://kodi.wiki/view/Audio/Video_plugin_tutorial for inspiration.

See http://kodi.wiki/view/Submitting_Add-ons to learn how to submit a
plugin to the Kodi community repo.

This add-on is available from the Kodi repository as
http://addons.kodi.tv/show/plugin.video.frikanalen/ .

Release process
----------------

We are currently targeting jarvis.

The following is a step-by-step procedure for releasing a new version:

0. Update the changelog.
0. Run `make prepare_release` from kodi-frikanalen.
0. Commit copied files in `../repo-plugins`.
0. Open a pull request on the
   [xbmc/repo-plugins](https://github.com/xbmc/repo-plugins) repository for the
   jarvis branch.
0. Wait on the review to start.
0. Address any code review issues.
0. When merged upstream, create a tag for the version and push it out.
