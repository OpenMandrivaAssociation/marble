%bcond_with marble_python

%bcond_without qt4

Summary:	A virtual globe and world atlas
Name:		marble
Version:	15.08.2
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		marble-15.08.0-qt4.patch
BuildRequires:	python-devel
BuildRequires:	quazip-devel
BuildRequires:	shapelib-devel
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgpsd)
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
%if %{with qt4}
# (tpg) Qt4 support
BuildRequires:	kdelibs-devel
BuildRequires:	qt4-qmlviewer
%endif

Requires:	marble-common = %{EVRD}

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files
%doc LICENSE.txt ChangeLog BUGS USECASES MANIFESTO.txt
%doc %{_kde5_docdir}/HTML/en/marble
%{_kde5_bindir}/marble
%{_kde5_bindir}/marble-mobile
%{_kde5_bindir}/marble-qt
%{_kde5_bindir}/marble-touch
%{_kde5_iconsdir}/*/*/apps/marble.*
%{_kde5_applicationsdir}/marble.desktop
%{_kde5_applicationsdir}/marble_geo.desktop
%{_kde5_applicationsdir}/marble_gpx.desktop
%{_kde5_applicationsdir}/marble_kml.desktop
%{_kde5_applicationsdir}/marble_osm.desktop
%{_kde5_applicationsdir}/marble_shp.desktop
%{_kde5_applicationsdir}/marble_worldwind.desktop
%{_kde5_applicationsdir}/marble-mobile.desktop
%{_kde5_applicationsdir}/marble-qt.desktop
%{_kde5_applicationsdir}/marble-touch.desktop
%{_kde5_services}/marble_part_gpx.desktop
%{_kde5_services}/marble_part_kml.desktop
%{_kde5_services}/marble_part_osm.desktop
%{_kde5_services}/marble_part_shp.desktop
%{_kde5_services}/marble_thumbnail_gpx.desktop
%{_kde5_services}/marble_thumbnail_kml.desktop
%{_kde5_services}/marble_thumbnail_osm.desktop
%{_kde5_services}/marble_thumbnail_shp.desktop
%{_kde5_datadir}/appdata/marble.appdata.xml

#---------------------------------------------

%package common
Summary:	A virtual globe and world atlas
Group:		Graphical desktop/KDE
%if %{with marble_python}
BuildRequires:	python-kde4
Requires:	python
%endif

%description common
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files common
%dir %{_kde5_datadir}/marble
%{_kde5_datadir}/marble/data
%{_kde5_libdir}/marble
%{_kde5_datadir}/config.kcfg/marble.kcfg
%{_kde5_datadir}/kxmlgui5/marble
%{_kde5_services}/marble_part.desktop
%{_kde5_services}/plasma-runner-marble.desktop
%{_datadir}/applications/marble_kmz.desktop
%_qt5_plugindir/*.so
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

%define major 22
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

%if %{with qt4}
%define marblewidget_major 22
%define libmarblewidget %mklibname marblewidget %{marblewidget_major}
%define marbledevel %mklibname marblewidget -d

%package -n %{libmarblewidget}
Summary:	Runtime library for marble Qt4
Group:		System/Libraries

%description -n %{libmarblewidget}
Runtime library for marble Qt4.

%files -n %{libmarblewidget}
%{_libdir}/libmarblewidget.so.0.*
%{_libdir}/libmarblewidget.so.%{marblewidget_major}


%package common-qt4
Summary:	A virtual globe and world atlas Qt4
Group:		Graphical desktop/KDE
%if %{with marble_python}
BuildRequires:	python-kde4
Requires:	python
%endif

%description common-qt4
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files common-qt4
%{_libdir}/kde4/plugins/marble

%package -n %{marbledevel}
Summary:	Devel library for marble Qt4
Group:		System/Libraries
Requires:	%{libmarblewidget} = %{EVRD}
Requires:	%{name}-devel = %{EVRD}
Provides:	%{name}-qt4-devel = %{EVRD}

%description -n %{marbledevel}
Devel library for marble Qt4.

%files -n %{marbledevel}
%{_libdir}/libmarblewidget.so
%{_datadir}/apps/cmake/modules/FindMarble.cmake
%endif

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
%{_includedir}/astro/
%{_includedir}/marble/
%{_datadir}/marble/cmake/FindMarbleQt5.cmake

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5 \
    -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
    -DQT5BUILD:BOOL=ON \
    -DWITH_DESIGNER_PLUGIN:BOOL=OFF \
%if %{without marble_python}
    -DEXPERIMENTAL_PYTHON_BINDINGS=FALSE \
    -DBUILD_python=FALSE
%else
    -DEXPERIMENTAL_PYTHON_BINDINGS=TRUE
%endif

%ninja

%if %{with qt4}
cd ..
mkdir build-qt4
pushd build-qt4
%cmake_kde4 ../.. \
    -DBUILD_MARBLE_APPS:BOOL=OFF \
    -DBUILD_MARBLE_TESTS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=OFF \
    -DCMAKE_MODULES_INSTALL_PATH:PATH="%{_datadir}/apps/cmake/modules" \
    -DEXPERIMENTAL_PYTHON_BINDINGS:BOOL=OFF \
    -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
    -DMARBLE_PLUGIN_PATH:PATH="%{_libdir}/kde4/plugins/marble" \
    -DMOBILE:BOOL=OFF \
    -DQT5BUILD=OFF \
    -DWITH_DESIGNER_PLUGIN:BOOL=OFF

# (tpg) Qt4 does not build with LTO
%make CFLAGS="$CFLAGS -fno-lto" CXXFLAGS="$CXXLAGS -fno-lto" FFLAGS="$FFLAGS -fno-lto" LDLAGS="$LDLAGS -fno-lto"
popd

%endif



%install
%if %{with qt4}
pushd build-qt4
%makeinstall_std -C build
# put FindMarble.cmake in the right place (as previous releases at least) -- rex
mkdir -p %{buildroot}%{_datadir}/apps/cmake/modules/
mv %{buildroot}%{_datadir}/marble/cmake/FindMarble.cmake \
   %{buildroot}%{_datadir}/apps/cmake/modules/FindMarble.cmake
# FIXME: qt4 build plugins are installed to same place at qt5
rm -rf %{buildroot}%{_libdir}/marble/plugins/*.so
rm -rf %{buildroot}/usr//qt4/imports/org/kde/edu/marble/MarbleSettings.qml
rm -rf %{buildroot}/usr/lib/qt4/imports/org/kde/edu/marble/libMarbleDeclarativePlugin.so
rm -rf %{buildroot}/usr/lib/qt4/imports/org/kde/edu/marble/qmldir
rm -rf %{buildroot}/usr/lib/qt4/imports/org/kde/edu/marble/MarbleSettings.qml
popd
%endif

%ninja_install -C build
# munge FindMarble.cmake (FIXME: make upstreamable patch to do the same)
mv %{buildroot}%{_datadir}/marble/cmake/FindMarble.cmake \
   %{buildroot}%{_datadir}/marble/cmake/FindMarbleQt5.cmake
sed -i -e "s|marblewidget |marblewidget-qt5 |g" \
   %{buildroot}%{_datadir}/marble/cmake/FindMarbleQt5.cmake
