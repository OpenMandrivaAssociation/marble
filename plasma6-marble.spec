# filter plugin provides
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$
%global __requires_exclude cmake.*Qt6WebEngine\)

Summary:	A virtual globe and world atlas
Name:		plasma6-marble
Version:	25.03.80
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		https://edu.kde.org
%define is_beta %(if test $(echo %{version} |cut -d. -f3) -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/marble-%{version}.tar.xz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(shapelib)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgps) >= 3.15
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Runner)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(Plasma) >= 6.0.0-1
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Phonon4Qt6Experimental)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Location)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(Qt6Positioning)
BuildRequires:	pkgconfig(Qt6SerialPort)
BuildRequires:	pkgconfig(Qt6WebChannel)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineQuick)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{mklibname marblewidget 22} < 15.12.1
Provides:	%{mklibname marblewidget 22} = 15.12.1
Obsoletes:	%{mklibname marblewidget -d} < 15.12.1
Obsoletes:	%{mklibname marblewidget -d} = 15.12.1

%patchlist
marble-16.08.2-soversion.patch

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files
%doc LICENSE.txt BUGS USECASES MANIFESTO.txt
%{_bindir}/marble
%{_bindir}/marble-behaim
%{_bindir}/marble-maps
%{_iconsdir}/*/*/apps/marble.*
%{_iconsdir}/*/*/apps/org.kde.marble.behaim.*
%{_iconsdir}/*/*/apps/org.kde.marble.maps.*
%{_datadir}/mime/packages/geo.xml
%{_datadir}/qlogging-categories6/marble.categories
%{_datadir}/applications/org.kde.marble.desktop
%{_datadir}/applications/org.kde.marble.behaim.desktop
%{_datadir}/applications/org.kde.marble.maps.desktop
%{_datadir}/metainfo/org.kde.marble.appdata.xml
%{_datadir}/metainfo/org.kde.marble.behaim.appdata.xml
%{_datadir}/metainfo/org.kde.marble.maps.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldmap.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap
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

%files common -f marble.lang
%dir %{_datadir}/marble
%{_datadir}/marble/data
%{_libdir}/marble
%{_datadir}/applications/marble_*.desktop
%{_libdir}/libmarblewidget-qt6.so.*
%{_libdir}/libastro.so.*
%{_qtdir}/plugins/marblethumbnail.so
%{_qtdir}/plugins/kf6/krunner/plasma_runner_marble.so
%{_qtdir}/plugins/libmarble_part.so
%{_qtdir}/qml/org/kde/marble
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kxmlgui5/marble

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name}-common = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
%dir %{_libdir}/cmake/Marble
%dir %{_libdir}/cmake/Astro
%{_libdir}/libastro.so
%{_libdir}/libmarblewidget-qt6.so
%{_includedir}/astro/
%{_includedir}/marble/
%{_libdir}/cmake/Marble/*.cmake
%{_libdir}/cmake/Astro/*.cmake

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n marble-%{version}

mv src/3rdparty/zlib src/3rdparty/zlib.UNUSED ||:

# Make current absl happy
sed -i -e 's,CMAKE_CXX_STANDARD 17,CMAKE_CXX_STANDARD 20,' CMakeLists.txt

# As of 20.08.0, the only effect of -DMOBILE is installing a smaller
# location cache. Given we target only higher end mobile devices for
# the moment, we can live with (and actually want) that.
# We may want to enable -DMOBILE=ON if it ever starts doing something
# more...

%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
	-DBUILD_MARBLE_APPS=ON \
	-DBUILD_MARBLE_TOOLS=ON \
	-DBUILD_WITH_DBUS=ON \
	-DBUILD_MARBLE_TESTS=OFF \
	-DBUILD_TESTING=OFF \
	-DWITH_DESIGNER_PLUGIN=OFF \
	-DKDE_INSTALL_CONFDIR=%{_sysconfdir}/xdg \
	-DMOBILE=OFF \
	-G Ninja

%build
%ninja_build -C build

%install

%ninja_install -C build

# qmake is obsolete-ish... And this location is just wrong
rm -rf %{buildroot}%{_prefix}/mkspecs

%find_lang marble --with-html --with-qt --all-name
