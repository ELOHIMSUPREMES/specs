Name: perl-OpenGL
Version: 0.6703
Release: alt1

Summary: Perl bindings to OpenGL API
Group: Development/Perl
License: Perl

Url: %CPAN OpenGL
# Cloned from git://pogl.git.sourceforge.net/gitroot/pogl/pogl
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel libfreeglut-devel libXi-devel libXmu-devel libXext-devel

%description
%summary

%prep
%setup -q
%patch -p1
rm test.pl

%build
%perl_vendor_build dist=NO_EXCLUSIONS

%install
%perl_vendor_install

%files
%perl_vendor_archlib/OpenGL*
%perl_vendor_autolib/OpenGL*
%doc TODO CHANGES README COPYRIGHT KNOWN_PROBLEMS Release_Notes SUPPORTS

%changelog
* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.6703-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt2
- rebuilt for perl-5.16

* Fri Jun 22 2012 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1
- initial build
