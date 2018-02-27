# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ perl(Encode.pm) perl(Module/Build.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           graphite2
Version:        1.2.2
Release:        alt1_4
Summary:        Font rendering capabilities for complex non-Roman writing systems
Group:          Development/Tools

License:        (LGPLv2+ or GPLv2+ or MPL) and (Netscape or GPLv2+ or LGPLv2+)
URL:            http://sourceforge.net/projects/silgraphite/
Source0:        http://downloads.sourceforge.net/silgraphite/graphite2-%{version}.tgz
Patch0:         graphite-arm-nodefaultlibs.patch
Patch1:         graphite2-1.2.0-cmakepath.patch

BuildRequires: ctest cmake
BuildRequires:  libfreetype-devel
BuildRequires:  doxygen asciidoc
BuildRequires:  texlive-fonts-recommended texlive-latex-recommended texlive-publishers texlive-latex-extra texlive-latex-extra

Obsoletes:      silgraphite < 2.3.1-5
Source44: import.info

%description
Graphite2 is a project within SILa.'s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create a.'smart fontsa.' capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Files for developing with graphite2
Group: Development/C

Obsoletes: silgraphite-devel < 2.3.1-5

%description devel
Includes and definitions for developing with graphite2.

%prep
%setup -q
%patch0 -p1 -b .arm
%patch1 -p1 -b .cmake

%build
%{fedora_cmake} -DGRAPHITE2_COMPARE_RENDERER=OFF .
make %{?_smp_mflags}
make docs
#sed -i -e 's!<a id="id[a-z]*[0-9]*"></a>!!g' doc/manual.html

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%check
#ctest

%files
%doc LICENSE COPYING ChangeLog
%{_bindir}/gr2fonttest
%{_libdir}/libgraphite2.so.3.0.1
%{_libdir}/libgraphite2.so.3

%files devel
#%doc doc/manual.html
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/graphite2-release.cmake
%{_libdir}/%{name}/graphite2.cmake
%{_includedir}/%{name}
%{_libdir}/libgraphite2.so
%{_libdir}/pkgconfig/graphite2.pc

%changelog
* Wed Aug 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_4
- fix in devel thanks to a.shabalin@

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4
- required by harfbuzz

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3
- initial fc import

