%bcond_with marble_python

Summary:	A virtual globe and world atlas
Name:		marble
Version:	17.03.80
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch1:		fix_c++_exception_issue.patch
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
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	pkgconfig(shared-mime-info)
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
%doc LICENSE.txt BUGS USECASES MANIFESTO.txt
%{_kde5_bindir}/marble-qt
%{_kde5_iconsdir}/*/*/apps/marble.*
%{_datadir}/mime/packages/geo.xml

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
%{_bindir}/marble
%{_sysconfdir}/xdg/marble.knsrc
%{_libdir}/qt5/plugins/libmarble_part.so
%{_libdir}/qt5/plugins/libmarblethumbnail.so
%{_libdir}/qt5/plugins/plasma_runner_marble.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/libmarblequick.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/qmldir
%{_prefix}/mkspecs/modules/qt_Marble.pri
%{_datadir}/applications/marble_geo.desktop
%{_datadir}/applications/marble_geojson.desktop
%{_datadir}/applications/marble_gpx.desktop
%{_datadir}/applications/marble_kml.desktop
%{_datadir}/applications/marble_kmz.desktop
%{_datadir}/applications/marble_shp.desktop
%{_datadir}/applications/marble_worldwind.desktop
%{_datadir}/applications/org.kde.marble-qt.desktop
%{_datadir}/applications/org.kde.marble.desktop
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kservices5/marble_part.desktop
%{_datadir}/kservices5/marble_thumbnail_geojson.desktop
%{_datadir}/kservices5/marble_thumbnail_gpx.desktop
%{_datadir}/kservices5/marble_thumbnail_kml.desktop
%{_datadir}/kservices5/marble_thumbnail_kmz.desktop
%{_datadir}/kservices5/marble_thumbnail_osm.desktop
%{_datadir}/kservices5/marble_thumbnail_shp.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.worldclock.desktop
%{_datadir}/kservices5/plasma-runner-marble.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.plasma.wallpaper.worldmap.desktop
%{_datadir}/kxmlgui5/marble/marble_part.rc
%{_datadir}/kxmlgui5/marble/marbleui.rc
%{_datadir}/metainfo/org.kde.marble.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.wallpaper.worldmap.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldclock.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/contents/ui/configMapDisplay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/contents/ui/configTimeZones.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.plasma.wallpaper.worldmap/contents/config/main.xml
%{_datadir}/plasma/wallpapers/org.kde.plasma.wallpaper.worldmap/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.plasma.wallpaper.worldmap/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.plasma.wallpaper.worldmap/metadata.desktop
%{_datadir}/plasma/wallpapers/org.kde.plasma.wallpaper.worldmap/metadata.json
%if %{with marble_python}
%{py_platsitedir}/PyKDE4/marble.so
%endif
%doc %{_docdir}/HTML/en/marble

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

%define major 27
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
Obsoletes:	%{_lib}marblewidget22 < 16.04.0
Obsoletes:	%{_lib}marblewidget23 < 16.04.0
Obsoletes:	%{_lib}marblewidget24 < 16.08.3

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
%dir %{_libdir}/cmake/Marble
%dir %{_libdir}/cmake/Astro
%{_kde5_libdir}/libastro.so
%{_kde5_libdir}/libmarblewidget-qt5.so
%{_kde5_libdir}/libmarbledeclarative.so
%{_includedir}/astro/
%{_includedir}/marble/
%{_libdir}/cmake/Marble/*.cmake
%{_libdir}/cmake/Astro/*.cmake

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

# (tpg) ../src/3rdparty/sgp4/sgp4ext.cpp:210:9: error: 'asinh' is missing exception specification 'throw()'

%cmake_kde5 \
    -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
    -DQTONLY=ON \
    -DQT5BUILD=ON \
    -DBUILD_MARBLE_APPS=ON \
    -DBUILD_WITH_DBUS=ON \
    -DBUILD_MARBLE_TESTS=OFF \
    -DBUILD_TESTING=OFF \
    -DWITH_DESIGNER_PLUGIN=OFF \
    -DKDE_INSTALL_CONFDIR=%{_sysconfdir}/xdg \
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
