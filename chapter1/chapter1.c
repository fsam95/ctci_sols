# include <stdio.h>
# include <stdlib.h>
# include <string.h>
/*
 * Reverses string in place
 */
void reverse(char * string){
  int length = (int) strlen(string);
  int middleIndex = length / 2;
  int i = 0;
  char holder;
  while (i < middleIndex){
    holder = string[length - 1 - i];
    string[length - 1 - i] = string[i]; 
    string[i] = holder;
    i++;
  }
} 

/*
 * Time complexity: O(n^{3}) because we loop over every character
 * and search for duplicates. When we find duplicates, we loop
 * over the remainder of the array. 
 */
void remove_duplicate_characters(char* string){
  int length = (int) strlen(string);
  int curr_index = 0;
  while (string[curr_index] != '\0'){
    int dup_search_i = curr_index + 1; 
    while (dup_search_i < length){
      if (string[curr_index] == string[dup_search_i]){
        int replace_i = dup_search_i;
        int next_i = dup_search_i + 1;
        while (replace_i != length){
          string[replace_i] = string[next_i];
          replace_i++;
          next_i++;
        }
        length = length - 1;
      } else {
        dup_search_i++;
      }
    }
    curr_index++; 
  }
}



int main(){
  char test_string[25] = "dcb";
  reverse(test_string);
  printf("%s\n", test_string);

  char test_string_two[6] = {'b', 'b', '\0'};
  char test_string_three[6] = "abcbd";
  remove_duplicate_characters(test_string_two);
  remove_duplicate_characters(test_string_three);
  printf("%s\n", test_string_two);
  printf("%s\n", test_string_three);

  return 0;
}
