#include <picojson.h>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <time.h>

int
main(int argc, char* argv[]) {
  clock_t t;
  t = clock();
  for (int n = 0; n < 1000; n++) {
    std::stringstream ss;
    std::ifstream f;
    f.open("person.json", std::ios::binary);
    ss << f.rdbuf();
    f.close();

    picojson::value v; ss >> v;
    picojson::array a = v.get<picojson::object>();
    int i, l = a.size();
    for (i = 0; i < l; i++) {
      std::cerr << a[i].get<picojson::object>()["age"].to_str() << std::endl;
    }
  }
  std::cout << "score: " << clock() - t << std::endl;
  return 0;
}
