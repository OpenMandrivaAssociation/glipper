%define name glipper
%define version 1.0
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Glipper is a clipboard manager for GNOME

Group:          Graphical desktop/GNOME
License:        LGPL
URL:            http://glipper.sourceforge.net/
Source0:        %name-%version.tar.bz2
#75x76 version of icon taken from homepage
Source1:	glipper-logo.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:	ImageMagick
BuildRequires:	gnome-python >= 2.10
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python-gconf gnome-python-gnomevfs gnome-python-applet

%description

Glipper is a clipboard manager for GNOME. It maintains a history 
of text copied to the clipboard from which you can choose. You 
can see this as a GNOME counterpart to KDE's Klipper.

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x 
%make 

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %name

%post
%update_icon_cache hicolor
%post_install_gconf_schemas glipper

%preun
%preun_install_gconf_schemas glipper

%postun
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/*.schema
%{py_platsitedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/bonobo/servers/*
%dir %_datadir/gnome/help/%{name}
%lang(fr) %_datadir/gnome/help/%{name}/fr/glipper.xml
%lang(de) %_datadir/gnome/help/%{name}/de/glipper.xml
%lang(it) %_datadir/gnome/help/%{name}/it/glipper.xml
%_datadir/gnome/help/%{name}/C/%{name}.xml
%_iconsdir/hicolor/*/apps/*
