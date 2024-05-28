# filter plugin provides
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$
%global __requires_exclude cmake.*Qt6WebEngine\)

Summary:	A virtual globe and world atlas
Name:		plasma6-marble
Version:	24.02.2
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://edu.kde.org
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
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Phonon4Qt6Experimental)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	kdoctools-devel
BuildRequires:	pkgconfig(Qt6Core)
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
https://invent.kde.org/education/marble/-/commit/c86acad932bfde97939a478cf91c792517e4ef72.patch
https://invent.kde.org/education/marble/-/commit/b2d4b490a473c4908472e4ae510c3409d9990079.patch
https://invent.kde.org/education/marble/-/commit/564f80907954fdf48f1239268cb8a7ee301e9c45.patch
https://invent.kde.org/education/marble/-/commit/ef0b71e56090b7ab2f5fee3d4a6f3b0ce54a9f99.patch
https://invent.kde.org/education/marble/-/commit/fe1f62dce00b269b3d7c13cfb8b24d8f2257516d.patch
https://invent.kde.org/education/marble/-/commit/09a94281dd26831ff013078400540e3c45adcb84.patch
https://invent.kde.org/education/marble/-/commit/3561baad96ca819acd6bb95fe81f01cfd553b783.patch
https://invent.kde.org/education/marble/-/commit/f4f954749319e78f159eeca0f6afe481082802ed.patch
https://invent.kde.org/education/marble/-/commit/47d7dbf722dc657f991066a9dcaf6105a632603d.patch
https://invent.kde.org/education/marble/-/commit/d35566f37be69578ecca1760f1ffd3425f350ece.patch
https://invent.kde.org/education/marble/-/commit/f9e5ca1a6489b81bbca8751ba5110c0ebfbd2b2f.patch
https://invent.kde.org/education/marble/-/commit/faabe5e7531edf28300df8659ac4ff402478f0d3.patch
https://invent.kde.org/education/marble/-/commit/ba8bdb97600884824f75aab134af2a04013b8710.patch
https://invent.kde.org/education/marble/-/commit/43b04faaa21f39c9ab0a7d213bedf72de83622b8.patch
https://invent.kde.org/education/marble/-/commit/c7e505ae581f3621515bad4f631dee0f49bb9eea.patch
https://invent.kde.org/education/marble/-/commit/ed2e746954f7dd23dd64c26bcf4bd3970b4850fb.patch
https://invent.kde.org/education/marble/-/commit/a114e3e915082356b60c4fd19f35e48837efb345.patch
https://invent.kde.org/education/marble/-/commit/f4d68e1d674723229be82c8fb3dda883907cb56a.patch
https://invent.kde.org/education/marble/-/commit/4e061d4138e6cd52fad6a3458f189ed36252e49a.patch
https://invent.kde.org/education/marble/-/commit/d61d252fc3b1fe3683e1b744a6a004956bd4bc47.patch
https://invent.kde.org/education/marble/-/commit/58269d19b742b05e2de970f0910d4de82e51c393.patch
https://invent.kde.org/education/marble/-/commit/b7fb0be069dc09993bbde4a3121d1f901acd9bd9.patch
https://invent.kde.org/education/marble/-/commit/46dd097951a1aa3c35dc6c0e4f80b8909d0da9f6.patch
https://invent.kde.org/education/marble/-/commit/78a04b3cca88a1c957c40f38839371bb53fdde91.patch
https://invent.kde.org/education/marble/-/commit/752859523042a90ae9fa7a5833065a5f3f5796ec.patch
https://invent.kde.org/education/marble/-/commit/0cb7755bb3494e1e32554bbe95fdee8b5988b5e8.patch
https://invent.kde.org/education/marble/-/commit/ad59d632c971cfe1b3e360c6be47ff289a6a6f20.patch
https://invent.kde.org/education/marble/-/commit/4f704c705589129b48a5523bf874f6fa2c391068.patch
https://invent.kde.org/education/marble/-/commit/39eea41edd09ffad74c21d91484bbeff192c70b0.patch
https://invent.kde.org/education/marble/-/commit/078d50d39f29b744ecf61e9d3fb31148ad4e9b3c.patch
https://invent.kde.org/education/marble/-/commit/2607571539efb3f25dedec517bae2234d688f0ca.patch
https://invent.kde.org/education/marble/-/commit/03884065ae73b8ca6f4149c30af178b6936277d1.patch
https://invent.kde.org/education/marble/-/commit/6f98f93ea30702b4abfaec244ee00c0c5b00cc6c.patch
https://invent.kde.org/education/marble/-/commit/9609ad03592da955a793690c7338c9ad34aee7c9.patch
https://invent.kde.org/education/marble/-/commit/e4349a6ea3d800cc02cc8030f15849932a93d170.patch
https://invent.kde.org/education/marble/-/commit/8ecf55a6edf11a8e7dfc82f60f88b0ef07a0e4c6.patch
https://invent.kde.org/education/marble/-/commit/d5f98903fac33b17fc2b2d90ded39b4ecc7c2e94.patch
https://invent.kde.org/education/marble/-/commit/480e67fc954dd91573639f9d73f5bfc835421870.patch
https://invent.kde.org/education/marble/-/commit/726052cf8dfb84db4ff7d872505e5c0bf9078fb1.patch
https://invent.kde.org/education/marble/-/commit/568aa62d03352040bb4b644dacf796e3e578eae2.patch
https://invent.kde.org/education/marble/-/commit/c90daf6e65615947c2d7792e50647cba743b9305.patch
https://invent.kde.org/education/marble/-/commit/2ef4ad1018bddbdd7e00517a36f5ed2e1314c27a.patch
https://invent.kde.org/education/marble/-/commit/65a238d5c7c6c214bbe2f894e8c14377e269f14d.patch
https://invent.kde.org/education/marble/-/commit/bc61543c671cbee19a7ce52cfcfba2dace4753f3.patch
https://invent.kde.org/education/marble/-/commit/fdb087ba3696293650c845e2c3de3b31795d9414.patch
https://invent.kde.org/education/marble/-/commit/4d98f8bcc51fcabc103a0b8affd8259eef3d196b.patch
https://invent.kde.org/education/marble/-/commit/459b7d840142494bd1b98e0f5c53fc52051c56aa.patch
https://invent.kde.org/education/marble/-/commit/5a0b2fd4ab8b12d372ed2cbcb49ed28d796ad618.patch
https://invent.kde.org/education/marble/-/commit/272148fbe56b0e5494e6a84597df7eba619825f0.patch
https://invent.kde.org/education/marble/-/commit/0125b6824980c5e15846d9eb2d31e6e71248cf7d.patch
https://invent.kde.org/education/marble/-/commit/102f68987acd4f6397c000640314189913d02b7f.patch
https://invent.kde.org/education/marble/-/commit/dc1ad6b7407cdf7c7700eb5bf6418a4c408f7ebb.patch
https://invent.kde.org/education/marble/-/commit/09c02fc04eb1d912f910714def0a239567688e2a.patch
https://invent.kde.org/education/marble/-/commit/72de2c920e3de14e18426cb32ed4053825813478.patch
https://invent.kde.org/education/marble/-/commit/4f6cf1a260e8374c3e3882050098b3a4b86f6f1d.patch
https://invent.kde.org/education/marble/-/commit/876d994800fea84a1b5ca2ffca91ce7a275fd191.patch
https://invent.kde.org/education/marble/-/commit/8cdf45027e7e510a4a010ed59bd7a46640180146.patch
https://invent.kde.org/education/marble/-/commit/53a76955d963a4637d93615cdb44d1dd60ba6abd.patch
https://invent.kde.org/education/marble/-/commit/b9c18be8d25a87883d3ffe5dde42ab73bf7806b8.patch
https://invent.kde.org/education/marble/-/commit/6b7758b80586fe2b0bda0e68b691052bd82ad82e.patch
https://invent.kde.org/education/marble/-/commit/f5878ada41310de976847c4e1f886c2be51bf280.patch
https://invent.kde.org/education/marble/-/commit/447f123a2c87a6712896becc91efea95b27e5c66.patch
https://invent.kde.org/education/marble/-/commit/b5424e7dacd2a59e448adcda42a2eb31eea1c9f0.patch
https://invent.kde.org/education/marble/-/commit/c5d8ff6d1c9200d3b635bc34ba2322c17e7c4f70.patch
https://invent.kde.org/education/marble/-/commit/b0d9fb72bea925fdb5e2b1b0a4b9697b245e1792.patch
https://invent.kde.org/education/marble/-/commit/1bd658c9e60fce91fe120f2b198a2c9c321197cc.patch
https://invent.kde.org/education/marble/-/commit/c261831d2bd698bc3d44489aee24a13e46c3ce63.patch
https://invent.kde.org/education/marble/-/commit/a78fafb5d1796729de17f2e7963dce8cfe700269.patch

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%files
%doc LICENSE.txt BUGS USECASES MANIFESTO.txt
%{_iconsdir}/*/*/apps/marble.*
%{_datadir}/mime/packages/geo.xml
%{_datadir}/qlogging-categories6/marble.categories
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
%{_datadir}/applications/marble_*.desktop
%{_libdir}/libmarblewidget-qt6.so.*
%{_libdir}/libastro.so.*
%{_libdir}/libmarbledeclarative.so.*
%{_qtdir}/plugins/marblethumbnail.so

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
%{_libdir}/libmarbledeclarative.so
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

%find_lang marble --with-html --with-qt || touch marble.lang
%find_lang marble_qt --with-html --with-qt || touch marble_qt.lang
%find_lang plasma_applet_org.kde.plasma.worldclock || touch plasma_applet_org.kde.plasma.worldclock.lang
%find_lang plasma_runner_marble || touch plasma_runner_marble.lang
%find_lang plasma_wallpaper_org.kde.plasma.worldmap || touch plasma_wallpaper_org.kde.plasma.worldmap.lang
cat *.lang >all.lang
