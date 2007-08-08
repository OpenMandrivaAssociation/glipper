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

BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:	ImageMagick
BuildRequires:	gnome-python >= 2.10
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python-gconf gnome-python-gnomevfs

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

# fd.o icons
mkdir -p %buildroot%{_iconsdir}/hicolor/{64x64,48x48,32x32,16x16}/apps
convert -scale 64 %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
convert -scale 48 %SOURCE1 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
convert -scale 32 %SOURCE1 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
convert -scale 16 %SOURCE1 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
# MDV icons
mkdir -p %buildroot{%_liconsdir,%_miconsdir}
convert -scale 48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -scale 32 %SOURCE1 %buildroot%_iconsdir/%name.png
convert -scale 16 %SOURCE1 %buildroot%_miconsdir/%name.png

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --add-category="Office" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

sed -e 's/%{name}.png/%{name}/' %buildroot%{_datadir}/applications/%{name}.desktop > %buildroot%{_datadir}/applications/%{name}.new && \
mv -f %buildroot%{_datadir}/applications/%{name}.new %buildroot%{_datadir}/applications/%{name}.desktop

%post
%update_icon_cache hicolor
%update_menus
%postun
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{name}.png
%dir %_datadir/gnome/help/%{name}
%lang(fr) %_datadir/gnome/help/%{name}/fr/glipper.xml
%lang(de) %_datadir/gnome/help/%{name}/de/glipper.xml
%_datadir/gnome/help/%{name}/C/%{name}.xml
%dir %_datadir/%{name}
%_datadir/%{name}/%{name}-properties.glade
%_iconsdir/*
%_liconsdir/*
%_miconsdir/*
