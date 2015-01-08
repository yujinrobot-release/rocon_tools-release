Name:           ros-indigo-rocon-python-comms
Version:        0.1.12
Release:        0%{?dist}
Summary:        ROS rocon_python_comms package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_python_comms
Source0:        %{name}-%{version}.tar.gz

Requires:       PyYAML
Requires:       ros-indigo-genpy
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-service-pair-msgs
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-unique-id
Requires:       ros-indigo-uuid-msgs
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rosunit

%description
Service pair libraries for pub/sub non-blocking services.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jan 08 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.12-0
- Autogenerated by Bloom

