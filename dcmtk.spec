%define major		3
%define libname		%mklibname dcmtk %major
%define develname	%mklibname dcmtk -d

Name:		dcmtk
Version:	3.6.0
Release:	1
Summary:	DICOM libraries and applications
Group:		System/Libraries
License:	BSD and MIT
URL:		http://dicom.offis.de/dcmtk.php.en
Source0:	%{name}-%{version}.tar.gz
Patch0:		dcmtk-3.6.0-mdv-link.patch
Patch1:		dcmtk-3.6.0-suse-Added-soname-information-for-all-targets.patch
Patch2:		dcmtk-3.6.0-suse-Install-libs-in-the-correct-arch-dir.patch
Patch3:		dcmtk-3.6.0-suse-Use-system-charls.patch
Patch4:		dcmtk-3.6.0-suse-Fixed-includes-for-CharLS-1.0.patch
Patch5:		dcmtk-3.6.0-suse-Add-soname-generation-for-modules-which-are-not-in-D.patch
Patch6:		dcmtk-3.6.0-mdv-dont-build-libcharls.patch
Patch7:		dcmtk-3.6.0-upstream-gcc47.patch
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%cmake
make

%install
pushd build
%makeinstall_std
popd

mv %{buildroot}%{_prefix}/etc %{buildroot}/

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_datadir}/dcmtk
%doc %{_defaultdocdir}/dcmtk/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/dcmtk/
