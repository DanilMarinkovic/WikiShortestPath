CXX      = g++
CXXFLAGS = -std=c++20 -O3 -Wall -Iinclude -I/usr/include/libxml2
LDFLAGS  = -lxml2

SRCS     = $(wildcard src/*.cpp)
OBJS     = $(SRCS:.cpp=.o)
TARGET   = wiki_shortest_path

$(TARGET): $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET) $(LDFLAGS)

src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f src/*.o $(TARGET)

