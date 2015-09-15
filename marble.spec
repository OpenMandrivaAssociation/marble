%bcond_with marble_python

Summary:	A virtual globe and world atlas
Name:		marble
Version:	15.08.0
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	python-devel
BuildRequires:	python-qt4-devel
BuildRequires:	quazip-devel
BuildRequires:	shapelib-devel
BuildRequires:	pkgconfig(libgpsd)
#BuildRequires:	pkgconfig(QtLocation)
BuildRequires:	qt4-qmlviewer
Requires:	marble-common = %{EVRD}

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files
%doc LICENSE.txt ChangeLog BUGS USECASES MANIFESTO.txt
%doc %{_kde_docdir}/HTML/en/marble
%{_kde_bindir}/marble
%{_kde_bindir}/marble-mobile
%{_kde_bindir}/marble-qt
%{_kde_bindir}/marble-touch
%{_kde_iconsdir}/*/*/apps/marble.*
%{_kde_applicationsdir}/marble.desktop
%{_kde_applicationsdir}/marble_geo.desktop
%{_kde_applicationsdir}/marble_gpx.desktop
%{_kde_applicationsdir}/marble_kml.desktop
%{_kde_applicationsdir}/marble_kmz.desktop
%{_kde_applicationsdir}/marble_osm.desktop
%{_kde_applicationsdir}/marble_shp.desktop
%{_kde_applicationsdir}/marble_worldwind.desktop
%{_kde_applicationsdir}/marble-mobile.desktop
%{_kde_applicationsdir}/marble-qt.desktop
%{_kde_applicationsdir}/marble-touch.desktop
%{_kde_libdir}/kde4/marblethumbnail.so
%{_kde_services}/marble_part_gpx.desktop
%{_kde_services}/marble_part_kml.desktop
%{_kde_services}/marble_part_kmz.desktop
%{_kde_services}/marble_part_osm.desktop
%{_kde_services}/marble_part_shp.desktop
%{_kde_services}/marble_thumbnail_gpx.desktop
%{_kde_services}/marble_thumbnail_kml.desktop
%{_kde_services}/marble_thumbnail_kmz.desktop
%{_kde_services}/marble_thumbnail_osm.desktop
%{_kde_services}/marble_thumbnail_shp.desktop
%{_kde_datadir}/appdata/marble.appdata.xml

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

%files -n marble-common
%{_kde_libdir}/kde4/plasma_runner_marble.so
%{_kde_libdir}/kde4/libmarble_part.*
%{_kde_datadir}/config.kcfg/marble.kcfg
%{_kde_datadir}/mime/packages/geo.xml
%{_kde_services}/marble_part.desktop
%{_kde_services}/plasma-runner-marble.desktop
%{_kde_libdir}/kde4/plugins/marble
%{_kde_appsdir}/marble
%if %{with marble_python}
%{py_platsitedir}/PyKDE4/marble.so
%endif
%{_qt_importdir}/org/kde/edu/marble

#-----------------------------------------------------------------------------

%package -n plasma-applet-kworldclock
Summary:	plasma kworldclock Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	marble = %{EVRD}
Provides:	plasma-applet

%description -n plasma-applet-kworldclock
plasma kworldclock Applet

%files -n plasma-applet-kworldclock
%{_kde_libdir}/kde4/plasma_applet_worldclock.so
%{_kde_services}/plasma-applet-kworldclock.desktop

#---------------------------------------------

%define astro_major 1
%define libastro %mklibname astro %{astro_major}

%package -n %{libastro}
Summary:	Runtime library for marble
Group:		System/Libraries

%description -n %{libastro}
Runtime library for marble.

%files -n %{libastro}
%{_kde_libdir}/libastro.so.0.*
%{_kde_libdir}/libastro.so.%{astro_major}

#---------------------------------------------

%define marblewidget_major 21
%define libmarblewidget %mklibname marblewidget %{marblewidget_major}

%package -n %{libmarblewidget}
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

%description -n %{libmarblewidget}
Runtime library for marble.

%files -n %{libmarblewidget}
%{_kde_libdir}/libmarblewidget.so.0.*
%{_kde_libdir}/libmarblewidget.so.%{marblewidget_major}

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libastro} = %{EVRD}
Requires:	%{libmarblewidget} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libastro.so
%{_kde_libdir}/libmarblewidget.so
%{_kde_libdir}/kde4/plugins/designer/*.so
%{_includedir}/astro/
%{_includedir}/marble/
%{_kde_appsdir}/cmake/modules/FindMarble.cmake

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	%if %{without marble_python}
	-DEXPERIMENTAL_PYTHON_BINDINGS=FALSE \
	-DBUILD_python=FALSE
	%else
	-DEXPERIMENTAL_PYTHON_BINDINGS=TRUE
	%endif

%make

%install
%makeinstall_std -C build
