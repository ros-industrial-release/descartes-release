Name:           ros-hydro-descartes-core
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS descartes_core package

Group:          Development/Libraries
License:        Apache2.0
URL:            https://github.com/industrial-moveit/descartes_core
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-roscpp
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rosunit

%description
The descartes_core package creates joint trajectories for trajectory plans.
Trajectory plans are typically underdefined paths through space that allow for
kinematic/dynamic tolerances, such as unspecified tool roll.

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
* Fri May 01 2015 Jorge Nicho <jnicho@swri.org> - 0.0.3-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Jorge Nicho <jnicho@swri.org> - 0.0.2-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Jorge Nicho <jnicho@swri.org> - 0.0.1-0
- Autogenerated by Bloom

