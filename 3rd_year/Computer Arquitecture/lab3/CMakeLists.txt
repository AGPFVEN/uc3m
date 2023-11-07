cmake_minimum_required(VERSION 3.23)
project(03_cache)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(loop_merge loop_merge.cpp)
add_executable(loop_merge_opt loop_merge_opt.cpp)
add_executable(aos aos.cpp)
add_executable(soa soa.cpp)
