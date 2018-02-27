# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Imager.pm) perl(Inline.pm) perl(Inline/Files.pm) perl(List/Util.pm) perl(Storable.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Time/HiRes.pm) perl(XSLoader.pm) perl(base.pm)
#BuildRequires: perl(Math/Primality.pm) perl(Math/Prime/FastSieve.pm) perl(Math/Prime/XS.pm)
# END SourceDeps(oneline)
%define module_version 0.07
%define module_name Data-BitStream-XS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: A class implementing a stream of bits and coding methods
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DA/DANAJ/%module_name-%module_version.tar.gz

%description
An XS implementation providing read/write access to bit streams.  This includes.many integer coding methods as well as straightforward ways to implement new
codes.

Bit streams are often used in data compression and in embedded products where
memory is at a premium.

This code provides a nearly drop-in XS replacement for the the Data::BitStream manpage
module.  If you do not need the flexibility of the Moose/Mouse/Moo system, you
can use this directly.

Versions 0.03 and later of the the Data::BitStream manpage class will attempt to use
this XS class if it is available.  Most operations will be 50-100 times faster,
while not sacrificing any of its flexibility, so it is highly recommended.  In
other words, if this module is installed, any code using the Data::BitStream manpage
will automatically speed up.

While direct use of the XS class is a bit faster than going through
Moose/Mouse/Moo, the vast majority of the benefit is internal.  Hence, for
maximum portability and flexibility just install this module for the speed,
and continue using the the Data::BitStream manpage class as usual.





%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO Changes README LICENSE examples
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

