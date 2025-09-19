#!/usr/bin/python
# encoding: utf8

# Smith configuration file for Idiqlat

# set the default output folders
DOCDIR = ["documentation", "web"]
genout = "generated/"

# set the font name and description
APPNAME = 'Idiqlat'
FAMILY = APPNAME
DESC_SHORT = "Font for the East Syriac script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
omitaps = '--omitaps "L,O,R"'

designspace('source/IdiqlatTestA.designspace',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    ),
    params = '--decomposeComponents --removeOverlaps -c ^_',
    version=VERSION,  # Needed to ensure dev information on version string
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", 
        mapfile = genout + "${DS:FILENAME_BASE}.map",
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
    )

def configure(ctx):
    ctx.find_program('ttfautohint')
 