#!/usr/bin/python
import sys
import os
import urllib
import subprocess
import shutil

files = {
	'QLColorCode' :
		'https://qlcolorcode.googlecode.com/files/QLColorCode-2.0.2.tgz',
	'QLStephen' :
		'https://github.com/whomwah/qlstephen/releases/download/1.4.2/QLStephen.qlgenerator.1.4.2.zip',
	'QLMarkdown' :
	    'https://github.com/downloads/toland/qlmarkdown/QLMarkdown-1.3.zip',
	'QuickLookJSON' :
	    'http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip',
	'QLPrettyPatch' :
	    'https://github.com/atnan/QLPrettyPatch/releases/download/v1.0/QLPrettyPatch.qlgenerator.zip',
# No DMG Support yet.
#	'QuickLookCSV' :
#	    'http://quicklook-csv.googlecode.com/files/QuickLookCSV.dmg'
    'BetterZipQL' :
        'http://macitbetter.com/BetterZipQL.zip',
    'WebP' :
        'https://github.com/dchest/webp-quicklook/releases/download/v2.1/WebP-2.1.qlgenerator.zip',
	}

cache_dir = '.qlcache'
destination_dir = os.path.expanduser('~/Library/QuickLook')

try:
    os.mkdir(cache_dir);
except OSError as detail:
    print detail

try:
    os.mkdir(destination_dir);
except OSError as detail:
    print detail


os.chdir(cache_dir)

for name, file in files.items():
    print "Downloading %s" % (name)
    file_name = file.split('/')[-1]
    file_ext = file_name.split('.')[-1]

    urllib.urlretrieve (file, file_name)

    if file_ext == 'zip':
        print 'Unzipping'
        subprocess.call(['unzip', file_name])


    elif file_ext == 'tgz':
        print 'Untarring'
        subprocess.call(['tar', '-xzf', file_name])

qldirs = [];

print "Searching for plugins"

for root, subdirs, files in os.walk('./'):
    for dirname in subdirs:
        if dirname.split('.')[-1] == 'qlgenerator':
            file_path = os.path.join(root, dirname)
            print "Found %s" % file_path
            qldirs.append(file_path)

for qldir in qldirs:
    print "Installing %s" % qldir

    try:
        shutil.move(qldir, destination_dir)
    except shutil.Error as detail:
        print detail



print "Restarting quicklook"
subprocess.call(['qlmanage', '-r'])

print 'Cleaning up'
os.chdir('../')
shutil.rmtree(cache_dir)

print 'Done.'