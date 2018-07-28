Summary:	A virtual globe and world atlas
Name:		marble
Version:	18.07.80
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
Patch0:		marble-16.08.2-soversion.patch
Patch1:		fix_c++_exception_issue.patch
BuildRequires:	python-devel
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
BuildRequires:	cmake(SharedMimeInfo)
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
BuildRequires:	pkgconfig(zlib)
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
%{_bindir}/marble*
%{_iconsdir}/*/*/apps/marble.*
%{_datadir}/mime/packages/geo.xml

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
%{_sysconfdir}/xdg/marble.knsrc
%dir %{_datadir}/marble
%{_datadir}/marble/data
%{_libdir}/marble
%{_libdir}/qt5/plugins/libmarblethumbnail.so
%{_libdir}/qt5/plugins/plasma_runner_marble.so
%{_libdir}/qt5/plugins/libmarble_part.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/libmarblequick.so
%{_libdir}/qt5/qml/org/kde/marble/private/plasma/qmldir
%{_prefix}/mkspecs/modules/qt_Marble.pri
%{_datadir}/applications/*.desktop
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
%{_libdir}/libastro.so.0.*
%{_libdir}/libastro.so.%{astro_major}

#---------------------------------------------

%define major 28
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
Obsoletes:	%{_lib}marblewidget25 < 17.04.0
Obsoletes:	%{_lib}marblewidget26 < 17.04.0
Obsoletes:	%{_lib}marblewidget27 < 17.07.0

%description -n %{libname}
Runtime library for marble.

%files -n %{libname}
%{_libdir}/libmarblewidget-qt5.so.0.*
%{_libdir}/libmarblewidget-qt5.so.%{major}

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
    -DMOBILE=OFF

%build
%ninja -C build

%install

%ninja_install -C build
%find_lang marble --with-html
%find_lang plasma_applet_org.kde.plasma.worldclock
%find_lang plasma_runner_marble
%find_lang plasma_wallpaper_org.kde.plasma.worldmap
TOP=`pwd`
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r|cut -d/ -f5)) $(echo $r |cut -b2-)" >>$TOP/qm.lang
done
cd "$TOP"
cat *.lang >all.lang
