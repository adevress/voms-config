## cmake build script for srm-ifce
project (voms-config-wlcg)
cmake_minimum_required (VERSION 2.6)




set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules/")
# load module
include(DefineInstallationPaths REQUIRED)


install(DIRECTORY config/vomses/
		DESTINATION ${SYSCONF_INSTALL_DIR}/vomses/ )
		
install(DIRECTORY config/vomsdir/
		DESTINATION ${SYSCONF_INSTALL_DIR}/grid-security/vomsdir/ )






