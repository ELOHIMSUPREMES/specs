# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define shortname lcf
%define major   0
%define libname lib%{shortname}%{major}
%define devname lib%{shortname}-devel

Name:           liblcf
Version:        0.4.1
Release:        alt1_3
Summary:        Library to handle RPG Maker 2000/2003 and EasyRPG projects
Group:          System/Libraries
License:        MIT
URL:            https://easy-rpg.org
Source0:        https://easy-rpg.org/downloads/player/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  libicu-devel
BuildRequires:  libtool-common
BuildRequires:  pkgconfig(expat)
Source44: import.info

%description
liblcf is a library to handle RPG Maker 2000 and 2003 game data.
It can read and write LCF and XML files. Part of C++ source files
can be regenerated from templates and CSV files using a Python script.

liblcf is part of the EasyRPG Project. More information is available
at the project website: easy-rpg.org

#----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Library to handle RPG Maker 2000/2003 and EasyRPG projects
Group:          System/Libraries

%description -n %{libname}
liblcf is a library to handle RPG Maker 2000 and 2003 game data.
It can read and write LCF and XML files. Part of C++ source files
can be regenerated from templates and CSV files using a Python script.

liblcf is part of the EasyRPG Project. More information is available
at the project website: easy-rpg.org

%files -n       %{libname}
%doc AUTHORS COPYING README
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

#----------------------------------------------------------------------

%package -n     %{devname}
Summary:        Development headers and library for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This package contains development headers and library for %{name},
a library which handles RPG Maker 2000/2003 and EasyRPG projects.

%files -n       %{devname}
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------

%prep
%setup -q

rm -f libtool

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete


%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3
- converted for ALT Linux by srpmconvert tools

