# Makefile for typst compilation by yangsl
# supports compiling all .typ files in the directory at once

FILE = main.typ

TYPST_COMPILER = compile

FONT_PATH = "fonts/"
FONT_FLAG = --font-path

TARGET = main.pdf

.PHONY: all clean

all: $(TARGET)

$(TARGET): 
	typst $(TYPST_COMPILER) ${FILE} ${FONT_FLAG} ${FONT_PATH}

clean:
	@rm -f main.pdf template.pdf

