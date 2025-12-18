CXX      = g++
CXXFLAGS = -std=c++17 -O3 -Wall
TARGET   = wiki_shortest_path
SRC      = src/main.cpp
all: $(TARGET)
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)
clean:
	rm -f $(TARGET)
