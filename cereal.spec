%define debug_package %{nil}

# Header only library
%define devname %mklibname cereal -d

Summary:	A C++11 library for serialization
Name:		cereal
Version:	1.2.2
Release:	0
License:	BSD
Group:		System/Libraries
URL:		https://uscilab.github.com/%{name}
Source0:	https://github.com/USCiLab/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		https://github.com/USCiLab/cereal/commit/8b8f5814e292e03bb5b07333a0e634ef0481c85b.patch
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	doxygen

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Library for parsing/formatting/validating all international phone numbers
License:	Apache License
Group:		Development/C++
BuildArch:      noarch
Requires:	boost-devel

%description -n %{devname}
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains the include files and the other resources for C++
devlopper.

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_datadir}/cmake/%{name}/%{name}-config.cmake
%doc README.md
%doc LICENSE

%prep
%setup -q

%build
%apply_patches
%global optflags %{optflags} -Wno-gnu

%cmake \
	-DSKIP_PORTABILITY_TEST:BOOL=ON	\
	-DTHREAD_SAFE:BOOL=ON		\
	%{nil}
%make

%install
%makeinstall_std -C build 

%check
%make -C build test

