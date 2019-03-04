Name:           ros-indigo-mir-navigation
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS mir_navigation package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/dfki-ric/mir_robot
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-amcl
Requires:       ros-indigo-base-local-planner
Requires:       ros-indigo-dwb-critics
Requires:       ros-indigo-dwb-local-planner
Requires:       ros-indigo-dwb-plugins
Requires:       ros-indigo-map-server
Requires:       ros-indigo-mir-driver
Requires:       ros-indigo-mir-dwb-critics
Requires:       ros-indigo-move-base
Requires:       ros-indigo-nav-core-adapter
Requires:       ros-indigo-sbpl-lattice-planner
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Launch and configuration files for move_base, localization etc. on the MiR
robot.

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
* Mon Mar 04 2019 Martin Günther <martin.guenther@dfki.de> - 1.0.3-0
- Autogenerated by Bloom

* Mon Jul 30 2018 Martin Günther <martin.guenther@dfki.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Jul 17 2018 Martin Günther <martin.guenther@dfki.de> - 1.0.1-0
- Autogenerated by Bloom

