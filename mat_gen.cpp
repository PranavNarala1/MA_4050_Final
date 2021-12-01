#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <math.h>
#include <iomanip>

using namespace std;

#define dims 101
#define dice_sides 6

int main(void) {
  ifstream chutes_in("chutes.csv");
  ifstream ladders_in("ladders.csv");
  ofstream output("coeffmat.csv");

  double coeff_mat[dims][dims];
  map<int, int> paths_to;
  map<int, int> paths_from;

  for (int i = 0; i < dims*dims; i++)
    coeff_mat[i/dims][i%dims] = 0.0;

  while (chutes_in.peek() != EOF) {
    int in1, in2;
    chutes_in >> in1 >> in2;
    paths_from[in1] = in2;
    paths_to[in2] = in1;
  }
  while (ladders_in.peek() != EOF) {
    int in1, in2;
    ladders_in >> in1 >> in2;
    paths_from[in1] = in2;
    paths_to[in2] = in1;
  }

  for (int i = 0; i < dims; i++) {
    // cout << "1";
    coeff_mat[i][i] = -1.0;
    if (paths_from.find(i) != paths_from.end())
      continue;
    // cout << "2" << endl;
    for (int j = 1; j <= dice_sides; j++) {
      if (i-j < 0)
        continue;
      coeff_mat[i][i-j] = 1.0 / (double)dice_sides;
      // cout << 1.0 / (double)dice_sides << endl;
    }
    // cout << "3" << endl;
    if (paths_to.find(i) != paths_to.end()) {
      for (int j = 1; j <= dice_sides; j++) {
        if (paths_to[i] - j < 0)
          continue;
        coeff_mat[i][paths_to[i] - j] = 1.0 / (double)dice_sides;
      }
    }
  }
  output << setprecision(6) << fixed;
  for (size_t i = 0; i < dims; i++) {
    for (size_t j = 0; j < dims; j++) {
      output << (double)coeff_mat[i][j] << " ";
    }
    output << endl;
  }
}