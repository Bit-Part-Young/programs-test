# Makefile for typst compilation by yangsl
# supports compiling all .typ files in the directory at once

TYPFILE = $(wildcard *.typ)

TYPST_COMPILER = compile

TARGET = $(patsubst %.typ,%.pdf,${TYPFILE})

.PHONY: all clean

all: $(TARGET)

$(TARGET): %.pdf : %.typ
	typst $(TYPST_COMPILER) $^

clean:
	@rm -f *.pdf
