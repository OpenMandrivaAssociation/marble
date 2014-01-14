%bcond_with marble_python

Summary:	A virtual globe and world atlas
Name:		marble
Version:	4.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	python-devel
BuildRequires:	python-qt4-devel
BuildRequires:	quazip-devel
BuildRequires:	shapelib-devel
BuildRequires:	pkgconfig(libgpsd)
BuildRequires:	pkgconfig(QtLocation)
BuildRequires:	qt4-qmlviewer
Requires:	libkdeedu
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
%{_kde_bindir}/marble-qt
%{_kde_bindir}/marble-touch
%{_kde_bindir}/tilecreator
%{_kde_bindir}/routing-instructions
%{_kde_iconsdir}/*/*/apps/marble.*
%{_kde_applicationsdir}/marble.desktop
%{_kde_applicationsdir}/marble_gpx.desktop
%{_kde_applicationsdir}/marble_kml.desktop
%{_kde_applicationsdir}/marble_kmz.desktop
%{_kde_applicationsdir}/marble_osm.desktop
%{_kde_applicationsdir}/marble_shp.desktop
%{_kde_services}/marble_part_gpx.desktop
%{_kde_services}/marble_part_kml.desktop
%{_kde_services}/marble_part_kmz.desktop
%{_kde_services}/marble_part_osm.desktop
%{_kde_services}/marble_part_shp.desktop

#---------------------------------------------

%define marblewidget_major 16
%define libmarblewidget %mklibname marblewidget %{marblewidget_major}

%package -n %{libmarblewidget}
Summary:	Runtime library for marble
Group:		System/Libraries
Obsoletes:	%{_lib}marblewidget13 < 4.9.0
Obsoletes:	%{_lib}marblewidget14 < 4.10.0
Obsoletes:	%{_lib}marblewidget15 < 4.11.0

%description -n %{libmarblewidget}
Runtime library for marble.

%files -n %{libmarblewidget}
%{_kde_libdir}/libmarblewidget.so.0.%{marblewidget_major}*
%{_kde_libdir}/libmarblewidget.so.%{marblewidget_major}

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

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libmarblewidget} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libmarblewidget.so
%{_includedir}/marble
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

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0
- New library major for libmarblewidget
- Add quazip-devel to BuildRequires
- Update files list

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-2
- Build QML import files properly (update BuildRequires and files)
- Add pkgconfig(QtLocation) to BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- New library major for libmarblewidget
- Add shapelib-devel to BuildRequires for more features
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- Update libmarblewidget major from 13 to 14

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- Add BuildConflicts qt4-qmlviewer
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- Update file list (kde4/imports/org/kde/edu/marble is not packaged in _libdir)
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 762496
- Backport to 2010.2 for MIB users
- We could add qt-mobility to BuildRequires but we don't do it for now
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762496
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758084
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 748797
- Fix file list
- New upstream tarball
- New upstream tarball $NEW_VERSION

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733064
- New upstream tarball 4.7.80

* Wed Nov 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 729225
- Fix major
- Import marble

