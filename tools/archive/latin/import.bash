#!/bin/bash

ar=$PWD/tools/archive/latin
glyphnames=$HOME/script/smithplus/etc/glyph_names/glyph_names.csv
import=$HOME/script/syrc/fonts/idiqlatsyriac_proto-local/latin/Lateef

pushd source/masters
for weight in Light Regular
do
    ufo=Idiqlat-${weight}.ufo

    # prepare
    psfdeleteglyphs -i $ar/delete.txt $ufo

    # import
    scale="--scale 0.875" # 10.5 / 12
    glyphs=$ar/import-${weight}.csv
    latin=${import}-${weight}.ufo
    # psfgetglyphnames -i $ar/import.txt -a $glyphnames $latin $glyphs
    psfcopyglyphs --rename new_name --unicode usv $scale -s $latin -i $ar/latin_import.csv -l ${weight}.log $ufo

    # cleanup
    # $HOME/script/tools/fix-spaces.py $ufo

    # check
    composites $ufo
    ls -l $ufo/glyphs/*copy?.glif

    # colors
    psfsetmarkcolors -i $ar/import.txt -u -c g_light_gray $ufo
    cut -d\, -f 2 $ar/latin_import.csv  | grep .latn > $ar/color_latin.txt
    psfsetmarkcolors -i $ar/color_latin.txt -c g_light_gray $ufo
    psfsetmarkcolors -i $ar/sorts_latin.txt -c g_light_gray $ufo
done
popd

# glyph data
ufo2glyphdata $HOME/script/adobe/agl-aglfn/aglfn.txt source/masters/*-Regular.ufo source/gd.csv
sort source/gd.csv | cut -d\, -f 1,2,5 > $HOME/guest/gd_sorted.csv
sort source/glyph_data.csv | cut -d\, -f 1,2,3 > $HOME/guest/glyph_data_sorted.csv
