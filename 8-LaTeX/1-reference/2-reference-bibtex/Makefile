# Makefile for report-template-MMMS
# reference: https://github.com/sjtug/SJTUThesis/blob/master/Makefile

# Basename of tex file
OBJ = main

# Option for latexmk
LATEXMK_OPT = -time -file-line-error -halt-on-error -interaction=nonstopmode

.PHONY: all pvc clean cleanall FORCE_MAKE auto help

auto: all clean

all: $(OBJ).pdf

help:
	@echo "Usage:"
	@echo "    make [option]"
	@echo "options:"
	@echo "    all         Compile tex file"
	@echo "    clean       Clean all work files"
	@echo "    cleanall    Clean all work files and pdf file"
	@echo "    auto        Excute all and clean"
	@echo "    help        Print this help message"

$(OBJ).pdf: $(OBJ).tex FORCE_MAKE
	@latexmk $(LATEXMK_OPT) $<

clean:
	-@latexmk -c -silent $(OBJ).tex 2> /dev/null
	-@rm -f $(OBJ).bbl 2> /dev/null

cleanall:
	-@latexmk -C -silent $(OBJ).tex 2> /dev/null
	-@rm -f $(OBJ).bbl 2> /dev/null
