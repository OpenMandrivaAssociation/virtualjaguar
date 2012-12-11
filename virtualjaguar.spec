Summary:	Atari Jaguar Emulator
Name:		virtualjaguar
Version:	2.0.2
Release:	2
Group:		Emulators
License:	GPLv3
URL:		http://icculus.org/virtualjaguar/
Source0:	http://www.icculus.org/virtualjaguar/tarballs/%{name}-%{version}.tar.bz2
Patch0:		virtualjaguar-2.0.2-gcc4.7.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcdio)

%description
Virtual Jaguar is software dedicated to emulating the Atari Jaguar hardware on
a standard PC. The software was originally developed by David Raingeard of
Potato Emulation and was released under the GPL on 25 June 2003.

Virtual Jaguar GCC/Qt is not just a port of the MS Visual C++/SDL sourcecode
but has also been extended and rewritten so that we can enjoy Atari Jaguar
emulation on every platform that has a GCC compiler and a port of Qt.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 res/vj.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Virtual Jaguar
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

%files
%doc docs/*
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Fri Jan 06 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.2-1mdv2011.0
+ Revision: 758197
- New version 2.0.2

* Thu Oct 20 2011 Andrey Bondrov <abondrov@mandriva.org> 2.0.1-1
+ Revision: 705492
- New bugfix version 2.0.1

* Fri Oct 14 2011 Andrey Bondrov <abondrov@mandriva.org> 2.0.0-1
+ Revision: 704652
- imported package virtualjaguar

