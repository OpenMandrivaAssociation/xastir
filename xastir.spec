Name:		xastir
Version: 	2.0.0
Release:	3
Summary: 	Amateur Station Tracking and Reporting system for amateur radio
Group:		Communications
License:	GPL
URL: 		http://www.xastir.org
Source0: 	http://prdownloads.sourceforge.net/xastir/xastir-%{version}.tar.gz
Source1:        http://prdownloads.sourceforge.net/xastir/xastir-sounds.tgz
Patch0:		xastir-desktop.diff
BuildRequires:	lesstif-devel
BuildRequires:	shapelib-devel
BuildRequires:	proj-devel
BuildRequires:	geotiff-devel
BuildRequires:	festival-devel
BuildRequires:	db5.3-devel
BuildRequires:	graphicsmagick-devel
Requires:	x11-font-adobe-75dpi
Patch1:		xastir-2-mapdir.patch

%description
Xastir is a graphical application that interfaces HAM radio
and internet access to realtime mapping software.

Install XASTIR if you are interested in APRS(tm) and HAM radio
software.

%prep
%setup -q
%setup -a1 -q

%patch0 -p1
%patch1 -p1


%build
./bootstrap.sh

CFLAGS=-I/usr/include/libgeotiff 
%configure2_5x 
%make

%install
%makeinstall_std

# Docs go into package docs area instead of here:
rm -rf %{buildroot}/usr/share/doc/xastir
mkdir -p %{buildroot}/usr/share/applications
cp xastir.desktop %{buildroot}/usr/share/applications/.
cp sounds/* %{buildroot}/usr/share/xastir/sounds/.

%files
# Documents:  Go into special doc area
%doc AUTHORS ChangeLog COPYING COPYING.LIB.LESSTIF DEBUG_LEVELS FAQ INSTALL LICENSE
%doc README README.Contributing README.CVS README.Getting-Started
%doc README.MAPS README.win32 UPGRADE


%{_bindir}/*
%{_datadir}/xastir/help
%{_datadir}/xastir/config
%{_datadir}/xastir/symbols
%{_mandir}/man1/xastir.1.*
%{_mandir}/man1/callpass.1.*
%{_mandir}/man1/testdbfawk.1.*
%{_mandir}/man1/xastir_udp_client.1.*
%{_libdir}/xastir
%{_datadir}/applications/xastir.desktop

# protect user-installed map and other files from being clobbered

%config %{_datadir}/xastir/maps
%config %{_datadir}/xastir/Counties
%config %{_datadir}/xastir/fcc
%config %{_datadir}/xastir/GNIS
%config %{_datadir}/xastir/sounds
