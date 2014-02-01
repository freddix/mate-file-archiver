Summary:	Archive manager for MATE
Name:		mate-file-archiver
Version:	1.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	d39a63d5e7d84c3ca2c810964837f9cc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	mate-doc-utils
BuildRequires:	libtool
BuildRequires:	mate-file-manager-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	rarian
Suggests:	bzip2
Suggests:	gzip
Suggests:	p7zip
Suggests:	tar
Suggests:	unrar
Suggests:	unzip
Suggests:	xz
Suggests:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Engrampa is an archive manager for the MATE environment. With File
Roller you can: create and modify archives; view the content of an
archive; view a file contained in the archive; extract files from the
archive. Engrampa is only a front-end (a graphical interface) to
various archiving programs.

%package -n mate-file-manager-extension-engrampa
Summary:	Engrampa extension for Caja
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	mate-file-manager

%description -n mate-file-manager-extension-engrampa
Engrampa extension for Caja file manager.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
mate-doc-prepare --copy --force
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*/*/*.la
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}//MateConf/gsettings/engrampa.convert
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ur_PK}

%find_lang engrampa --with-mate --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%scrollkeeper_update_postun
%update_desktop_database
%update_icon_cache hicolor
%update_gsettings_cache

%files -f engrampa.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_libdir}/mate-file-archiver
%attr(755,root,root) %{_bindir}/engrampa
%attr(755,root,root) %{_libdir}/mate-file-archiver/*.sh
%attr(755,root,root) %{_libdir}/mate-file-archiver/rpm2cpio
%{_datadir}/engrampa
%{_datadir}/mate-file-archiver
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/engrampa.*

%files -n mate-file-manager-extension-engrampa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/*.so

