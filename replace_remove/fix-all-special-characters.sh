#!/bin/bash

./remove_parentheses_files_folders.sh $1
./replace_hyphen_with_underscores.sh $1
./replace_spaces_with_underscores.sh $1
./replace_under_hyphen_under_with_underscores.sh $1
./replace_triple_with_underscores.sh $1
