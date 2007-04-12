Name:           glipper
Version:        0.95.1
Release:        %mkrel 1
Summary:        Glipper is a clipboardmanager for GNOME

Group:          Graphical desktop/GNOME
License:        LGPL
URL:            http://glipper.sourceforge.net/
Source0:        %name-%version.tar.bz2 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  gtk2-devel

%description

Glipper is a clipboardmanager for GNOME (and other WMs), it 
maintains a history of text copied to the clipboard from which 
you can choose. You can see this as a GNOME counterpart to 
KDE's Klipper.

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/glipper
%{_datadir}/applications/glipper.desktop
%{_datadir}/glipper/glipper-properties.glade
%{_datadir}/gnome/help/glipper/C/glipper.xml
%{_datadir}/gnome/help/glipper/de/glipper.xml
%{_datadir}/gnome/help/glipper/fr/glipper.xml
%{_datadir}/pixmaps/glipper.png

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure 
%make 


%install
rm -rf %buildroot
make install DESTDIR=%buildroot
%find_lang %name


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --add-category="Office" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT


