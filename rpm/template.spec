Name:           ros-melodic-mir-dwb-critics
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS mir_dwb_critics package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/dfki-ric/mir_dwb_critics
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-angles
Requires:       ros-melodic-costmap-queue
Requires:       ros-melodic-dwb-critics
Requires:       ros-melodic-dwb-local-planner
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-nav-2d-msgs
Requires:       ros-melodic-nav-2d-utils
Requires:       ros-melodic-nav-core2
Requires:       ros-melodic-nav-grid-iterators
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-costmap-queue
BuildRequires:  ros-melodic-dwb-critics
BuildRequires:  ros-melodic-dwb-local-planner
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-nav-2d-msgs
BuildRequires:  ros-melodic-nav-2d-utils
BuildRequires:  ros-melodic-nav-core2
BuildRequires:  ros-melodic-nav-grid-iterators
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs

%description
Trajectory critics for the dwb_local_planner that work well together with the
SBPL global planner on the MiR robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Mar 05 2019 Martin Günther <martin.guenther@dfki.de> - 1.0.3-0
- Autogenerated by Bloom

