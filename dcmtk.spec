%define oname DCMTK
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major		3
%define libname		%mklibname dcmtk %major
%define develname	%mklibname dcmtk -d

Name:		%{lname}
Version:	3.6.2
Release:	1
Summary:	DICOM libraries and applications
Group:		System/Libraries
License:	BSD and MIT
URL:		http://dicom.offis.de/dcmtk.php.en
Source0:	https://github.com/DCMTK/%{name}/archive/%{oname}-%{version}.tar.gz
Patch1:		%{name}-3.6.2-fix-type.patch
Patch2:		%{name}-3.6.2-unbundle-libcharls.patch

BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	tiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	wrap-devel
BuildRequires:	CharLS-devel

%description
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

DCMTK has been used at numerous DICOM demonstrations to provide central,
vendor-independent image storage and worklist servers (CTNs - Central Test
Nodes). It is used by hospitals and companies all over the world for a wide
variety of purposes ranging from being a tool for product testing to being
a building block for research projects, prototypes and commercial products.

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_datadir}/dcmtk
%{_mandir}/man1/*.1*
%doc %{_defaultdocdir}/dcmtk/*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	DICOM libraries
Group:		System/Libraries

%description -n %{libname}
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

This package contains shared libraries.

%files -n %{libname}
%{_libdir}/*.so.*

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	DICOM libraries development files
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}

%description -n %{develname}
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

This package contains files required for development only.

%files -n %{develname}
%{_includedir}/dcmtk/
%{_libdir}/*.so
%dir %{_libdir}/cmake/%{name}/
%{_libdir}/cmake/%{name}/*cmake

#---------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{oname}-%{version}
%apply_patches

# remove bundled libs
rm -fr dcmjpls/libcharls

%build
export CC=gcc
export CXX=g++

%cmake \
	-DDCMTK_INSTALL_LIBDIR:STRING=%{_lib} \
	-DDCMTK_INSTALL_ETCDIR:STRING=%{_sysconfdir}/%{name} \
	-DDCMTK_INSTALL_CMKDIR:STRING=%{_lib}/cmake/%{name} \
	%{nil}
%make

%install
%makeinstall_std -C build

