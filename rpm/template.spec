Name:           ros-hydro-descartes
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS descartes package

Group:          Development/Libraries
License:        Apache2.0
URL:            http://wiki.ros.org/descartes_moveit
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-descartes-core
Requires:       ros-hydro-descartes-moveit
Requires:       ros-hydro-descartes-planner
Requires:       ros-hydro-descartes-trajectory
BuildRequires:  ros-hydro-catkin

%description
Descartes is a ROS-Industrial project for performing path-planning on under-
defined Cartesian trajectories. More details regarding motivation can be found
in rep-I0003.rst.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Apr 09 2015 Shaun Edwards <sedwards@swri.org> - 0.0.2-0
- Autogenerated by Bloom

