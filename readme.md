# Quick Look plugins

> List of useful [Quick Look](http://en.wikipedia.org/wiki/Quick_Look) plugins for developers


## Install

### Using [Homebrew Cask](https://github.com/phinze/homebrew-cask)

- Run `brew cask install <package>`

#### Install all

```
brew cask install qlcolorcode qlstephen qlmarkdown quicklook-json qlprettypatch quicklook-csv betterzipql webp-quicklook suspicious-package
```

### Manually

- Click "download manually"
- Move the downloaded .qlgenerator file to /Library/QuickLook
- Run `qlmanage -r`


## Plugins


### [QLColorCode](https://code.google.com/p/qlcolorcode/)

> Preview source code files with syntax highlighting

Run `brew cask install qlcolorcode` or [download manually](https://qlcolorcode.googlecode.com/files/QLColorCode-2.0.2.tgz)

![](screenshots/QLColorCode.png)


### [QLStephen](https://github.com/whomwah/qlstephen)

> Preview plain text files without a file extension. Example: README, CHANGELOG, etc.

Run `brew cask install qlstephen` or [download manually](https://github.com/whomwah/qlstephen/releases)

![](screenshots/QLStephen.png)


### [QLMarkdown](https://github.com/toland/qlmarkdown)

> Preview Markdown files

Run `brew cask install qlmarkdown` or [download manually](https://github.com/downloads/toland/qlmarkdown/QLMarkdown-1.3.zip)

![](screenshots/QLMarkdown.png)


### [QuickLookJSON](http://www.sagtau.com/quicklookjson.html)

> Preview JSON files

Run `brew cask install quicklook-json` or [download manually](http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip)

![](screenshots/QuickLookJSON.png)


### [QLPrettyPatch](https://github.com/atnan/QLPrettyPatch)

> Preview .patch files

Run `brew cask install qlprettypatch` or [download manually](https://github.com/atnan/QLPrettyPatch/releases)

![](screenshots/QLPrettyPatch.png)


### [QuickLookCSV](https://github.com/p2/quicklook-csv)

> Preview CSV files

Run `brew cask install quicklook-csv` or [download manually](http://quicklook-csv.googlecode.com/files/QuickLookCSV.dmg)

![](screenshots/QuickLookCSV.png)


### [BetterZipQL](http://macitbetter.com/BetterZip-Quick-Look-Generator/)

> Preview archives

Run `brew cask install betterzipql` or [download manually](http://macitbetter.com/BetterZipQL.zip)

![](screenshots/BetterZipQL.png)


### [WebP](https://github.com/dchest/webp-quicklook)

> Preview WebP images

Run `brew cask install webp-quicklook` or [download manually](https://github.com/dchest/webp-quicklook/releases)

![](screenshots/WebP.png)


### [Suspicious Package](http://www.mothersruin.com/software/SuspiciousPackage/)

> Preview the contents of a standard Apple installer package

Run `brew cask install suspicious-package` or [download manually](http://www.mothersruin.com/software/downloads/SuspiciousPackage.dmg)

![](screenshots/SuspiciousPackage.png)


## More

- [Provisioning](https://github.com/chockenberry/Provisioning) - preview .mobileprovision (iOS) and .provisionprofile (OS X) files
- [CertQuickLook](https://code.google.com/p/cert-quicklook/) - preview various unprotected certificate tokens like X509 certificates, DER or PEM
- [CocoaDeveloper Quicklook Plugin](http://kfi-apps.com/plugins/ipaql/) - preview iOS / OS X app and provision information


## Tip

Run this in your terminal to allow text selection in the Quick Look window:

```
defaults write com.apple.finder QLEnableTextSelection -bool true && killall Finder
```


## License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Sindre Sorhus](http://sindresorhus.com) has waived all copyright and related or neighboring rights to this work. This work is published from: Norway.

-

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/sindresorhus/quick-look-plugins/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/0b54c5ec592f8133bd3d1b7abea99ef1 "githalytics.com")](http://githalytics.com/sindresorhus/quick-look-plugins)
