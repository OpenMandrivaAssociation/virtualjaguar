Summary:	Atari Jaguar Emulator
Name:		virtualjaguar
Version:	2.1.0
Release:	2
Group:		Emulators
License:	GPLv3
URL:		http://icculus.org/virtualjaguar/
Source0:	http://www.icculus.org/virtualjaguar/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

%description
Virtual Jaguar is software dedicated to emulating the Atari Jaguar hardware on
a standard PC. The software was originally developed by David Raingeard of
Potato Emulation and was released under the GPL on 25 June 2003.

Virtual Jaguar GCC/Qt is not just a port of the MS Visual C++/SDL sourcecode
but has also been extended and rewritten so that we can enjoy Atari Jaguar
emulation on every platform that has a GCC compiler and a port of Qt.

%prep
%setup -q -n %{name}

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

