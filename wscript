#!/usr/bin/python
# encoding: utf8

# Smith configuration file for Idiqlat

# set the default output folders
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Idiqlat'

# set the font family name
FAMILY = APPNAME

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
omitaps = '--omitaps "L,O,R, center"'

# location for misc build results
generated = 'generated/'

opts = preprocess_args({'opt': '--autohint'}, {'opt': '--norename'}, {'opt': '--quick'}, {'opt': '--regOnly'})

cmds = [cmd('ttx -m ${DEP} -o ${TGT} ${SRC}', ['source/jstf.ttx']) ]
if '--norename' not in opts:
    cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']))
if '--autohint' in opts:
    # Note: in some fonts ttfautohint-generated hints don't maintain stroke thickness at joins; test thoroughly
    cmds.append(cmd('${TTFAUTOHINT} -n -c  -W ${DEP} ${TGT}'))
else:
    cmds.append(cmd('gftools fix-nonhinting --no-backup -q ${DEP} ${TGT}'))

# designspace('source/Idiqlat.designspace',
designspace('source/IdiqlatTestA.designspace',
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
#    params = '--decomposeComponents --removeOverlaps -c ^_',
    params = '-c ^_',
    version=VERSION,  # Needed to ensure dev information on version string
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", 
        mapfile = generated + "${DS:FILENAME_BASE}.map",
        master="source/opentype/main.feax", to_ufo = 'True',
        make_params = '--ignoreglyphs ' + omitaps,
        depends = ['source/opentype/gsub.feax', 'source/opentype/gpos.feax'],
        ),
#    typetuner = typetuner("source/typetuner/feat_all.xml"),
    script='syrc',
    pdf = fret(params='-oi'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        ),
    shortcircuit = False,
    )

def configure(ctx):
    ctx.find_program('ttfautohint')
 