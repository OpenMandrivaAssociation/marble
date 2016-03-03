%bcond_with marble_python

Summary:	A virtual globe and world atlas
Name:		marble
Version:	15.12.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch1:		marble-15.12.2-use-std-for-math-functions.patch
BuildRequires:	python-devel
BuildRequires:	quazip-devel
BuildRequires:	shapelib-devel
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgpsd) >= 3.15
BuildRequires:	pkgconfig(phonon)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	kdoctools-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Location)
BuildRequires:	pkgconfig(Qt5Positioning)
Requires:	marble-common = %{EVRD}
Obsoletes:	%{mklibname marblewidget 22} < 15.12.1
Provides:	%{mklibname marblewidget 22} = 15.12.1
Obsoletes:	%{mklibname marblewidget -d} < 15.12.1
Obsoletes:	%{mklibname marblewidget -d} = 15.12.1

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files
%doc LICENSE.txt ChangeLog BUGS USECASES MANIFESTO.txt
%doc %{_kde5_docdir}/HTML/en/marble
%{_kde5_bindir}/marble-qt
%{_kde5_iconsdir}/*/*/apps/marble.*
%{_kde5_applicationsdir}/marble_gpx.desktop
%{_kde5_applicationsdir}/marble_kml.desktop
%{_kde5_applicationsdir}/marble_osm.desktop
%{_kde5_applicationsdir}/marble_shp.desktop
%{_kde5_applicationsdir}/marble-qt.desktop
%{_kde5_datadir}/appdata/marble.appdata.xml

#---------------------------------------------

%package common
Summary:	A virtual globe and world atlas
Group:		Graphical desktop/KDE
%if %{with marble_python}
BuildRequires:	python-kde4
Requires:	python
%endif

Obsoletes:	marble-common-qt4 < 15.12.1
Provides:	marble-common-qt4 = 15.12.1

%description common
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files common
%dir %{_kde5_datadir}/marble
%{_kde5_datadir}/marble/data
%{_kde5_libdir}/marble
%{_datadir}/applications/marble_kmz.desktop
%if %{with marble_python}
%{py_platsitedir}/PyKDE4/marble.so
%endif

#---------------------------------------------

%define astro_major 1
%define libastro %mklibname astro %{astro_major}

%package -n %{libastro}
Summary:	Runtime library for marble
Group:		System/Libraries

%description -n %{libastro}
Runtime library for marble.

%files -n %{libastro}
%{_kde5_libdir}/libastro.so.0.*
%{_kde5_libdir}/libastro.so.%{astro_major}

#---------------------------------------------

%define major 23
%define libname %mklibname marblewidget-qt5 %{major}

%package -n %{libname}
Summary:	Runtime library for marble
Group:		System/Libraries
Obsoletes:	%{_lib}marblewidget13 < 4.9.0
Obsoletes:	%{_lib}marblewidget14 < 4.10.0
Obsoletes:	%{_lib}marblewidget15 < 4.11.0
Obsoletes:	%{_lib}marblewidget16 < 4.12.0
Obsoletes:	%{_lib}marblewidget17 < 4.13.0
Obsoletes:	%{_lib}marblewidget18 < 4.14.4
Obsoletes:	%{_lib}marblewidget19 < 4.14.4
Obsoletes:	%{_lib}marblewidget20 < 15.04.02
Obsoletes:	%{_lib}marblewidget21 < 15.08.01

%description -n %{libname}
Runtime library for marble.

%files -n %{libname}
%{_kde5_libdir}/libmarblewidget-qt5.so.0.*
%{_kde5_libdir}/libmarblewidget-qt5.so.%{major}

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libastro} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde5_libdir}/libastro.so
%{_kde5_libdir}/libmarblewidget-qt5.so
%{_kde5_libdir}/libmarbledeclarative.so
%{_includedir}/astro/
%{_includedir}/marble/
%{_datadir}/marble/cmake/FindMarbleQt5.cmake

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches
# (tpg) ../src/3rdparty/sgp4/sgp4ext.cpp:210:9: error: 'asinh' is missing exception specification 'throw()'
export CC=gxx
export CXX=g++

%cmake_kde5 \
    -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
    -DQTONLY=ON \
    -DQT5BUILD=ON \
    -DBUILD_MARBLE_APPS=ON \
    -DBUILD_WITH_DBUS=ON \
    -DBUILD_MARBLE_TESTS=OFF \
    -DBUILD_TESTING=OFF \
    -DWITH_DESIGNER_PLUGIN=OFF \
    -DMOBILE=OFF \
%if %{without marble_python}
    -DEXPERIMENTAL_PYTHON_BINDINGS=FALSE \
    -DBUILD_python=FALSE
%else
    -DEXPERIMENTAL_PYTHON_BINDINGS=TRUE
%endif

%build
%ninja -C build

%install

%ninja_install -C build
# munge FindMarble.cmake (FIXME: make upstreamable patch to do the same)
mv %{buildroot}%{_datadir}/marble/cmake/FindMarble.cmake \
   %{buildroot}%{_datadir}/marble/cmake/FindMarbleQt5.cmake
sed -i -e "s|marblewidget |marblewidget-qt5 |g" \
   %{buildroot}%{_datadir}/marble/cmake/FindMarbleQt5.cmake
