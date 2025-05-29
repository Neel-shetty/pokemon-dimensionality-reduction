#!/usr/bin/env bash

pdflatex report.tex
if [ $? -ne 0 ]; then
    echo "Error: pdflatex failed to compile report.tex"
    exit 1
fi

bibtex report
if [ $? -ne 0 ]; then
    echo "Error: bibtex failed to process report"
    exit 1
fi

pdflatex report.tex
if [ $? -ne 0 ]; then
    echo "Error: pdflatex failed to compile report.tex again"
    exit 1
fi
pdflatex report.tex
if [ $? -ne 0 ]; then
    echo "Error: pdflatex failed to compile report.tex a third time"
    exit 1
fi