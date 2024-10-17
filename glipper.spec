%define name glipper
%define version 1.0
%define release %mkrel 11

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Clipboard manager for GNOME

Group:          Graphical desktop/GNOME
License:        GPL+
URL:            https://glipper.sourceforge.net/
Source0:        %name-%version.tar.bz2
Patch0:		glipper-1.0-link.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:	imagemagick
BuildRequires:	gnome-python >= 2.10
BuildRequires:	gnome-python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python-gconf
BuildRequires:	gnome-python-gnomevfs
BuildRequires:	gnome-python-applet
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	gnome-python-applet

%description
Glipper is a clipboard manager for GNOME. It maintains a history 
of text copied to the clipboard from which you can choose. You 
can see this as a GNOME counterpart to KDE's Klipper.

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
# Don't break pkg-config with an invalid file
echo "Name: %name" >> data/glipper.pc
echo "Version: %version" >> data/glipper.pc
echo "Description: Clipboard manager for GNOME" >> data/glipper.pc

%build
%configure2_5x --disable-schemas-install
%make 

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %{name}

%post
%update_icon_cache hicolor
%{post_install_gconf_schemas glipper}

%preun
%{preun_uninstall_gconf_schemas glipper}

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
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
