%define _disable_rebuild_configure 1
%define _disable_lto 1
%define oname Xastir

Name:		xastir
Version: 	2.1.0
Release:	1
Summary: 	Amateur Station Tracking and Reporting system for amateur radio
Group:		Communications
License:	GPL
URL: 		http://www.xastir.org
Source0: 	https://github.com/Xastir/Xastir/archive/Release-%{version}/%{oname}-Release-%{version}.tar.gz
Source1:        http://prdownloads.sourceforge.net/xastir/xastir-sounds.tgz
Patch0:		xastir-desktop.diff
BuildRequires:	motif-devel
BuildRequires:	shapelib-devel
BuildRequires:	proj-devel
BuildRequires:	geotiff-devel
BuildRequires:	festival-devel
BuildRequires:	db-devel
BuildRequires:	graphicsmagick-devel
Requires:	x11-font-adobe-75dpi

%description
Xastir is a graphical application that interfaces HAM radio
and internet access to realtime mapping software.

Install XASTIR if you are interested in APRS(tm) and HAM radio
software.

%prep
%setup -q n %{oname}-Release-%{version}
%setup -a1 -q
%apply_patches


%build
export CC=gcc
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
%{_datadir}/xastir/scripts
%{_mandir}/man1/xastir.1.*
%{_mandir}/man1/callpass.1.*
%{_mandir}/man1/testdbfawk.1.*
%{_mandir}/man1/xastir_udp_client.1.*
%{_datadir}/applications/xastir.desktop

# protect user-installed map and other files from being clobbered

%config %{_datadir}/xastir/maps
%config %{_datadir}/xastir/Counties
%config %{_datadir}/xastir/fcc
%config %{_datadir}/xastir/GNIS
%config %{_datadir}/xastir/sounds
