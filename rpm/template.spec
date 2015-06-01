Name:           ros-indigo-rocon-tools
Version:        0.1.20
Release:        1%{?dist}
Summary:        ROS rocon_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rocon_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-ebnf
Requires:       ros-indigo-rocon-interactions
Requires:       ros-indigo-rocon-launch
Requires:       ros-indigo-rocon-master-info
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-redis
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-rocon-python-wifi
Requires:       ros-indigo-rocon-semantic-version
Requires:       ros-indigo-rocon-uri
BuildRequires:  ros-indigo-catkin

%description
Utilities and tools developed for rocon, but usable beyond the boundaries of
rocon.

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

* Tue Dec 02 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.11-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.10-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

