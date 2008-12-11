%define name glipper
%define version 1.0
%define release %mkrel 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Clipboard manager for GNOME

Group:          Graphical desktop/GNOME
License:        LGPL
URL:            http://glipper.sourceforge.net/
Source0:        %name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:	imagemagick
BuildRequires:	gnome-python >= 2.10, gnome-python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python-gconf gnome-python-gnomevfs gnome-python-applet

Requires(post,preun): GConf2

%description
Glipper is a clipboard manager for GNOME. It maintains a history 
of text copied to the clipboard from which you can choose. You 
can see this as a GNOME counterpart to KDE's Klipper.

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make 

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %name

%post
%update_icon_cache hicolor
%{post_install_gconf_schemas glipper}

%preun
%{preun_uninstall_gconf_schemas glipper}

%postun
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/*
%{py_sitedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/bonobo/servers/*
%{_libdir}/pkgconfig/*.pc
%dir %_datadir/gnome/help/%{name}
%lang(fr) %_datadir/gnome/help/%{name}/fr/glipper.xml
%lang(de) %_datadir/gnome/help/%{name}/de/glipper.xml
%lang(it) %_datadir/gnome/help/%{name}/it/glipper.xml
%_datadir/gnome/help/%{name}/C/%{name}.xml
%_iconsdir/hicolor/*/apps/*
