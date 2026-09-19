#!/usr/bin/env bash
set -euo pipefail

src="$1"
dir="$(dirname "$src")"
base="$(basename "$src")"
out="${src%.*}"

shopt -s nullglob
sources=("$dir"/*.cpp)

if [[ "$base" == "main.cpp" && ${#sources[@]} -gt 1 ]]; then
    g++ -fdiagnostics-color=always -g -Wall "--std=${CPPSTD:-c++11}" "${sources[@]}" -I"$dir" -o "$out"
else
    g++ -fdiagnostics-color=always -g -Wall "--std=${CPPSTD:-c++11}" "$src" -o "$out"
fi
