# Makefile for LaTeX compilation

# Set the name of the main tex file (without the .tex extension)
MAIN = main

# Set the LaTeX compiler
LATEX_COMPILER = xelatex
REFERENCE_COMPILER = bibtex

# Set the target file (PDF output)
TARGET = $(MAIN).pdf

# Define the default target
all: $(TARGET)

# Define the target to build the PDF output and clean up auxiliary files
$(TARGET): $(MAIN).tex
	$(LATEX_COMPILER) $(MAIN).tex
	$(REFERENCE_COMPILER) $(MAIN).aux
	$(LATEX_COMPILER) $(MAIN).tex
	$(LATEX_COMPILER) $(MAIN).tex

clean:
	rm -f $(MAIN).aux ${MAIN}.bbl ${MAIN}.bcf $(MAIN).blg \
		$(MAIN).fdb_latexmk $(MAIN).fls $(MAIN).log $(MAIN).out \
		$(MAIN).run.xml $(MAIN).toc $(MAIN).xdv

# Define the target to clean up generated pdf files
distclean: 
	rm -f $(MAIN).pdf

# Phony targets (targets that are not real files)
.PHONY: all distclean clean
