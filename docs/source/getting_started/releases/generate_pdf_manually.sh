#!/bin/bash

rm -rf build/
sphinx-build -b latex . build
cd build/
sed -i 's/\\section/\\subsection/g' release_note_572.tex
sed -i 's/\\chapter/\\section/g' release_note_572.tex
sed -i '/Release date/d' release_note_572.tex
pdflatex release_note_572.tex 
pdflatex release_note_572.tex 
