# filter plugin provides
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$

Summary:	A virtual globe and world atlas
Name:		marble
Version:	24.05.0
Release:	5
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		https://edu.kde.org
%define is_beta %(if test $(echo %{version} |cut -d. -f3) -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		marble-16.08.2-soversion.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(shapelib)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgps) >= 3.15
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Package)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(Phonon4Qt5Experimental)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	kdoctools-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Qml)
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
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(Qt5Positioning)
BuildRequires:	pkgconfig(Qt5SerialPort)
BuildRequires:	pkgconfig(Qt5WebChannel)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
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
%{_bindir}/marble
%{_iconsdir}/*/*/apps/marble.*
%{_datadir}/mime/packages/geo.xml
%{_datadir}/qlogging-categories5/marble.categories
#---------------------------------------------

%package qtonly
Summary:	Qt-Only version of Marble
Group:		Graphical desktop/KDE

%description qtonly
Qt-Only version of Marble.

This is the same as the regular marble application, except
it has a reduced dependency chain, a smaller memory footprint,
and a slightly reduced feature set.

You may want to install %{name}-qtonly if you're on a very
low memory system, or if you're targeting an embedded

%files qtonly
%{_bindir}/marble-qt
%{_datadir}/applications/org.kde.marble-qt.desktop
#---------------------------------------------

%package common
Summary:	A virtual globe and world atlas
Group:		Graphical desktop/KDE
Obsoletes:	marble-common-qt4 < 15.12.1
Provides:	marble-common-qt4 = 15.12.1

%description common
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files common -f all.lang
%dir %{_datadir}/marble
%{_datadir}/marble/data
%{_libdir}/marble
%{_libdir}/qt5/plugins/libmarble_part.so
%{_libdir}/qt5/plugins/marblethumbnail.so
%{_libdir}/qt5/plugins/kf5/krunner/plasma_runner_marble.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/libmarblequick.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/qmldir
%{_prefix}/mkspecs/modules/qt_Marble.pri
%{_datadir}/applications/marble_*.desktop
%{_datadir}/applications/org.kde.marble.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kxmlgui5/marble
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap

#---------------------------------------------

%define astro_major 1
%define libastro %mklibname astro %{astro_major}

%package -n %{libastro}
Summary:	Runtime library for marble
Group:		System/Libraries

%description -n %{libastro}
Runtime library for marble.

%files -n %{libastro}
%{_libdir}/libastro.so.%(echo %{version}|cut -d. -f1).*
%{_libdir}/libastro.so.%{astro_major}

#---------------------------------------------

%define major 28
%define libname %{_lib}marblewidget-qt5

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
Obsoletes:	%{_lib}marblewidget25 < 17.04.0
Obsoletes:	%{_lib}marblewidget26 < 17.04.0
Obsoletes:	%{_lib}marblewidget27 < 17.07.0
Obsoletes:	%{_lib}marblewidget-qt5_28 < 22.03.80

%description -n %{libname}
Runtime library for marble.

%files -n %{libname}
%{_libdir}/libmarblewidget-qt5.so.%(echo %{version}|cut -d. -f1).*
%{_libdir}/libmarblewidget-qt5.so.28

#----------------------------------------------------------------------------

%define declarative_major 0
%define libdeclarative %mklibname marbledeclarative %{declarative_major}

%package -n %{libdeclarative}
Summary:	Runtime library for marble
Group:		System/Libraries
Conflicts:	marble-devel < 17.04.0-2

%description -n %{libdeclarative}
Runtime library for marble.

%files -n %{libdeclarative}
%{_libdir}/libmarbledeclarative.so.%{declarative_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libastro} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libdeclarative} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%dir %{_libdir}/cmake/Marble
%dir %{_libdir}/cmake/Astro
%{_kde5_libdir}/libastro.so
%{_kde5_libdir}/libmarbledeclarative.so
%{_kde5_libdir}/libmarblewidget-qt5.so
%{_includedir}/astro/
%{_includedir}/marble/
%{_libdir}/cmake/Marble/*.cmake
%{_libdir}/cmake/Astro/*.cmake

#----------------------------------------------------------------------

%prep
%autosetup -p1

mv src/3rdparty/zlib src/3rdparty/zlib.UNUSED ||:

# Make current absl happy
sed -i -e 's,CMAKE_CXX_STANDARD 17,CMAKE_CXX_STANDARD 20,' CMakeLists.txt

# As of 20.08.0, the only effect of -DMOBILE is installing a smaller
# location cache. Given we target only higher end mobile devices for
# the moment, we can live with (and actually want) that.
# We may want to enable -DMOBILE=ON if it ever starts doing something
# more...

%cmake_kde5 \
	-DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
	-DBUILD_MARBLE_APPS=ON \
	-DBUILD_WITH_DBUS=ON \
	-DBUILD_MARBLE_TESTS=OFF \
	-DBUILD_TESTING=OFF \
	-DWITH_DESIGNER_PLUGIN=OFF \
	-DKDE_INSTALL_CONFDIR=%{_sysconfdir}/xdg \
	-DMOBILE=OFF

%build
%ninja_build -C build

%install

%ninja_install -C build
%find_lang marble --with-html
%find_lang plasma_applet_org.kde.plasma.worldclock
%find_lang plasma_runner_marble
%find_lang plasma_wallpaper_org.kde.plasma.worldmap
TOP=$(pwd)
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r|cut -d/ -f5)) $(echo $r |cut -b2-)" >>$TOP/qm.lang
done
cd "$TOP"
cat *.lang >all.lang
