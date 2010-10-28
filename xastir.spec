Name:		xastir
Version: 	1.9.8
Release:	%mkrel 2
Summary: 	Amateur Station Tracking and Reporting system for amateur radio
Group:		Communications
License:	GPL
URL: 		http://www.xastir.org
Source0: 	http://prdownloads.sourceforge.net/xastir/xastir-%{version}.tar.gz
Source1:        http://prdownloads.sourceforge.net/xastir/xastir-sounds.tgz
Patch0	:	xastir-desktop.diff
BuildRequires:	%{mklibname openmotif}-devel
BuildRequires:	libshapelib-devel
BuildRequires:	libproj-devel



%description
Xastir is a graphical application that interfaces HAM radio
and internet access to realtime mapping software.

Install XASTIR if you are interested in APRS(tm) and HAM radio
software.

%prep
%setup -q
%setup -a1
%patch0 -p 1

%build
./bootstrap.sh

CFLAGS=-I/usr/include/libgeotiff %configure --with-bdb-libdir=/usr/lib --with-bdb-incdir=/usr/include/db43

%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

# Docs go into package docs area instead of here:
rm -rf ${RPM_BUILD_ROOT}/usr/share/doc/xastir
mkdir -p ${RPM_BUILD_ROOT}/usr/share/applications
cp xastir.desktop ${RPM_BUILD_ROOT}/usr/share/applications/.
cp sounds/* ${RPM_BUILD_ROOT}/usr/share/xastir/sounds/.

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)

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
# %dir %attr(666,root,root) %{_datadir}/xastir/maps/GPS
%config %{_datadir}/xastir/Counties
%config %{_datadir}/xastir/fcc
%config %{_datadir}/xastir/GNIS
%config %{_datadir}/xastir/sounds


