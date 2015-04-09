Name:           ros-hydro-descartes-moveit
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS descartes_moveit package

Group:          Development/Libraries
License:        Apache2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cmake-modules
Requires:       ros-hydro-descartes-core
Requires:       ros-hydro-descartes-trajectory
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-moveit-ros-planning
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-rosconsole-bridge
Requires:       ros-hydro-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-descartes-core
BuildRequires:  ros-hydro-descartes-trajectory
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-moveit-ros-planning
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-rosconsole-bridge
BuildRequires:  ros-hydro-rosunit
BuildRequires:  ros-hydro-tf

%description
Moveit wrapper functions for descartes base types

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
* Thu Apr 09 2015 Jorge Nicho <jnicho@swri.org> - 0.0.2-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Jorge Nicho <jnicho@swri.org> - 0.0.1-0
- Autogenerated by Bloom

