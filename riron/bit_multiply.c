#include <iostream>
#include <bitset>

using std::cout; using std::endl;
using std::string; using std::bitset;

int main(int argc, char *argv[])
{
  string bset_string_1 = argv[1];
  cout << bset_string_1 << endl;

  string bset_string_2 = argv[2];
  cout << bset_string_2 << endl;

  bitset<8> bset1(bset_string_1);
  bitset<8> bset2(bset_string_2);

  bitset<8> bset3(0);

  bset3 = bset1 * bset2;
  
  return 0;
}
