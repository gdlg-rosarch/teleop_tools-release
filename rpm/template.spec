Name:           ros-indigo-mouse-teleop
Version:        0.2.6
Release:        0%{?dist}
Summary:        ROS mouse_teleop package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       numpy
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin

%description
A mouse teleop tool for holonomic mobile robots.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Apr 06 2018 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.6-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.5-0
- Autogenerated by Bloom

* Wed Nov 30 2016 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Thu Mar 24 2016 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Tue Feb 02 2016 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.1-1
- Autogenerated by Bloom

* Tue Feb 02 2016 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

