Name:           ros-indigo-rocon-interactions
Version:        0.1.23
Release:        0%{?dist}
Summary:        ROS rocon_interactions package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_interactions
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-genpy
Requires:       ros-indigo-rocon-app-manager-msgs
Requires:       ros-indigo-rocon-bubble-icons
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-icons
Requires:       ros-indigo-rocon-interaction-msgs
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-rocon-std-msgs
Requires:       ros-indigo-rocon-uri
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-unique-id
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rosunit

%description
Interaction management for human interactive agents in the concert.

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
* Mon Jul 13 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.23-0
- Autogenerated by Bloom

* Thu Jul 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.21-0
- Autogenerated by Bloom

* Mon Jun 01 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.20-1
- Autogenerated by Bloom

* Mon Jun 01 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.20-0
- Autogenerated by Bloom

* Wed May 27 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.19-0
- Autogenerated by Bloom

* Wed May 06 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.18-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.17-0
- Autogenerated by Bloom

* Mon Mar 02 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.16-0
- Autogenerated by Bloom

* Sat Feb 28 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.15-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.14-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.13-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.12-0
- Autogenerated by Bloom

