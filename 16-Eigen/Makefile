
SRC = $(wildcard *.cpp)
OBJ = $(patsubst %.cpp,%.o,$(SRC))
EXE = $(patsubst %.cpp,%,$(SRC))

EigenINC = -I${HOME}/src/eigen-3.4.0


all: $(OBJ)

%.o: %.cpp
	$(CXX) $< -o $@ $(EigenINC)

clean:
	@rm -f $(OBJ)
