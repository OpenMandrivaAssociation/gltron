%define name	gltron
%define version	0.70
%define release	%mkrel 13

Summary:	Gltron, a 3d lightcycle game using OpenGL
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Url:		https://gltron.sourceforge.net
Source:		gltron-%version.tar.bz2
Source1:	gltron-xpm.tar.bz2
Patch0:		gltron-0.70-gcc4.patch
Patch1:		gltron-0.70-sys-cflags.patch
Patch2:		gltron-0.70-link.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  png-devel
BuildRequires:  mesagl-devel
BuildRequires:	smpeg-devel

%description
A very nice Tron game using OpenGL.

%prep
%setup -q
%patch0 -p1 -b .gcc4
%patch1 -p0 -b .cflags
%patch2 -p0 -b .link

%build
touch AUTHORS NEWS
autoreconf -fi
%configure2_5x --bindir=%_gamesbindir \
	--datadir=%_gamesdatadir --disable-warn \
	--disable-sdltest
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
tar xfj %{SOURCE1}
install -m0644 gltron-16.png $RPM_BUILD_ROOT%{_miconsdir}/gltron.png
install -m0644 gltron-32.png $RPM_BUILD_ROOT%{_iconsdir}/gltron.png
install -m0644 gltron-48.png $RPM_BUILD_ROOT%{_liconsdir}/gltron.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gltron
Comment=3d lightcycle game
Exec=%{_gamesbindir}/gltron
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_gamesbindir}/gltron
%dir %{_gamesdatadir}/gltron/
%{_gamesdatadir}/gltron/art
%{_gamesdatadir}/gltron/data
%{_gamesdatadir}/gltron/music
%{_gamesdatadir}/gltron/scripts
%{_miconsdir}/gltron.png
%{_iconsdir}/gltron.png
%{_liconsdir}/gltron.png
%{_datadir}/applications/mandriva-%{name}.desktop


