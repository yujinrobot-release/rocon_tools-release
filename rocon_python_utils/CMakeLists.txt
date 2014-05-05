##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(rocon_python_utils)

##############################################################################
# Catkin
##############################################################################

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

##############################################################################
# Tests
##############################################################################

if (CATKIN_ENABLE_TESTING)
  find_package(catkin REQUIRED rostest rosunit)
  add_subdirectory(tests)
endif()

##############################################################################
# Installs
##############################################################################

#install(
#    PROGRAMS 
#        scripts/rocon_interactions
#    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#    )

#install(DIRECTORY launch
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
